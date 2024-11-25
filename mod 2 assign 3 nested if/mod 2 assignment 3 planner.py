"""this code had 3 tasks first task recommend where to go based on user input second task recommend upsaling
additional services third task decided who would cater
"""

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

additional_recommendation = "audio system" if attendees > 100 else "projector"
print(f"Recommended: {additional_recommendation}")

vegetarian = input("Do you want vegetarian food? (yes/no): ").strip().lower()
caterer = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print(f"Recommended Caterer: {caterer}")
