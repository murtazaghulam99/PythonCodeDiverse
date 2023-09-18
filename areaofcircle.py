# Area of a Circle Calculation
def areaOfCircle(radius):
  return 3.14 * radius * radius

def main():
  radius = float(input("Enter the radius of a circle: "))

  area = areaOfCircle(radius)

  print("The area of the circle is", area)

if __name__ == "__main__":
  main()
