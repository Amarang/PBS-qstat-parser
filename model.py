import commands

class Node:
    def __init__(self,nodeID,cores):
        self.nodeID = nodeID
        self.cores=cores
        
    def getCores(self): return self.cores
    def getID(self): return self.nodeID
    def getNumCores(self): return len(self.cores)
        
class Job:
    def __init__(self):
        self.jobID = ""
        self.nodes = []
        
    def populateInfo(self, jobls, line):
        self.jobID =  jobls[0]
        self.username =  jobls[1]
        self.queue =  jobls[2]
        self.jobName =  jobls[3]
        self.sessionID =  jobls[4]
        self.numNodes =  jobls[5]
        self.numCores =  jobls[6]
        self.memory =  jobls[7]
        self.wallTime =  jobls[8]
        self.status = jobls[9]
        self.elapsedTime = jobls[10]
        self.coresString = jobls[11]
        if(self.isRunning()): self.makeNodes(self.numNodes, self.numCores, self.coresString)
        self.fullLine = line
        
    def makeNodes(self, nNodes, nCores, coresStr):
        cStr = coresStr.split("+")
        uniqueCPUs = list(set([i[1:].split("/")[0] for i in cStr]))
        #print uniqueCPUs
        for cpu in uniqueCPUs:
            #print cStr
            n = Node(cpu, [int(i.split("/")[1]) for i in cStr if cpu in i])
            self.nodes.append(n)
        
    def isRunning(self): return self.status == "R"
    def getID(self): return self.jobID
    def getUsername(self): return self.username
    def getQueue(self): return self.queue
    def getJobName(self): return self.jobName
    def getSessionID(self): return self.sessionID
    def getNumNodes(self): return self.numNodes
    def getNumCores(self): return self.numCores
    def getMemory(self): return self.memory
    def getNodes(self): return self.nodes
    def getWallTime(self):
        hh, mm = self.wallTime.split(":")
        return 3600*int(hh) + 60*int(mm)
    def getStatus(self): return self.status
    def getElapsedTime(self):
        hh, mm = self.elapsedTime.split(":")
        return 3600*int(hh) + 60*int(mm)
    def getCoresString(self): return self.coresString
    def getFullLine(self): return self.fullLine

def parseInfo():
    j = Job()
    jList = []
    (status, output) = commands.getstatusoutput('qstat -n -1')
    if(status != 0):
        print "Status error: %d != 0" % status
        return
    for line in output.split("\n")[5:]: # first 5 lines = junk
        j = Job()
        print line
        j.populateInfo(line.split(), line)
        jList.append(j)
    return jList
        
def main():
    
    jobList = parseInfo()
    
    for j in jobList:
        if(j.isRunning()):
            print j.getID(), j.getNodes()[0].getID(), j.getNodes()[0].getCores()
            
if __name__ == '__main__':
    main()
