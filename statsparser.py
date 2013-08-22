import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time, matplotlib, sys, os

inp = open("../usermon.txt","r")

data = {}
for line in inp.readlines():
    if(line[:2]=="##"): continue
    v = line.split()
    if(len(v) < 5):
        print v
    # v[-1] --> last one should be time
    utcTime = round(1.0*int(v[-1])/10) * 10
    username = v[0]
    runningJobs = int(v[1])
    queuedJobs = int(v[2])
    nCores = int(v[3])
    if(utcTime not in data):
        data[utcTime] = []
    
    data[utcTime].append([username, runningJobs, queuedJobs, nCores])

def getParameter(e, parameter):
    if(parameter is None): return e[1]+e[2]
    if(parameter == "running jobs"): return e[1]
    if(parameter == "queued jobs"): return e[2]
    if(parameter == "total jobs"): return e[1]+e[2]
    if(parameter == "cores"): return e[3]
    if(parameter == "cores per job"): 
        if e[1] == 0: return 0
        else: return e[3]/e[1]
    
def getJobUsage(data, filterByUser=None, parameter=None):
    timestamps = []
    values = []

    for key in data:
        timestamps.append(key)
        
        values.append(sum([getParameter(e,parameter) for e in data[key] if (e[0]==filterByUser or filterByUser is None)]))
    
    temp = zip(timestamps, values)
    temp.sort()
    timestamps, values = zip(*temp) 
    dates=[dt.datetime.fromtimestamp(ts) for ts in timestamps]
    return dates, values

users = []
for k in data.keys():
    for e in data[k]:
        users.append(e[0])
users = list(set(users))
users.append(None)

# format plot/axesi
font = {'size': 8}
matplotlib.rc('font', **font)
plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation=25 )
ax=plt.gca()
xfmt = md.DateFormatter('%d %b %H:%M')
ax.xaxis.set_major_formatter(xfmt)
# 
flag = "cores per job"
if len(sys.argv) == 2:
    flag = sys.argv[1]
    
for user in users:
    dates, values = getJobUsage(data, user, flag)
    plt.plot(dates,values,label=user)
ax.legend(loc=1, borderaxespad=0.5)#, prop={'size': 8})
plt.savefig("temp.png")
os.system("eog temp.png")
os.system("rm temp.png")
