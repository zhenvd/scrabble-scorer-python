# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
};

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if old_point_structure[point_value].index(char) != -1:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints;

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   word = ""
   word = input("Enter a word to score: ")
 
   return word;


def simple_scorer(word):
   return len(word)

def vowel_bonus_scorer(word):
    score = 0;
    vowels = 'aeiou'

    for char in word:

        if vowels.find(char.lower()) != -1 :
            score += 3
        else:
            score += 1

    return score

def scrabble_scorer(word):
    score = 0

    for char in word:
        score += new_point_structure[char.lower()]

    return score

# is there a better way to write this?
scoring_algorithms = (
    {
        "name": "Simple",
        "description": "One point per character",
        "scorer_function": simple_scorer
    },
    {
        "name": "Vowel Bonus",
        "description": "Vowels are worth 3 points",
        "scorer_function": vowel_bonus_scorer
    },
    {
        "name": "Scrabble",
        "description": "Uses scrabble point system",
        "scorer_function": scrabble_scorer
    }
)

def scorer_prompt():
    print("Which scoring algorithm would you like to use?\n")
    for scorer in scoring_algorithms:
        option_number = scoring_algorithms.index(scorer)
        print(str(option_number) + " - " + scorer["name"]+": " + scorer["description"]);
    
    choice = int(input("Enter 0, 1, or 2:"))

    return scoring_algorithms[choice];

def transform(letters_by_score):
    scores_by_letter = {};

    for score in letters_by_score:
        letters = letters_by_score[score]

        for letter in letters:
            scores_by_letter[letter.lower()] = int(score)       

    return scores_by_letter

new_point_structure = transform(old_point_structure)

def run_program():
    word = initial_prompt()
    scorer = scorer_prompt()["scorer_function"]

    score = scorer(word)
    print('Score for {word}: {score}\n'.format(word = word, score = score))
   