import matplotlib.pyplot as plt

class Rectangle():
	def __init__(self, cords ):
		self.topleft = tuple([ int(i) for i in cords.split(" ")[:2] ])
		self.bottomright = tuple([ int(i) for i in cords.split(" ")[2:] ])
		self.topright = ( self.topleft[ 0 ], self.bottomright[ 1] )
		self.bottomleft = (self.bottomright[ 0 ]  , self.topleft[ 1] )

	def RelativeLocation( self,  point ):
		# If inside or on Rect returns True
		x, y = point	
		if (self.topleft[ 0 ] <= x <= self.bottomright[ 0 ]) and ( self.topleft[ 1] <= y <= self.bottomright[ 1] ):
			return True
		else :
			return False
	
	def InRect( self,  point ):
		# If inside or on Rect returns True
		x, y = point	
		if (self.topleft[ 0 ] < x < self.bottomright[ 0 ]) and ( self.topleft[ 1] < y < self.bottomright[ 1] ):
			return True
		else :
			return False

	def OnRect( self,  point ):
		#print point 
		# if inside returns False on and outside returns true
		x, y = point	
		if x == self.topleft[ 0 ] and ( self.topleft[ 1]<= y <= self.topright[ 1 ] )  :
			return True
		elif x == self.bottomright[ 0 ] and ( self.bottomleft[ 1]<= y <= self.bottomright[ 1 ] )  :
			return True
		elif y == self.topleft[ 1 ] and ( self.topleft[ 0]<= x <= self.bottomleft[ 0 ] )  :
			return True
		elif y == self.bottomright[ 1 ] and ( self.topright[ 0]<= x <= self.bottomright[ 0 ] )  :
			return True
		else :
			return False
						
def CheckIntersection( RectList, point ):
	if sum([ 1 if Rect.RelativeLocation( point ) else 0 for Rect in RectList ] ) == 2:
		return True

def Machine( RectList, point1, point2 ):
	if point1[ 0 ] == point2[ 0 ] :
		Interpoint = ( point1[ 0 ] , 0.9*point1[ 1] + 0.1*point2[ 1 ] )  
	if point1[ 1 ] == point2[ 1 ] :
		Interpoint = (  0.9*point1[ 0] + 0.1*point2[ 0 ], point1[ 1 ] )  


	edges = sum([ 1 if Rect.OnRect( Interpoint  ) else 0 for Rect in RectList ] ) 
	inrect = sum([ 1 if Rect.InRect( Interpoint  ) else 0 for Rect in RectList ] )
	#print edges, inrect, point2
	if (edges >= 1) and ( inrect == 0 ) :
		return True
	else :
		return False

def RecursiveConnect(RectList, point, IntPoints, path ):
	path.append( point )
	#print point
	#print path
	#print len(IntPoints )
	#IntPoints.remove( point )
	sameX = { probe[1]-point[1] : probe    for probe in IntPoints if probe[ 0 ] == point[ 0 ] }
	sameXpos = [ sameX[ dist ] for dist in sorted(sameX) if dist > 0 ]
	sameXneg = [ sameX[ dist ] for dist in sorted(sameX) if dist < 0 ]

	sameY = { probe[0]-point[0] : probe    for probe in IntPoints if probe[ 1 ] == point[ 1 ] }
	sameYpos = [ sameY[ dist ] for dist in sorted(sameY) if dist > 0 ]
	sameYneg = [ sameY[ dist ] for dist in sorted(sameY) if dist < 0]

	#print sameXpos, sameXneg
	#print sameYpos, sameYneg
	
	points = []
	if len(sameXpos ) != 0:
		points.append( sameXpos[ 0 ] )
	if len(sameXneg) != 0 :
		points.append( sameXneg[ -1 ] )
	if len(sameYpos) != 0:
		points.append( sameYpos[ 0 ] )
	if len(sameYneg) != 0 :
		points.append( sameYneg[ -1 ] )
	
	for probe in points :
			if Machine(RectList, point , probe ) and ( probe not in path ):
				path = RecursiveConnect(RectList, probe , IntPoints, path )
				return path
	return path

				
