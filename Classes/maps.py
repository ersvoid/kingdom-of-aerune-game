from Characters.npc import town_pop, bandits, guards, trolls, wizards, leaders
from Functions.generate_character import random_bandit


class Location:
    def __init__(self, name, index, intro, pop, lst, i1="", i2="", i3="", o1="", o2=""):
        self.name = name
        self.index = index
        self.intro = intro
        self.pop = pop
        self.lst = lst
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.o1 = o1
        self.o2 = o2

    def get_name(self):
        return self.name

    def __str__(self):
        print(self.intro)

    def census(self):
        return len(self.pop)

    def list_map(self):
        for i in self.lst:
            print(i)


# Shops
s0_intro = """The blacksmith looks up from his labor as you approach him."""
s0_shop = Location("Blacksmith", "s0", s0_intro, [town_pop[1]], [])

# Houses
h0_intro = """The house is in bad shape, even for this village.  The door is little more than thick burlap stretched 
across a wooden frame and opens onto a dirt-floored shack with a shoddily-thatched roof.  There is a decent framed-bed, 
at least, shoved into a corner, a wooden chest beside it, and one chair next to a table in the opposite corner.  A lone 
villager stands inside, surprised at your intrusion."""
h0_house = Location("House", "h0", h0_intro, [town_pop[3]], [])

h1_intro = """QUEST MENU"""
h1_hall = Location("QUEST", "h1", h1_intro, [town_pop[0]], [])

# Inn
i0_intro = """The inn is the largest building in town, though it is still one story it has a massive stone fireplace in
the center of the main hall and you are bathed in warm, low light as you enter.  The innkeeper looks up from a bar 
towards you and welcomes you in."""
i0_inn = Location("Inn", "i0", i0_intro, [town_pop[2]], [])

t0_town_list = [s0_shop, i0_inn, h0_house, h1_hall]

# Towns
t0_intro = """You stand at the entrance of a small village of about ten small cottages.  The smell of firewood 
and food drifts lazily from several of the stone chimneys.  A loud clank followed by a metallic ring echoes down the 
the only street from a blacksmith's anvil outside one of the cottages."""
t0_town = Location("Town", "t0", t0_intro, town_pop, t0_town_list)

t1_intro = """After several more hours of walking, and as the light begins to fade, you see a walled village next to a 
large forest.  There are no lights or sounds from this town."""
t1_town = Location("Abandoned Town", "t1", t1_intro, town_pop, t0_town_list)

# Dungeons
q0_intro = """In the darkness, you see a glimmering light and moving shadows through the trees.  As you approach, you 
see three tents casting large, darting shadows into the woods beside a fire flaring in the cold night wind.  A lone 
figure sits beside the fire, looking through a backpack."""
q0_i1 = "You have decided to embark on your first quest and save the town from bandits!"
q0_i2 = """You make your way out of town as the villagers cheer you on.  News has spread quickly of your 
heroism.  You set upon the dirt path towards the woods.  You are halfway there when you notice another
trail diverging off and entering the woods in a different location than the main path.  The trail is faint, 
but looks fresh.  You follow the trail into the woods."""
q0_i3 = "The sky darkens, but now you can see a faint glimmer in front of you."
q0_o1 = "You have killed the bandit!"
q0_o2 = "You begin the walk back to the village."
q0_dung = Location("Bandit Campsite", "d0", q0_intro, bandits, [], q0_i1, q0_i2, q0_i3, q0_o1, q0_o2)

d1_intro = """There are two men standing beside a campfire and three tents.  One of the men, grabs his pack and heads into
the trees, running as fast as he can through the bramble.  The other man, sighs, turns to face you, and pulls out his
sword."""
q1_i1 = """You feel a sense of urgency to deal with the remaining bandits in fear of their reprisals upon the 
town.  You hastily make for the road again and are quickly within range of the trees."""
q1_i2 = """You know your way now and run through the trees.  You arrive back at the campsite in the woods.  You can 
hear voices up ahead. You slow down and listen from behind a tree. This time there are 
two other bandits, sitting forlornly around the dying fire.  It sounds like the two men are arguing.
'We should leave this area! They know where we are and they\'ll be back to kill the rest of us!'
'You can leave if you like, coward! I will stay here and kill everyone in that town if I have too!'"""

