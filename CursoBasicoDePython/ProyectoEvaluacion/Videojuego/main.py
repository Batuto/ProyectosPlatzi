import random


MSG = """I will choose a number from 1 to 100,
and you must try to guess it before exceeding
your maximum attempts.
"""
DIFFICULTY = { 'easy': 15,
               'medium': 8,
               'hard': 5, }


def safe_ask_number(msg):
    try:
        answer = int(input(msg))
    except ValueError:
        print('Please write a number.')
        answer = safe_ask_number(msg)
    finally:
        return answer


def select_difficulty(again=''):
    msg='select a valid option:\n>>> '
    for dif, attm in DIFFICULTY.items():
        print(f'>>> {dif.capitalize()} - {attm} attempts.')
    answer = input(again + msg.capitalize()).lower()
    return DIFFICULTY.get(answer) or select_difficulty('Please ')


def main():
    print(MSG)
    difficulty = select_difficulty()
    r_num = random.randint(1,100)
    ASK_M = 'Give me a number:\n>>> '
    for i in range(difficulty):
        number = safe_ask_number(ASK_M)
        if number > r_num:
            ASK_M = 'Try again with a smaller number.\n>>> '
        elif number < r_num:
            ASK_M = 'Try again with a bigger number.\n>>> '
        elif number == r_num:
            print('Congratulations!, You got it.')
            break

    print('Thank you for playing.')


if __name__ == '__main__':
    main()
