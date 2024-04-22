def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True
    
number = int(input("Enter a number:"))
if is_prime(number):
    print("That is a prime number")
else:
    print("nope")









# def fizzBuzz(x):
#     while x > 0:
#         if x % 3 == 0 and x % 5 == 0:
#             print('fizzbuzz')
#         elif x % 5 == 0:
#             print('buzz')
#         elif x % 3 == 0:
#             print('fizz')
#         else: 
#             print(x)
#         x -= 1
# fizzBuzz(100)










# def isPalindrome(x):
#     x = x.replace(" ", "").lower()
#     return x == x[::-1]
# x = str(input('Enter a text: '))
# palindrome = isPalindrome(x)
# print(palindrome)










# def myfactorialfunc(x):
#     y = 1
#     while x > 0:
#         y *= x
#         x -= 1
#     return(y)
# x = int(input('Enter a number: '))
# factorial = myfactorialfunc(x)
# print(factorial)