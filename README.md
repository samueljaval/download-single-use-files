# Download Single-Use Files!

When this python script is running, everytime the user downloads a file to the "Downloads" directory, it will ask through a pop-up window if they want to make this download a single-use file. A single-use file would be a file that is opened right after the download and deleted after that. So once closed the file will never be accessible again. The point of this is to automatically get rid of all the files we download to just have a quick look at them and never use again.

YOUR "DOWNLOADS" DIRECTORY WILL FOREVER BE "CLEAN"!

 - This script will only run on macOS
 - It should be run with python3 or more recent version
 - As it is, it only works for files downloaded from chrome and safari but can be easily modified to cover more browsers (comments in the code can help know what to change)


![pop-up window that will appear when a file is downloaded](img/popup.png)

- If you click yes, the file will open and it will be single-use
- If you click no, the file won't open but will remain in the "Downloads" directory
- If you click no & move, you can choose which directory you want to put your file in

You can run the script in the background using the following command: <br/>
```
nohup python single_use_files.py &
```
or <br/>
```
nohup python3 single_use_files.py &
```
(depending on how you call python from your terminal)

You can then close your terminal and the script will still be running.

To stop the script from running, you need to run the following command : <br/>
```
ps aux | grep single_use_file
```

which will give you something looking like this : <br/>
```
username           18091   0,0  0,2   395900  16112   ??  S     4:24     0:07.84 /Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python various_codes/download-single-use-files/single_use_files.py
```

you can kill the script using :
```
kill 18091
```
(of course you would use your equivalent number, called "PID")
