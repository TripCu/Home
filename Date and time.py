from datetime import datetime
import re
print("Welcome to Date and Time inc just ask for the date or the time")
current_datetime = datetime.now()
def process_text(text):
    keywords = ["time", "date"]
    pattern = "|".join(keywords)
    match = re.search(pattern, text)
    if match:
        if match.group() == "time":
            print("Current time:", current_datetime.time())
            military_time = datetime.now().time()
            standard_time = military_time.strftime("%I:%M %p")
            print("Standard time:",standard_time)
        elif match.group() == "date":
           print("Current date:", current_datetime.date()) 
           print("Current day:", current_datetime.strftime("%A"))
           print("Current year:", current_datetime.year)
    else:
        print("Sorry, I didn't understand that.")

text = input("Enter some text: ")
process_text(text)
