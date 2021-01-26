# # Orginal code to debug
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # <-- problem resolved
        print("FizzBuzz")
    elif number % 3 == 0:
            print("Fizz")
    elif number % 5 == 0: # <-- problem resolved
            print("Buzz")
    else:
        print([number])

# In this debug exercise we put it into a debugger.  We see it count 1, 2, but from the first if statement it prints Fizz. but then it continues to evalulate all the if statements below. so it also prints Fizz.  Then the last if is false, so it hits the else and prints the number.  These ifs have to be indented. The first if statement is or so every time its either or it prints fizz, buzz, but also goes through the other statements and prings fizz and buzz and catches else.
# The resolution was the or statement to and and also the third if statement to elif 