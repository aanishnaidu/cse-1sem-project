import serial
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
from datetime import datetime

FMT = '%H:%M:%S'



global starttime
global starttime1
global starttime2
global starttime3

global n
n=0
global n1
n1=0
global n2
n2=0
global n3
n3=0
global m
m=0
global m1
m1=0
global m2
m2=0
global m3
m3=0


listforled1=[]
listforled2=[]
listforled3=[]
listforled4=[]
daylist=[]
daylist1=[]
daylist2=[]
daylist3=[]


arduinoData = serial.Serial("com10",9600)



scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('SpreadsheetExample-d3073b7321fe.json',scope)
gc = gspread.authorize(credentials)
wks=gc.open('iot').sheet1##wks is the file name so use it

##row,coloum
j1=3#increment for a cycle of on and off
k1=1#incriment only for a day
j2=3
j3=3
j4=3
k2=2
k3=3
k4=4


wks.update_cell(5,5,'hi')
constant_time=1


while(1==1):
    x=(arduinoData.read().decode('utf-8'))
    print(x)

    
    present_time=datetime.now().strftime("%d")
    difference=int(present_time)-constant_time


        
    if(x=='1'):
        
        if(n!=1):
            
            time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("start time = ",time) ##there is upload to be done here this is the start time
            starttime=(datetime.now().strftime('%H:%M:%S'))
            daylist.append(starttime)
            wks.update_cell(k1,j1,starttime)
            n=1
            m=0       
    elif(x=='2'):
        if(m!=2):
            
            endtime=(datetime.now().strftime('%H:%M:%S'))
            print(endtime)##there is no upload required but this is the end time
            
            time_interval= (datetime.strptime(endtime, FMT) - datetime.strptime(starttime, FMT))
            tdelta=str(time_interval)
            print(tdelta)##this is to be uploaded this is the duration 
            daylist.append(tdelta)

            
            
            wks.update_cell(k1,j1,starttime)
            
            j1+=1
            wks.update_cell(k1,j1,tdelta)
            ##this is to be uploaded this is the start time and duration
            n=0
            m=2
            j1+=1
    elif(x=='3'):
        if(n1!=1):
            time1=(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print("start time = ",time1) ##there is upload to be done here this is the start time
            starttime1=(datetime.now().strftime('%H:%M:%S'))
            daylist1.append(starttime1)
            n1=1
            m1=0
    elif(x=='4'):
        if(m1!=2):
            endtime1=(datetime.now().strftime('%H:%M:%S'))
            print(endtime1)##there is no upload required but this is the end time
            
            time_interval1= (datetime.strptime(endtime1, FMT) - datetime.strptime(starttime1, FMT))
            tdelta1=str(time_interval1)
            print(tdelta1)##this is to be uploaded this is the duration 
            daylist1.append(tdelta1)

            
            
            wks.update_cell(k2,j2,starttime1)
            
            j2+=1
            wks.update_cell(k2,j2,tdelta1)
            ##this is to be uploaded this is the start time and duration
            n1=0
            m1=2
            j2+=1
    elif(x=='5'):
        if(n2!=1):
            time2=(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print("start time = ",time2) ##there is upload to be done here this is the start time
            starttime2=(datetime.now().strftime('%H:%M:%S'))
            daylist2.append(starttime2)
            n2=1
            m2=0
    elif(x=='6'):
        if(m2!=2):
            endtime2=(datetime.now().strftime('%H:%M:%S'))
            print(endtime2)##there is no upload required but this is the end time
            
            time_interval2= (datetime.strptime(endtime2, FMT) - datetime.strptime(starttime2, FMT))
            tdelta2=str(time_interval2)
            print(tdelta2)##this is to be uploaded this is the duration 
            daylist2.append(tdelta2)

            
            
            wks.update_cell(k3,j3,starttime2)
            
            j3+=1
            wks.update_cell(k3,j3,tdelta2)
            ##this is to be uploaded this is the start time and duration
            n2=0
            m2=2
            j3+=1
    elif(x=='7'):
        if(n3!=1):
            time3=(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print("start time = ",time3) ##there is upload to be done here this is the start time
            starttime3=(datetime.now().strftime('%H:%M:%S'))
            daylist3.append(starttime3)
            n3=1
            m3=0
    elif(x=='8'):
        if(m3!=2):
            endtime3=datetime.now().strftime('%H:%M:%S')
            print(endtime3)##there is no upload required but this is the end time
            
            time_interval3= datetime.strptime(endtime3, FMT) - datetime.strptime(starttime3, FMT)
            tdelta3=str(time_interval3)
            print(tdelta3)##this is to be uploaded this is the duration 
            daylist3.append(tdelta3)

            
            
            wks.update_cell(k4,j4,starttime3)
            
            j4+=1
            wks.update_cell(k4,j4,tdelta3)
            ##this is to be uploaded this is the start time and duration
            n3=0
            m3=2
            j4+=1
    elif(difference>0):
        j1=3               #j1 is coloum reset
        j2=3
        j3=3
        j4=3
        k1=4*difference      #k1 is row increment
        k2=4*difference
        k3=4*difference
        k4=4*difference
        listforled1.append(daylist)
        listforled2.append(daylist1)
        listforled3.append(daylist2)
        listforled4.append(daylist3)
        daylist.clear()
        daylist1.clear()
        daylist2.clear()
        daylist3.clear()
    for i in range (len(listforled1)):
        for j in range(0,len(listforled1[i]),2):
            object1 = datetime.strptime(listforled1[i][j],FMT)
            object2 = datetime.strptime(listforled1[i][j+1],FMT)
            min1 = object1 - timedelta(seconds=600)
            min2 = object2 - timedelta(seconds=600)
            max1 = object1 + timedelta(seconds=600)                            
            max2 = object2 + timedelta(seconds=600)
      


         
        for k in range(len(listforled1)):
            if(k!=i):
                for l in range(0,len(listforled1[k]),2):
                    object3 = datetime.strptime(listforled1[k][l],FMT)
                    object4 = datetime.strptime(listforled1[k][l+1],FMT)
                     
                     
                    if(object3>=min1 and object3<=max1):
                        if(object4<=max2 and object4>= min2):
                            arduinoData.write('2')
    for i in range (len(listforled2)):
        for j in range(0,len(listforled2[i]),2):
            object1 = datetime.strptime(listforled2[i][j],FMT)
            object2 = datetime.strptime(listforled2[i][j+1],FMT)
            min1 = object1 - timedelta(seconds=600)
            min2 = object2 - timedelta(seconds=600)
            max1 = object1 + timedelta(seconds=600)                            
            max2 = object2 + timedelta(seconds=600)
  


         
        for k in range(len(listforled2)):
            if(k!=i):
                for l in range(0,len(listforled2[k]),2):
                    object3 = datetime.strptime(listforled2[k][l],FMT)
                    object4 = datetime.strptime(listforled2[k][l+1],FMT)
                     
                     
                    if(object3>=min1 and object3<=max1):
                        if(object4<=max2 and object4>= min2):
                            arduinoData.write('4')
    for i in range (len(listforled3)):
        for j in range(0,len(listforled3[i]),2):
            object1 = datetime.strptime(listforled3[i][j],FMT)
            object2 = datetime.strptime(listforled3[i][j+1],FMT)
            min1 = object1 - timedelta(seconds=600)
            min2 = object2 - timedelta(seconds=600)
            max1 = object1 + timedelta(seconds=600)                            
            max2 = object2 + timedelta(seconds=600)
      


         
        for k in range(len(listforled3)):
            if(k!=i):
                for l in range(0,len(listforled3[k]),2):
                    object3 = datetime.strptime(listforled3[k][l],FMT)
                    object4 = datetime.strptime(listforled3[k][l+1],FMT)
                     
                     
                    if(object3>=min1 and object3<=max1):
                        if(object4<=max2 and object4>= min2):
                            arduinoData.write('6')
    for i in range (len(listforled4)):
        for j in range(0,len(listforled4[i]),2):
            object1 = datetime.strptime(listforled4[i][j],FMT)
            object2 = datetime.strptime(listforled4[i][j+1],FMT)
            min1 = object1 - timedelta(seconds=600)
            min2 = object2 - timedelta(seconds=600)
            max1 = object1 + timedelta(seconds=600)                            
            max2 = object2 + timedelta(seconds=600)
  


         
        for k in range(len(listforled4)):
            if(k!=i):
                for l in range(0,len(listforled4[k]),2):
                    object3 = datetime.strptime(listforled4[k][l],FMT)
                    object4 = datetime.strptime(listforled4[k][l+1],FMT)
                     
                     
                    if(object3>=min1 and object3<=max1):
                        if(object4<=max2 and object4>= min2):
                            arduinoData.write('8')
        
    
    
    