q1_i3 = """You decide that listening behind a tree isn't why you traveled halfway across the empire...
You jump out from behind the tree and draw forth your weapon."""
q1_o1 = "You have defeated the bandit!"
q1_o2 = "You begin the walk back to the village."
q1_dung = Location("Bandit Campsite", "d1", d1_intro, bandits, [], q1_i1, q1_i2, q1_i3, q1_o1, q1_o2)

d2_intro = """As your are making your way back to the bandits' hideout, you see a lone figure walking your way down the
path.  It is a tall, broad figure and he slowly draws his sword as he nears..."""
q2_i1 = """The mayor assures you that the leader of the bandits is the only remaining member still in the area.  He says
that the same carriage that brought you was waylaid by the ruffian and everyone murdered and robbed of their 
possessions.  You imagine yourself among them had you any delay in your own trip to the frontier.  Perhaps another 
young adventurer to help the town was struck down before his time..."""
q2_i2 = """You shake off these thoughts of the meaninglessness of existence.  The flow of time and our paths through 
it our but for the gods to worry about.  You must face the leader of the bandits and defeat him or more innocent 
people will die."""
q2_i3 = """You leave town as the women of the village wave you off with tears in their eyes. They don't think you 
will return."""
q2_o1 = "You have killed the Bandit Leader!"
q2_o2 = "You begin the walk back to the village."
q2_dung = Location("Forest", "d2", d2_intro, leaders, [], q2_i1, q2_i2, q2_i3, q2_o1, q2_o2)

d3_intro = """The sun is shining and you are excited to be back on the road again.  You should make the next village 
before nightfall.  Up ahead is a short, covered bridge and you decide to take a rest.  As you near the bridge, you are
overcome by the smell of rotting bodies strewn about below on the banks of the river.  A huge, ragged man is beside 
one of the bodies, eating the flesh raw.  He turns, sees you, and the eyes roll back into his head..."""
q3_i1 = """The mayor thanks you for all that you have done, but now he worries about the neighboring village.  They 
have not sent word for some time and though they are better protected than this village, they are further into the 
untamed frontier where wild men and magic roam."""
q3_i2 = """You say your good byes and receive as many in return.  You wonder if you will ever see any of these people 
again, if your path will lead you back to them some day.  You worry not, and ready yourself for the long journey 
ahead."""
q3_i3 = """The village fades in the distance behind you and soon all you can hear is the chittering of birds and the
wild wind blowing over the grass."""
q3_o1 = "You have killed the bridge troll!"
q3_o2 = "You begin the walk back to the village."
q3_dung = Location("Bridge", "d3", d3_intro, trolls, [], q3_i1, q3_i2, q3_i3, q3_o1, q3_o2)

d4_intro = """The town has been deserted, but you see smoke drifting from one of the houses.  You decide to 
investigate."""
q4_i1 = "You leave the bridge and all the death behind..."
q4_i2 = """You try to forget the images racing through your mind: all the bodies strewn about, ripper apart, the 
fetid horror with the blood dripping down his lips..."""
q4_i3 = """As the sun falls, the shadows lengthen and play tricks on your tired mind... Every tree is another 
abomination reaching to taste your flesh... As you round a bend, you are relieved to spot the next village on a small 
hill.  The village looks dark behind a tall palisade, but the main gate is open.  You pass through the remnants of an 
older wall, made of stone and ruined, at the base of the hill.  You begin the slow walk up to and through the main 
gate."""
q4_o1 = "You have killed the ruthless vagabond!"
q4_o2 = "You begin the walk back to the village."
q4_dung = Location("Village Hall", "d4", d4_intro, leaders, [], q4_i1, q4_i2, q4_i3, q4_o1, q4_o2)

