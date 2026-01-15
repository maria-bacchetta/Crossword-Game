#OOP VERSION 4
import numpy as np
import time


with open('game_log.txt', mode =  'w') as game_log:
    game_log.write('username\tminutes  seconds\n')

dict_definitions = {"title":"----DEFINITIONS----", "title2": "ACROSS", "1": "1. like a gpa", "2":"2. felt deep affection","3":"3. ___ us, mobile game with an imposter","4":"4. lift or move to a higher position or level", "5":"5. brought to the final point, finished","title3": "DOWN", "A":"A. stare in an angry or fierce way ", "B":"B. one of two famous ancient cultures, like the great __ empire", "C":"C. keep away from or stop oneself from doing (something)", "D":"D. compact, thick, heavy of a substance maybe", "E":"E. sharpened", "Exit":"0. MainMenu"}
dict_answers = {"1":"GRADE", "2":"LOVED", "3":"AMONG", "4":"RAISE", "5":"ENDED", "A":"GLARE", "B":"ROMAN", "C": "AVOID", "D":"DENSE", "E":"EDGED"}


class Crossword():
    def __init__(self, rows, columns, dict_definitions, dict_answers):
        self.rows = rows
        self.columns = columns
        self.dict_definitions = dict_definitions
        self.dict_answers = dict_answers
    
    def create_empty_array(self):
        self.crossword_array = np.full((self.rows,self.columns),"_")
        return self.crossword_array
    

    def create_answer_array(self):
        self.list_answers = list(self.dict_answers.values())
        self.array_list = []
        for i in range(5):
            self.array_list.append(list(self.list_answers[i]))
            i += 1
        self.complete_array = np.array(self.array_list)
        return self.complete_array
    
    def __str__(self):
        return f"{self.create_empty_array()} \n\n{self.create_answer_array()}"     #GOTTA REMOVE THIS AT SOME POINT


class Game(Crossword):
    
    def log_in(self):
        x = input("Please write your username to play: ")
        confirm = input("Do you confirm your username? [Y/N]:")
        if confirm == "Y" or confirm == "y":
            with open('game_log.txt', mode =  'a') as game_log:
                game_log.write(x + 2*'\t')
            self.main_intro()
        else:
            self.log_in()
    
    def main_intro(self):
        print("-----Welcome to the crossword game!-----")
        global start
        start = time.perf_counter()
        #print("you start time is: ", start)
        print(self.create_empty_array())
        print()
        self.main_menu()

    def main_menu(self):
        print_mainmenu = [print(item) for item in ["----MAIN MENU----","1. see definitions","2. see game log","3. new game","0. exit game"]]
        x = input(">>Please select an option (type number): ")
        
        if x == "1":
            print()
            self.definition_menu()
        elif x == "2":
            print()
            self.open_game_log()
        elif x == "3":
            print()
            self.log_in()
        else:
            n = input("Are you sure you want to exit? [Y/N]:")
            if n == "Y" or n == "y":
                print()
            else:
                self.main_menu()
    
    def definition_menu(self):
        print_mainmenu = [print(item) for item in dict_definitions.values()]
        global x
        x = input("Select option (write number or capital letter): ")
        if x != 0:
            self.guess_word()
        else:
            self.main_intro()

    def guess_word(self):
        global word                             
        
        if x in dict_answers.keys() :
            word = dict_answers[x]
            blankguess = ["_" for item in word]
            print (dict_definitions[x],blankguess)
            global guess
            y = True
            while y == True:
                guess = str(input(">>write your guess: "))
                print("your guess is: ",list(guess.upper()))
                if len(guess) != len(word):
                    print("ERROR///Please put the right number of letters")
                    self.guess_word()
                y = input("Do you confirm your guess? [Y/N]: ")
                if y == "Y" or y == "y":
                    self.add_word_to_matrix()
                else:
                    y = True
        else:
            if x != '0':
                print("ERROR///Please input a digit or a capital letter that is listed///")
            self.definition_menu()
        #check_word()


    def add_word_to_matrix(self):
        try:
            self.crossword_array[int(x)-1] = list(guess.upper())            
        except ValueError :                                                 
            #print("i am in the value error block")
            if x == "A" :
                #print("i am in the if block")
                y = 0
            elif x =="B":
                y = 1
            elif x =="C":
                y = 2
            elif x =="D":
                y = 3
            elif x =="E":
                y =4
            self.crossword_array[:,y] = list(guess.upper())
        print()
        print("----Your crossword----")
        print(self.crossword_array)
        print()
        self.check_endgame()
    
    def check_endgame(self):
        #print("in timer_check method")
        if np.array_equal(self.crossword_array, self.create_answer_array()):
            #print("in if statement under timer_check")
            end = time.perf_counter()
            #print("the end time is ", end)
            print()
            print('>>>>CONGRATULATIONS<<<<')
            timer = end-start
            minutes = timer/60.
            seconds = timer - int(minutes)*60
            with open('game_log.txt', mode =  'a') as game_log:
                print(f'{int(minutes):<10}{int(seconds):<10}', file=game_log)
            print("You finished the crossword in ", int(minutes),":", int(seconds))
            print()
            self.main_menu()
        else:
            #print("in the else block of timer_check")
            self.definition_menu()

    def open_game_log(self):
        print("----GAME LOG----")
        with open('game_log.txt', mode =  'r') as game_log:
            try:
                for record in game_log:
                    username, minutes, seconds = record.split()             
                    print(f'{username:<10}{minutes:<10}{seconds:<10}')
            except ValueError:
                print("Error///no data in game log")
                print()
        print()
        self.main_menu()

Game1 =Game(5,5,dict_definitions, dict_answers)   
Game1.log_in()

