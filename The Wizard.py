#This is the first line

print("Greetings! So you want to be an adventurer?")
#Player enters name + counter for invalid names
playername = input("What is your name, brave soul? ")
namingcounter = 0
#Check if name contains only letters and while-loop with increasing counter for invalid names resulting in Bob as name
while not all(letter.isalpha() for letter in playername):
    namingcounter += 1
    if namingcounter == 1:
        print("That doesn't look like a name to me. Please use only letters.")
        playername = input("Let us try again. What is your name, brave soul? ")
    elif namingcounter == 2:
        print("Your name contains strange signs! Please use only letters, you can't be THIS fance they aren't able to discribe you proper.")
        playername = input("This is getting tiresome. Please tell me your name, brave soul? ")
    elif namingcounter == 3: 
        print("You aren't very good at this! I will just assign you a name if you prove incapable to follow even my most clear instgructions.")
        playername = input("ARGH. You can't be serious? ")
    elif namingcounter == 4:
        print("I cannot imagine you are incable of finishing this easy task. Are you perhabs pla<ying a prank on me?")
        playername = input("I DARE you to give me a proper name this time! ")
    elif namingcounter == 5:
        print("Enough of this foolishness! I shall name you myself! I declare you shall be called Bob!")
        playername = "Bob"
        break
    else:
        break
      
#Comments on name length and special message for Bob
if len(playername) <= 3 and playername is not "Bob":
    print("A rather short name! I will just assume your parents where not of noble birth and couldn't afford more letters. How tragic")
elif len(playername) >= 4 and len(playername) <= 8:
    print("A fine name! It has a nice ring to it. Not too long and not too short. Just about right.")
elif len(playername) > 8:
    print("What a long and fancy name you have! You must come from a noble family with a long history and a vault full of letters!")
elif playername == "Bob":
    print("Ok Bob, listen! You have an important task ahead of you. You must choose your path wisely!!!")
if playername == "Bob":
    print("Ok Bob, listen. YOU NEED A CLASS, OK? Warrior, Rogue, Wizard, whatever. Just pick one. They do differnt stuff, but don't worry. Just write the one down you are able to spell.")
    playerclass = input("Enter Warrior, Rogue, or Wizard. ")
else:
    print(f"And now dear {playername} you must choose your path.")
    print("There are three possible professions. You can aspire be a Warrior. Mighty in battle and tough as nails.")
    print("You can be a Rogue. Stealthy and cunning, striking from the shadows.")
    print("Or you can be a Wizard. Master of the arcane arts, wielding powerful magic.")
    print("Choose wisely, for your path will define your destiny!")
    playerclass = input("Enter Warrior, Rogue, or Wizard? ")

playerclass = playerclass.capitalize()
classcounter = 0
#Check if class is valid, if not increase counter and give hints, after invalid inputs, if player is Bob give special hints
while playerclass not in ["Warrior", "Rogue", "Wizard", "Jester"]:
    if playername != "Bob":
        playerclass = input(f"That is not a valid class {playername}. You need to choose Warrior, Rogue or Wizard.")
    else:
        playerclass = input("Ok Bob. I know this is very difficult for you. But I will help you through it. You see the keyboard right? Its the thing your fingers are probably touching right now. It has letters on it. You need to use those letters to spell W-i-z-a-r-d!")
        if playerclass.capitalize() == "Wizard":
            print("I..I..I can't believe it! You did it Bob! You spelled Wizard! Bob!!! You are amazing! A six letter Word! And it has a Z in it which is a very hard to use letter! I am so proud of you!")
        elif playerclass.capitalize() in ["Warrior", "Rogue"]:
            print(" Bob! I am so proud of you! You spelled a whole word! Even if it is not the one I asked for. But hey, you are on the right track! You can do it Bob!")
        else:
            classcounter += 1
            if classcounter == 1:
                playerclass = input("No Bob, that is still not correct. But I believe in you! You can do it! Just try again!")
            elif classcounter == 2:
                playerclass = input("Bob, Bob! What are you doing? Please for the love of all that is holy just type Wizard! You can do it Bob! I know you can!")
            elif classcounter == 3:
                print("Bob, I thought about us. You and me. I think the dilemma we are in is part my fault. Non of the 3 ways I laid out is the right one for you. I think, no, I KNOW you are born to be a jester.")
                playerclass = "Jester"
              

    

while playerclass != "Wizard":
    if playerclass == "Warrior":
        print(f"Ah, a Warrior! Brave and strong. {playername}. You will excel in close combat and lead your allies to victory.")
        print("Warriors are known for their resilience and prowess in battle. You will be a formidable force on the battlefield.")
        print("But let me be frank with you for a moment: When you are at this point this means you are either a friend of my creator or you play this to asses his skills. Either way...")
        print("you are probably an egghead, a nerd, a pencilpusher. Sorry to say it this directly but I mean it as a compliment. You have probably a fine head on your shoulders.")
        print("It would be a shame if you would lose it because some absolutly incompetent fool would come along and chop it off in a close quarters battle, would it?")
        playerclass = input("I think you should consider a different path. Maybe Rogue or Wizard?")
    if playerclass == "Rogue":
        print(f"A Rogue! Stealthy and cunning. {playername}. You will excel in agility and precision, striking from the shadows.")
        print("Rogues are known for their versatility and resourcefulness. You will be a master of deception and surprise attacks.")
        print("But let me be frank with you for a moment: When you are at this point this means you are either a friend of my creator or you play this to asses his skills. Either way...")
        print("you are probably an nerdy, inteligent and careful guy. Do you really want to risk your brain getting bashed in by some brutish oaf who is angry because you stole his wallet?")
        print("It would be a shame if you endet in a shallow grave or a dungeon because your hand trembled as you tryed to rob a baron and he caught you in the act.")
        playerclass = input("No. I think you should consider a different path. Maybe Warrior or Wizard?")
    if playerclass == "Jester":
        print(f"A Jester! Witty and entertaining. {playername}. You will excel in bringing joy and laughter to those around you... and probably bringing some headaches as well.")
        print("Jesters are known for their cleverness and humor. You will be a master of wit and satire.")
        print("But let me be frank with you for a moment: When you are at this point this means you are either a friend of my creator or you play this to asses his skills. Either way...")
        print("you are probably a fun and creative person. But do you really want to risk your life for the sake of a joke?")
        print(f"And {playername}! It would be a real shame if you would end up as the butt of a cruel prank.")
        print("No. I think you should consider a different path. I know I suggested that you should be a jester but I reassesed the options and you should really consider Wizard.")
        print("You can still be funny and entertaining as a Wizard. You can use your magic to create illusions and entertain people.")
        print(f"You are now a Wizard {playername}.")
        playerclass == "Wizard"

print(f"Excellent choice, {playername} the {playerclass}! You will be a master of the arcane arts, wielding powerful magic.")
#This is the last line