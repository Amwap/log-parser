# -*- coding: utf-8 -*-
import os
import re
from Session import Session
from Log import Log
import shutil

def parsing():
    
    session_list = []
    buffer = {}
    log_list = [[[]]]

    config = open(".\config.txt")
    path_to_main_dir = config.readline()
    for file in os.listdir(path_to_main_dir):
        shutil.copy(path_to_main_dir+"\\"+file, ".\Логи")

    for file in os.listdir(".\Логи"):
        f = open(".\Логи\\" + file)
        for line in f:
            log_split = re.split(r" |@|,", str(line[:-1]))
            if line[48] == "@":
                DATE = log_split[0] 
                TIME = log_split[1]
                MAC = log_split[4]
                INTERFACE = log_split[5]
                STATUS = log_split[6]
                INFO = ""

                for word in log_split[7:]:
                    INFO = INFO + " " + word
                #           0     1     2       3        4      5               
                new_log = (DATE, TIME, MAC, INTERFACE, STATUS, INFO)
                session_id = (MAC,INTERFACE)

                if len(buffer.keys()) != 0:
                    for item in buffer.copy().keys():
                        key = buffer[item].separator(session_id,new_log)
                        if type(key) is tuple:
                            log_list.append(buffer.pop(key).list)

                        elif type(key) is list:
                            buffer[key[1]] = Session(key[1])
                            buffer[key[1]].separator(session_id,new_log)
                            log_list.append(buffer.pop(key[0]).list)

                else:
                    buffer[session_id] = Session(session_id)
                    key = buffer[session_id].separator(session_id,new_log)
                    if type(key) is tuple:
                        log_list.append(buffer.pop(key).list)

                    elif type(key) is list:
                        buffer[key[1]] = Session(key[1])
                        buffer[key[1]].separator(session_id,new_log)
                        log_list.append(buffer.pop(key[0]).list)

                if not session_id in buffer.keys() and log_list[-1][-1] != new_log:
                    buffer[session_id] = Session(session_id)
                    key = buffer[session_id].separator(session_id,new_log)
                    if type(key) is tuple:
                        log_list.append(buffer.pop(key).list)

        for key in buffer.copy().keys():
            log_list.append(buffer.pop(key).list)

        f.close()

    for l in log_list:
        if l !=[[]]:
            session_list.append(Log(l))


    return session_list