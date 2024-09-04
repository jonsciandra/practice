class Goblin:
    def __init__(self,gobName,gobJob,gobInterest):
        self.gobName = gobName
        self.gobJob = gobJob
        self.gobInterest = gobInterest
        
    def gobDetails(self):
        print(self.gobName,"is a", self.gobJob, "that enjoys", self.gobInterest)

def makeGoblin():
    print("\n")
    gobName = input("Give this goblin a name: ")
    gobJob = input("Give this goblin a job: ")
    gobInterest = input("Give this goblin an interest: ")
    my_goblin = Goblin(gobName,gobJob,gobInterest)
    return my_goblin # This returns our goblin to the rest of the program(caller?)

running = True

gobRoster={}

while running:

    userchoice = input("""\nWelcome to the Goblin Personnel Database. Please select an option and press enter:

      A) Make a goblin

      B) Find a goblin

      C) Show me all the goblins.

      > """)

    userchoice = userchoice.lower()

    if userchoice == "a":
        my_goblin = makeGoblin() 
        gobRoster[my_goblin.gobName.lower()] = my_goblin #makes a dictionary entry using the name from the goblin we just returned, and makes it so that entry = that goblin we made

    elif userchoice == "b":
        desiredGob = input("\nTell me what goblin you want to find: ")
        desiredGob = desiredGob.lower()                             # input creates a variable w/ name of goblin we wanna find
        if desiredGob in gobRoster:                                 #searches our dictionary for an entry with the name of the goblin entered
            foundGob = gobRoster[desiredGob]                        #assigns found goblin to a new variable name for ease of reference
            print("\n"+foundGob.gobName,"is a",foundGob.gobJob,"who enjoys",foundGob.gobInterest+".") #prints the info
        else:
            print("\nGoblin not found.")

    elif userchoice == "c":
        if gobRoster == {}:
            print("\nThere are no goblins currently.")
        else:
            print("\n")
            for keys in gobRoster:
                print(keys)

    else:
        print("\nPlease try another command!")
    
    
