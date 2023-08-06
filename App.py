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

#Function

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

#Function with return

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100)              # write the result


#Default Argument
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')

#Keyword argument

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# keyword argument and positional arguments

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


#special arguments
'''
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
'''


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

pos_only_arg(1)
kwd_only_arg(arg=3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

#Arbitary argument list

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")

#unpacking arguments

list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
list(range(*args))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#Lambda function
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

#DocString

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')


#try and except

try :
    answer=10/0
    number=int(input("Enter a number "))
    print(number)
except ZeroDivisionError as err :
    print(err)
except ValueError as err :
    print(err)


#Reading file
# r - read, w - write , a - append , r+ - read and write

readfile=open('readfile.txt','r')

print(readfile.readable()) # return whether true or false , if r or not

print(readfile.read()) # display whole file

print(readfile.readline()) # will display 1st  line
print(readfile.readline()) # will display 2nd  line
print(readfile.readline()) # will display 3rd  line

print(readfile.readlines()) # Display all lines in array
print(readfile.readlines()[1]) # Display the second line

#readlines in for loop

for line in readfile.readlines() :
    print(line)

readfile.close()

#Write file

writefile=open("readfile.txt","w")
writefile.write("\nNewly added line by a - append ")
writefile.close()

writefile=open("writefile.py","w")
writefile.write("print('Created new py file using w')")
writefile.close()

writefile=open("writefile.py","w")
writefile.write("print('overwrited the content of the file')")
writefile.close()


#Modules and Pip
import DemoModule
print(DemoModule.roll_dice(5))

#Pip , to load external package or module

''' 
    pip install pandas
    pip uninstall pandas
'''


#Class and Object

from Student import Student

student1=Student("Rachel","Arts",9.9,False)
student2=Student("Monica","Displine",10,False)
print(student1.name)
print(student1.gpa)
print(student2.name)







