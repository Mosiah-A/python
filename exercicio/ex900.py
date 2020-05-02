#using loop while
n = int(input())
cont = 0
while cont <= n:
    cont += 1
    if cont % 3 == 0 and cont % 5 == 0:
        print('FizzBuzz')
    if cont % 3 == 0 and cont % 5 != 0:
        print('Fizz')
    if cont % 5 == 0 and cont % 3 != 0:
        print('Buzz')
    if cont > n:
        break
    if cont % 3 != 0 and cont % 5 != 0:
        print(cont)

# using looping for
n = int(input())
for cont in range(1,n+1):
    if cont % 3 == 0 and cont % 5 == 0:
        print('FizzBuzz')
    if cont % 3 == 0 and cont % 5 != 0:
        print('Fizz')
    if cont % 5 == 0 and cont % 3 != 0:
        print('Buzz')
    if cont > n:
        break
    if cont % 3 != 0 and cont % 5 != 0:
        print(cont)

