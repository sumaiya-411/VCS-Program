import datetime

# Get the current hour
current_hour = datetime.datetime.now().hour

# Greet based on time
if 5 <= current_hour < 12:
    print("Good Morning! ☀️")
elif 12 <= current_hour < 17:
    print("Good Afternoon! 😊")
elif 17 <= current_hour < 21:
    print("Good Evening! 🌇")
else:
    print("Good Night! 🌙")
