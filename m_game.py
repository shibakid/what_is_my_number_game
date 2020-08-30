m=[]
n=[]
for i in range(0,10000):
	m.append(str(i))
for i in m:
	n.append(list(i))
for i in n:
	while len(i)!=4:
		i.insert(0,'0')
posib=n

def test(sol,tester):
	
	sol_1=sol[:]
	test_1=tester[:]
	corr_all_num=0
	while test_1:	
		j=test_1.pop()	
		for i in sol_1:
			if j==i:
				corr_all_num+=1
				sol_1.remove(i)
				break
	
	sol_2=sol[:]
	test_2=tester[:]
	corr_dig_num=0
	for i in range(0,4):
		if sol_2[i]==test_2[i]:
			corr_dig_num+=1

	result=(corr_all_num,corr_dig_num)
	return result
	
def choicut(tester,hint,posib):
	posib_1=[]
	while posib:
		x=posib.pop()
		index=test(x,tester)
		if index == hint:
			posib_1.append(x) 
	return posib_1

import random
sol=random.choice(posib)
hint=(0,0)
tester=random.choice(posib)

while True:
	print('\nMy turn!\nYour number is ',end='')
	for i in tester:
		print(i,end='')
	
	hint_num=input("\nHow many correct number ")
	while int(hint_num)>4:
		print('The answer is not correct please try again.',end='')
		hint_num=input("\nHow many correct number ")
	
	hint_dig=input("How many correct digit ")
	while int(hint_dig)>int(hint_num):
		print('The answer is not correct please try again.',end='')
		hint_dig=input("\nHow many correct digit ")
	hint=(int(hint_num),int(hint_dig))
	
	if hint==(4,4):
		print('I won')
		q=input('Do you want to know my number?(Yes press 1)')
		if int(q)==1:
			print('my number is ')
			for i in sol:
				print(i,end='')
		break
	
	print('\nYour turn!')
	your_tester=input("What number are you going to ask me? ")
	your_tester=list(list(your_tester))
	while len(your_tester)!=4:
		print('The answer is not correct please try again.')
		your_tester=input("What number are you going to ask me? ")
		your_tester=list(list(your_tester))
	result=test(your_tester,sol)
	
	if result==(4,4):
		print('Wow. It is my number. You win!!')
		break
	
	print('You have '+str(result[0])+' correct number')
	print('You have '+str(result[1])+' correct digit')
	print('-------------------------------------------')
	
	posib=choicut(tester,hint,posib)
	try:
		del tester
		tester=random.choice(posib)
		
	except IndexError:
		print('Something is wrong!! my number is ')
		for i in sol:
			print(i,end='')
		print('\nPlease check your answer. \nIf all correct please contact me.\nshibakidwinzcrow@gmail.com  \nThank you.')
		break

		
