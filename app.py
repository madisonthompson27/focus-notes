"""
A program that incorperates a timer, notes section, audio, and a customizable backgrounds to allow the user a dedicated study experience.
As long as the countdown timer is running, the user can only exit the program from their OS. This ensures a focused environment. 
Music and customizable graphics encourage personalized learning. 
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


#creating the time, date, and timer widgets. 

#creating a label to display the current date.
labelDate = labelSettings(root, text=f"{datetime.now():%a, %b %d %Y}")

#creating a label for time
def refresh_clock():
    labelTime.config(text=time.strftime("%I:%M:%S %p", time.localtime()))
    root.after(1000, refresh_clock)

#this label will display the time
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

#creating a label to let the user know what the timer is for. 
labelCountdown = labelSettings(root, text="Work Countdown")

#assigning entry boxes with user input variables
entryHour = entrySettings(root, textvariable=hour, justify=CENTER)
entryMinute = entrySettings(root, textvariable=minute, justify=CENTER)
entrySecond = entrySettings(root, textvariable=second, justify=CENTER)


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
labelAudioOptions = labelSettings(root, text="Music-")
labelAudioOptions['font'] = ("Terminal", 10)

#creating a variable to store the audio option selected
audioSelected = StringVar()

#menu of audio options
audioOptions = ["classical", "electronic", "ambient", "upbeat", "slow"]

#making the actual audio menu
menuAudio = OptionMenu(root, audioSelected, *audioOptions)


#making a label for the color theme menus
labelColorThemes = labelSettings(root, text="Theme Options")

#options for the color theme dropdown menus
colorOptions = ["white", "black", "purple", "blue", "teal", "pink", "red", "maroon", "gray", "gold", "silver", "green", "yellow"]


#creating a stringVar to house the selected text and cursor color
textSelected = StringVar()

#creating a label for the text color
labelText = labelSettings(root, text="Text-")
labelText['font'] = ("Terminal", 10)

#creating a dropdown menu to allow the user to select the text and cursor color
menuText = OptionMenu(root, textSelected, *colorOptions)


#defining a variable to hold the selected border value
borderSelected = StringVar()

#label for button color
labelButtons = labelSettings(root, text="Button-")
labelButtons['font'] = ("Terminal", 10)

#creating a dropdown menu to allow the user to select the button and border color
menuBorder = OptionMenu(root, borderSelected, *colorOptions)


#defining a variable to hold the selected value
backgroundSelected = StringVar()

#label for background color
labelBackground = labelSettings(root, text="Back-")
labelBackground['font'] = ("Terminal", 9)

#creating a dropdown menu to allow the user to select the background color
menuBackground = OptionMenu(root, backgroundSelected, *colorOptions)


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


#placing a button to allow the user to quit the program
quitButton = buttonSettings(root, text="Quit", command=quit)
quitButton['bg'] = 'maroon'


#placing widgets

#placing a widget labeling the color theme options
labelColorThemes.place(x=25, y=125, height=20, width=150)

#placing the color theme widgets- text color
labelText.place(x=25, y=150, height=20, width=75)
menuText.place(x=100, y=150, height=20, width=75)

#placing color theme widgets- border color
labelButtons.place(x=25, y=175, height=20, width=75)
menuBorder.place(x=100, y=175, height=20, width=75)

#placing color theme widgets- background color
labelBackground.place(x=25, y=200, height=20, width=75)
menuBackground.place(x=100, y=200, height=20, width=75)

#placing the audio options and menu
labelAudioOptions.place(x=25, y=225, height=20, width=75)
menuAudio.place(x=100, y=225, height=20, width=75)

#label for the date, top right
labelDate.place(x=935, y=25)

#label for the time, top right
labelTime.place(x=1135, y=25)
root.after_idle(refresh_clock)

#top left, labels and entries for the countdown fields
labelCountdown.place(x=25, y=25, height=20, width=150)

entryHour.place(x=25, y=50, height=20, width=50)
entryMinute.place(x=75, y=50, height=20, width=50)
entrySecond.place(x=125, y=50, height=20, width=50)

buttonTimer.place(x=25, y=75, height=20, width=150)

#labels for bottom left, entries for the document settings
labelDocName.place(x=25, y=300)
entryDocName.place(x=25, y=325, height=20, width=150)

labelDocHeader.place(x=25, y=350)
entryDocHeader.place(x=25, y=375, height=20, width=150)

labelDocAuthor.place(x=25, y=400)
entryDocAuthor.place(x=25, y=425, height=20, width=150)

labelDocDate.place(x=25, y=450)
entryDocDate.place(x=25, y=475, height=20, width=150)

labelDocTimes.place(x=25, y=500)
entryDocTimes.place(x=25, y=525, height=20, width=150)

labelDocKeywords.place(x=25, y=550)
entryDocKeywords.place(x=25, y=575, height=20, width=150)

#center frame, main textbox. 
journalBox.place(x=200, y=50, height=625, width=1050)

#export button, bottom left. 
exportButton.place(x=25, y=620, height=25, width=150)

#quit button, allows the user to exit the program
quitButton.place(x=25, y=650, height=25, width=150)

#loop
root.mainloop()
