import webbrowser
import time
import math

def add(n1, n2):
    print(int(n1) + int(n2))
def sub(n1, n2):
    print(int(n1) - int(n2))
def mult(n1, n2):
    print(int(n1) * int(n2))
def div(n1, n2):
    print(int(n1) / int(n2))
def remain(n1, n2):
    print(int(n1) % int(n2))
def power(n1, n2):
    print(int(n1) ** int(n2))
def pi():
    print(math.pi)

print("Welcome to M3r_\'s math problem solver!")
print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random \n Remainder \n Power, ** \n pi")
while True:
    start = input("So, what type of math problem are we doing today? \n").lower()
    time.sleep(1)
    if start in ['add', 'addition', 'Addition', 'sub', 'subtraction', 'Subtraction', 'mult', 'multiplication', 'Multiplication', 'div', 'division', 'Division', '*', '/', '-', '+', 'remainder', 'power', '**', 'pi']:
        n1 = input("Input the first number: \n")
        n2 = input("Input the second number: \n")
        if start == 'add':
            add(n1, n2)
        elif start == 'sub':
            sub(n1, n2)
        elif start == 'mult':
            mult(n1, n2)
        elif start == 'div':
            div(n1, n2)
        elif start == 'division':
            div(n1, n2)
        elif start == 'addition':
            add(n1, n2)
        elif start == 'Addition':
            add(n1, n2)
        elif start == 'Division':
            div(n1, n2)
        elif start == 'subtraction':
            sub(n1, n2)
        elif start == 'Subtraction':
            sub(n1, n2)
        elif start == 'multiplication':
            mult(n1, n2)
        elif start == 'Multiplication':
            mult(n1, n2)
        elif start == 'help':
            print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random \n Remainder \n Power, ** \n pi")
        elif start == '69':
            url = 'https://youtu.be/U2OjsKMcZQA'
            webbrowser.register('chrome',
	        None,
	        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)
            print("Enjoy fireball :D")
        elif start == 'Help':
            print(" Addition, + \n Subtraction, - \n Division, / \n Multiplication, * \n Random \n Remainder \n Power, ** \n pi")
        elif start == '/':
            div(n1, n2)
        elif start == '*':
            mult(n1, n2)
        elif start == '+':
            add(n1, n2)
        elif start == '-':
            sub(n1, n2)
        elif start == 'remainder':
            remain(n1, n2)
        elif start == 'Remainder':
            remain(n1, n2)
        elif start == 'power':
            power(n1, n2)
        elif start == 'Power':
            power(n1, n2)
        elif start == '**':
            power(n1, n2)
        elif start == 'pi':
            pi()
	elif start == 'Pi'
		pi()
