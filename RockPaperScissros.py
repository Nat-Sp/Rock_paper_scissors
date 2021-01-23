import os
from random import choice


class Game:
    def __init__(self):
        self.current_player = None
        self.score = 0
        self.player_option = None
        self.computer_option = None
        self.running = True

    def run(self):
        self.greeting()
        self.set_up_file()
        while self.running:
            self.player_option = input('Rock, paper, scissors?')
            self.computer_option = choice(['rock', 'scissors', 'paper'])
            self.update_file_score()
            if self.valid_option():
                self.result()

    def result(self):
        condition = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if self.player_option == "!exit":
            print("Bye!")
            self.running = False

        elif self.player_option == "!rating":
            print(f'Your rating: {self.score}')

        elif self.player_option == self.computer_option:
            print(f"There is a draw ({self.computer_option})")
            self.score += 50

        elif self.computer_option == condition[self.player_option]:
            print(f"Well done. Computer chose {self.computer_option} and failed")
            self.score += 100

        else:
            print(f"Sorry, but computer chose {self.computer_option}")

    def valid_option(self) -> bool:
        valid_options = ['rock', 'scissors', 'paper', '!exit', '!rating']
        if self.player_option in valid_options:
            return True

        print('Invalid input')
        return False

    def greeting(self):
        name = input('Enter your name: ')
        print('Hello, ' + name)
        self.current_player = name

    def get_file_score(self):
        file = open('rating.txt', 'r')
        for line in file:
            name, score = line.split()
            if name == self.current_player:
                self.score = int(score)
        file.close()

    def set_up_file(self):
        try:
            file_size = os.path.getsize('rating.txt')
            if file_size == 0:
                file = open('rating.txt', 'a')
                file.write(self.current_player + ' ' + str(self.score))
                file.close()
            else:
                self.get_file_score()
        except FileNotFoundError:
            file = open('rating.txt', 'w')
            file.write(self.current_player + ' ' + str(self.score))
            file.close()

    def update_file_score(self):
        file = open('rating.txt', 'r')
        new_file_content = []
        for line in file:
            split_line = line.split()
            new_line = split_line[0] + ' ' + str(self.score)
            new_file_content.append(new_line)
            print(new_file_content)
        file.close()

        writing_file = open("rating.txt", "w")
        writing_file.writelines(new_file_content)
        writing_file.close()


if __name__ == "__main__":
    r = Game()
    r.run()