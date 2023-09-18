def medianOfThreeValues(x, y, z):
  if x >= y and x <= z:
    return x
  elif x <= y and x >= z:
    return x
  elif y >= x and y <= z:
    return y
  else:
    return z

def main():
  x, y, z = map(float, input("Enter three numbers: ").split())

  median = medianOfThreeValues(x, y, z)

  print("The median of the three numbers is", median)

if __name__ == "__main__":
  main()
