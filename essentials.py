# define Python user-defined exceptions
"Includes all the essential libraries you could need. Such as time, os, math and much more."
class Errors():
    "Includes all potiental raised errors when using this library"
    def __init__(self):
        self.errortype = "FATAL ERROR"
    class InvalidArgument(Exception):
        "Raised when an invalid argument is given"
        def __init__(self, thing, nonint = False, given = None, highmax = False):
            self.given = given
            self.message = f"FATAL ERROR: {thing} cannot be {given}"
            if (nonint == True):
                self.message = f"FATAL ERROR: {given} is not an integer"
            if (highmax == True):
                self.message = f"FATAL ERROR: Minimum cannot be higher then maximum"
            super().__init__(self.message)
    class TooLargeError(Exception):
        "Raised when a value too large is attempted to be passed"
        def __init__(self):
            self.message = "FATAL ERROR: Number is too large"
            super().__init__(self.message)


class Graphics():
    "Includes all graphics related things like creating windows adding buttons and so much more"
    class Window():
        def __init__(self):
            pass
        def newWindow(title:str, width:int, height:int, bgcolor:str = "lightgray"):
            from tkinter import Tk
            if (title == None or isinstance(title, str) == False):
                raise Errors.InvalidArgument(thing="Title", given=title)
            window = Tk(screenName=title)
            window.title(title)
            window.configure(width=width, height=height, bg=bgcolor)
            winWidth = window.winfo_reqwidth()
            winwHeight = window.winfo_reqheight()
            posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
            posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
            window.geometry("+{}+{}".format(posRight, posDown))
            window.mainloop()


    class Buttona(): 
        "Includes all types of buttons"
        def textButton(window, text:str, bx:int, by:int):
            from tkinter import Button
            btn=Button(Window, text="This is Button widget", fg='blue')
            btn.place(x=bx, y=by)

class Keyboard():
    def __init__(self):
        pass
    def block(key: str = None):
        "Doesn't register keyboard input until a certain key is pressed. If no key is given it will block keyboard input forever \na key is the keyboard input or multiple keys such as 'w' or 'enter' or 'alt+F4'"
        if (key == None):
            from keyboard import wait
            wait()
        if (isinstance(key, str) == False and key != None):
            raise Errors.InvalidArgument("Key", given=key)
    def press(key: str = None):
        "Presses and then releases a key. \na key is the keyboard input or multiple keys such as 'w' or 'enter' or 'alt+F4'"
        if (key == None):
            raise TypeError(key)
            #raise Errors.InvalidArgument("Key", given=key)
        if (isinstance(key, str) == False and key != None):
            raise TypeError(key)
            #raise Errors.InvalidArgument("Key", given=key)
        from keyboard import press_and_release
        try:
            press_and_release(key)
        except ValueError:
             error(f"Cannot press key {key} because it is not mapped to any key")
    def press_hold(key: str = None):
        "Presses a key and holds the key until the script stops or the release function is called"
        if (key == None):
            raise TypeError(key)
            #raise Errors.InvalidArgument("Key", given=key)
        if (isinstance(key, str) == False and key != None):
            raise TypeError(key)
            #raise Errors.InvalidArgument("Key", given=key)
        from keyboard import press
        try:
            press(key)
        except ValueError:
             error(f"Cannot press key {key} because it is not mapped to any key")      
    def release(key: str = None):
        "Releases the key given if the key given is currently being held down"
        if (key == None):
            raise TypeError(key)
            #raise Errors.InvalidArgument("Key", given=key)
        if (isinstance(key, str) == False and key != None):
            raise TypeError(key)
            #raise Errors.InvalidArgument("Key", given=key)
        from keyboard import release
        try:
            release(key)
        except ValueError:
             error(f"Cannot press key {key} because it is not mapped to any key")  
    def write(text: str):
        "Make the keyboard write a certain text"
        if (isinstance(text, str) == False):
            raise TypeError(text)
            #raise Errors.InvalidArgument("Key", given=key)
        from keyboard import write
        write(text=text)
    def is_pressed(key: str):
        "Check to see if a certain key is being pressed. Returns true if the key is pressed. Returns false otherwise"
        if (isinstance(key, str) == False):
            raise TypeError(key)
            #raise Errors.InvalidArgument("Key", given=key)
        from keyboard import is_pressed
        ispress = is_pressed(key)
        return ispress
    def on_press(callback):
        "Calls the function given when any key is pressed. (Function given must have a self argument)"
        from keyboard import on_press
        on_press(callback=callback)

     
    

def warn(text: str):
     print(f"WARNING: {text}")
    
