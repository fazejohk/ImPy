#! /usr/bin/python

while 1:
	with open("test.txt", 'w+') as f:
		for i in range(1000):
			f.write(i)
