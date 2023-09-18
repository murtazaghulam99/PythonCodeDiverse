def BMI(weight, height):
  return weight / (height ** 2)

def main():
  weight = float(input("Enter your weight in kilograms: "))
  height = float(input("Enter your height in meters: "))

  BMI_result = BMI(weight, height)

  if BMI_result < 18.5:
    print("Your BMI is underweight.")
  elif BMI_result < 25:
    print("Your BMI is normal.")
  elif BMI_result < 30:
    print("Your BMI is overweight.")
  else:
    print("Your BMI is obese.")

if __name__ == "__main__":
  main()
