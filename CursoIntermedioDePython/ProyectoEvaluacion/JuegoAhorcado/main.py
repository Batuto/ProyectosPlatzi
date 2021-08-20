from os import system
from random import choice
from time import sleep
from unicodedata import normalize


class HangManGame(object):
    def __init__(self):
        self.FH = b'\xe2\x99\xa5'
        self.VH = b'\xe2\x99\xa1'
        self.LVL_S_MSG = '''
        Welcome to the HangMan Game
        Please select the level:
        1 (default) - Easy - 15 Mistakes 
        2 - Medium - 9 Mistakes 
        3 - Hard - 5 Mistakes 
        '''
        self.level = self.select_level()
        self.get_word()
        self.redraw_scr(self.org_word)
        self.norm()
        self.redraw_scr(self.norm_word)


    def select_level(self):
        self.redraw_scr(self.LVL_S_MSG)
        self.level = int(self.input('>> '))


    def get_word(self):
        with open('./files/data.txt', 'r', encoding='utf8') as f:
            self.org_word = choice(f.readlines())
            f.close()


    def norm(self):
        self.norm_word = normalize('NFD', self.org_word)
        self.norm_word = self.norm_word.encode('ascii', 'ignore').decode('utf8')

    # TODO:
    # Add a method to split the word and the indexes, filter maybe with
    # a dictionary conversion


    def redraw_scr(self, context=''):
        system('clear')
        print(context)


    def input(self, msg):
        try:
            usr_value = input(msg)
            return usr_value
        except KeyboardInterrupt:
            self.redraw_scr()
            print("Thank you for using this game.")
            self.stimer_print("Closing...")
            exit()


    def stimer_print(self, text, time=0.3):
        # TODO: Make the delay work properly.
       for char in text+'\n':
           print(char, end="")
           sleep(time)

   
def main():
    game = HangManGame()


if __name__ == '__main__':
    main()
