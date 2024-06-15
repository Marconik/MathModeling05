# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:27:53 2024

@author: mamin
"""

from datetime import timedelta as td

from TR import TRA

#0:HF,1:HN,2:FY,3:BZ,4:BB,5:HB,6:SZ,7:CZ,8:MAS,9:WH
#10:XC,11:HS,12:TL,13:CZ,14:AQ,15:LA

"""
Part 2: 0-14-13-12-11-9-10-8-7-6-5-4-3-2-1-15-0
"""
[X014,N014]=TRA.ReadData("014")
[X1413,N1413]=TRA.ReadData("1413")
[X1312,N1312]=TRA.ReadData("1312")
[X1211,N1211]=TRA.ReadData("1211")
[X119,N119]=TRA.ReadData("119")
[X910,N910]=TRA.ReadData("910")
[X108,N108]=TRA.ReadData("108")
[X87,N87]=TRA.ReadData("87")
[X76,N76]=TRA.ReadData("76")
[X65,N65]=TRA.ReadData("65")
[X54,N54]=TRA.ReadData("54")
[X43,N43]=TRA.ReadData("43")
[X32,N32]=TRA.ReadData("32") 
[X21,N21]=TRA.ReadData("21") 
[X115,N115]=TRA.ReadData("115") 
[X150,N150]=TRA.ReadData("150") 

MaxT=td(days=20)
BestR=[]

Route2=[X1413,X1312,X1211,X119,X910,X108,X87,X76,X65,X54,X43,X32,X21,X115,X150]

for staTra in X014:
    Otime=staTra.start
    Stime=staTra.arrive
    TalT=Stime-Otime
    tR=[staTra]
    for M in Route2:
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
            
with open("results2.txt","w") as file:
    file.write('Route2:\n')
    for x in BestR:
        file.write(x.print()+'\n')
        
    file.write('Tatal Time: '+str(MaxT))
        
    
    
           