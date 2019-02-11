 # -*- coding: utf-8 -*-
from tkinter import *

from time import strftime as stt
from datetime import datetime as dt
import Search
import pyperclip
import Parser

back_ground = "white"
font_ground = "black"


class Window:
    def __init__(self,session_list):
        self.session_list = session_list
        self.drop_check = False

        self.window = Tk()
        self.window.title("Мечта, если дать ей волю, всегда одолеет реальность")

        labelFrom = Label(text="From",fg=font_ground, bg=back_ground)  .grid(row=2, column=1, sticky=W)
        labelTo = Label(text="To",fg=font_ground, bg=back_ground)      .grid(row=3, column=1, sticky=W)

        labelYear = Label(text="Year",fg=font_ground, bg=back_ground)  .grid(row=1, column=2, sticky=W)
        labelMonth = Label(text="Month",fg=font_ground, bg=back_ground).grid(row=1, column=4, sticky=W)
        labelDay = Label(text="Day",fg=font_ground, bg=back_ground)    .grid(row=1, column=6, sticky=W)
        labelHour = Label(text="Hour",fg=font_ground, bg=back_ground)  .grid(row=1, column=8, sticky=W)
        labelMin = Label(text="Min",fg=font_ground, bg=back_ground)    .grid(row=1, column=10,sticky=W)
        labelSec = Label(text="Sec",fg=font_ground, bg=back_ground)    .grid(row=1, column=12,sticky=W)
        labelMac = Label(text="Mac address",fg=font_ground, bg=back_ground).grid(row=2, column=16)

        labelMac = Label(text="        From Date       /     Time                      To Date        /    Time                                 MAC                            Session time",
                         fg=font_ground, bg=back_ground).grid(row=5, column=1, columnspan=20,sticky=W)

        labelSlash1 = Label(text="/",fg=font_ground, bg=back_ground)   .grid(row=2, column=3, sticky=W)
        labelSlash2 = Label(text="/",fg=font_ground, bg=back_ground)   .grid(row=2, column=5, sticky=W)
        labelSlash3 = Label(text="/",fg=font_ground, bg=back_ground)   .grid(row=3, column=3, sticky=W)
        labelSlash4 = Label(text="/",fg=font_ground, bg=back_ground)   .grid(row=3, column=5, sticky=W)

        labelDash1 = Label(text=" - ",fg=font_ground, bg=back_ground)  .grid(row=2, column=7, sticky=W)
        labelDash2 = Label(text=" - ",fg=font_ground, bg=back_ground)  .grid(row=3, column=7, sticky=W)
        labelDash3 = Label(text="  ",fg=font_ground, bg=back_ground)   .grid(row=2, column=13,sticky=W)
        labelDash4 = Label(text="  ",fg=font_ground, bg=back_ground)   .grid(row=3, column=13,sticky=W)
        labelDash5 = Label(text="  ",fg=font_ground, bg=back_ground)   .grid(row=3, column=15,sticky=W)
        labelDash6 = Label(text="  ",fg=font_ground, bg=back_ground)   .grid(row=3, column=15,sticky=W)
        labelDash7 = Label(text="  ",fg=font_ground, bg=back_ground)   .grid(row=2, column=17,sticky=W)
        labelDash7 = Label(text="  ",fg=font_ground, bg=back_ground)   .grid(row=6, column=1, sticky=W)
        labelDash7 = Label(text="  ",fg=font_ground, bg=back_ground)   .grid(row=4, column=1, sticky=W)

        labelColon1 = Label(text=":",fg=font_ground, bg=back_ground)   .grid(row=2, column=9, sticky=W)
        labelColon2 = Label(text=":",fg=font_ground, bg=back_ground)   .grid(row=2, column=11,sticky=W)
        labelColon3 = Label(text=":",fg=font_ground, bg=back_ground)   .grid(row=3, column=9, sticky=W)
        labelColon4 = Label(text=":",fg=font_ground, bg=back_ground)   .grid(row=3, column=11,sticky=W)


        self.fromYear = Entry(self.window, width=5, bg=back_ground);  self.fromYear.grid(row=2, column=2, sticky=W)
        self.fromMonth = Entry(self.window, width=5, bg=back_ground); self.fromMonth.grid(row=2, column=4)
        self.fromDay = Entry(self.window, width=5, bg=back_ground);   self.fromDay.grid(row=2, column=6, sticky=W)
        self.fromHour = Entry(self.window, width=5, bg=back_ground);  self.fromHour.grid(row=2, column=8, sticky=W)
        self.fromMin = Entry(self.window, width=5, bg=back_ground);   self.fromMin.grid(row=2, column=10,sticky=W)
        self.fromSec = Entry(self.window, width=5, bg=back_ground);   self.fromSec.grid(row=2, column=12,sticky=W)

        self.toYear = Entry(self.window, width=5, bg=back_ground);    self.toYear.grid(row=3, column=2, sticky=W)
        self.toMonth = Entry(self.window, width=5, bg=back_ground);   self.toMonth.grid(row=3, column=4)
        self.toDay = Entry(self.window, width=5, bg=back_ground);     self.toDay.grid(row=3, column=6, sticky=W)
        self.toHour = Entry(self.window, width=5, bg=back_ground);    self.toHour.grid(row=3, column=8, sticky=W)
        self.toMin = Entry(self.window, width=5, bg=back_ground);     self.toMin.grid(row=3, column=10,sticky=W)
        self.toSec = Entry(self.window, width=5, bg=back_ground);     self.toSec.grid(row=3, column=12,sticky=W)

        self.Mac = Entry(self.window, width=20, bg=back_ground); self.Mac.grid(row=3, column=16,sticky=W)
        
        self.dropButton = Button(self.window, text="Drop", bg="silver", command=self.drop)              .grid(row=1, column=14,sticky=W)
        self.fromButton = Button(self.window, text="This day", bg="silver", command=self.this_day)          .grid(row=2, column=14,sticky=W)
        self.toButton = Button(self.window, text="Copy MAC", bg="silver", command=self.last_input)          .grid(row=3, column=14,sticky=W)
        self.goButton = Button(self.window, text="Go!",height = 3, width = 7, bg="silver", command=self.go) .grid(row=2, column=18,rowspan=2, sticky=W)

        txt_frame = Frame(self.window)
        txt_frame.grid(row=6, column=1,columnspan=20, sticky=W)

        self.logList = Text(txt_frame, borderwidth=3, relief="sunken")
        self.logList.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        scroll = Scrollbar(txt_frame, command=self.logList.yview)
        scroll.grid(row=0, column=1, sticky='nsew')
        self.logList['yscrollcommand'] = scroll.set


        self.go()
        self.window.mainloop()

    def go(self):
        self.logList.delete(1.0,END)
        for session in Search.search(self.session_list, self.get_date(), self.Mac.get()):
            time_in = str(session.TIME_IN)
            time_out = str(session.TIME_OUT)
            time = str(session.TIME)
            user = session.INTERFACE
            inter = session.INTERFACE
            if time_in == "()":
                time_in = "????-??-?? ??:??:??"

            if time_out == "()":
                time_out = "????-??-?? ??:??:??"

            if time == "()":
                time = "No time"

            self.logList.insert(1.0,"| " + time_in +" | "+ time_out +" | "+ user +" | "+ time +"\n" )

    def this_day(self):
        self.drop()
        self.fromYear.insert(0,stt("%Y")) # в stt импортируется strftime модуля time
        self.fromMonth.insert(0,stt("%m"))
        self.fromDay.insert(0,stt("%d"))
        self.fromHour.insert(0,"0")
        self.fromMin.insert(0,"0")
        self.fromSec.insert(0,"0")

        self.toYear.insert(0,stt("%Y"))
        self.toMonth.insert(0,stt("%m"))
        self.toDay.insert(0,stt("%d"))
        self.toHour.insert(0,"23")
        self.toMin.insert(0,"59")
        self.toSec.insert(0,"59")

    def drop(self):
        self.Mac.delete(0,END)

        self.fromYear.delete(0,END)
        self.fromMonth.delete(0,END)
        self.fromDay.delete(0,END)
        self.fromHour.delete(0,END)
        self.fromMin.delete(0,END)
        self.fromSec.delete(0,END)

        self.toYear.delete(0,END)
        self.toMonth.delete(0,END)
        self.toDay.delete(0,END)
        self.toHour.delete(0,END)
        self.toMin.delete(0,END)
        self.toSec.delete(0,END)

    def last_input(self):        
        self.Mac.insert(0,pyperclip.paste())

    def get_date(self):
        if self.fromYear.get() == '' and self.toMin.get() == '':
            range = None

        else:
            range = (
                dt(int(self.fromYear.get()), int(self.fromMonth.get()), int(self.fromDay.get()),
                   int(self.fromHour.get()), int(self.fromMin.get()),   int(self.fromSec.get())),

                dt(int(self.toYear.get()), int(self.toMonth.get()), int(self.toDay.get()),
                   int(self.toHour.get()), int(self.toMin.get()),   int(self.toSec.get()))
                )
        
        return range

window = Window(Parser.parsing())
