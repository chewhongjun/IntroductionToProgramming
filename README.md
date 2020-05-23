# Pandas Basics

Author: Chew Hong Jun  

This repository is an introduction to python with a focus on _python syntax_ and _Programming logic_ which is similar for all languages !  
It will have a collection of code snippets and tutorials all mashed together!       

------

## Pre-Requisites

### Required

- VS code installed https://code.visualstudio.com/docs/?dv=win32user
- Python installed https://code.visualstudio.com/docs/python/python-tutorial & https://www.python.org/downloads/
- git bash (optional)
  
  - if you have installed it correctly  
    [ CTRL-SHIFT-` ] to launch bash terminal
  
    ```python
    hongjun@XPS9570:~/Gits/IntroductionToProgramming$ python3 --version
    Python 3.7.6

    or

    hongjun@XPS9570:~/Gits/IntroductionToProgramming$ py -3 --version
    Python 3.7.6
    ```
### Creating Your Own Workspace
- [ CTRL-SHIFT-` ] to launch bash terminal
    - terminal commands 
    ```bash
    mkdir MathewSumWorkspace
    cd MathewSumWorkspace
    ls
    ```
## Table Of Contents <a name="top"></a>

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
   2.13 [multi-line print](#2.13)  
   2.14 [dictionary](#2.14) 
   2.15 [Functions](#2.15)    
   2.16 [Functions, parameters](#2.16)  
   2.17 [MINI-PROJECT 1 TIK-TAK-TOE](#2.17)
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

**Key Learning Resources**

Useful tutorials: <https://www.tutorialspoint.com/python_pandas/python_pandas_introduction.htm>
<https://pythonprogramming.net/introduction-learn-python-3-tutorials/>
<https://www.youtube.com/channel/UCwRXb5dUK4cvsHbx-rGzSgw>


---

**Credits:**

A lot of these notes I'm adapting from 

<https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html>

<https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python>

<https://www.tutorialspoint.com/python_pandas/python_pandas_introduction.htm>