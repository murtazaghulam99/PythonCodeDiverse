from math import sqrt

def euclideanDistance(x1, y1, x2, y2):
  return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
  x1, y1, x2, y2 = map(float, input("Enter the coordinates of point 1 (x, y): ").split())

  distance = euclideanDistance(x1, y1, x2, y2)

  print("The Euclidean distance between the two points is", distance)

if __name__ == "__main__":
  main()
