#coding: utf-8
from datetime import time, date
import datetime


def search(session_list, range, mac_addres):
    conclusion = []
    print(mac_addres)
    if range == None and mac_addres != '':
        for session in session_list:
            
            if session.INTERFACE == mac_addres:
                conclusion.append(session)

        return conclusion

    if range == None: 
        return session_list

    data_start = range[0]
    data_stop = range[1]
    
    for session in session_list:
        check = False
        mac = False
        if mac_addres == "":
            mac = True

        try:
            if session.TIME_OUT >= data_start and session.TIME_OUT <= data_stop:
                check = True
        except:
            pass

        try:
            if session.TIME_IN <= data_stop and session.TIME_IN >= data_start:
                check = True
        except:
            pass

        if session.INTERFACE == mac_addres:
            mac = True

        if check and mac:
            conclusion.append(session)
            
        
    return conclusion