# Program prints ten verses of the song the ants go marching

def intro(num):

    ant = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    print("The ants go marching {0} by {0}, hurrah! hurrah!".format(ant[num]))
    print("The ants go marching {0} by {0}, hurrah! hurrah!".format(ant[num]))
    print("The ants go marching {0} by {0},".format(ant[num]))


def mainVerse(num):

    action = ["suck his thumb", "tie her shoe", "climb a tree", "shut the door", "take a dive", "pick up sticks",
            "pray to heaven", "roller skate", "check the time", "shout 'THE END!'"]

    print("The little one stops to {0},".format(action[num]))

def outro():

    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!\n")

def fullSong(num):

    intro(num-1)
    mainVerse(num-1)
    outro()

def main():
    for i in range(1, 11):
        fullSong(i)
        
main()