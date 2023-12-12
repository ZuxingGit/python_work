pizzas=['pizza1','pizza2','pizza3']
friend_pizzas=pizzas[:]

pizzas.append('pz1')
friend_pizzas.append("pz_1")
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
    
print("My friend's favorite pizzas are:")
for pz in friend_pizzas:
    print(pz)