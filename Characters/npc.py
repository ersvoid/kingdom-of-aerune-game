from Functions.generate_character import random_npc, random_char
from Classes.inventory import long_sword, bastard_sword, great_sword, great_axe, fire_staff, short_sword
from Classes.magic import heal, firebolt

# Village people

blacksmith = random_npc(prof="shop")
innkeeper = random_npc(prof="inn")
mayor = random_npc(prof="mayor")
npc_town1 = random_npc()
npc_town2 = random_npc()
npc_town3 = random_npc()
npc_town4 = random_npc()
npc_town5 = random_npc()

town_pop = [mayor, blacksmith, innkeeper, npc_town1, npc_town2, npc_town3, npc_town4, npc_town5]


# Enemies


m_lst = [firebolt, heal]
w_lst = [short_sword, long_sword, great_axe, great_sword, fire_staff, bastard_sword]


bandit1 = random_char(0, [], w_lst[0])
bandit2 = random_char(0, [], w_lst[0])
bandit3 = random_char(0, [], w_lst[0])
bandit4 = random_char(0, [], w_lst[1])
bandit5 = random_char(0, [], w_lst[1])

sentry = random_char(100,  [], w_lst[3], a=8)
bodyguard = random_char(100,  [], w_lst[3], a=10)

bandit_leader = random_char(200,  [], w_lst[5], a=5)
fake_mayor = random_char(500, [], w_lst[5], a=6)
new_leader = random_char(100, [], w_lst[5], a=7)

troll = random_char(500,  [], w_lst[2], a=5)

wizard = random_char(1000,  m_lst, w_lst[4], a=10)

bandits = [bandit1, bandit2, bandit3]
guards = [sentry, bodyguard]
leaders = [bandit_leader, fake_mayor, new_leader]
trolls = [troll]
wizards = [wizard]
