def pattern(n):
  for i in range(n):
    for j in range(i + 1):
      print("*", end="")
    print()

def main():
  n = int(input("Enter the number of rows: "))

  pattern(n)

if __name__ == "__main__":
  main()
