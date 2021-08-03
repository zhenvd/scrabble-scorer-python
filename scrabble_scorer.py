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

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints;

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")


def simple_scorer():
   return 

def vowel_bonus_scorer():
    return 

def scrabble_scorer():
    return

# is there a better way to write this?
scoring_algorithms = ()

def scorer_prompt():
    return 

def transform():
    return

# new_point_structure = transform(old_point_structure)

## how much of this to give to students?
def run_program():
    word = initial_prompt()
    # scorer = scorer_prompt()["scorer_function"]

    # score = scorer(word)
    # print('Score for {word}: {score}\n'.format(word = word, score = score))

   