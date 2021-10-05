import os
import csv
import sys

CandidateList=[]
CandidateVoteList=[]
TotalVotes=0

CsvPath= os.path.join("Resources","election_data.csv")

with open(CsvPath) as CsvFile:
    CsvReader= csv.reader(CsvFile, delimiter=",")

    for i in CsvReader:
        if TotalVotes>0:
            if not(i[2] in CandidateList):
                CandidateList.append(i[2])
        TotalVotes+=1
    for n in range(len(CandidateVoteList),len(CandidateList)):
        CandidateVoteList.append(0)
    
with open(CsvPath) as CsvFile:
    CsvReader= csv.reader(CsvFile, delimiter=",")
    count=0
    for i in CsvReader:
        if count>0:
            for j in range(len(CandidateList)):
                if CandidateList[j]==i[2]:
                    CandidateVoteList[j]=CandidateVoteList[j]+1
        count+=1
MaxIndex=0
MaxVotes=0
for i in range(len(CandidateVoteList)):
    if CandidateVoteList[i]>MaxVotes:
        MaxVotes=CandidateVoteList[i]
        MaxIndex=i
print("Election Results")
print("---------------------")
print(f"Total Votes: {TotalVotes-1}")
print("---------------------")
for i in range(len(CandidateList)):
    print(f"{CandidateList[i]}: {round(float(CandidateVoteList[i])*100/(TotalVotes-1),3)}%  ({CandidateVoteList[i]}) ")
print("---------------------")
print(f"Winner: {CandidateList[MaxIndex]}")
print("---------------------")


with open("Analysis/Analysis.txt","w") as f:
    sys.stdout=f
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {TotalVotes-1}")
    print("---------------------")
    for i in range(len(CandidateList)):
        print(f"{CandidateList[i]}: {round(float(CandidateVoteList[i])*100/(TotalVotes-1),3)}%  ({CandidateVoteList[i]}) ")
    print("---------------------")
    print(f"Winner: {CandidateList[MaxIndex]}")
    print("---------------------")