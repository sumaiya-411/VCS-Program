import datetime

def get_greeting(hour):
    """Returns a greeting based on the hour of the day."""
    if 5 <= hour < 12:
        return "Good Morning! ☀️"
    elif 12 <= hour < 17:
        return "Good Afternoon! 😊"
    elif 17 <= hour < 21:
        return "Good Evening! 🌇"
    else:
        return "Good Night! 🌙"

def main():
    now = datetime.datetime.now()
    current_hour = now.hour
    current_time = now.strftime("%I:%M %p")

    print(f"Current time: {current_time}")
    print(get_greeting(current_hour))

if __name__ == "__main__":
    main()
