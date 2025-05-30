import ttkbootstrap as ttk
from tkinter import messagebox
import datetime as dt
import pygame

class AlarmClock:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")
        self.root.title("Alarm Clock")
        self.root.geometry("500x500")

        pygame.mixer.init()
        pygame.mixer.music.load('clock-alarm-8761.mp3')

        self.hour = 7  #default values
        self.min = 0

        self.mainframe = ttk.Frame(self.root, padding=20)
        self.mainframe.pack(fill="x")

        self.labelstyle = ttk.Style()
        self.labelstyle.configure("Alarm.TLabel", background="indigo", foreground="white",
                                  font="Roboto 20 bold", borderwidth=2,
                                  relief="groove", anchor="center")

        self.alarmtime = ttk.StringVar()
        self.alarmtime.set("07:00")   #default
        self.alarmlabel = ttk.Label(self.mainframe, style="Alarm.TLabel",
                                    textvariable=self.alarmtime, justify="center",
                                    anchor="center", relief="groove")
        self.alarmlabel.pack(side="top", fill="both", expand=True)

        #---------------------------------------------------------------#
        self.hourentryframe = ttk.Frame(self.root, padding=20)
        self.hourentryframe.pack(side="top", fill="x")

        self.instructionhourlabel = ttk.Label(self.hourentryframe, style="Alarm.TLabel",
                                              text="Enter hour desired (using 24h format): ",
                                              relief="groove", font="Roboto 10")
        self.instructionhourlabel.pack(side="left", fill='both', expand=True)

        self.hourtxt = ttk.StringVar()
        self.hourtxt.set("7")
        self.hourentry = ttk.Entry(self.hourentryframe, bootstyle="primary", textvariable=self.hourtxt)
        self.hourentry.pack(side="left", fill="both", expand=True)
        self.hourentry.bind("<Return>", self.sethour)

        self.sethourbtn = ttk.Button(self.hourentryframe, text="Set Hour", bootstyle="success",
                                     command=self.sethour)
        self.sethourbtn.pack(side="left", fill="x", expand=True)

        #---------------------------------------------------------#
        self.minentryframe = ttk.Frame(self.root, padding=20)
        self.minentryframe.pack(side="top", fill="both")

        self.instructionminlabel = ttk.Label(self.minentryframe, style="Alarm.TLabel",
                                              text="Enter minute desired (0-59):",
                                              relief="groove", font="Roboto 10")
        self.instructionminlabel.pack(side="left", fill='both', expand=True)

        self.mintxt = ttk.StringVar()
        self.mintxt.set("7")
        self.minentry = ttk.Entry(self.minentryframe, bootstyle="primary", textvariable=self.mintxt)
        self.minentry.pack(side="left", fill="both", expand=True)
        self.minentry.bind("<Return>", self.setmin)

        self.setminbtn = ttk.Button(self.minentryframe, text="Set Minute", bootstyle="success",
                                     command=self.setmin)
        self.setminbtn.pack(side="left", fill="x", expand=True)

        #--------------------------------------------------------------------#
        self.timeframe = ttk.Frame(self.root, padding=20)
        self.timeframe.pack(side="top", fill="x")

        self.explanationlabel = ttk.Label(self.timeframe, style="Alarm.TLabel",
                                          text="Current Time:")
        self.explanationlabel.pack(side="left", fill="x", expand=True)

        self.currenttime = ttk.StringVar()
        self.currenttimelabel = ttk.Label(self.timeframe, style="Alarm.TLabel",
                                          textvariable=self.currenttime)
        self.currenttimelabel.pack(side="left", fill="x", expand=True)
        self.updatetime()

        self.checkalarm()


        self.root.mainloop()

    def sethour(self, event=None):
        print("Hour pressed")
        try:
            if int(self.hourtxt.get()) > 24 or int(self.hourtxt.get()) < 0:
                messagebox.showerror("Error", "Please enter a valid integer (0-24).")
                self.hourentry.delete(0, ttk.END)
            else:
                self.hour = int(self.hourtxt.get())
                self.hourentry.delete(0, ttk.END)
                print(self.hour)
                self.setalarm()
        except Exception as e:
            messagebox.showerror("Error", "PLease Enter an integer (0-24)!")
            self.hourentry.delete(0, ttk.END)

    def setmin(self, event=None):
        print("Minute pressed")
        try:
            if int(self.mintxt.get()) > 59 or int(self.mintxt.get()) < 0:
                messagebox.showerror("Error", "Please enter a valid integer (0-59).")
                self.minentry.delete(0, ttk.END)
            else:
                self.min = int(self.mintxt.get())
                self.minentry.delete(0, ttk.END)
                print(self.hour)
                self.setalarm()
        except Exception as e:
            messagebox.showerror("Error", "PLease Enter an integer (0-59)!")
            self.minentry.delete(0, ttk.END)

    def setalarm(self):
        #######   function will only call when setmin or sethour is called
        if self.hour < 10 and self.min < 10: #checking if it is 2 digits or not
            self.alarmtime.set(f"0{self.hour}:0{self.min}")
        elif self.hour < 10:
            self.alarmtime.set(f"0{self.hour}:{self.min}")
        elif self.min < 10:
            self.alarmtime.set(f"{self.hour}:0{self.min}")
        else:
            self.alarmtime.set(f"{self.hour}:{self.min}")

        messagebox.showinfo(title="Alarm Set", message=f"Alarm has been set to {self.alarmtime.get()}.")


    def checkalarm(self):
        now = dt.datetime.now()
        if now.hour == self.hour and now.minute == self.min:
            print("alarm clokc linging!!!")
            pygame.mixer.music.play(-1)
            response = messagebox.askyesno("Alarm Clock Ringing", f"It's {self.alarmtime.get()}! \n"
                                                       f"Do you want to snooze?")
            if response:
                pygame.mixer.music.stop()
                self.min += 5
                if self.min > 59:
                    self.hour += 1
                    self.min -= 60
                self.setalarm()
            if not response:
                pygame.mixer.music.stop()
                self.root.after(60000, self.checkalarm)  #prevent alarm from ringing twice
                return
        self.root.after(1000, self.checkalarm)

    def updatetime(self):
        now = dt.datetime.now()
        if now.hour < 10 and now.minute < 10 and now.second < 10:  # Checking if all are single digits
            self.currenttime.set(f"0{now.hour}:0{now.minute}:0{now.second}")
        elif now.hour < 10 and now.minute < 10:
            self.currenttime.set(f"0{now.hour}:0{now.minute}:{now.second}")
        elif now.hour < 10 and now.second < 10:
            self.currenttime.set(f"0{now.hour}:{now.minute}:0{now.second}")
        elif now.minute < 10 and now.second < 10:
            self.currenttime.set(f"{now.hour}:0{now.minute}:0{now.second}")
        elif now.hour < 10:
            self.currenttime.set(f"0{now.hour}:{now.minute}:{now.second}")
        elif now.minute < 10:
            self.currenttime.set(f"{now.hour}:0{now.minute}:{now.second}")
        elif now.second < 10:
            self.currenttime.set(f"{now.hour}:{now.minute}:0{now.second}")
        else:
            self.currenttime.set(f"{now.hour}:{now.minute}:{now.second}")

        self.root.after(1000, self.updatetime)






if __name__ == "__main__":
    AlarmClock()