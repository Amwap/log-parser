# -*- coding: utf-8 -*-
import datetime

def get_dt(tp):
    mounth = {"Jan": 1,"Feb": 2,"Mar":3,
                "Apr":4,"May":5,"Jun":6,
                "Jul":7,"Aug":8,"Sep":9,
                "Oct":10,"Nov":11,"Dec":12,}

    date = datetime.date(int(tp[0].split("/")[2]),int(mounth[tp[0].split("/")[0]]), int(tp[0].split("/")[1]))
    time = datetime.time(int(tp[1].split(":")[0]), int(tp[1].split(":")[1]), int(tp[1].split(":")[2]))
                    
    return datetime.datetime.combine(date, time)

class Log:
    def __init__(self, session_list): #list = [(DATE, TIME, MAC, INTERFACE, STATUS, INFO), ...]
        self.MAC = session_list[0][3]
        self.INTERFACE = session_list[0][2]
        self.TIME_IN = ()
        self.TIME_OUT = ()  #Jan/28/2019 08:12:21
        self.TIME = ()
        self.LOG_LIST = session_list

        
        if len(session_list) == 1:
            if session_list[0][4] == "disconnected":
                self.TIME_OUT = get_dt((session_list[0][0], session_list[0][1]))

            elif session_list[0][4] == "connected":
                self.TIME_IN = get_dt((session_list[0][0], session_list[0][1]))

        else:
            
            for log in session_list:
                if log[4] == "connected" and self.TIME_IN == ():
                    self.TIME_IN = get_dt((log[0], log[1]))

                elif log[4] == "disconnected" and self.TIME_OUT == ():
                    self.TIME_OUT = get_dt((log[0], log[1]))

            if self.TIME_IN != () and self.TIME_OUT != ():
                self.TIME = self.TIME_OUT - self.TIME_IN

