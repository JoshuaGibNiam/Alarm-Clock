import ttkbootstrap as ttk
import datetime as dt
import time
import threading

class AlarmClock:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")
        self.root.title("Alarm Clock")
        self.root.geometry("500x500")

        self.mainframe = ttk.Frame(self.root, padding=20)
        self.mainframe.pack(fill="x")

        self.labelstyle = ttk.Style()
        self.labelstyle.configure("Alarm.TLabel", background="indigo", foreground="white",
                                  font="Roboto 20 bold", borderwidth=2,
                                  relief="grooved", anchor="center")

        self.alarmtime = ttk.StringVar()
        self.alarmtime.set("7:00")   #default
        self.alarmlabel = ttk.Label(self.mainframe, style="Alarm.TLabel",
                                    textvariable=self.alarmtime, justify="center",
                                    anchor="center")
        self.alarmlabel.pack(side="top", fill="both", expand=True)




        self.root.mainloop()


if __name__ == "__main__":
    AlarmClock()