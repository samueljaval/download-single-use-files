#!/usr/bin/env python3

# will only work on macOS
# currently works for chrome and safari downloads but can easily be modified for more browsers

import tkinter as tk
import glob
import os
import time
import sys

# centering the pop up window
def center(root):
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

# called when click on the 'yes' button -> single use file
# checkfornew is the newly downloaded file name, root is the pop up window
# we open the file and delete it from the Downloads file to ensure the single use
def delete(checkfornew,root):
    os.system('open ' + fit_to_unix(checkfornew))
    time.sleep(1)
    os.remove(checkfornew)
    root.destroy()


def create_popup(checkfornew,root):
    canvas = tk.Canvas(root, width = 160, height = 50)
    center(root)
    root.title("Single use file?")
    canvas.pack()
    button_yes = tk.Button (root, text='yes',command = lambda *args: delete(checkfornew,root))
    button_no = tk.Button (root, text='no', command = root.destroy)
    canvas.create_window(50, 30, window=button_yes)
    canvas.create_window(115,30, window=button_no)
    root.mainloop()

# get the name of the newly downloaded file
def newest_file():
    list_of_files = glob.glob(os.path.expanduser('~')+"/Downloads/*")  # goes to the user's root directory
    latest_file = max(list_of_files, key=os.path.getmtime)      #most recent file in the directory
    return latest_file

# unix uses a \ before every space and parenthesis
def fit_to_unix(filename):
    newname = ""
    for char in filename:
        if char == " " or char == "(" or char == ")":
            newname += "\\" + char
        else :
            newname += char
    return newname

def size_downloads():
    return len(os.listdir(os.path.expanduser('~')+"/Downloads"))

#'.crdownload' is what chrome uses for the temporary file while it's being downloaded
#'.download' is what safari uses for the temporary file while it's being downloaded
# if you are using other browsers you can just add the extension they use for downloading files
def main():
    newest = newest_file()
    size_folder = size_downloads()
    while True:
        checkfornew = newest_file()
        new_size_folder = size_downloads()
        time.sleep(1)
        if new_size_folder >= size_folder:      #check if the new most recent is not due to a deletion
            if not checkfornew.endswith('.crdownload') and not checkfornew.endswith('.download'):
                if checkfornew != newest :
                    root = tk.Tk()
                    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
                    create_popup(checkfornew,root)
                    newest = newest_file()
        size_folder = new_size_folder

main()
