from time import sleep, time
import random

starttime = time()

print (str(starttime))
int1 = random.randint(20, 100)
int2 = random.randint(20, 100)
sum = int1 + int2

# Get user input
while True:
    try:
        ans = int(input('What is '+str(int1)+' + '+str(int2)+' ? '))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

timetaken = round(time()-starttime, 1)
verdict = ['wrong.', 'correct.'][ans==sum]
print('You took '+str(timetaken)+'s and your answer is '+verdict)

if verdict=='wrong.':
    print('The correct answer is '+str(sum)+'.')

sleep(5)
