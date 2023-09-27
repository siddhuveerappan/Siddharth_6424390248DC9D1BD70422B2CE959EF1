class player:
    def play():
        print("The player is playing cricket")

class batsman(player):
    def play(self):
        print("The batsman is batting")

class bowler(player):
    def play(self):
        print("The bowler is bowling")

def main():
    batsmanObj = batsman()
    bowlerObj = bowler()

    batsmanObj.play()
    bowlerObj.play()

if __name__ == "__main__":
    main()
