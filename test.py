print("1. Celsius to Fahrenheit Conversion\n2. Fahrenheit to Celsius Conversion\n3. Exit")
conversion_type = int(input("Enter choice (1/2/3): "))

if conversion_type == 1:
    cel = float(input("Enter temperature in Celcius: "))
    far = (cel * 9/5) + 32
    print(str(cel) + "°C is equal to " + str(round(far)) + "°F")
elif conversion_type == 2:
    far = float(input("Enter temperature in Fahrenheit: "))
    cel = (far - 32) * 5/9
    print(str(far) + "°F is equal to " + str(round(cel)) + "°C")
elif conversion_type == 3:
    exit()
else:
    print("Error Conversion Type Input!!")












# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num == 2:
#         return True
#     elif num % 2 == 0:
#         return False
#     else:
#         divisor = 3
#         while divisor * divisor <= num:
#             if num % divisor == 0:
#                 return False
#             divisor += 2
#         return True
    
# number = int(input("Enter a number:"))
# if is_prime(number):
#     print("That is a prime number")
# else:
#     print("nope")









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