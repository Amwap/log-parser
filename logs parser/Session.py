# -*- coding: utf-8 -*-
class Session:
    def __init__(self, id):
        self.id = id
        self.list = []
    
    def separator(self, session_id, new_log): # session_id = (INTERFACE, MAC)
            if self.id != session_id:
                if self.id[0] != session_id[0] and self.id[1] != session_id[1]:
                    return None

                elif self.id[0] != session_id[0] and self.id[1] == session_id[1]:
                    return [self.id, session_id]

                elif self.id[0] == session_id[0] and self.id[1] != session_id[1]:
                    return None

            elif new_log[4] == "connected":
                if len(self.list) == 0:
                    self.list.append(new_log)
                    return None

                elif self.list[-1][4] == "reassociating":
                    self.list.append(new_log)
                    return None
                
                else:
                    return [self.id,self.id]

            elif new_log[4] == "reassociating":
                self.list.append(new_log)
                return None

            elif new_log[4] == "disconnected":
                self.list.append(new_log)
                return self.id
