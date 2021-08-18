# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85

OLD_POINT_STRUCTURE = {
  0: [' '],  
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
    print("Let's play some Scrabble!\n")
    word = input("Enter a word to score: ")
    return word

def simple_scorer(word):
    word = list(word)
    return len(word)

def vowel_bonus_scorer(word):
    vowels = 'aeiou'
    points = 0
    for letter in word:
        if letter in vowels:
            points += 3
        else:
            points += 1
    return points

def scrabble_scorer(word):
    word = word.upper()
    letterPoints = 0

    for char in word:
        # for point_value in new_point_structure.values():
        for (key, values) in new_point_structure.items():
            if char is key:
                letterPoints += values
                # letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = values)

    return letterPoints
    # return old_scrabble_scorer(word)

scoring_algorithms = (
    {
        "name" : "Simple Score", 
        "description" : "Each letter is worth 1 point.", 
        "scoring_function" : simple_scorer
    },
    {
        "name" : "Bonus Vowels", 
        "description" : "Vowels are 3 pts, consonants are 1 pt.", 
        "scoring_function" : vowel_bonus_scorer
    },
    {
       "name" : "Scrabble", 
       "description" : "The traditional scoring algorithm.", 
       "scoring_function" : scrabble_scorer
    })

def scorer_prompt(word):
    while True:
        scoring_method = input("""
        Which scoring algorithm would you like to use?
        0 - Simple: One point per character
        1 - Vowel Bonus: Vowels are worth 3 points
        2 - Scrabble: Uses scrabble point system
        Enter 0, 1, or 2:
        """)
        try:
            scoring_method = int(scoring_method)
        except:
            print("\nPlease use numeric digits")
            continue
        if scoring_method < 0 or scoring_method > 2:
            print("\nPlease enter 0, 1, or 2")
            continue
        break #breaks out of while loop

    if scoring_method is 0:
        return simple_scorer(word)
    elif scoring_method is 1:
        return vowel_bonus_scorer(word)
    else:
        return scrabble_scorer(word)

def transform(OLD_POINT_STRUCTURE):
    NEW_POINT_STRUCTURE = {}
    for (key, values) in OLD_POINT_STRUCTURE.items():
        for value in values:
            NEW_POINT_STRUCTURE[value] = key
    return NEW_POINT_STRUCTURE

new_point_structure = transform(OLD_POINT_STRUCTURE)

def run_program():
    word = initial_prompt()
    choice = scorer_prompt(word)
    print(f"Score for {word}: {choice}")
