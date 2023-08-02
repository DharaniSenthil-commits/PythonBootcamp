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