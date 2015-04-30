from collections import deque
import numpy as np

#Harmful = []
#Danger = []

#Harmful = ["0 0 250 250","250 250 500 500"]
#Danger = ["0 250 250 500","250 0 500 250"]
	
#Harmful = ["0 0 250 250","250 250 500 500"]
#Danger = ["0 251 249 500","251 0 500 249"]

Harmful =["468 209 456 32",
 "71 260 306 427",
 "420 90 424 492",
 "374 253 54 253",
 "319 334 152 431",
 "38 93 204 84",
 "246 0 434 263",
 "12 18 118 461",
 "215 462 44 317",
 "447 214 28 475",
 "3 89 38 125",
 "157 108 138 264",
 "363 17 333 387",
 "457 362 396 324",
 "95 27 374 175",
 "381 196 265 302",
 "105 255 253 134",
 "0 308 453 55",
 "169 28 313 498",
 "103 247 165 376",
 "264 287 363 407",
 "185 255 110 415",
 "475 126 293 112",
 "285 200 66 484",
 "60 178 461 301",
 "347 352 470 479",
 "433 130 383 370",
 "405 378 117 377",
 "403 324 369 133",
 "12 63 174 309",
 "181 0 356 56",
 "473 380 315 378"]
Danger = ["250 384 355 234",
 "28 155 470 4",
 "333 405 12 456",
 "329 221 239 215",
 "334 20 429 338",
 "85 42 188 388",
 "219 187 12 111",
 "467 453 358 133",
 "472 172 257 288",
 "412 246 431 86",
 "335 22 448 47",
 "150 14 149 11",
 "224 136 466 328",
 "369 209 184 262",
 "274 488 425 195",
 "55 82 279 253",
 "153 201 65 228",
 "208 230 132 223",
 "369 305 397 267",
 "200 145 98 198",
 "422 67 252 479",
 "231 252 401 190",
 "312 20 0 350",
 "406 72 207 294",
 "488 329 338 326",
 "117 264 497 447",
 "491 341 139 438",
 "40 413 329 290",
 "148 245 53 386",
 "147 70 186 131",
 "300 407 71 183",
 "300 186 251 198",
 "178 67 487 77",
 "98 158 55 433",
 "167 231 253 90",
 "268 406 81 271",
 "312 161 387 153",
 "33 442 25 412",
 "56 69 177 428",
 "5 92 61 247"]


class Regions:
	def __init__(self, cords, offset= (0,0) ):
		cord1 = np.subtract( tuple([ int(i) for i in cords.split(" ")[:2] ]) , offset )
		cord2 = np.subtract( tuple([ int(i) for i in cords.split(" ")[2:] ]), offset )
	
		if (cord1[ 0 ] <= cord2[ 0 ]) :
			self.xmax = cord2[ 0 ]
			self.xmin = cord1[ 0 ] 
		else:
			self.xmax = cord1[ 0 ]
			self.xmin = cord2[ 0 ] 

		if( cord1[ 1 ] <= cord2[ 1 ] ):
			self.ymax = cord2[ 1 ] 
			self.ymin = cord1[ 1 ]
		else :
			self.ymax = cord1[ 1 ] 
			self.ymin = cord2[ 1 ]



	def RelativeLocation( self,  point ):
		# If inside or on Rect returns True
		x, y = point	
		if ( self.xmin <= x <= self.xmax) and ( self.ymin <= y <= self.ymax ):
			return True
		else :
			return False

DangerList = [ Regions( cords   ) for cords in Danger ]  
HarmfulList = [ Regions( cords ) for cords in Harmful ]  
queue = [ ( 0,0 )]
#
#for Drect in HarmfulList :
#	print Drect.xmin, Drect.ymin, Drect.xmax ,Drect.ymax
#
AdMatrix = [ [ 0 ] *  501 for x in range(501) ]

for (x,y) in [ (a,b) for a in range( 501 ) for b in range( 501 ) ] :
	if sum([ 1 if HarmfulRegion.RelativeLocation( (x, y) ) else 0 for HarmfulRegion in HarmfulList ]) != 0 : 
		AdMatrix[ x ][ y ] = 1 
	if sum([ 1 if DangerRegion.RelativeLocation( (x, y) ) else 0 for DangerRegion in DangerList ]) != 0 :  
		AdMatrix[ x ][ y ] = -1
		
		
def BFS( start , end ):

	count = 0
	oldIntercept = 0
	while( len( queue ) != 0 ):
	
		parent = queue.pop( 0 ) 
		parentIntercept = parent[ 0 ] + parent[ 1 ]

		if (oldIntercept != parentIntercept) :
			if ( AdMatrix[parent[0]][parent[1]] == 0 ) :
				count = count 
			else:
				count += 1
			oldIntercept = parentIntercept

		AdMatrix[ parent[ 0 ] ][parent[ 1 ] ] = 2 


		if (parent[ 0 ] == 500 )and (parent[ 1]<500 ):
			newpoints = [ (parent[ 0 ] + offx , parent[ 1 ] + offy ) for offx, offy in [ (0,1)]  ] 
			unvisited = [ point for point in newpoints if (point[ 0 ] >=0 and point[ 1] >=0) if AdMatrix[ point[ 0 ] ][ point[ 1 ] ] not in [ -1 , 2 ] if point not in queue ]
		elif (parent[ 1 ] == 500 )and (parent[ 0]<500 ):
			newpoints = [ (parent[ 0 ] + offx , parent[ 1 ] + offy ) for offx, offy in [ (1,0)]  ] 
			unvisited = [ point for point in newpoints if (point[ 0 ] >=0 and point[ 1] >=0) if AdMatrix[ point[ 0 ] ][ point[ 1 ] ] not in [ -1 , 2 ] if point not in queue ]
		elif (parent[ 1 ] == 500 ) and ( parent[ 1 ] == 500 ):
			unvisited = [] 
		else:
			newpoints = [ (parent[ 0 ] + offx , parent[ 1 ] + offy ) for offx, offy in [ (1,0), (0,1)]  ] 
			unvisited = [ point for point in newpoints if (point[ 0 ] >=0 and point[ 1] >=0) if AdMatrix[ point[ 0 ] ][ point[ 1 ] ] not in [ -1 , 2 ] if point not in queue ]

		
		if (end != parent ) :
			normalpoints = [ point for point in unvisited if AdMatrix[ point[0]][point[1]] == 0 ] 
			if len( normalpoints ) == 0 :
				map( lambda x : queue.append( x ) , unvisited )
			else:
				map( lambda x : queue.append( x ) , normalpoints )

		else:
			return count 
		if ( len(queue) == 0 ):
			print count, parent  
			return -1

	return count 

print BFS( (0,0), (500,500 ) )
