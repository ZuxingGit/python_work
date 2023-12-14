favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
people = {"Adam", "Eva", "Simon", "Joe", "jen", "sarah"}

for voter in favorite_languages.keys():
    if voter in people:
        print(f"{voter.title()}, thank you for your responding.")
    else:
        print(f"Please take a poll, {voter.title()}")
