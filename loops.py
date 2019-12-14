'''for i in range(10):
    print(i)
n = int(input("Enter a number: "))
for i in range(1,11):
    print(n, '*' , i , '=' , i*n)

    
a = 5
temp = a
fac = 1
while a > 0:
    fac *= a
    a -= 1
print('factorial of', temp, 'is: ', fac)'''


a = 0
b = 1
n = int(input("Enter number of terms: "))
print('Fibonacci series upto', n, 'terms is: ')
print(a, b, end=' ')
for i in range(n-2):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
print("\nEnd of program")
