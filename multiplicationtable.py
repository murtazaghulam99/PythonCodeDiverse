def multiplicationTable(n):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      print(i, "*", j, "=", i * j, end="\t")
    print()

def main():
  n = int(input("Enter the number of rows in the multiplication table: "))

  multiplicationTable(n)

if __name__ == "__main__":
  main()
