'''
This file contains helper functions used in the app
You have functions to get the newest file in a directory, fit a path to unix conventions,
get the size of the Downloads folder, delete a file, and move a file
'''


import os
import glob
import time
import multiprocessing as mp


def security(checkfornew):
    check1 = check_item(checkfornew,"/-")
    check2 = check_item(checkfornew,"~")
    check3 = check_item(checkfornew,"..")
    check4 = check_item(checkfornew,"*")
    check5 = secure_path(checkfornew)
    check6 = check_item(checkfornew,"$")
    check7 = check_item(checkfornew,":")
    if check1 and check2 and check3 and check4 and check5 and check6 and check7:
        return True
    else :
        return False


# unix uses a \ before every space and parenthesis
# fitting a path string to unix conventions
def fit_to_unix(filename):
    newname = ""
    for char in filename:
        if char == " " or char == "(" or char == ")":
            newname += "\\" + char
        else :
            newname += char
    return newname


# get the name of the newly downloaded file
def newest_file():
    list_of_files = glob.glob(os.path.expanduser('~')+"/Downloads/*")
    latest_file = max(list_of_files, key=os.path.getmtime)      #most recent file in the directory
    return latest_file


#returns number of elements in Downloads directory
def size_downloads():
    return len(os.listdir(os.path.expanduser('~')+"/Downloads"))



####################### removing file functions ##############################

# check that the path is correct up to Downloads
def secure_path(checkfornew):
    right_path = os.path.expanduser('~')+"/Downloads/"
    i = 0
    while i < len(right_path):
        if not(checkfornew[i] == right_path[i]):
            return False
        i+=1
    return True

# returns True if item not in checkfornew
def check_item(checkfornew,item):
    for char in checkfornew:
        if char == item:
            return False
    return True

# deleting file in another thread to allow delayed deletion (time chosen by user)
# This is done with Python multiprocessing in the remove() function
def thread_removing(checkfornew, time_del):
    time.sleep(time_del)
    #security layer!!
    if security(checkfornew):
        # i don't know the inner workings of os.remove so i treated it
        # and secured it as if it was the "rm" unix command to be safe.
        # Even if it might not be necessary, it doesn't hurt
        os.remove(checkfornew)

# opening the file before deleting it in another thread
def remove(checkfornew, time_del):
    if security(checkfornew):
        os.system('open ' + fit_to_unix(checkfornew))
    time.sleep(0.5)
    p = mp.Process(target=thread_removing, args=(checkfornew, time_del,))
    p.start()

######################### end removing file functions ###################



######################## moving file functions ##########################

# read the result of the dialog to choose a folder
def read_chosen_folder(result):
    read = ""
    for x in result[0][18:-1]:
        if x == ":":
            read += "/"
        else :
            read += x
    return fit_to_unix(read)

# moving the file to the chosen folder
def move(checkfornew):
    result  = os.popen("""osascript -e 'choose folder' """).readlines()
    if result != []:
        os.chdir(os.path.expanduser('~'))
        os.system("cd ../..")
        if security(checkfornew):
            os.system("mv " + fit_to_unix(checkfornew) + " " + read_chosen_folder(result))

##########################  end moving file functions ###################