d5_intro = """You have decided to explore the area and set out from the gates of town.  You have been wandering around 
the countryside for about an hour when you realize you are being watched.  You brandish your weapon and call out for 
the coward."""
q5_i1 = """The town is a graveyard.  There are not many people left besides those with the means to defend themselves.  
The bodies piled up in the streets and there are not enough people to dig graves, so the remaining villages 
constructed a large funeral pyre and the bodies laid inside..."""
q5_i2 = """Now that there are so few remaining, the town, and the mayor, look to you, their savior, for guidance.  You 
are not sure how you can be of help with the town itself, but you assure the people that you will remain for awhile 
and patrol the area."""
q5_i3 = """This new life is becoming more than you had imagined.  Now burdened with responsibility, you see why so 
many turn to thievery and murder for profit and power.  You smile to yourself...  Maybe in the next life, you think."""
q5_o1 = "You have killed the new Bandit Leader!"
q5_o2 = "You begin the walk back to the village."
q5_dung = Location("Forest", "d5", d5_intro, leaders, [], q5_i1, q5_i2, q5_i3, q5_o1, q5_o2)

d6_intro = """One day, while on patrol, you are caught off guard as you round small grouping of trees.  A pale, thin 
man with deep bags under his eyes jumps from the trees and stands in your way."""
q6_i1 = """You make a new life for yourself in this village.  You have become the sheriff and sole protector of these
people.  Their lives depend on you.  You awake every morning in your own home now, gifted to you by the people of the 
town for saving them.  Its not much and in fact is probably the worst house in town, but you are not bothered.  You 
will not remain in the place forever.  Soon, greater adventure will call to you."""
q6_i2 = """Your daily patrol takes you out and away from town, but never too far.  You make a point to travel to the 
bridge every few days to ensure that no new demon has taken refuge there.  Soon, messengers from the previous 
village return and trade begins and a new life is born in the village you saved."""
q6_i3 = """Every week or so, a new person arrives to make a new life for themselves on the frontier, undeterred by the 
recent horrors visited upon this town.  Quite like you, you suppose."""
q6_o1 = "You have killed the wizard's apprentice!"
q6_o2 = "You begin the walk back to the village."
q6_dung = Location("Inn", "61", d6_intro, bandits, [], q6_i1, q6_i2, q6_i3, q6_o1, q6_o2)

d7_intro = """Everyone in town knows where the abandoned tower in the woods is located.  They point you in the right 
direction and you have barely trekked for an hour when you see the crumbling structure rising through the tree tops on 
a distant hill.  You make your way to the bottom of the hill and find no clear path to the top.  You will have to climb.
Luckily, the hill is actually an uplifted block of layered quartzarenite with cross-cutting faults at around 70 degree 
to the bedding plane.  So, fairly easily crack climbing.  Though, it takes you several hours to get to the top because 
you didn't realize you had a fear of heights.  You climb over the edge and collapse beside a tree. 
\n
You fall asleep...\n
You wake up from a dream of your first kiss back at the academy...\n
You drink from your canteen and prepare yourself.  You begin your final approach on the tower.  As you get nearer, you 
notice a guard posted out front.  You draw your weapon as you approach..."""
q7_i1 = """You had no idea that a frontier savage could learn the fine art and science of magic!  Magic is taught in the
inner empire only, by law.  In fact, you had to secure several permits to travel outside the inner empire as a 
magic-user..."""
q7_i2 = """Is there some form of unknown, primal magic out here in the wild?  No, no that can't be it, you think.  The
wild man had a staff.  The same staff that they make in the magic academy!  This wild man could never had been an 
academic!  He could hardly control the staff he was wielding!"""
q7_i3 = """You decide to ask around town about the man and his staff.  Where could he have gotten it?  Where there any 
mages out here that they knew of? Perhaps, mages they thought were killed or had to be dead by now?  You only get back 
one answer: 'All the bad people go to the tower and come back evil...'"""
q7_o1 = "You have killed the bandit!"
q7_o2 = "You begin the walk back to the village."
q7_dung = Location("Wizard's Tower Entrance", "d7", d7_intro, guards, [], q7_i1, q7_i2, q7_i3, q7_o1, q7_o2)

