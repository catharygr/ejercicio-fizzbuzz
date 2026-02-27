def mi_fizz_buzz(min_num, max_num):
  for num in range(min_num, max_num + 1):
   if num % 3 == 0 and num % 5 == 0:
     print("fizzbuzz")
   elif num % 3 == 0:
     print("fizz")
   elif num % 5 == 0:
     print("buzz")
   else:
     print(num) 

mi_fizz_buzz(1,100)