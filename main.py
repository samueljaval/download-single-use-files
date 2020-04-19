'''
Single-Use File App

This app was created by Samuel Javal in April 2020
It will only work on macOS
Currently works for chrome and safari downloads but can easily be modified for more browsers
Can be made into a standalone app with py2app
'''

import dialogs
from inf_loop import main_loop
import multiprocessing as mp
import rumps

# This is the class defining the Mac MenuBar item which is the main user
# interface and center of the app
class MenuBar(rumps.App):

    started = 0       # will be 1 or 0, 1 when the app is running, 0 when it is paused
    time_del = 0.02   # time after which a single-use file will be deleted
                      # can be set by the user with the Set Time button

    @rumps.clicked("Help/About")
    def help_about(self, _):
        dialogs.help_text()

    @rumps.clicked("Start")
    def start(self, _):
        if self.started == 0:
            dialogs.start_dialog()
            self.p1 = mp.Process(target=main_loop, args=(self.time_del,))
            self.p1.start()
            self.started = 1
        else :
            dialogs.already_started()

    @rumps.clicked("Pause")
    def pause(self, _):
        if self.started == 1:
            dialogs.pause_dialog()
            self.started = 0
            self.p1.terminate()
            self.p1.join()
        else :
            dialogs.wrong_pause()

    @rumps.clicked("Set Time")
    def set_time(self, _):
        result = dialogs.time_dialog()
        if result != []:
            number = result[0][34:-1]
            if number.replace('.','',1).isdigit():
                self.time_del = round(float(number),1)*60.0
            else :
                dialogs.enter_number_dialog()

    @rumps.clicked("Quit App")
    def quit_app(self, _):
        if self.started == True:
            self.p1.terminate()
            self.p1.join()
        rumps.quit_application()

# Startup of Single-Use File App
dialogs.intro()
if __name__ == "__main__":
    app = MenuBar("⬇️App", quit_button=None)
    app.run()
