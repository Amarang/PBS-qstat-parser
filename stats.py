import commands, model as m, utilities as u



jobList = m.parseInfo()
runningls = []
queuedls = []
users = []
cores = {}
for j in jobList:
    user = j.getUsername()
    users.append(user)
    if j.isRunning():
        runningls.append(user)
        #if(user == "therealc"): print "DFDFDF"
        if(user not in cores): cores[user] = 0
        cores[user] += j.getNumCores()
    else:
        queuedls.append(user)
        
#print runningls
users = u.removeDuplicates(users)
#print users
userRunning = u.frequencyDictionary(runningls)
#print userRunning["therealc"]
userQueued = u.frequencyDictionary(queuedls)
  
print "####"
date = commands.getstatusoutput("date +%s")[1]

for user in users:
    print user, 
    
    try: print userRunning[user], 
    except: print 0,
    
    try: print userQueued[user],
    except: print 0,
    
    try: print cores[user],
    except: print 0,
    
    print date
print "####"
