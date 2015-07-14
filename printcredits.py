import os
import time
import sys

def credits():
	for i in range(50):
		print
	fname = "credits.txt"
	with open(os.getcwd()+"/"+fname) as f:
	  content = f.readlines()

	n = 0
	image = []
	for i in content:
	  for j in i:
	    image.append(j)

	for i in range(len(image)):
	    # sys.stdout.write('\b\b\b')
	    sys.stdout.write(image[i])
	    sys.stdout.flush()
	    time.sleep(0.003)
	print