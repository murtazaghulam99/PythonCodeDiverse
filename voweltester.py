def isVowel(char):
  vowels = ["a", "e", "i", "o", "u"]

  return char in vowels

def main():
  char = input("Enter a character: ")

  result = isVowel(char)

  if result:
    print("The character is a vowel.")
  else:
    print("The character is not a vowel.")

if __name__ == "__main__":
  main()
