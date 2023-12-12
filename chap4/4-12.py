my_foods=['pizza','falafel','carrot cake']
# friend_foods=my_foods
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for f in my_foods:
    print(f)

print("\nMY friend's favorite foods are:")
for f in friend_foods:
    print(f)