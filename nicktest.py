import commands, model as m, utilities as u



jobList = m.parseInfo()
runningls = []
queuedls = []
users = []
for j in jobList:
    users.append(j.getUsername())
    if j.isRunning():
        runningls.append(j.getUsername())
    else:
        queuedls.append(j.getUsername())
        
users = u.removeDuplicates(users)
userRunning = u.frequencyDictionary(runningls)
userQueued = u.frequencyDictionary(queuedls)
#u.printDictionary(usernameDict)
  
print "####"
for user in users:
    print user, 
    
    try: print userRunning[user], 
    except: print 0,
    
    try: print userQueued[user],
    except: print 0,
    
    print commands.getstatusoutput("date +%s")[1]
print "####"