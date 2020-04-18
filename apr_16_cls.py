
'''

list1 = ["hello", "bcd", "gcd", "hhmmm", "python","hh","wwww"]

even =[]
odd = []
for i in list1:
    if len(i)%2 ==0:
        even.append(i)
    elif len(i) %2 !=0:
        odd.append(i)
print(even)
print(odd)


#Program1:  #check whether a no is prime or not

n = 11
i = 2
for i in range(2,n-1):
    if n%i==0:
        print(n,"is non prime")
        break
else:
    print(n,"is prime numbers")
    
        


#Program2   #check list of prime numbers within a range
    
a = int(input("enter start value:"))
b = int(input("enter second value:"))
prime = [ ]
nonprime = [ ] 

for i in range(a,b):
    for n in range(2,i-1):
        if i%n == 0:
            #print(i,"is not prime num")
            nonprime.append(i)
            break
    else:
       # print(i,"is prime num")
        prime.append(i)

print("list of Prime num:",prime)
print("list of non Prime num:",nonprime)




#Program3: check whether a no is armstrong or not

n = int(input("Enter the number:"))
i = n
sum1 = 0
while n>0:
    rem = n%10
    sum1 += rem**3
    n  //= 10
    

print(sum1)

if sum1 == i:
    print("Given num is armstrong ")
else:
    print("Given num is not armstrong ")



#Program4:   list of armstrong numbers between two ranges
a = int(input("Enter starting value:"))
b = int(input("Enter ending value:"))
arm = [ ]
narm = [ ] 
for i in range(a,b):
    #print(i)
    sum1 = 0
    n = i
    
    while i>0:
        rem=i%10
        rem=rem**3
        sum1=sum1+rem
        i=i//10
    if sum1 == n:
        #print(n,"arm")
        arm.append(n)
    else:
        #print(n,"non arm")
        narm.append(n)
print("armstrong num list:",arm)
#print("non armstrong num list:",narm)







#Program5:   sum of digits 


n = int(input("enter the number:"))

sum1 = 0

while n>0:         #145
    rem = n % 10   #14
    sum1 =sum1+rem  #0+5
    n = n//10      #14
     
print("sum of Digits:",sum1)

if sum1%2 ==0:
    print("Sum of digits is even num")
else:
    print("Sum of digits is odd num")




#Program6:  product of digits
n = int(input("enter the number:"))

mul = 1


while n>0:        #140
    rem = n % 10  #0
    n = n//10       #14
    if rem  == 0:
        #rem.replace()
        continue
    
    mul =mul*rem
                 
print(mul)





#Program7:  add all odd numbers, ever numbers in a number separately, check whether both are equal or not

a = [5,6,7,8,2,21,23,24,16]
even = []
odd  = []


for i in a:
    if i%2 ==0:
        even.append(i)
        
    else:
        odd.append(i)

        
print(even,odd)
x=sum(even)
y=sum(odd)
print(x,y)

if x==y:
    print("Sum of numbers is eual")
else:
    print("sum of numbers is ! equal")


    
#Program8:  add all positive numbers, negative numbers in a number separately, check whether both are equal or not

a = [2,3,-4,5,6,-7,10,4,-10,3,-5,6,-7,7,8,-9,1,2,3,4,-5]
plus = [ ]
minus = [ ]

for i in a:
    if i>0:
        plus.append(i)
    elif i<0:
        minus.append(i)
print(plus)
print(minus)

x = sum(plus)
y = sum(minus)
print(x,y)

if x==y:
    print("Sum of numbers is eual")
else:
    print("sum of numbers is ! equal")



#Program9:  fizzbuzz

i = int(input("enter number:"))
for n in range(1,i+1):
        
    if n%3 == 0 and n%5 == 0:
        print(n,"fizzbuzz")
    
    elif n%3 == 0:
        print(n,"fizz")
    
    elif n%5 == 0:
        print(n,"buzz")
    else:
        print(n,"NA")        



#program10 (*)

#get a list/set of numbers from user (dynamic)


n = int(input("enter no of elements:"))
a = [ ]
b = set()
c = ()

for i in range(1,n+1):

#    k=int(input("enter integer value"))   # enter integer values
 #   l=input("enter string values:")       # enter string values
  #  a.append(k)
   # b.add(l)
    
    #b.add(l)

    m=int(input("enter values for Tuple:"))
    c.append(m)
#print(a)
print(c)
#print(b)



#program11   #factorial of a number

#6 ==> 6*5*4*3*2*1 ==>720

n = int(input("Enter the num :"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)

### By using for loop
n = int(input("Enter the num :"))
fact=1
for i in range(1,n+1):
    fact=fact*i

print(fact)







    

#Program 12:  fibonacci series

#0,1,1,2,3,5,8,13,21




Number = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
i = 0
First_Value = 0
Second_Value = 1
           
# Find & Displaying Fibonacci series
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           i = i + 1




'''


























    