d8_intro = """You walk through the ruined archway and descend into a recessed chamber lined with tapestries.  There is 
only a single man sitting in a chair in the center of the room.  He looks up from his book and smiles at you..."""
q8_i1 = """The sentry is dead at your feet.  He was not a mage.  The tower rises above you.  Now that you see it 
up close, you realize that only the top layers have crumbled away.  There must be at least four levels of usable 
rooms in this tower..."""
q8_i2 = """The tower is made of some kind of black stone, maybe volcanic, but it does not feel like natural stone.  
The tower entrance is a large archway of crumbling, white stones each carved with a large fade rune."""
q8_i3 = """The people in the village are not safe with a wild mage teaching backwoods savages the laws of the 
multiverse.  You are not safe until this evil is stopped."""
q8_o1 = "You have killed the wizard's bodyguard!"
q8_o2 = "You begin the walk back to the village."
q8_dung = Location("Wizard's Tower Foyer", "d8", d8_intro, guards, [], q8_i1, q8_i2, q8_i3, q8_o1, q8_o2)

d9_intro = """You know this man...\n
This outcast was from before your time at the academy, but everyone in the empire knows him.  He was ousted for 
inhumane treatment of his students and practicing forbidden magics.  He even killed another professor when he left, 
vowing to return, or worse, he was recorded saying. It seems he had been up to worse, lately.\n
You draw your weapon, hopefully, not for the last time."""
q9_i1 = """Upon the death of the guard, you search the chamber for any clues.  You notice one of the tapestries is 
blowing in the wind, but the room is still.  You pull the rotting curtain aside and reveal a long, slowly winding 
staircase leading upwards.  You begin to climb the rough-hewn stone steps and are surprised by the increasing warmth.  
The staircase opens onto a large sanctuary with broken wooden pews strewn about and large stone urn in the center of 
the chamber.  There is a very tall and very thin man with long white hair standing at the chalice, chanting to 
himself."""
q9_i2 = """He has not noticed you yet.  He wears the faded robes of a professor of arcane science from the academy.  
This is the evil that has pervade this land.  An old teacher..."""
q9_i3 = """'So you killed my apprentice?' he doesn't even look up. 'I thought as much, but I did hope he would kill 
you for your intrusion into my plans.  I need that village.  I'm tired of being in this tower!  I need a real 
stronghold along the trade routes to start my own school of magic!'"""
q9_o1 = "You have killed the wizard!"
q9_o2 = "You begin the walk back to the village."
q9_dung = Location("Wizard's Tower Sanctuary", "d9", d9_intro, wizards, [], q9_i1, q9_i2, q9_i3, q9_o1, q9_o2)

towns = [t0_town, t1_town]
shops = [s0_shop]
inns = [i0_inn]
houses = [h0_house]
halls = [h1_hall]
dungeons = [q0_dung, q1_dung, q2_dung, q3_dung, q4_dung, q5_dung, q6_dung, q7_dung, q8_dung, q9_dung]

camp_intro = "You decide to stop and make camp. It is almost night by the time you are done."
c1_i1 = ""
c1_i2 = ""
c1_i3 = ""
c1_o1 = ""
c1_o2 = ""
camp = Location("Camp", "c1", camp_intro, [], [], c1_i1, c1_i2, c1_i3, c1_o1, c1_o2)
