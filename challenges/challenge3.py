'''
Given a lowercase string that has alphabetic characters only and no spaces,
 return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
'''
# Defining the function to take in a lowercase string as an argument


def solve(lowercaseString):

    # Input validation
    if not lowercaseString.islower() or any(char.isspace() for char in lowercaseString):
        print("Error: Please input a lowercase string with no spaces.")
        return

    # Initialization of the variables
    vowels = "aeiou"
    consonant_substrings = []  # An empty list to store the values of consonant substrings
    # Will be used to accumulate the value of the current consonant substring
    current_substring_value = None
    # Looping through the string by iterating through each character
    for char in lowercaseString:

        # Check if the current character is not a vowel
        if char not in vowels:
            # If current_substring_value is None, it is initialized to 0
            if current_substring_value is None:
                current_substring_value = 0

                # Calculate consonant value
            current_substring_value += ord(char) - ord("a") + 1
        else:
            # If the current character is a vowel and current_substring_value is not None,
            # it means the end of a consonant substring.
            # The accumulated value is appended to the list of consonant_substrings,
            # and current_substring_value is reset to None.
            if current_substring_value is not None:
                consonant_substrings.append(current_substring_value)
                current_substring_value = None

    # After the loop, the function returns the maximum value in the list of consonant_substrings.
    # The default=0 ensures that if there are no consonant substrings, it returns 0.
    return max(consonant_substrings, default=0)


# Calling the function with examples and printing out the result in the terminal
print(solve("zodiacs"))  # 26
print(solve("strength"))  # 57
print(solve("Stregth"))   # Please input a lowercase string with no spaces.
print(solve("my zodiac"))  # Please input a lowercase string with no spaces.
