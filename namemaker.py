import math
import random

while True:
    print("")
    print("Welcome to the Name Maker!")
    print("Made by Spencer Boggs")
    restart = False
    while (restart == False):
        try: 
            minLetters = int(input("Enter the minimum number of letters: "))
        except ValueError:
            print("Please enter valid a number.")
            minLetters = 0
            restart = True
        try:
            maxLetters = int(input("Enter the maximum number of letters: "))
        except ValueError:
            print("Please enter valid a number.")
            maxLetters = 0
            restart = True
        try:
            minVowels = int(input("Enter the minimum number of vowels: "))
        except ValueError:
            print("Please enter valid a number.")
            minVowels = 0
            restart = True
        try:
            maxVowels = int(input("Enter the maximum number of vowels: "))
        except ValueError:
            print("Please enter valid a number.")
            maxVowels = 0
            restart = True
        try:
            generations = int(input("Enter the number of names to generate: "))
        except ValueError:
            print("Please enter valid a number.")
            generations = 0
            restart = True

        if(restart == False):
            if (minLetters != 0) and (maxLetters != 0) and (generations != 0):
                if ((maxLetters == 0) and (minLetters == 0)) or (minLetters > maxLetters) or (minVowels > maxVowels) or (minVowels > maxLetters):
                    print("")
                    print("Please enter numbers greater than 0 for min and max.")
                    print("And make sure min is less than max.")
                    restart = True
                else:
                    vowels = ["a", "e", "i", "o", "u"]
                    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

                    for i in range(generations):
                        while (maxVowels > len(vowels)):
                            vowels = vowels + vowels

                        vowelSample = random.sample(vowels, random.randint(minVowels, maxVowels))
                        maxConsonants = maxLetters - len(vowels)

                        while (maxConsonants > len(consonants)):
                            consonants = consonants + consonants

                        consonantSample = random.sample(consonants, maxConsonants)
                        all = vowelSample + consonantSample

                        length = random.randint(minLetters, maxLetters)
                        
                        while (length > len(all)):
                            all = all + all

                        result = "".join(random.sample(all, length))
                        print(result)
                    print("")

            else:
                print("Please enter numbers greater than 0 for min and max letters.")
