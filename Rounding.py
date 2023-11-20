import time

f = open('pipline.txt', 'r+')
number = f.readline()
f.truncate(0)
f.close
# print(number)

newnum = float(number)

#number = 1000212.135124235325125252

roundednumber = round(newnum, 2)

#print("rounding ", newnum, " by 2 decimal places: ", roundednumber)

f = open('pipline.txt', 'r+')
f.write(str(roundednumber))
f.close()