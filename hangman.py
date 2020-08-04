from os import system,name
import random
import re
from getch import pause

def clear(): 
	# for windows 
	    if name == 'nt': 
	    	_ = system('cls')
	# for mac and linux(here, os.name is 'posix') 
	    else:
	    	_ = system('clear')

play='y'
while play=='y' or play=='Y':
	play='n'
	
	print('\t\t\t\t\t\tHANGMAN GAME\n\n\n')
	n=input("Enter a word:")
	v=n
	n=re.findall(r'[A-Za-z ]',n)
	clear()
	
	k=random.randint(1,len(n)-2)
	b=k
	a=list()
	s=list()
	print('\t\t\t\t\t\tHANGMAN GAME\n\n\n')

	#inserting empty spaces in random places in string
	while k!=0:
		p=random.randint(0,len(n)-1)
		if n[p]!='_' and n[p]!=' ':
			a.append([p,n[p]])
			s.append(n[p])
			n[p]='_'
			k-=1
		else:continue
	
	s=set(s)
	for i in range(len(n)):
		print(n[i],end=' ')
	
	print()
	print("You are given {0} trial to complete the word".format(b+2))
	
	x = 0
	
	#number of trials
	for j in range(b+2):
		trial_ans=input('Enter your character:')
		if trial_ans in s:
			for i in range(len(a)):
				if a[i][1]==trial_ans:
					n[a[i][0]]=trial_ans
		else:
			print("\nwrong guess")
		if '_' in n:
			print('\n\n')
			for i in range(len(n)):
				print(n[i],end=' ')
			print('\n\n')
			print('Trials left:{}'.format(b+1-j))
		else:
			print("YOU WON")
			print('\n')
			for i in range(len(n)):
				print(n[i],end=' ')
			print('\n\n')
			x=1
			break
	if x==0:
		print("YOU LOST")
		print("Correct word is: " + v)
	pause("click any key to continue")
	clear()
	play = input("Do you want to play again(Enter y/Y):")
	clear()
print('\n\nThank you for playing')
pause()
