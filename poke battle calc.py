print('pokemon battle calculator')
x=int()
y=int()
z=int()
print('choose a starter')
#comment line for git test
#starter=input('''press:-
                    #1)A for charmander
                    #2)B for squirtle
                    #3)C for bulbasaur
                #''')
print('''REMEMBER:-
            (1)-->HP
            (2)-->ATTACK
            (3)-->DEFENSE
            (4)-->SPECIAL ATTACK
            (5)-->SPECIAL DEFENSE
            (6)-->SPEED
        ''')
print('now please feed the info of your starter pokemon')
HP_BAR=int(input('(1)'))
ATTACK=int(input('(2)'))
DEFENSE=int(input('(3)'))
SPECIAL_ATTACK=int(input('(4)'))
SPECIAL_DEFENSE=int(input('(5)'))
SPEED=int(input('(6)'))
HP_NUMBER=(int(HP_BAR)*10)
Q=input('press b to start and r to exit')
while Q=='b':
    print('lets start the battle!!')
    print('please type the stats of the wild pokemon')
    HP_BAR_W=int(input('(1)'))
    ATTACK_W=int(input('(2)'))
    DEFENSE_W=int(input('(3)'))
    SPECIAL_ATTACK_W=int(input('(4)'))
    SPECIAL_DEFENSE_W=int(input('(5)'))
    SPEED_W=int(input('(6)'))
    HP_NUMBER_W=(int(HP_BAR_W)*10)
    start_conform=input('all set press OK to start')
    while start_conform=='OK':
        if  HP_NUMBER_W<=0:
            print('you have fainted the wild pokemon')
            break
        if  HP_NUMBER<=0:
            print('your pokemon is fainted!')
            break
        print('its your turn')
        print('your pokemon HP: ',int(HP_NUMBER))
        print('wild pokemon HP: ',int(HP_NUMBER_W))
        dice_number=int(input('roll a dice and enter in to attack '))
        HP_NUMBER_W=HP_NUMBER_W-(dice_number+(ATTACK/2)+(SPECIAL_ATTACK)-(SPECIAL_DEFENSE_W/3)-(DEFENSE_W/3)-(SPEED_W/4))
        dice_number_w=int(input('roll a dice forwild pokemon to attack '))
        HP_NUMBER=HP_NUMBER-(dice_number_w+(ATTACK_W/2)+(SPECIAL_ATTACK_W)-(SPECIAL_DEFENSE/3)-(DEFENSE/3)-(SPEED/4))
        if  HP_NUMBER_W<=0:
            print('you have fainted the wild pokemon')
            break
        if  HP_NUMBER<=0:
            print('your pokemon is fainted!')
            break
        x+=1

        
        
        
    
    

 
