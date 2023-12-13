# usernames = []
usernames = ["Simon", "Jack", "admin", "Amy", "Mike"]

if usernames:
    for name in usernames:
        if name.lower() == "admin":
            print(f"Hello {name}, would u like to see a status report?")
        else:
            print(f"Hello, {name.title()}, thank u for logging in again.")
else:
    print("We need to find some users!")
