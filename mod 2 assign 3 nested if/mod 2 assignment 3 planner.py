# task 2 enhance the code to recommend additional things like "audio system" or "projector"

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

additional_recommendation = "audio system" if attendees > 100 else "projector"
print(f"Recommended: {additional_recommendation}")
