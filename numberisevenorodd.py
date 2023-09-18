def isEven(number):
  return number % 2 == 0

def main():
  number = int(input("Enter a number: "))

  result = isEven(number)

  if result:
    print("The number is even.")
  else:
    print("The number is odd.")

if __name__ == "__main__":
  main()
