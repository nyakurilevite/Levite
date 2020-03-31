from gtts import gTTS
import random
from playsound import playsound
import os
from tkinter import *
from tkinter import messagebox


class MyWindow:
    def __init__(self, win):
        
     self.lbl1 = Label(win,bg='coral', text='Welcome to the text to speech app', font=("Britannic Bold", "22"))
     self.lbl1.place(x=200, y=20)
     self.lbl2 = Label(win,bg='coral', text='Please enter the text to be spoken below', font=("Britannic Bold", "12"))
     self.lbl2.place(x=200, y=80)
     self.text = Text(win, font=("Tahoma", "8"))
     self.text.place(x=200, y=150)
     self.speechbtn=Button(win, text='Speech', font=("Tahoma", "18"), command=self.speechcmd)
     self.speechbtn.place(x=200, y=500)
     self.speechbtn=Button(win, text='Exit', font=("Tahoma", "18"), command=win.destroy)
     self.speechbtn.place(x=620, y=500)



    def speechcmd (self):
        msg = str(self.text.get("1.0", "end-1c"))
        msg_length = len(msg)
        if msg_length > 0:
            def createFolder(directory):
                try:
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                except OSError:
                    print('Error: Creating directory. ' + directory)

            # Example
            createFolder('./voice/')
            mytext = msg

            # Language in which you want to convert
            language = 'en'

            # Passing the text and language to the engine,
            # here we have marked slow=False. Which tells
            # the module that the converted audio should
            # have a high speed
            myobj = gTTS(text=mytext, lang=language, slow=False)

            # Saving the converted audio in a mp3 file named
            # welcome
            for x in range(10):
                file = random.randint(1, 200000)
            filename = str("voice/") + str(file) + str(".mp3")
            msg = messagebox.showinfo("Notification", "File location:" + filename)
            myobj.save(filename)
            playsound(filename)
        elif msg_length == 0:
            msg = messagebox.showwarning("Notification", "Please write message to speech!!")
window= Tk()
mywin = MyWindow(window)
window.title('Text to speech')
window.geometry("800x600+500+100")
window.iconbitmap('icons/calculator.ico')
window["bg"] = "coral"
window.resizable(False, False)
window.mainloop()