#cordList = ["48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547" ,"0 -1 399 0", "0 599 399 600", "-1 0 0 599","399 0 400 599" ] 
cordList = ["-1 192 400 207", "-1 392 400 407", "120 -1 135 600", "260 -1 275 600","0 -1 399 0", "0 599 399 600", "-1 0 0 599","399 0 400 599" ]
#cordList = ["-1 292 400 307","0 -1 399 0", "0 599 399 600", "-1 0 0 599","399 0 400 599"]
#
#cordList =["-1 20 400 20", "-1 44 400 44", "-1 68 400 68", "-1 92 400 92",
# "-1 116 400 116", "-1 140 400 140", "-1 164 400 164", "-1 188 400 188",
# "-1 212 400 212", "-1 236 400 236", "-1 260 400 260", "-1 284 400 284",
# "-1 308 400 308", "-1 332 400 332", "-1 356 400 356", "-1 380 400 380",
# "-1 404 400 404", "-1 428 400 428", "-1 452 400 452", "-1 476 400 476",
# "-1 500 400 500", "-1 524 400 524", "-1 548 400 548", "-1 572 400 572",
# "-1 596 400 596", "5 -1 5 600", "21 -1 21 600", "37 -1 37 600",
# "53 -1 53 600", "69 -1 69 600", "85 -1 85 600", "101 -1 101 600",
# "117 -1 117 600", "133 -1 133 600", "149 -1 149 600", "165 -1 165 600",
# "181 -1 181 600", "197 -1 197 600", "213 -1 213 600", "229 -1 229 600",
# "245 -1 245 600", "261 -1 261 600", "277 -1 277 600", "293 -1 293 600",
# "309 -1 309 600", "325 -1 325 600", "341 -1 341 600", "357 -1 357 600",
# "373 -1 373 600", "389 -1 389 600",
#"0 -1 399 0", "0 599 399 600", "-1 0 0 599","399 0 400 599" ]
RectList = [ Rectangle( cords ) for cords in cordList ]  

setX = set( i.topleft[0] for i in RectList  )
setX.update( i.bottomright[0] for i in RectList  )
setY = set( i.topleft[1] for i in RectList  )
setY.update( i.bottomright[1] for i in RectList  )
#print setX, setY

AllPoints = [ ( x, y ) for x in setX for y in setY ]

IntPoints = list(set([ point if CheckIntersection( RectList , point ) else (0,0) for point in AllPoints ]))

map( lambda x : IntPoints.append( x ), [ rect.topleft for rect in RectList ]  )
map( lambda x : IntPoints.append( x ), [ rect.topright for rect in RectList ]  )
map( lambda x : IntPoints.append( x ), [ rect.bottomright for rect in RectList ]  )
map( lambda x : IntPoints.append( x ), [ rect.bottomleft for rect in RectList ]  )
#map( lambda x : IntPoints.append( x ), [ x for x in screenpoints ]  )

IntPoints = [ point for point in IntPoints if 0<= point[0 ] <= 399 and 0<= point[1 ] <= 599]

paths = [ RecursiveConnect(RectList, point, IntPoints , [] ) for point in IntPoints  ]

paths = []
for point in IntPoints:
	if sum([ 1 for path in paths if point in path ]) == 0:		
		paths.append(RecursiveConnect(RectList, point, IntPoints , [] ) )
		paths[-1].append( paths[ -1 ][ 0 ] )
print paths
#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#for path in paths:
#	ax.plot(  [ x[ 0] for x in path], [ x[1] for x in path] )
#ax.scatter(  [ x[ 0] for x in IntPoints], [ x[1] for x in IntPoints] )
#plt.show()


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
markerline, stemlines, baseline = plt.stem(  range( 20 ), [2,4,4,2,2,4,4,2,2,4,4,2,2,4,4,2,2,4,4,2 ],'-.' )
ax.plot(  range( 20 ), [2,4,4,2,2,4,4,2,2,4,4,2,2,4,4,2,2,4,4,2 ] )
plt.setp( markerline,'markerfacecolor','k' )
ax.set_xlabel('Samples')
ax.set_ylabel('Active Cores')
plt.setp( stemlines,'markerfacecolor','k' )
ax.set_xlim( (-1,20) )
ax.set_ylim( (0,5) )
#ax.scatter(  [ x[ 0] for x in IntPoints], [ x[1] for x in IntPoints] )
plt.show()
