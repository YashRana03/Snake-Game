from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 12, "normal")


# ScoreBoard class: creates a scoreboard to keep track of the game score
class ScoreBoard(Turtle):
    # Initialises the ScoreBoard object
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_high_score())
        self.goto(0, 275)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    # Reads the all-time high score from a txt file and returns it
    def get_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()
        return high_score

    # Updates the scoreboard on the screen
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    # Resets the score to zero
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # Increases the score by one
    def increase(self):
        self.score += 1
        self.update_scoreboard()

