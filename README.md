# Python Basics

Author: Chew Hong Jun  

This repository is an introduction to python with a focus on _python syntax_ and _Programming logic_   
which is similar for all languages !  
It will have a collection of code snippets and tutorials all mashed together!       

------

## Pre-Requisites

### Required

- VS code installed https://code.visualstudio.com/docs/?dv=win32user
- Python installed https://code.visualstudio.com/docs/python/python-tutorial & https://www.python.org/downloads/
- git bash (optional)
  
  - if you have installed it correctly  
    [ CTRL-SHIFT-` ] to launch bash terminal in vs code
  
    ```python
    hongjun@XPS9570:~/Gits/IntroductionToProgramming$ python3 --version
    Python 3.7.6

    or

    hongjun@XPS9570:~/Gits/IntroductionToProgramming$ py -3 --version
    Python 3.7.6
    ```
### Creating Your Own Workspace
- [ CTRL-SHIFT-` ] to launch bash terminal in vs code
    - terminal commands 
    ```bash
    mkdir MathewSumWorkspace
    cd MathewSumWorkspace
    ls
    ```
---
## Table Of Contents <a name="top"></a>
1.[Week1 Question](#wk1)

1. [Introduction](#1)    
2. [Python Basics](#2)    
   2.1 [Print Function](#2.1)    
   2.2 [Math](#2.2)    
   2.3 [variables](#2.3)    
   2.4 [while loop](#2.4)    
   2.5 [for loop](#2.5)    
   2.6 [if](#2.6)    
   2.7 [if-else](#2.7)    
   2.8 [if-elif-else](#2.8)   
   2.9 [List and tuples](#2.9)  
   2.10 [List Manipulation](#2.10)  
   2.11 [Multi-dimension list](#2.11)   
   2.12 [try-except](#2.12)  
   2.13 [Multi-line print](#2.13)  
   2.14 [Dictionary](#2.14)   
   2.15 [Functions](#2.15)    
   2.16 [Functions, parameters](#2.16)  
   2.17 [MINI-PROJECT 1 TIC-TAC-TOE](#2.17)
3. [Python intermediate]()  
    3.1 [Global vs local]()  
    3.2 [Writing to file]()  
    3.3 [Apppending to file]()  
    3.4 [Reading from file]()  
    3.5 [Object Oriented Programming, classes]()  
    3.6 [Getting user input]()  
    3.7 [statistics]()  
    3.8 [Import modules]()  
    3.9 [Reading from a csv]()  
    3.10 [built-in-functions]()
    3.11 [OS Module]()  
    3.12 [SYS Module]()  
    3.13 [urlib Module]()  
    3.14 [Regular Expressions]()  
    3.15 [parsing websites, urlib re]()  
    3.16 [GUI tkinter #1 basic]()  
    3.17 [GUI tkinter #2 buttons]()  
    3.18 [GUI tkinter #3 event handling]()  
    3.19 [GUI tkinter #4 menu]()  
    3.20 [GUI tkinter #5 images and text]()  
    3.21 [GUI tkinter #6 forms]()  
    3.22 [GUI tkinter #7 mini-project]()  
4. [Python advanced](#4)    
    4.1 [multi treading]()  
    4.1 [cx freeze]()  
    4.1 [subprocess]()  
    4.1 [graphing]()  
    4.1 [ftp transfers]()  
    4.1 [socket intro]()  
    4.1 [socket port scanner]()  
    4.1 [soocket multi tread port scannerr]()  
    4.1 [socket binding and listening]()  
    4.1 [socket client server]()  
    4.1 [sqlite3 python #1]()  
    4.1 [sqlite3 python #2]()  
    4.1 [sqlite3 python #3]()  
    4.1 [sqlite3 python #4]()  
    4.1 [sqlite3 python #5]()  

5. [EXTRA: Helpful Notes](#5) 

## 1. Introduction <a name="1"></a>

> [Python](https://www.python.org/) programming language. is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. 
>
> *What can you do with Python?* Just about anything, and most things quite easily. Topics like data analysis, machine learning, web development, desktop applications, robotics, and more are all things that you can immediately begin doing with Python without much effort.
> 
> <https://www.python.org/>

We will be going throught python and basic computing logic on how to write basic programs using python

- variables
- types
- operators
- control
    - if, elif, else
    - boolean
    - while
    - for
    - nesting
- algorithms
- program design

[Introductory video](https://www.youtube.com/watch?v=Y8Tko2YC5hA)


**Key Learning Resources**

Useful tutorials:   
<https://pythonprogramming.net/>  
<https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ>  
<https://www.youtube.com/channel/UCZUyPT9DkJWmS_DzdOi7RIA>  
<https://www.geeksforgeeks.org/python-programming-language/>  
<https://algo.is/>  

**Credits:**

A lot of these notes I'm adapting from:  
<https://pythonprogramming.net/>  
<https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ>  
<https://www.youtube.com/channel/UCZUyPT9DkJWmS_DzdOi7RIA>  
<https://www.geeksforgeeks.org/python-programming-language/>  
<https://www.tutorialspoint.com/>
<https://algo.is/>  


---

## 2. Python Basics <a name="2"></a>

### 2.1 Print Function <a name="2.1"></a>
[go to top](#top)


Note that print() is built-in function of python.


>print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
>Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.
>
>All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; >they can also be None, which means to use the default values. If no objects are given, print() will just write end.
>
>The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text > >strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.

<https://docs.python.org/3/library/functions.html#print>  
**The print function is a fundamental function in the python**. It's one of the most commonly manipulated in python for command line applications.
It's okay if you dont understand the above documentation we will go throught it in a short while!

**Lets try it out**
```python
print("Hello World!")

#Or

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()


tutorial1/helloworld.py
```

What is going on here?
- arguments are parsed in
- coverted into strings
- shown in sys.out

**Try It Out**

```
1. Print your name and your age
```

**Additional points**
```
print("Hi" + "there")
Hithere
print("Hi" + " there")
Hi there
print("Hi" * 5)
HiHiHiHiHi

print("Hi" + 5)
  File "/home/hongjun/Gits/IntroductionToProgramming/Tutorial1/helloworld.py", line 11, in <module>
    print("Hi" + 5)
TypeError: can only concatenate str (not "int") to str

print("Hi" + str(5))
Hi5

print(6+7)
13

```
[go to top](#top)

---
### 2.2 math <a name="2.2"></a>
You have the basic math operators(+, -, *, %, /)  
Operator precedence applies   
```python
print(5+2)
print(5-3)
print(5%2)
print(5*2)
print(2*2+1)
print(2*(2+1))
print(4**4)

7
2
1
10
5
6
256
```

Float(decimal) vs Integers(whole numbers)  
- As a rule of thumb floats have a higher rank that  intergers
- As a result floatt * interger = float
```python
print(type(5.0))
print(type(5))

<class 'float'>
<class 'int'>

print(5.0+2)
print(5.0*2)

7.0
10.0
``` 

[go to top](#top)

---
### 2.3 Variables <a name="2.3"></a>

Variables are used to store data lets try it out

additional videos:<https://www.youtube.com/watch?v=cQT33yu9pY8>

PEP8:
```
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
```

* I perfer camel casing an example would be (phoneNumber, homeAddress)
* try to make your variable short and meaningful
* avoid variable naming (x,y,z) good in math but bad is programming

```python
#Legal variable names:
myvar = "John"     
my_var = "John"     //Acceptable
_my_var = "John"
myVar = "John"      //Acceptable
MYVAR = "John"      //Acceptable for constants
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
```

**Taking user input**

We can take in a user input and store them into a variable  
Similiar to math it works right to left  
let's take a look at this example

```python
myName=input("Enter your name: ")
print(myName)

Enter your name: Jay
Jay
```
**Try It Out**

```
Using variables
1. Print your name and your age
2. Your favourite food and it's location
```

**Additional Points**
```python
myName = "jay"
myFood = "fish fillet"
print(myName + " LOVES " +myFood)

>jay LOVES fish fillet

print(myName + " LOVES " +myFood*5)

>jay LOVES fish filletfish filletfish filletfish filletfish fillet

x,y=(1,2)
print(x)
print(y)

>1
>2
```
### 2.4 while loop <a name="2.4"></a>

It's not easy to explain how it works, but looking at the example it will make more sense!


While the condition variable is less than 10, we will print the condition variable out.  
After printing out the condition, we will add 1 to the current condition. 

The condition is a "counter". We just want to count 1 for every iteration and eventually stop at our limit
```python
condition=1
while condition < 10:
    print(condition)
    condition = condition + 1

1
2
3
4
5
6
7
8
9
```



**Lets see how can this be used in real life**  
Assuming we had something built to detect weather   
The loop would continue running while it was raining outside. When the rain stopped, the loop would cease.

This is an example of an infinite loop, ctrl-c to exit
```python
isRaining = True
while(isRaining):
    print("Its raining close the windows")

Its raining close the windows
Its raining close the windows
Its raining close the windows
Its raining close the windows
Its raining close the windows
...
...
```
---

## Question of the week <a name="wk1"></a>
*Your goal is not to finish all the questions, but to understand how does variables, math operators and the while loop works. Do not be pressured to do all of it!   
Take your time and think about the questions dont rush into finding the answers :)  
if you have finished and are looking for more stuff to do youtube is your friend*
```
1. Take in 10 user input(integers), and print the average on screen

2. Take user input(integer) until 'q' has been entered, print in this format  
 __integers has been entered, with an average value of __, and their product is __.  

    Example:
    user input:1
    user input:2
    user input:3
    user input:q
    3 integers has been entered, with an average value of 2, and their product is 6  

3. Using a while loop print
    *
    **
    ***
    ****
4. Using a while loop print
    *****
    ****
    ***
    **
    *
5. Do questions 3-4 but allow user input

    Example:
    user input:3
    ***
    **
    *

Additional Hard Question: 

1. Make a christmas tree (The code i used implemented a for loop that we didnt cover on the first lesson)
       *       
      ***      
     *****     
    *******    
   *********   
  ***********  
 ************* 
    \====/    

2. Make a guessing game

Guess a number from 1 and 10: 2
You guessed wrongly
 Try again!
Guess a number from 1 and 10: 1
You guessed wrongly
 Try again!
Guess a number from 1 and 10: 3
You guessed wrongly
 Try again!
Guess a number from 1 and 10: 4
You guessed wrongly
 Try again!
Guess a number from 1 and 10: 5
You guessed wrongly
 Try again!
Guess a number from 1 and 10: 6
You guessed wrongly
 Try again!
Guess a number from 1 and 10: 7
Congrats! You guessed the right number

```
---
### 2.5 for loop <a name="2.5"></a>


Both for loops and while loops  work in a similiar manner, both allowing you to iterate. However, while loops are generally used for infinite actions where as for loops are for finitie with a predetermined length.


While Loop
- run __While__ its sunny.

For Loop
- run __For__ 4 rounds.



A for loop can be used in  a few ways

1. Iterating through a list:
```
shoppingList = ["Detergent","Toothpaste","Shower Gell","Ice Cream"]

for item in shoppingList:
    print(item)

Detergent
Toothpaste
Shower Gell
Ice Cream
```

2. Iterating through a generator function (range):
```
for num in range(1,10):
    print(num)

1
2
3
4
5
6
7
8
9
```

**Let's try it out!**

* The goal is to print number 7 through 22.
* Print a list of your favourite food items.

---

### 2.6 if statement <a name="2.6"></a>

the **if** statement is one of the basic ways we can express logic

* lets go through an example of how it can be used!  
we have 2 algebric expressions x,y and if x is more than y, we will print ITSLARGER!!!!
* we notice that nothing is printed out. Can we think why?
```python
x=20
y=60

if(x>y):
    print("ITSLARGER!!!!")
```
* lets try again with a different set of number
* It prints! why?
```python
x=300
y=60

if(x>y):
    print("ITSLARGER!!!!")
```

### Additional thinking questions
what do you think will happen when x, y have the same value?  
and what will happen if we change the > to < 

### Practice questions 

try the above statements with different operators such as 

* ==
* !=
* \>
* \>=
* <
* <=
----
### 2.7 if-else statement <a name="2.7"></a>
__if-Else__ statement is an extension of the if block. It is the opposite of if, the else statement has to be after an if statement otherwise the program will not run.  

* Example  
```
if it is sunny:  
    Go for a run  
else:  
    watch netflix
```

### Lets try it out

```python
x = 5
if (x%==0):
    print("It is even")
else:
    print("It is odd")
```

The if else statement can used in combination with the for loop. If we want to we can iterate through a set of numbers and check if they are even or odd.

```python
for i in range(1,10):
    if(i%2==0):
        print("its even")
    else:
        print("its odd")
```


### Practice questions

Lets try some hands on!  
* iterate through numbers 1, 20. If the number is divisable by 3, print "it divides". Else we print "it does not"
* iterate through the foodList and print the "FAV" when its your favourite good else print "NAH"


---


