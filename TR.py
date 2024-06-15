# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:28:45 2024

@author: mamin
"""

import pandas as pd
from datetime import timedelta as td

class TRA:
    def __init__(self,name,start,arrive):
        self.name=name
        self.start=td(hours=int(start[0:2]),minutes=int(start[3:5]))
        self.arrive=td(hours=int(arrive[0:2]),minutes=int(arrive[3:5]))
        
    def ReadData(filename):
        data=pd.read_csv(filename+'.csv',header=0)
        data=data.values
        Num=int(data.size/4)
        X=[]
        for i in range(Num):
            X.append(TRA(data[i][0],data[i][1],data[i][2]))
        return [X,Num]
    
    def print(self):
        return str(self.name)+' '+str(self.start)+' '+str(self.arrive)