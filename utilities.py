import os, sys


def removeDuplicates(ls,index=None):
	"""
	removeDuplicates(list,index=None)
	
	Returns list with no duplicates.
	
	If index specified, duplication checking will be
	done by comparing the index'th value of each element
	(i.e., uniquification is done using a specified column
	of a 2D list, if specified)
	"""
	outls = []
	checkls = []
	if(index is None):
		for elem in ls:
			if(elem not in outls):
				outls.append(elem)
	else:
		if(index < len(ls[0])):
			for elem in ls:
				if(elem[index] not in checkls):
					checkls.append(elem[index])
					outls.append(elem)
		else:
			print "index out of range. returning input."
			return ls
	return outls
    
def frequencyDictionary(ls):
    """
    frequencyDictionary(ls)
    
    Creates a dictionary where keys are the unique
    elements of the input list, and values are the
    associated frequencies of the keys in the list.
    """
    d = {}
    for e in ls:
        if e in d: d[e] += 1
        else: d[e] = 0
    return d

def printDictionary(d):
    """
    printDictionary(d)
    
    Prints a dictionary in a pretty way
    """
    for k, v in d.items():
        print "%s\t%s" % (str(k), str(v))
		
def avg(ls):
	"""
	avg(list)
	
	Returns the average of the input list.
	"""
	return float(sum(ls))/len(ls)
    
def handleParams():
    """
    handleParams()
    
    Takes piped arguments and appends them to end of command line
    arguments. Returns a list.   
    """
    args = sys.argv
    if not sys.stdin.isatty():
        args += sys.stdin.read().replace('\n','').replace('\r','').split(' ')
        args = filter(None, args) # removes empty elems
    return args
 