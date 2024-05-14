import math
import sys

state = input()

base = int(input())

alphabetdigit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if state == "encrypt":
	msg = sys.stdin.read()
	record = []
	for char in msg:
		msg1 = ord(char)
		record.append(msg1)
		
	for number in record:
		a = number
		power = int(math.log(a)//math.log(base))
		basepower = base**power
		
		for e in range(power,-1,-1):
			b = a 
			basepower = base**e
			quotient = b//basepower
			remainder = b%basepower
			a = remainder 
			print(alphabetdigit[quotient], end = "")
			
		print(" ", end = "")
			
	print()
	
if state == "decrypt":
	c = input().split()
	for d in c:
	
		length = len(d)
		exp = length -1
		total = 0
		for word in d:
		
			location = alphabetdigit.index(word)
			baseexp = base**exp
			number = location*baseexp
			total = total + number
			exp = exp - 1
			
		c = chr(total)
		print(c, end = "")
		
	print()
		
	
		
