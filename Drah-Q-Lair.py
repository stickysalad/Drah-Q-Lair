confirm = 'yes' or 'y'
badEnd = 'The night is young, and the dead will live forever. . .'
import sys



print('Welcome to Drah-Q-Lair')
print('What is your name. . .')

p1name = input() #player name

print('The storm crashes behind you as you stand on the porch of the first floor of Draculas accursed mansion.')
print('Late night drinkers from the bar at the nearby town spoke of a nefarious meeting between Dracula and his Minions of Mayhem.')
print(p1name + ', it is your job to rid the world of these evils in ONE NIGHT! ! !')

print('Open the door . . ?')

while True:
    print('Type "yes" or "no". . .')
    answer = input()
    if answer == confirm:
        print('The doors swing wide as you enter into the cold and dimly lit mansion.')
        break
    elif answer == 'no':
        sys.exit(print('You turn away from the mansion, never to be heard from again. . .')) #How do I end the program here?
        break
    else:
        print('You mumble something incoherent at the door and it stares back at you vacantly.')

if answer == confirm:
    print('As the heavy wooden doors creak open you are struck awoke in the night by your campfire, which has long since died.')

## SECONDARY IDEA SO FAR ##
print('There is a large campfire at your feet, embers burning as if only recently snuffed out. At opposite ends from you there are 2 nap sacks that appear to be empty. Would you like to. . .') 
print('Look at the nap sacks / Check out the fire / Wander into the dark?')

answer = input() # Nap Sacks in the Darkness
while answer != str.casefold('check out the fire'):
    if answer == str.casefold('wander into the dark'):
        print('You wander aimlessly into the woods, eventually being mauled by some unseen enemy of the night')
        print(badEnd)
        break
    if answer == str.casefold('Look at the nap sacks'):
        print('You deftly put your hands out in front of you as you lumber towards the empty nap sacks.')
        print('Which one would you like to examine, left or right? Or, return to campfire?')
        answer = input()
        if answer == str.casefold('left'):
            print('You walk up to the sack on the left but find it increasingly difficult to make anything out in the peering blackness. Return to campfire?')
            answer = input()
            if answer == str.casefold('yes'):
                print('You turn back to face the campfire, still ashes and embers amongst the forest floor.')
            break
        elif answer == str.casefold('right'):
            print('You walk up to the sack on the right but find it increasingly difficult to make anything out in the peering blackness. Return to campfire?')
            answer = input()
            if answer == str.casefold('yes'):
                print('You turn back to face the campfire, still ashes and embers amongst the forest floor.')
        break
    elif answer == str.casefold('return to campfire'):
        print('You turn back to face the campfire, still ashes and embers amongst the forest floor.')
        break
#    else:
#        print('Please type "left", "right", or "return to campfire".')
# I can't figure out how to add this to the loop so that if someone types something other than a recognizable input it will offer that text and then return to the loop.

if answer == str.casefold('return to campfire'):
    print('Examine campfire?')
    answer = input()
if answer == 'yes':
    print('There seems to still be enough embers to start the fire back up, if done properly. Rekindle the fire?')
if answer == str.casefold('check out the fire'):
    print('There seems to still be enough embers to start the fire back up, if done properly. Rekindle the fire?')




## END OF SECONDARY IDEA ##




#def(p1stats):
#    HP = 100



## GENERAL NOTES
# Can I set text-write speed?
# How do I keep track of their placement on map?
# Design map layout
# Wolfman -> Swamp Thing -> Frakenstein's Monster -> Mr. Hyde -> Dracula
# C'Thulhu bad end will be a series of variable checks on p1char, for C'thulhu good ending items


## WOLFMAN'S FOREST
# Start in the middle of the night at a campfire. Your two companions are missing, except for their lugagge.
#

## SWAMPMAN'S LAIR
# Backwater hut / swamp locale
#

## FRANKENSTEIN'S MONSTER
# Located in a 3 story windmill

## MR. HYDE'S MANSION
# Located in a mansion of course.
#
