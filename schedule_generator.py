#Notes:
# file.open/write/close writes to the file name in the same directory this .py file is.
# The file doesn't need to be created first before running

# Determine division/order. Input year as first parameter, all division A members first, then all division b members second
# Running the schedule_generator will create a text file with weekly matchups

#10 teams, 2x division, 1x opposite division
def schedule_generator(year, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5):

    file = open(f'{year}_generated_schedule.txt', "w")
    file.write(f'Week 1' + '\n'
          + f'{a1} @ {b2}' + '\n'
          + f'{a2} @ {a3}' + '\n'
          + f'{a4} @ {a5}' + '\n'
          + f'{b1} @ {b5}' + '\n'
          + f'{b3} @ {b4}' + '\n\n'
          + f'Week 2' + '\n'
          + f'{a1} @ {a4}' + '\n'
          + f'{a2} @ {b3}' + '\n'
          + f'{a3} @ {a5}' + '\n'
          + f'{b1} @ {b4}' + '\n'
          + f'{b2} @ {b5}' + '\n\n'
          + f'Week 3' + '\n'
          + f'{a1} @ {a5}' + '\n'
          + f'{a2} @ {a4}' + '\n'
          + f'{a3} @ {b4}' + '\n'
          + f'{b1} @ {b2}' + '\n'
          + f'{b3} @ {b5}' + '\n\n'
          + f'Week 4' + '\n'
          + f'{a1} @ {a3}' + '\n'
          + f'{a2} @ {a5}' + '\n'
          + f'{a4} @ {b5}' + '\n'
          + f'{b1} @ {b3}' + '\n'
          + f'{b2} @ {b4}' + '\n\n'
          + f'Week 5' + '\n'
          + f'{a1} @ {a2}' + '\n'
          + f'{a3} @ {a4}' + '\n'
          + f'{a5} @ {b1}' + '\n'
          + f'{b2} @ {b3}' + '\n'
          + f'{b4} @ {b5}' + '\n\n'
          + f'Week 6' + '\n'
          + f'{a1} @ {b3}' + '\n'
          + f'{a2} @ {b4}' + '\n'
          + f'{a3} @ {b5}' + '\n'
          + f'{a4} @ {b1}' + '\n'
          + f'{a5} @ {b2}' + '\n\n'
          + f'Week 7' + '\n'
          + f'{a1} @ {b1}' + '\n'
          + f'{a2} @ {b2}' + '\n'
          + f'{a3} @ {b3}' + '\n'
          + f'{a4} @ {b4}' + '\n'
          + f'{a5} @ {b5}' + '\n\n'
          + f'Week 8' + '\n'
          + f'{a1} @ {b4}' + '\n'
          + f'{a2} @ {b5}' + '\n'
          + f'{a3} @ {b1}' + '\n'
          + f'{a4} @ {b2}' + '\n'
          + f'{a5} @ {b3}' + '\n\n'
          + f'Week 9' + '\n'
          + f'{a1} @ {a5}' + '\n'
          + f'{a2} @ {b1}' + '\n'
          + f'{a3} @ {a4}' + '\n'
          + f'{b2} @ {b3}' + '\n'
          + f'{b4} @ {b5}' + '\n\n'
          + f'Week 10' + '\n'
          + f'{a1} @ {a4}' + '\n'
          + f'{a2} @ {a5}' + '\n'
          + f'{a3} @ {b2}' + '\n'
          + f'{b1} @ {b4}' + '\n'
          + f'{b3} @ {b5}' + '\n\n'
          + f'Week 11' + '\n'
          + f'{a1} @ {a2}' + '\n'
          + f'{a3} @ {a5}' + '\n'
          + f'{a4} @ {b3}' + '\n'
          + f'{b1} @ {b5}' + '\n'
          + f'{b2} @ {b4}' + '\n\n'
          + f'Week 12' + '\n'
          + f'{a1} @ {a3}' + '\n'
          + f'{a2} @ {a4}' + '\n'
          + f'{a5} @ {b4}' + '\n'
          + f'{b1} @ {b3}' + '\n'
          + f'{b2} @ {b5}' + '\n\n'
          + f'Week 13' + '\n'
          + f'{a1} @ {b5}' + '\n'
          + f'{a2} @ {a3}' + '\n'
          + f'{a4} @ {a5}' + '\n'
          + f'{b1} @ {b2}' + '\n'
          + f'{b3} @ {b4}' + '\n\n')
    file.close()

schedule_generator(2022, 'dan','geiss','hahne','tom','aaron','rob','shelby','colin','josh','matthew')
