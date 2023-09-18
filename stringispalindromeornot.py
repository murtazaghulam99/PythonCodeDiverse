def isPalindrome(input_str):
    n = len(input_str)
    for i in range(0, n // 2):
        if input_str[i] != input_str[n - i - 1]:
            return False
    return True

def main():
    input_str = input("Enter a string: ")
    result = isPalindrome(input_str)

    if result:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
