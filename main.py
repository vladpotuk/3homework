def main():

   start = int(input("Введіть початок діапазону: "))

   end = int(input("Введіть кінець діапазону: "))





   for i in range(start, end + 1):

       if i % 3 == 0 and i % 5 == 0:

           print("Fizz Buzz")

       elif i % 3 == 0:

           print("Fizz")

       elif i % 5 == 0:

           print("Buzz")

       else:

           print(i)

if __name__ == "__main__":

   main()