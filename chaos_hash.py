import time
import random

name = input('username:\n')
print('Hi, %s.' % name)
time.sleep(1)
print("logging you to system…")
time.sleep(3)
input('target:\n')
time.sleep(0.01)
time.sleep(4)
for x in range(9):
  time.sleep(0.1)
  print('decoding_:', x)

number = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)
number5 = random.randint(0,9)
number6 = random.randint(0,9)
number7 = random.randint(0,9)
number8 = random.randint(0,9)
number9 = random.randint(0,9)
number10 = random.randint(0,9)

password = number * number2 + number3
password2 = password + number5 * number6
password3 = password * password2 + number7
password4 = password + password2 + password3
password5 = password4 * password3 * password4
finalPassword = password5 * password5
print('------------------------')
print('Cracked Hash:')
crackedHash = finalPassword

print(crackedHash)
 
