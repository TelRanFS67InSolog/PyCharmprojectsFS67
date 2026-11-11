from Hero_Class import Hero

David = Hero('David',100)
Goliaf = Hero('Goliaf',100)

print(David.health())
print(Goliaf.health())
input('Press Enter for next round')


while (David.health_int()) > 0 and (Goliaf.health_int()) > 0:
    print()
    print(David.attack())
    print(Goliaf.attack())
    print(David.damage())
    print(Goliaf.damage())
    print(David.health())
    print(Goliaf.health())
    input('Press Enter for next round')

print('*'*50)
print ('        David:', ['Loser', 'Winner'][bool(David.health_int())])
print ('        Goliaf:', ['Loser', 'Winner'][bool(Goliaf.health_int())])
print('*'*50)