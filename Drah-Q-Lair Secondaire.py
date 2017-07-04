##badEnd = 'The night is young, and the dead will live forever. . .'
##
##print('There is a large campfire at your feet, embers burning as if only recently snuffed out. At opposite ends from you there are 2 nap sacks that appear to be empty. Would you like to. . .') 
##print('Look at the nap sacks / Check out the fire / Wander into the dark?')
##
##nap sacks in the darkness
##answer = input()
##while answer != str.casefold('check out the fire'):
##    if answer == str.casefold('wander into the dark'):
##        print('You wander aimlessly into the woods, eventually being mauled by some unseen enemy of the night')
##        print(badEnd)
##        break
##    if answer == str.casefold('Look at the nap sacks'):
##        print('You deftly put your hands out in front of you as you lumber towards the empty nap sacks.')
##        print('Which one would you like to examine, left or right? Or, return to campfire?')
##        answer = input()
##        if answer == str.casefold('left'):
##            print('You walk up to the sack on the left but find it increasingly difficult to make anything out in the peering blackness.')
##        elif answer == str.casefold('right'):
##            print('You walk up to the sack on the right but find it increasingly difficult to make anything out in the peering blackness.')
##    elif answer == str.casefold('return to campfire'):
##        print('You turn back to face the campfire, still ashes and embers amongst the forest floor.')
##        break
#    else:
#        print('Please type "left", "right", or "return to campfire".')

#print('Would you like to... Look at the nap sacks / Check out the fire / Wander into the dark?')


##print('There is a large campfire at your feet, embers burning as if only recently snuffed out. At opposite ends from you there are 2 nap sacks that appear to be empty. Would you like to. . .') 
##print('Look at the nap sacks / Check out the fire / Wander into the dark?')
##
###nap sacks in the darkness
##answer = input()
##if answer == str.casefold('Look at the nap sacks'):
##    print('You deftly put your hands out in front of you as you lumber towards the empty nap sacks.')
##
##while True:
##    print('Which one would you like to examine, left or right? Or, return to campfire?')
##    answer = input()
##    if answer == str.casefold('left'):
##        print('You walk up to the sack on the left but find it increasingly difficult to make anything out in the peering blackness.')
##    elif answer == str.casefold('right'):
##        print('You walk up to the sack on the right but find it increasingly difficult to make anything out in the peering blackness.')
##    elif answer == str.casefold('return to campfire'):
##        print('You turn back to face the campfire, still ashes and embers amongst the forest floor.')
##        break
##    else:
##        print('Please type "left", "right", or "return to campfire".')
##
##print('Would you like to... Look at the nap sacks / Check out the fire / Wander into the dark?')



## SIMULATED BATTLE ##
import random
p1HP = 100
wolfHP = 20 

print('A Wolf jumps out at you ! ! !')
while wolfHP >= 1:
    print('Would you like to Attack / Run?')
    answer = input()
    if answer == str.casefold('attack'):
        import random
        damage = random.randint(0,10)
        if damage == 0:
            print('You swing your sword and miss!')
        print('You deal ' + str(damage) + ' damage to the wolf!')
        wolfHP = wolfHP - damage
        print(wolfHP)
    elif answer == str.casefold('run'):
        import random
        chance2run = random.randint(1,100)
        if chance2run <= 50:
            print('You can\'t get away!')
        if chance2run >= 51:
            print('You flee into the woods, never to be seen by this wolf again!')
            break

if wolfHP <= 0:
    print('You have bested the vile wolf!')

print(p1HP)




# MAP LAYOUT - on XY grid (A1, B6, C3, etc) make an (if p1char(location) = d3 print effect) loop
# Secret C'thulhu win item on each floor
# 
