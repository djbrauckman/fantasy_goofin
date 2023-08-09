import random

league_members = ['Danny','Aaron','Hahne','Geiss','Colin','Tom','Shelby','Matthew','Josh','Robert']
random.shuffle(league_members)
division_a = league_members[:5]
division_b = league_members[5:] 
print(division_a)
print(division_b)


