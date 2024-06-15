# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:24:01 2024

@author: mamin
"""

from datetime import timedelta as td

from TR import TRA

#0:HF,1:HN,2:FY,3:BZ,4:BB,5:HB,6:SZ,7:CZ,8:MAS,9:WH
#10:XC,11:HS,12:TL,13:CZ,14:AQ,15:LA

"""
Part 1: 0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-0-15-0
"""
[X01,N01]=TRA.ReadData("01")
[X12,N12]=TRA.ReadData("12")
[X23,N23]=TRA.ReadData("23")
[X34,N34]=TRA.ReadData("34")
[X45,N45]=TRA.ReadData("45")
[X56,N56]=TRA.ReadData("56")
[X67,N67]=TRA.ReadData("67")
[X78,N78]=TRA.ReadData("78")
[X89,N89]=TRA.ReadData("89")
[X910,N910]=TRA.ReadData("910")
[X1011,N1011]=TRA.ReadData("1011")
[X1112,N1112]=TRA.ReadData("1112")
[X1213,N1213]=TRA.ReadData("1213") 
[X1314,N1314]=TRA.ReadData("1314") 
[X140,N140]=TRA.ReadData("140") 
[X015,N015]=TRA.ReadData("015") 
[X150,N150]=TRA.ReadData("150") 

MaxT=td(days=20)
BestR=[]

Route1=[X12,X23,X34,X45,X56,X67,X78,X89,X910,X1011,X1112,X1213,X1314,X140,X015,X150]

for staTra in X01:
    Otime=staTra.start
    Stime=staTra.arrive
    TalT=Stime-Otime
    tR=[staTra]
    for M in Route1:
        K=[x for x in M if x.start>Stime]
        if not K:
            K=M[0]
            Otime=K.arrive
            TalT=TalT+td(days=1)+Otime-Stime
            Stime=Otime
            tR.append(K)
        else:
            K=K[0]
            Otime=K.arrive
            TalT=TalT+Otime-Stime
            Stime=Otime
            tR.append(K)
            
    if TalT<MaxT:
        BestR=tR
        MaxT=TalT
            
with open("results.txt","w") as file:
    file.write('Route1:\n')
    for x in BestR:
        file.write(x.print()+'\n')
        
    file.write('Tatal Time: '+str(MaxT))
        
    
    
           