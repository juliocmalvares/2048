#!/usr/bin/python3
# -*- coding: utf8 -*-

def mergeLine(line: list):
	moved = True
	merged = [0,0,0,0]
	while(moved):
		moved=False
		print(line)
		for i in range(len(line) - 2, -1, -1):
			if (line[i+1] == 0 and line[i] != 0):
				line[i], line[i+1] = line[i+1], line[i]
				merged[i], merged[i+1] = merged[i+1], merged[i]
				moved = True
			elif(line[i+1] == line[i] and merged[i+1]==0 and merged[i]==0):
				line[i], line[i+1] = 0, 2*line[i]
				merged[i], merged[i+1] = 0, 1
				moved = True		
	return line

vetor = [1,1,1,4]
vetorB = [1,1,1,4]
print(vetor)

print('-----')
print(mergeLine(vetor))
print('-----')
print(mergeLine(vetorB[::-1])[::-1])
