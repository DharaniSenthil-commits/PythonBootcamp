#Print statement
print("Hello World")

#print statement with custom input
CharacterName="Dharani"
CharacterAge="23"
print(CharacterName+" will become Full Stack Developer")
print("She is "+CharacterAge+" now  , within few years , she can achieve her goals")

#String
word='Python'
print(len(word)) #length
print(word[2]) #indexing
print(word[2:4]) # Slicing - start always included and end always excluded
phrase='Developer Dharani'
print(len(phrase))
print(phrase.upper()) # to lowercase
print(phrase.lower()) # to uppercase
print(phrase.isupper()) # check entire string is uppercase
print(phrase.upper().isupper()) #convert to upper and check it is uppercase
print(phrase.index('a')) #get the index of first a
print(phrase.replace('Dharani','DQ'))#replace Dharani to DQ

#Numbers

from math import *
number=5
print(str(number)+" changed number to string to concatenate")
number=3.2
print(round(number)) #round off :: 3.2 --> 3 , 3.6 --> 4
print(ceil(number)) # ceil --> large close --> 3.2 --> 4
print(floor(number)) # floor --> small close --> 3.2 --> 3
print(pow(3,2)) # 3 power 2 --> 3^2 -> 9
print(sqrt(36)) # sqrt root value --> 6
number=-5
print(abs(number)) # get the absolute value


#Custom Input from User
Name=input("Please Enter the Name : ")
print("Hello " +Name+ " !")

#List
FriendsList=["Chandler","Rachel","Monica","Joey","Phebe","Ross"]
NumberList=[1,5,9,2,0]

FriendsList.extend(NumberList)
print(FriendsList)

FriendsList=["Chandler","Rachel","Monica","Joey","Phebe","Ross"]

FriendsList.append("Gauther")
print(FriendsList)

FriendsList.pop()
print(FriendsList)

FriendsList.insert(1,"Janice")
FriendsList.insert(2,"Janice")
print(FriendsList)

print(FriendsList.count("Janice"))

FriendsList.remove("Janice")
print(FriendsList)

FriendsList.clear()
print(FriendsList)

NumberList.sort()
print(NumberList)

NumberList.reverse()
print(NumberList)

#Tuple --> Immutable

Coordinates=(10,20)
print(Coordinates[0],Coordinates[1])

#Function

def greetings(Name,Age):
    print("Namaste " + Name +"! You are "+ Age)

greetings("Dharani","23")
greetings("Anu","23")
greetings("Ice","23")

#Function with return Statement

def cube(number):
    return number*number*number

print(cube(8))


#Control Flow

#if

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


#while

a, b = 0, 1
while a < 1000:
    print(a,end=",")
    a, b = b, a+b

print()
SecretWord="Dharani"
GuessWord=""
GuessCount=0
GuessLimit=3
OutofGuess=False

while GuessWord != SecretWord and not(OutofGuess) :
    if GuessCount < GuessLimit :
        GuessWord = input("Enter your guess : ")
        GuessCount = GuessCount+1
    else :
        OutofGuess=True

if OutofGuess :
    print("Sorry , your are out of Limit . You LOSE !")
else :
    print("You win")

#for

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# break , for loop else clause ----> prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


#continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

#pass

class MyEmptyClass:
    pass

#match --> not implied in 02/08/2023

#exponent function

def raise_to_power(BaseNum,PowNum):
    Result=1
    for index in range(PowNum):
        Result=Result*BaseNum
    return Result

print(raise_to_power(3,2))


# 2D List

NumberGrid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(NumberGrid[2][1])

for row in NumberGrid :
    for col in row:
        print(col)

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper() :
                translation=translation+"G"
            else :
                translation = translation + "g"
        else :
            translation=translation+letter
    return translation

print(translate(input("Enter the Phrase : ")))


#comment --> hash to comment the code short description