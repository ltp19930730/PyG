''' read a input file and add the number of
    the line to the last of the sentence
'''
import fileinput

for line in fileinput.input():
    line = line.rstrip()
    num = fileinput.lineno()
    print "%-40s ###%2i" %(line,num)
