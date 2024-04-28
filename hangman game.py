import random
import time

class HangmanGame:
    def __init__(self):
        self.word = ""
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        self.start_time = None
        self.end_time = None
        self.player_scores = {}
        self.categories = {
            "Animals": ['elephant', 'tiger', 'giraffe', 'lion', 'zebra', 'monkey'],
            "Movies": ['avatar', 'jaws', 'inception', 'titanic', 'matrix', 'frozen'],
            "Countries": ['canada', 'brazil', 'india', 'china', 'germany', 'australia'],
            "Sports": ['football', 'tennis', 'basketball', 'swimming', 'cricket', 'volleyball']
        }

    def choose_word(self, category):
        if category in self.categories:
            word_list = self.categories[category]
            self.word = random.choice(word_list)
        else:
            print("Invalid category. Choosing a random word.")
            self.word = random.choice(list(self.categories.values())[0])

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def calculate_score(self):
        elapsed_time = self.end_time - self.start_time
        score = round((1 / elapsed_time) * 1000) - (self.incorrect_guesses * 10)
        return max(score, 0)

    def update_leaderboard(self, player_name, score):
        if player_name in self.player_scores:
            if score > self.player_scores[player_name]:
                self.player_scores[player_name] = score
        else:
            self.player_scores[player_name] = score

    def display_leaderboard(self):
        sorted_scores = sorted(self.player_scores.items(), key=lambda x: x[1], reverse=True)
        print("\n--- LEADERBOARD ---")
        for i, (player, score) in enumerate(sorted_scores):
            print(f"{i+1}. {player}: {score} points")
        print("------------------")

    def provide_hint(self):
        hint_options = ["definition", "synonym", "clue"]
        hint = random.choice(hint_options)
        if hint == "definition":
            # Provide definition hint
            print("Hint: The word refers to a particular thing or concept.")
        elif hint == "synonym":
            # Provide synonym hint
            synonyms = {
                "elephant": ["pachyderm", "mammoth"],
                "tiger": ["feline", "panthera tigris"],
                "giraffe": ["tall mammal", "long neck"],
                "lion": ["king of the jungle", "panthera leo"],
                "zebra": ["hoofed mammal", "black and white stripes"],
                "monkey": ["primate", "tree-dweller"],
                "avatar": ["virtual representation", "digital form"],
                "jaws": ["shark movie", "great white"],
                "inception": ["dream within a dream", "Leonardo DiCaprio"],
                "titanic": ["shipwreck", "Rose and Jack"],
                "matrix": ["red pill or blue pill", "Keanu Reeves"],
                "frozen": ["Elsa and Anna", "Let It Go"],
                "canada": ["maple leaf", "hockey"],
                "brazil": ["Carnival", "Samba"],
                "india": ["Taj Mahal", "Bollywood"],
                "china": ["Great Wall", "Pandas"],
                "germany": ["Oktoberfest", "Berlin"],
                "australia": ["Kangaroos", "Sydney Opera House"],
                "football": ["soccer", "FIFA"],
                "tennis": ["Grand Slam", "Wimbledon"],
                "basketball": ["NBA", "Michael Jordan"],
                "swimming": ["Olympic sport", "butterfly stroke"],
                "cricket": ["bat and ball", "Sachin Tendulkar"],
                "volleyball": ["beach sport", "spiking the ball"]
            }
            print("Hint: A synonym for the word is:", random.choice(synonyms[self.word]))
        else:
            # Provide clue hint
            clues = {
                "elephant": "This animalhas a long trunk and large ears.",
                "tiger": "This animal is known for its stripes and is a member of the cat family.",
                "giraffe": "This animal has a long neck and is the tallest land animal.",
                "lion": "This animal is often referred to as the king of the jungle.",
                "zebra": "This animal is known for its black and white stripes.",
                "monkey": "This animal is a primate and is known for its tree-dwelling habits.",
                "avatar": "This movie is set in a virtual world where people can create avatars.",
                "jaws": "This movie is about a man-eating great white shark.",
                "inception": "This movie explores the concept of dreams within dreams.",
                "titanic": "This movie is based on the tragic sinking of a famous ship.",
                "matrix": "This movie is known for its iconic red pill or blue pill choice.",
                "frozen": "This movie features princesses Elsa and Anna and the popular song 'Let It Go'.",
                "canada": "This country is known for its maple leaf symbol and love for hockey.",
                "brazil": "This country is famous for its Carnival celebrations and energetic Samba dance.",
                "india": "This country is home to the Taj Mahal and a thriving Bollywood film industry.",
                "china": "This country is known for its Great Wall and adorable pandas.",
                "germany": "This country is famous for its Oktoberfest and the capital city of Berlin.",
                "australia": "This country is known for its unique wildlife, including kangaroos, and the Sydney Opera House.",
                "football": "This sport is also known as soccer and is played with a round ball.",
                "tennis": "This sport is played with a racket and a ball on a court.",
                "basketball": "This sport features teams trying to score points by shooting a ball through a hoop.",
                "swimming": "This sport involves propelling oneself through water using various strokes.",
                "cricket": "This sport is played with a bat and a ball and is popular in many countries.",
                "volleyball": "This sport is played with a ball over a net, and teams try to score points by hitting the ball over the net."
            }
            print("Hint:", clues[self.word])

    def play(self):
        print("Welcome to Hangman!")
        player_name = input("Please enter your name: ")
        category = input("Choose a category (Animals, Movies, Countries, Sports): ").capitalize()
        self.choose_word(category)
        print("Selected word:", self.display_word())
        self.start_timer()

        while True:
            guess = input("Guess a letter: ").lower()

            if guess == "hint":
                self.provide_hint()
                continue

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid guess. Please enter a single letter.")
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.word:
                print("Correct!")
                print("Word:", self.display_word())
            else:
                print("Incorrect!")
                self.incorrect_guesses += 1
                print("Attempts remaining:", self.max_incorrect_guesses - self.incorrect_guesses)

            if self.display_word() == self.word:
                self.stop_timer()
                score = self.calculate_score()
                print("Congratulations! You guessed the word:", self.word)
                print("Time taken:", round(self.end_time - self.start_time, 2), "seconds")
                print("Score:", score, "points")
                self.update_leaderboard(player_name, score)
                self.display_leaderboard()
                break

            if self.incorrect_guesses == self.max_incorrect_guesses:
                self.stop_timer()
                print("Game over! You ran out of attempts.")
                print("The word was:", self.word)
                self.display_leaderboard()
                break


game = HangmanGame()
game.play()