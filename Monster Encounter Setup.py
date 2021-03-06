import random

player_hp = 1000

num_spawned_monsters = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
random.shuffle(num_spawned_monsters)
if num_spawned_monsters[0] == 1:
    ai_type = ["boss"]  # will create variety later
elif num_spawned_monsters[0] == 2:
    ai_type = ["brothers"]  # will create variety later
elif num_spawned_monsters[0] == 3:
    ai_type = ["triplets"]  # will create variety later
elif num_spawned_monsters[0] == 4:
    ai_type = ["troggies"]  # will create variety later
elif num_spawned_monsters[0] == 5:
    ai_type = ["bug swarm"]  # will create variety later
random.shuffle(ai_type)
monster_ai = ai_type[0]
#Setting required variables depending on what enemy type is selected for the encounter
if monster_ai == "boss":
    #attack and ability list to be read by the chosen_attack_ai function
    attacks = ["Hammer slam"]  # will add more later
    ai_group_hp = 1500
    ai_power = 80
    ai_spawned = 1
    enter_word = "a"
    nickname = "Boss"
elif monster_ai == "brothers":
    attacks = ["Beat Down"]  # will add more later
    ai_group_hp = 750
    ai_power = 40
    ai_spawned = 2
    enter_word = "2"
    nickname = "Brother"
elif monster_ai == "triplets":
    attacks = ["Starlight beam"]  # will add more later
    ai_group_hp = 500
    ai_power = 25
    ai_spawned = 3
    enter_word = "the"
    nickname = "Triplet"
elif monster_ai == "troggies":
    attacks = ["Slash"]  # will add more later
    ai_group_hp = 375
    ai_power = 10
    ai_spawned = 4
    enter_word = "some"
    nickname = "Troggie"
elif monster_ai == "bug swarm":
    attacks = ["Scratch"]
    ai_group_hp = 300
    ai_power = 5
    ai_spawned = 5
    enter_word = "a"
    nickname = "Bug"

print("You encountered {} {}!".format(enter_word, monster_ai))
#nul variable set to be read by the encounter section to determine how many of what enemy to make selectable to attack and interact with
nul = 1337.1337
if ai_spawned == 1:
    ai_1_hp = ai_group_hp
    ai_2_hp = nul
    ai_3_hp = nul
    ai_4_hp = nul
    ai_5_hp = nul
    print(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
elif ai_spawned == 2:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = nul
    ai_4_hp = nul
    ai_5_hp = nul
    print(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
elif ai_spawned == 3:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = ai_group_hp
    ai_4_hp = nul
    ai_5_hp = nul
    print(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
elif ai_spawned == 4:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = ai_group_hp
    ai_4_hp = ai_group_hp
    ai_5_hp = nul
    print(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
elif ai_spawned == 5:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = ai_group_hp
    ai_4_hp = ai_group_hp
    ai_5_hp = ai_group_hp
    print(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
else:
    print("something went wrong :(")

def chose_attack_ai(attacks, ai_power, monster_ai):
    global damage_done_ai
    damage_done_ai = 0
    #This layer of 'if' statements selects which path of calculations will be taken dependant on what enemy is active
    if monster_ai == "boss":
        #Setting the different attack/ability values for the specific enemy
        Hammer_slam = [2 * ai_power, 2.1 * ai_power, 2.2 * ai_power, 2.3 * ai_power, 2.4 * ai_power, 2.5 * ai_power]
        #Randomly selecting which attack/ability to use
        random.shuffle(attacks)
        #Branching off into the different attacks variables
        if attacks[0] == 'Hammer slam':
            random.shuffle(Hammer_slam)
            crit_chance = random.randint(0, 9)
            if crit_chance == 9:
                damage_done_ai = Hammer_slam[0] * 2
                print("crit")
            elif crit_chance == 8:
                damage_done_ai = Hammer_slam[0] * 2
                print("crit")
            else:
                damage_done_ai = Hammer_slam[0]
                print("no crit")
    elif monster_ai == "brothers":
        Beat_down = [1 * ai_power, 1.1 * ai_power, 1.2 * ai_power, 1.3 * ai_power, 1.4 * ai_power, 1.5 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Beat Down":
            random.shuffle(Beat_down)
            crit_chance = random.randint(0, 9)
            if crit_chance == 9:
                damage_done_ai = Beat_down[0] * 2
                print("crit")
            elif crit_chance == 8:
                damage_done_ai = Beat_down[0] * 2
                print("crit")
            else:
                damage_done_ai = Beat_down[0]
                print("no crit")
    elif monster_ai == "triplets":
        Starlight_beam = [1.5 * ai_power, 1.6 * ai_power, 1.7 * ai_power, 1.8 * ai_power, 1.9 * ai_power, 2 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Starlight beam":
            random.shuffle(Starlight_beam)
            crit_chance = random.randint(0, 9)
            if crit_chance == 9:
                damage_done_ai = Starlight_beam[0] * 2
                print("crit")
            elif crit_chance == 8:
                damage_done_ai = Starlight_beam[0] * 2
                print("crit")
            else:
                damage_done_ai = Starlight_beam[0]
                print("no crit")
    elif monster_ai == "troggies":
        Slash = [1.5 * ai_power, 1.6 * ai_power, 1.7 * ai_power, 1.8 * ai_power, 1.9 * ai_power, 2 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Slash":
            random.shuffle(Slash)
            crit_chance = random.randint(0, 9)
            if crit_chance == 9:
                damage_done_ai = Slash[0] * 2
                print("crit")
            elif crit_chance == 8:
                damage_done_ai = Slash[0] * 2
                print("crit")
            else:
                damage_done_ai = Slash[0]
                print("no crit")
    elif monster_ai == "bug swarm":
        Scratch = [1 * ai_power, 1.1 * ai_power, 1.2 * ai_power, 1.3 * ai_power, 1.4 * ai_power, 1.5 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Scratch":
            random.shuffle(Scratch)
            crit_chance = random.randint(0, 9)
            if crit_chance == 9:
                damage_done_ai = Scratch[0] * 2
                print("crit")
            elif crit_chance == 8:
                damage_done_ai = Scratch[0] * 2
                print("crit")
            else:
                damage_done_ai = Scratch[0]
                print("no crit")
    else:
        print("something went wrong :(")

chose_attack_ai(attacks, ai_power, monster_ai)
print(damage_done_ai)
