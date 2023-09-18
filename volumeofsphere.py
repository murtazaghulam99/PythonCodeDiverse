def volumeOfSphere(radius):
  return (4 / 3) * 3.14 * radius ** 3

def main():
  radius = float(input("Enter the radius of a sphere: "))

  volume = volumeOfSphere(radius)

  print("The volume of the sphere is", volume)

if __name__ == "__main__":
  main()
