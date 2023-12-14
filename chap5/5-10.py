current_users = ["Simon", "Jack", "admin", "Amy", "Mike"]
new_users = ["Simon", "Jack", "adam", "eva", "Marco"]

for new_user in new_users:
    if new_user.lower() in current_users or new_user.title() in current_users:
        print(f"{new_user}--need a new username.")
    else:
        print(f"{new_user} is available.")
