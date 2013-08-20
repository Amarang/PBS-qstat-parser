import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time


inp = open("usermon.txt","r")

data = {}
for line in inp.readlines():
    if(line[:2]=="##"): continue
    v = line.split()
    
    # v[-1] --> last one should be time
    utcTime = round(1.0*int(v[-1])/10) * 10
    username = v[0]
    runningJobs = int(v[1])
    queuedJobs = int(v[2])
    if(utcTime not in data):
        data[utcTime] = []
    
    data[utcTime].append([username, runningJobs, queuedJobs])
    
def getJobUsage(data, filterByUser=None):
    timestamps = []
    values = []

    for key in data:
        timestamps.append(key)
        
        values.append(sum([e[1]+e[2] for e in data[key] if (e[0]==filterByUser or filterByUser is None)]))
    
    temp = zip(timestamps, values)
    temp.sort()
    timestamps, values = zip(*temp) 
    dates=[dt.datetime.fromtimestamp(ts) for ts in timestamps]
    return dates, values
# print values 

#print temp

users = []
for k in data.keys():
    for e in data[k]:
        users.append(e[0])
users = list(set(users))
users.append(None)

plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation=25 )
ax=plt.gca()
xfmt = md.DateFormatter('%d %b %H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_yscale('log')

for user in users:
    dates, values = getJobUsage(data, user)
    plt.plot(dates,values,label=user)
ax.legend(bbox_to_anchor=(0.9, 1.0), loc=2, borderaxespad=0.)
plt.show()