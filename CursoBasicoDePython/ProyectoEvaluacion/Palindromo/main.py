def main():
    word = input('Enter a word and I will tell you if it is a palindrome'
                 '\n>>> ')
    # Remove the spaces and make all characters lowercase
    word = word.replace(' ','').lower()
    # Reverse the word
    drow = word[::-1]
    print('It is palindrome' if word == drow else 'It is not palindrome')


if __name__ == '__main__':
    main()
