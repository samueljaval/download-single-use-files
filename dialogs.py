'''
This file contains all the necessary dialog functions for the App
The dialogs with text and buttons are made with and osascript command
which runs Applescript code. os.popen is used to get the result (button pressed)
or folder chosen which would be printed in a shell if run there.
The notifications are made with the pync library instead of Applescript for esthetic reasons.
I also commented a way to have notifications using rumps but it is not used here.
'''

import os
import pync
from helpers import remove, move
# import rumps for the other way of notifying

def notify(checkfornew, time_del):
    result = os.popen("""osascript -e 'display dialog "Do you want what you just downloaded to be a single-use file?" buttons {"Yes","No & Move","No"} default button "No" with title "Single-Use File? " with icon Caution
'""").readlines()
    if result == ['button returned:Yes\n']:
        remove(checkfornew, time_del)
    if result == ['button returned:No & Move\n']:
        move(checkfornew)

def help_text():
    os.system("""osascript -e 'display dialog "Whenever you download a file to your Downloads folder, the app will ask you if you want to make it a single-use file.

If you say yes, the file will be opened and once you close it, it will be deleted from your computer (preventing accumulation of files). You can choose the amount of time after which the file is deleted.

If you say no, you will also have the option to move the file you just downloaded to some folder other than the Downloads one.

Enjoy!

{This app was created by Samuel Javal in April 2020}" buttons {"OK"} default button "OK" with title "Single-Use File App - Help/About"
'""")

def intro():
    os.system("""osascript -e 'display dialog "You just opened the Single-Use File App.
Your Downloads directory will forever be clean!

Check your MENU BAR at the top of your screen to launch the app!

You can also click Help/About, Pause, Set Time or Quit App in your menu bar." buttons {"OK"} default button "OK" with title "Single-Use File App"
'""")

def start_dialog():
    pync.notify("You successfully started the app. It is now running.", title="Single-Use File App")
    # other ways to do it :
    # rumps.notification("Single-Use File App", "You successfully started the app. It is now running.")
    # os.system("""osascript -e 'display notification "You successfully started the app. It is now running." with title "Single-Use File App"'
# """ )
def already_started():
    pync.notify("Warning: You already started the app, you cannot start it again.", title="Single-Use File App")

def wrong_pause():
    pync.notify("Warning: You have not started the app, you cannot pause it.", title="Single-Use File App")

def pause_dialog():
    pync.notify("You successfully paused the app.", title="Single-Use File App")

def time_dialog():
    result = os.popen("""osascript -e 'display dialog "Singe-Use file App gives you the option to choose the amount of time the single-use file will stay alive.

After how long do you want your single-use files to be deleted?
If you enter 0.5 it will be 0 minutes and 30 seconds. The default value is set to 1 second.

Note : To confirm the change, pause and start the app." default answer "Enter the number your want (in minutes)" with title "Single-Use File App - Set Time"' """).readlines()
    return result

def enter_number_dialog():
    pync.notify("WARNING : You have to enter a valid number.", title="Single-Use File App")