def error(text: str):
    print(f"ERROR: {text}")

class Math():
    "Includes a bunch of math related functions"
    def __init__(self):
        pass
    def floor(number: float):
        "Rounds to the largest integer less than or equal to the given number. (Basically just rounds down if possible)"
        from math import floor
        if (number == None):
            raise Errors.InvalidArgument(thing="Number", given=number) 
        floor(number)
    def ceil(number: float):
        "Rounds to the smaller integer greater than or equal to a given number. (Basically just rounds up if possible)"
        from math import ceil
        if (number == None):
            raise Errors.InvalidArgument(thing="Number", given=number) 
        ceil(number)
    def isfinite(x):
        "Returns true if the value given is infinite returns false if it isn't"
        from math import isfinite
        if (x == None):
            raise Errors.InvalidArgument(thing="Number", given=x)
        return isfinite(x)
    def isinfinite(x):
        "Returns true if the value given is positive or negative infinity if not returns false"
        from math import isinf
        if (x == None):
            raise Errors.InvalidArgument(thing="Number", given=x)
        return isinf(x)       
    def isnan(x):
        "Returns true if the value given is NaN (not a number) returns false otherwise"
        from math import isnan
        if (x == None):
            raise Errors.InvalidArgument(thing="Number", given=x)
        return isnan(x)      
    def generateNumber(min: int, max: int):
        "Generates a random number between the minimum and the maximum"
        if (min == None or isinstance(min, float) == True):
            raise Errors.InvalidArgument(thing="Minimum", given=min)
        if (min >= max):
            raise Errors.InvalidArgument(thing="", nonint=False, given=None, highmax=True)
        if (max == None or isinstance(max, float) == True):
            raise Errors.InvalidArgument(thing="Maximum", given=max)
        from random import randint
        number = randint(min, max)
        return number
    def pow(base, exponent, showfullnumber=False):
        "Returns the number acquired when raising the base to the power of the exponent "
        if (showfullnumber == False):
            try:
                return base**exponent / 1000
            except OverflowError:
                from math import inf
                return inf 
        if (base**exponent > 2**1024 and showfullnumber == True):
            raise Errors.TooLargeError
    
        return base**exponent



class Miscellaneous():
    def __init__(self):
        pass
    def coinFlip():
        from random import randint
        coin = randint(1, 2)
        if coin == 1:
            return "Heads"
        if coin == 2:
            return "Tails"

class OS():
    "Relating to all things regarding operating system"
    def __init__(self):
        pass

    def platform():
        "Returns the platform the user is running such as 'Windows' 'Linux' 'Mac' returns None if it can't be determined"
        import platform
        if (platform.system() == ""):
            return None
        else:
            return platform.system()
    def user():
        "Returns the user logged in.. Does not work with Emscripten or WASI"
        from os import getlogin
        return getlogin
    class Path():
        def __init__(self):
            pass
        def exists(path):
            "Returns True if the path given exists. Returns false otherwise"
            from os.path import exists
            if (path == None):
                raise Errors.InvalidArgument(thing="Path", given=None)
            return exists(path=path)
        def isabs(path):
            "Returns true if the path given is an absolute path. Returns False otherwise"
            from os.path import isabs
            if (path == None):
                raise Errors.InvalidArgument(thing="Path")
            return isabs(path)

        def isfile(path):
            "Returns true if the path given is a file. Returns False otherwise"
            from os.path import isfile
            if (path == None):
                raise Errors.InvalidArgument(thing="Path")
            return isfile(path)

        def isfolder(path):
            "Returns true if the path given is a folder. Returns False otherwise"
            from os.path import isdir
            if (path == None):
                raise Errors.InvalidArgument(thing="Path")
            return isdir(path)
        
        def getsize(path):
            "Returns the size of the given path in bytes. Returns an error if the file doesn't exist or is inaccessible"
            from os.path import getsize
            if (path == None):
                raise Errors.InvalidArgument(thing="Path")
            filesize = None
            try:
                filesize = getsize(path)
                return filesize
            except OSError:
                error(f"Cannot get size of file {path}. The file either doesn't exist or is inaccessible")
                return False            


class Time():
    def __init__(self):
        pass

    def epoch():
        "Returns the amount of seconds that have passed since January 1st, 1970 (start of computer time)."
        from time import time
        epochtime = time()
        return epochtime
    def pause(seconds: float):
        "Pauses the script for a given time (in seconds)"
        from time import sleep
        if (seconds == None):
            raise Errors.InvalidArgument(thing="Seconds", given=seconds)
        sleep(seconds)