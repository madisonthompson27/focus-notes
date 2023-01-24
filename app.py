"""
A program that incorperates a timer, notes section, audio, and various notes formats.
Notes formats are available for code, meetings, journals, and cornell.
When exported, files can have a name, date, title, time, and duration.      
"""

#imports
from tkinter import *
from datetime import *
import time as time


#creating a window, works in fullscreen mode to prevent distractions.
root = Tk()

#root title
root.title("Focus Notes")

#root icon
#FIXME

#fullscreen mode
root.attributes('-fullscreen', True)


#making the background color black
root.configure(bg="black")


#creating a timer that will countdown from the user-specified time


#creating a function to open the export menu when the button is pressed
def openExport(choice):
    if choice == 0:
        #exportMenu
        pass


#defining default attributes for buttons
class entrySettings(Entry):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = dict()
        kwargs['fg'] = 'white',
        kwargs['bg'] = 'black',
        kwargs['highlightcolor'] = 'purple',
        kwargs['highlightbackground'] = 'purple',
        kwargs['highlightthickness'] = 1,
        kwargs['insertbackground'] = 'white',
        super().__init__(*args, **kwargs)
        
        
#defining default attributes for labels
class labelSettings(Label):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = dict()
        kwargs['font'] = ("Terminal", 16)
        kwargs['fg'] = 'white',
        kwargs['bg'] = 'black',
        super().__init__(*args, **kwargs)
        

#defining default attributes for buttons
class buttonSettings(Button):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = dict()
        kwargs['font'] = ("Terminal", 16)
        kwargs['fg'] = 'white',
        kwargs['bg'] = 'purple',
        super().__init__(*args, **kwargs)


#defining default attributes for the text field
class textSettings(Text):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = dict()
        kwargs['fg'] = 'white',
        kwargs['bg'] = 'black',
        kwargs['highlightcolor'] = 'purple',
        kwargs['highlightbackground'] = 'purple',
        kwargs['highlightthickness'] = 1,
        kwargs['insertbackground'] = 'white',
        kwargs['width'] = 175,
        super().__init__(*args, **kwargs)


#defining default attributes for message boxes
class messageSettings(Message):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = dict()
        kwargs['fg'] = 'white',
        kwargs['bg'] = 'black',
        kwargs['highlightcolor'] = 'purple',
        kwargs['highlightbackground'] = 'purple',
        kwargs['highlightthickness'] = 1,
        kwargs['insertbackground'] = 'white',
        kwargs['width'] = 175,
        super().__init__(*args, **kwargs)

#creating a label to display the current date
labelDate = labelSettings(root, text=f"{datetime.now():%a, %b %d %Y}")

#creating a label for time
def refresh_clock():
    labelTime.config(text=time.strftime("%I:%M:%S %p", time.localtime()))
    root.after(1000, refresh_clock)

labelTime = labelSettings(root)


#creating the countdown timer

#declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

#assigning entry boxes with user input variables
entryHour = entrySettings(root, textvariable=hour)

entryMinute = entrySettings(root, textvariable=minute)

entrySecond = entrySettings(root, textvariable=second)


def submit():
    try:
        # the input provided by the user is stored in a tempvar until the countdown begins
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input positive values")
  
    #while loop to iterate as long as the timer is positive
    while temp > -1:
		
        #divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)

        #converting into seconds
        hours = 0
        if mins > 60:
			
            #divmod(firstvalue = temp//60, secondvalue = temp%60)
            hours, mins = divmod(mins, 60)
		
        #using format() method to store the value up to two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a message encourages the user to take a break
        if (temp == 0):
            
            
            #stops the timer from repeating
            break
		
        # after every one sec the value of temp will be decremented by one
        temp -= 1

# button to allow the user to start the timer
buttonTimer = buttonSettings(root, text="Start", command= submit)


#creating a label for audio options
labelAudioOptions = labelSettings(root, text="Music")


#creating a label that allows the user to change the color theme
labelColorTheme = labelSettings(root, text="Color Theme")

#FIXME create images for background color, text color. Five each.


#creating entry fields for optional export to the pdf file.
labelDocName = labelSettings(root, text="Document Name")
entryDocName = entrySettings(root)


#creating entry fields for the document's heading
labelDocHeader = labelSettings(root, text="Heading")
entryDocHeader = entrySettings(root)


#creating entry fields for the document's author
labelDocAuthor = labelSettings(root, text="Author")
entryDocAuthor = entrySettings(root)


#creating entry fields for the document's date
labelDocDate = labelSettings(root, text="Date")
entryDocDate = entrySettings(root)


#creating entry fields for the document's heading
labelDocTimes = labelSettings(root, text="Times")
entryDocTimes = entrySettings(root)


#creating entry fields for the document's heading
labelDocKeywords = labelSettings(root, text="Keywords")
entryDocKeywords = entrySettings(root)


#creating an entry field for the main textbox
journalBox = textSettings(root)


#placing a button to export the text to a pdf
exportButton = buttonSettings(root, text="Export PDF", command=lambda: openExport(0))


#placing widgets
labelDate.place(x=935, y=25)

labelTime.place(x=1135, y=25)
root.after_idle(refresh_clock)

entryHour.place(x=25, y=25, height=20, width=50)
entryMinute.place(x=75, y=25, height=20, width=50)
entrySecond.place(x=125, y=25, height=20, width=50)

buttonTimer.place(x=25, y=50, height=20, width=150)

labelDocName.place(x=25, y=325)
entryDocName.place(x=25, y=350, height=20, width=150)

labelDocHeader.place(x=25, y=375)
entryDocHeader.place(x=25, y=400, height=20, width=150)

labelDocAuthor.place(x=25, y=425)
entryDocAuthor.place(x=25, y=450, height=20, width=150)

labelDocDate.place(x=25, y=475)
entryDocDate.place(x=25, y=500, height=20, width=150)

labelDocTimes.place(x=25, y=525)
entryDocTimes.place(x=25, y=550, height=20, width=150)

labelDocKeywords.place(x=25, y=575)
entryDocKeywords.place(x=25, y=600, height=20, width=150)

journalBox.place(x=200, y=50, height=625, width=1050)

exportButton.place(x=25, y=650, height=25, width=150)

#loop
root.mainloop()