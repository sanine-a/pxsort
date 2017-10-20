import cv2 as cv
import numpy as np
from random import randint

def brightness(image, x, y):
	'''Returns a measure of the brightness of the pixel (x,y) in a given image.'''
	r = image.item(y,x,0)
	g = image.item(y,x,1)
	b = image.item(y,x,2)
	return r+g+b

def get_vertical_intervals(image, bmin, bmax):
	'''Get brightness intervals of [image] between bmin and bmax.'''
	intervals = []			#what we'll return
	in_interval = False		#variable to keep track of our intervals
	interval_start = (0,0)	#remember where the interval started
	for x in range(0, image.shape[1]):
		for y in range(0, image.shape[0]):
			#should this pixel be in an interval?
			b = brightness(image, x, y)
			if b > bmin and b < bmax:
				bmatch = True
			else:
				bmatch = False
			
			#starting an interval
			if bmatch and not in_interval:
				interval_start = (x,y)
				in_interval = True

			#ending an interval
			if in_interval and not bmatch:
				intervals.append( (interval_start, (x,y-1)) )
				in_interval = False

		#end interval at the edge of the image
		if in_interval:
			intervals.append( (interval_start, (x,y)) )
			in_interval = False
	return intervals

def get_horizontal_intervals(image, bmin, bmax):
	'''Get brightness intervals of [image] between bmin and bmax.'''
	intervals = []			#what we'll return
	in_interval = False		#variable to keep track of our intervals
	interval_start = (0,0)	#remember where the interval started
	for y in range(0, image.shape[0]):
		for x in range(0, image.shape[1]):
			#should this pixel be in an interval?
			b = brightness(image, x, y)
			if b > bmin and b < bmax:
				bmatch = True
			else:
				bmatch = False
			
			#starting an interval
			if bmatch and not in_interval:
				interval_start = (x,y)
				in_interval = True

			#ending an interval
			if in_interval and not bmatch:
				intervals.append( (interval_start, (x-1,y)) )
				in_interval = False

		#end interval at the edge of the image
		if in_interval:
			intervals.append( (interval_start, (x,y)) )
			in_interval = False
	return intervals

def colorize(image, intervals):
	'''Color in intervals with random colors'''
	for interval in intervals:
		color = np.array([ randint(0,255), randint(0,255), randint(0,255) ])
		for y in range(interval[0][1], interval[1][1]):
			image[y, interval[0][0]] = color

def vertical_sort (image, bmin, bmax):
	'''Actually do the pixelsort!'''
	intervals = get_vertical_intervals(image, bmin, bmax)
	for interval in intervals:
		x  = interval[0][0]
		y1 = interval[0][1]
		y2 = interval[1][1]
		tmp = image[y1:y2,x,:]
		tmp.sort(axis = 0)
		image[y1:y2,x,:] = tmp

def horizontal_sort (image, intervals):
	'''Actually do the pixelsort!'''
	intervals = get_horizontal_intervals(image, bmin, bmax)
	for interval in intervals:
		x1 = interval[0][0]
		x2 = interval[1][0]
		y  = interval[0][1]
		tmp = image[y,x1:x2,:]
		tmp.sort(axis = 0)
		image[y,x1:x2,:] = tmp
