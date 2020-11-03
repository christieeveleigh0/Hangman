import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    """ Return the users' guesses
    """
    return input('Guess the missing letter: ').lower()
 

def ask_file_name():
    """ Request which file should be used. If nothing is typed in, short_words.txt is used
    """
    file_name = input("Words file? [leave empty to use short_words.txt] : ")

    if not file_name:
        return 'short_words.txt' 
    return file_name


def select_random_word(words):
    """ Selecting a random word from the list we got in ask_file_name(). 
        Removing whitespace.
    """
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


def random_fill_word(word):
    """ Replaces a random character in the word from select_random_word() with an underscore
    """
    random_index = random.randint(0, len(word) - 1)
    new_word = []

    for i in range(0, len(word)):
        if i != random_index:
            new_word.append("_")
        else:
            new_word.append(word[random_index])

    return ''.join(new_word)


def is_missing_char(original_word, answer_word, char):
    
    duplicate_in_original = 0
    duplicate_in_answer = 0
    for i in range(0, len(original_word)):
        if char == original_word[i]:
            duplicate_in_original = duplicate_in_original + 1
    for i in range(0, len(original_word)):
        if char == answer_word[i]:
            duplicate_in_answer = duplicate_in_answer + 1

    if duplicate_in_original > 1: 
        return True

    if char in original_word and char not in answer_word:
        return True
    else: 
        return False



def fill_in_char(original_word, answer_word, char):
    added_char = []
    for i in range(0, len(original_word)):
        if char == original_word[i]:
            added_char.append(original_word[i])
        elif(original_word[i] == answer_word[i]):
            added_char.append(answer_word[i])
        else: 
            added_char.append("_")
    return ''.join(added_char)


def do_correct_answer(original_word, answer, guess):
    """ Prints the correct answer
    """
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


def do_wrong_answer(answer, number_guesses):
    """ Prints a message if the user guesses incorrectly
    """
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


def draw_figure(number_guesses):
    hangman = [
'''/----
|   0
|  /|\\
|   |
|  / \\
_______''',
'''/----
|   0
|  /|\\
|   |
|
_______''',
'''/----
|   0
|   |
|   |
|
_______''',
'''/----
|   0
|
|
|
_______''',
'''/----
|
|
|
|
_______'''
]
    print(hangman[number_guesses])


def run_game_loop(word, answer):

    number_of_guesses = 5 
    break_out = False

    print("Guess the word: "+answer)

    while(break_out == False):
        guess = get_user_input()
        if guess == 'exit' or guess == 'Exit' or guess == 'quit' or guess == 'Quit':
            print("Bye!")
            break

        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            number_of_guesses = number_of_guesses - 1
            do_wrong_answer(answer, number_of_guesses)
            
        if number_of_guesses == 0:
            break_out = True
            print("Sorry, you are out of guesses. The word was: "+word)
        
        if word == answer:
            break_out = True


if __name__ == "__main__":
    if len(sys.argv) == 1:
        words_file = "short_words.txt"
    else:
        words_file = sys.argv[1]

    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

