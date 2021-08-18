from os import system
from random import choice
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
        self.level = int(input('>> '))
        print(self.level)


    def get_word(self):
        with open('./files/data.txt', 'r', encoding='utf8') as f:
            self.org_word = choice(f.readlines())
            f.close()


    def norm(self):
        self.norm_word = normalize('NFD', self.org_word)
        self.norm_word = self.norm_word.encode('ascii', 'ignore').decode('utf8')


    def redraw_scr(self, context):
        # system('clear')
        print(context)
    
    
def main():
    game = HangManGame()

if __name__ == '__main__':
    main()
