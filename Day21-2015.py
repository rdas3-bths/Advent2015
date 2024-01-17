def get_item_stats(equipment, item_stats):
    weapon = equipment[0]
    armor = equipment[1]
    ring1 = equipment[2]
    ring2 = equipment[3]

    weapon_cost = item_stats[weapon]["cost"]
    armor_cost = item_stats[armor]["cost"]
    ring1_cost = item_stats[ring1]["cost"]
    ring2_cost = item_stats[ring2]["cost"]
    total_cost = weapon_cost + armor_cost + ring1_cost + ring2_cost

    weapon_dmg = item_stats[weapon]["damage"]
    armor_dmg = item_stats[armor]["damage"]
    ring1_dmg = item_stats[ring1]["damage"]
    ring2_dmg = item_stats[ring2]["damage"]
    total_dmg = weapon_dmg + armor_dmg + ring1_dmg + ring2_dmg

    weapon_armor = item_stats[weapon]["armor"]
    armor_armor = item_stats[armor]["armor"]
    ring1_armor = item_stats[ring1]["armor"]
    ring2_armor = item_stats[ring2]["armor"]
    total_armor = weapon_armor + armor_armor + ring1_armor + ring2_armor

    # print(equipment)
    # print("Total cost is", total_cost)
    # print("Total damage is", total_dmg)
    # print("Total armor is", total_armor)
    return total_cost, total_dmg, total_armor


def do_fight(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    boss_damage = boss_damage - player_armor
    player_damage = player_damage - boss_armor
    while player_hp > 0 and boss_hp > 0:
        boss_hp = boss_hp - player_damage
        if boss_hp < 1 and player_hp > 0:
            return True
        player_hp = player_hp - boss_damage

    return False


# initialize lists
weapons = ["Dagger", "Shortsword", "Warhammer" , "Longsword", "Greataxe"]
armor_list = ["None", "Leather", "Chainmail", "Splintmail", "Bandedmail", "Platemail"]
left_ring = [ "None", "Damage1", "Damage2", "Damage3", "Defense1", "Defense2", "Defense3" ]
right_ring = [ "None", "Damage1", "Damage2", "Damage3", "Defense1", "Defense2", "Defense3" ]

equipment_combinations = []
for w in weapons:
    for a in armor_list:
        for lr in left_ring:
            for rr in right_ring:
                if lr == "None" and rr == "None":
                    equipment_combinations.append((w, a, lr, rr))
                elif lr != rr:
                    equipment_combinations.append((w, a, lr, rr))

print(len(equipment_combinations))
item_stats = {}

for line in open("data/Day21-2015_Input"):
    line = line.rstrip()
    while line.find("  ") != -1:
        line = line.replace("  ", " ")

    item = {}
    data = line.split(" ")
    item_name = data[0]
    item_cost = int(data[1])
    item_damage = int(data[2])
    item_armor = int(data[3])
    item_stats[item_name] = { "cost" : item_cost, "damage": item_damage, "armor": item_armor }


boss_hp = 109
boss_damage = 8
boss_armor = 2
player_hp = 100
losing_costs = []

item_stats["None"] = { "cost": 0, "damage": 0, "armor": 0 }
for equipment in equipment_combinations:
    cost, damage, armor = get_item_stats(equipment, item_stats)
    if not do_fight(player_hp, damage, armor, boss_hp, boss_damage, boss_armor):
        losing_costs.append(cost)

print(max(losing_costs))