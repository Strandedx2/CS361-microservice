import time

f = input("enter a number: ")

number = float(f)

g = open('pipline.txt', 'r+')
g.write(str(number))
g.close()

