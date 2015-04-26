from collections import deque

# Disjoint trees can be present
# Simple greedy DFS won't work
# Check for all possible DFS outcomes and choose the best one
	
#connections = ["","2 3 5","4 5","5 6","7","7 8","8 9","10", "10 11 12","11","12","12",""]
#cost =["","3 2 9","2 4","6 9","3","1 2","1 2","5", "5 6 9","2","5","3",""]
connections = ["","2 3","3 4 5","4 6","5 6","7","5 7",""]
cost = ["","30 50","19 6 40","12 10","35 23","8","11 20",""]

conList = [ [ int(element) for element in a.split(" ") ] if a is not "" else []  for a in connections  ]
costList = [ [ int(element) for element in a.split(" ") ] if a is not "" else []  for a in cost  ]

AdMatrix = [ [0]*len(conList) for a in range(len(conList))]
for (index,(con,cost)) in enumerate(zip( conList, costList)):
	if con == [] or cost == [] :
		continue 
	else:
		for (col, value) in zip( con, cost ):
			AdMatrix[ index ][ col ] = value

def findRoot( AdMatrix ):
	Roots = []
	for col in range(len(AdMatrix)):
		if sum([ row[ col ] for row in AdMatrix ]) == 0:
			Roots.append( col )	
	return Roots



def DFS( root , cost, AdMatrix ):
	increment = max( AdMatrix[ root ] )
	if increment  == 0 :
		return cost
	else:
		cost = max([ DFS( index , cost + AdMatrix[ root ][ index ] , AdMatrix ) if child!=0 else 0 for index,child in enumerate(AdMatrix[ root ]) ])
		return cost	

cost = []
#print findRoot( AdMatrix )
for root in findRoot( AdMatrix):
	cost.append(DFS( root, 0 , AdMatrix ))

print max(cost)

