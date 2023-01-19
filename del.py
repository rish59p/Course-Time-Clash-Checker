import PyPDF2 as pdf
import pandas as pd
import tabula as tb
import numpy as np

#courselistdum = tb.read_pdf("R:\ML-CruX\Proj-1\Data\TIMETABLE II SEMESTER 2022 -23(1)(1).pdf", pages='all')
#tb.convert_into("Data\Draft Timetable II Sem 2022 -23 STUDENTS .pdf", "Proj-1\Data\courselist.csv", output_format="csv", pages = 'all')
clsheet = pd.read_csv(r"Data\courselist.csv")
courselist = pd.DataFrame(data=clsheet)
reccl = courselist.iloc[:,[1,9,10,11]]
print("Enter your Branch: (CS/ECE/EEE/ENI/MECH/CHEM/CIVIL/BPHARM/{for dual degree: enter as follows MATH+ENI})")
branch = input()
print ("Enter your Year and Semester: (ex: 2-II) ")
year = input()
cdclist = pd.read_csv(r"Data\cdc.csv")
shortlist=pd.DataFrame(data=cdclist.loc[((cdclist['YEAR']==year)&(cdclist['BRANCH']==branch))])
start = shortlist.axes[0][0]
size = shortlist.shape[0]
dum = np.array(reccl[reccl["COURSE NO."]==shortlist['CDCs'][start]][["COMPRE\rDATE &\rSESSION","Unnamed: 10", "Unnamed: 11"]])
timeutil = pd.DataFrame(data=dum)
for i in range(start+1,start+size):
    dumarr = np.array(reccl[reccl["COURSE NO."]==shortlist['CDCs'][i]][["COMPRE\rDATE &\rSESSION","Unnamed: 10", "Unnamed: 11"]])
    dumdf = pd.DataFrame(data=dumarr)
    timeutil = pd.concat([timeutil,dumdf], ignore_index=True)
print(f"Enter the Course Code of Your Huel/Del: ")
reqcourse = input()
time = reccl[reccl["COURSE NO."]==reqcourse][["COMPRE\rDATE &\rSESSION","Unnamed: 10","Unnamed: 11"]]
end = timeutil.shape[0]
count = 0
for j in range(0,end-1):
    if (((time.loc[time.first_valid_index()][0] == timeutil.loc[j][0])&(time.loc[time.first_valid_index()][1] == timeutil.loc[j][1]))|(time.loc[time.first_valid_index()][2] == timeutil.loc[j][2])):
        print("Time Clash detected!")
        print("You cannot take", reqcourse, "course")
        count=0
        break
    else:
        count=1

if (count == 1): 
    print("You can take the course: ", reqcourse, " without any clash")
