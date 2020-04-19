'''
This file contains the main loop of the app. It is an infinite loop
checking if the user has downloaded a new file. If they have, it asks
the user if they want it to be a single-use file (can choose Yes, No & Move, No)

This infinite loop is run as another process to prevent the UI the app from being
stuck in it. This is done with python multiprocessing
'''

import time
import dialogs
from helpers import newest_file, size_downloads

#'.crdownload' is what chrome uses for the temporary file while it's being downloaded
#'.download' is what safari uses for the temporary file while it's being downloaded
# if you are using other browsers you can just add the extension they use for downloading files
# This is the core part of the app
def main_loop(time_del):   # time_del will be passed to notify and is the delay for deletion
                           # chosen by the user (or the default one) if user wants a single-use file
    newest = newest_file()
    size_folder = size_downloads()
    while True:
        checkfornew = newest_file()
        new_size_folder = size_downloads()
        time.sleep(1)
        if new_size_folder >= size_folder:      #check if the new most recent is not due to a deletion
            #wait for when the file is actually fully donwloaded
            if not checkfornew.endswith('.crdownload') and not checkfornew.endswith('.download'):
                if checkfornew != newest :
                    time.sleep(1)
                    # asking the user what they want to do with the file
                    dialogs.notify(checkfornew, time_del)
                    time.sleep(1)
        # updating most recent file of directory unless the most recent is being downloaded
        if not checkfornew.endswith('.crdownload') and not checkfornew.endswith('.download'):
            newest = checkfornew
        size_folder = new_size_folder
