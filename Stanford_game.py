import random

abc = 'abcdefghijklmnopqrstuvwxyz '
letter_list = list(abc)
letter_points = [1, 2, 2, 2, 1, 2, 2, 3, 1, 2, 3, 2, 2, 2, 1, 2, 3, 2, 2, 2, 1, 2, 3, 4, 2, 4, 1]
main_dict = dict(zip(letter_list, letter_points))

lives = 5
countries = "United States, United Kingdom, Canada, Australia, Germany, France, Japan, China, Brazil, Peru, " \
            "India, Mexico, Argentina, South Africa, Egypt, Italy, Spain, Sweden, Saudi Arabia, Nigeria, Argelia, " \
            "Belgium, Czech Republic, Netherlands, Chile, Venezuela, Cuba, Portugal, Costa Rica, Greece, Kuwait, " \
            "Colombia, Ireland, Scotland"

country_list = countries.split(", ")

def main():
    '''
    The main function sets the game with a dictionary, and country names.
    Also, starts the game and the selection menu
    :return: 
    '''


    # main set4


    # first messages
    print('Welcome to Hangman!!!\ndeveloped by Max\n')
    main_menu = int(input('What do you want to do?\nSelect one of the following options\n1 to start the game\n2 to '
                      'see the rules\n3 to end the game\n'))

    if main_menu == 1:
        start_game()
    elif main_menu == 2:
        rules()
    else:
        print('See you next time!!')


def start_game():
    remaining_lives = lives
    guess_word = random.choice(country_list)
    guess_word = guess_word.lower()
    len_word = len(guess_word)
    display_word = list('_' * len_word)
    good_guesses = 0
    finish_game = True
    chosen_letter_list = []
    score = 0



    print('\nWelcome to the game!!\nI am thinking a country name of', len_word, 'letters','\nYou have', lives, 'guesses left\n'
     
        'Available letters: ', abc)
    while remaining_lives > 0 and finish_game:
        result = ''
        while True:
            chosen_letter = input('\nPlease guess a letter: ')

            if chosen_letter not in chosen_letter_list:
                chosen_letter_list.append(chosen_letter)
                break
            else:
                print('You already guessed that letter, please try again!')

        if chosen_letter in guess_word:
            score += int(main_dict[chosen_letter])
            for i in range(len(guess_word)):
                if guess_word[(i-1)] == chosen_letter:
                    display_word[(i-1)] = chosen_letter
                else:
                    pass
            for item in display_word:
                result += item + ' '

            print('Good guess: ', result)
            good_guesses += int(guess_word.count(chosen_letter))
            if good_guesses == len_word:
                print('Congratulations! You guessed the country\n')
                finish_game = False

            # guess_word.count(chosen_letter)
        else:
            remaining_lives -= 1
            print('Oops! That letter is not in my word')
            print('You have', remaining_lives, 'remaining lives')

    if finish_game ==  True:
        print('\nSorry, you ran out of guesses. The word was else.')
        print('The country that I was thinking was', guess_word)
    # print(guess_word)
    # print(display_word)

    if remaining_lives == 5:
        score *= 2
    print('\nThanks for playing! We hope you have enjoyed it!')
    print('\n** Your score is:', score, '**')


def rules():
    print('\nGame Rules!\n')
    print('* You have 5 lives to guess the country.\n* Each letter has an individual score.\n* If you guess the word'
          'with all of your lives, your score will increase two times.\n* Letter Points: vocals 1 point each'
          '; h, k, q, and w count by 2; x, and z count by 4')

    confirmation1 = input('Do you want to go back to main menu? Select Y to play or N to end\n')
    if confirmation1 == 'Y' or confirmation1 == 'y':
        main()
    elif confirmation1 == 'N' or confirmation1 == 'n':
        print('Have a nice day!')
    else:
        print('Please insert a correct value')
        rules()

if __name__ == '__main__':
    main()




