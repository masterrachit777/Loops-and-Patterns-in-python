#Simple pattern
n= int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        print(i, end=' ')
    print('\n')

#Triangular pattern with *
m = int(input("Enter the number of rows: "))
for i in range(1, m+1):
    for j in range(1, m+1):
        if i+j <= m:
            print(' ', end=' ')
        else:
            print('* ', end=' ')
    print('\n')

#To check whether number is palindrome or not
a = int(input("Enter a number: "))
temp = a
rev = 0
while a > 0:
    rev = (rev*10) + (a%10)
    a //= 10
print('Reverse of number is: ', rev)
if temp == rev:
    print('It is a Palindrome')
else:
    print('It is not a Palindrome')

#Pattern of Heart
for r in range(6):
    for c in range(7):
        if r==0 and c%3!=0 or r==1 and c%3==0 or r+c==8 or r-c ==2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('\n')
