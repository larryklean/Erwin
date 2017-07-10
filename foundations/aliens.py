# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     for name, value in alien.items():
#         print(str(name) + str(value))

aliens = []

for alien_number in range(0, 30):
    new_alien = {'color': 'red', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    alien['color'] = 'yellow'
    alien['points'] = 15
    alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

print('Total aliens %s' % str(len(aliens)))
