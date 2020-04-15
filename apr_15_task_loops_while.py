
'''
#####################
a = int(input("enter first number:"))
b = int(input("enter second num:"))


sum = 0
rem = a % 10
sum = a //10
sum = sum+rem
print(sum)
if sum == b:
    print("Equal")

else:
    print("not equal")

    
###################
x = "krishna"
if "kr" in x:
    print("if:True")
elif "na8" in x:
    print("elif1: true")
else:
    print("else: false")


##############
i =10

while i>5:
    print(i)
    i = i-1  (if we comment this means output will infinite loop)
print("out of while")




##############
a = int(input("enter the num:"))
i=0
while i<=a:
    print(i)
    i=i+1
    #print(i)




    
#############

#Print only even number bw 0 to x

x = int(input("enter num:"))
i = 0

while (i<= x):
    print(i)
    i=i+2



#print only even number from (user input) to (user input) while

i = int(input("enter initial value:"))
x = int(input("enter ending value:"))
while (i<= x):
    print(i)
    i=i+2




#multiples of 5 bw 100 to 200

i = 100
x = 200
while i<=x:
    print(i)
    i=i+5
    


#multiples of 8 bw <user input > to <user output>

i = int(input("enter initial value:"))
x = int(input("enter ending value:"))
while i<=x:
    print(i)
    i=i+8
    


#Hackerrank if else
n = int(input("enter the value:"))

if (n%2 != 0):
    print("Given num is odd")

elif (n%2 == 0) and (n>=2 and n<=5):
    print("Not weird")
elif (n%2 == 0) and (n>=6 and n<=20):
    print("weird")
elif (n%2 == 0) and (n>20):
    print("Not weird")


#Hackerrank loops

n = int(input("enter the value:"))
i =0
while i<n:
    print(i**2)
    i=i+1


    

