import random
import time
import os
import json
import webbrowser

print("Welcome to M3r_\'s math problem solver!")
def help ():
    print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random")
help()
start = input("So, what type of math problem are we doing today? \n")
if start == "multiplication":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) * int(y)
    print(sum)
if start == "Multiplication":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) * int(y)
    print(sum)
if start == "*":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) * int(y)
    print(sum)
if start == "division":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) / int(y)
    print(sum)
if start == "Division":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) / int(y)
    print(sum)
if start == "/":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) / int(y)
    print(sum)
if start == "addition":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) + int(y)
    print(sum)
if start == "Addition":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) + int(y)
    print(sum)
if start == "+":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) + int(y)
    print(sum)
if start == "subtraction":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) - int(y)
    print(sum)
if start == "Subtraction":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) - int(y)
    print(sum)
if start == "-":
    x = input("Input the first number: ")
    y = input("Input the second number: ")
    sum = int(x) - int(y)
    print(sum)
if start == "random":
    print(random.randrange(69, 420))
if start == "help":
    print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random")
if start == "Help":
    print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random")
if start == "69":
    url = 'https://youtu.be/U2OjsKMcZQA'
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    print("Enjoy fireball :D")
if start == "cock":
    url = 'https://youtu.be/U2OjsKMcZQA'
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    print("Enjoy fireball :D")
else:
    print("That is either not a valid phrase or was mistyped :c sorry")
    time.sleep(2)
def answers ():
    if start == "multiplication":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) * int(y)
        print(sum)
    if start == "Multiplication":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) * int(y)
        print(sum)
    if start == "*":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) * int(y)
        print(sum)
    if start == "division":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) / int(y)
        print(sum)
    if start == "Division":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) / int(y)
        print(sum)
    if start == "/":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) / int(y)
        print(sum)
    if start == "addition":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) + int(y)
        print(sum)
    if start == "Addition":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) + int(y)
        print(sum)
    if start == "+":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) + int(y)
        print(sum)
    if start == "subtraction":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) - int(y)
        print(sum)
    if start == "Subtraction":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) - int(y)
        print(sum)
    if start == "-":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        sum = int(x) - int(y)
        print(sum)
    if start == "random":
        print(random.randrange(69, 420))
    if start == "help":
        print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random")
    if start == "Help":
        print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random")
    if start == "69":
        url = 'https://youtu.be/U2OjsKMcZQA'
        webbrowser.register('chrome',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
        print("Enjoy fireball :D")
    if start == "cock":
        url = 'https://youtu.be/U2OjsKMcZQA'
        webbrowser.register('chrome',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
        print("Enjoy fireball :D")
    else:
        time.sleep(2)
        print("That is either not a valid phrase or was mistyped :c sorry")
def ask ():
    close = input("Would you like to close this window? Y/N\n")
    if close == "Y":
        exit()
    if close == "N":
        start = input("So, what type of math problem are we doing today? \n")
        answers()
    if close == "y":
        exit()
    if close == "n":
        start = input("So, what type of math problem are we doing today? \n")
        answers()
    if close == "Yes":
        exit()
    if close == "No":
        start = input("So, what type of math problem are we doing today? \n")
        answers()
    if close == "yes":
        exit()
    if close == "no":
        start = input("So, what type of math problem are we doing today? \n")
        answers()

ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()
ask()

