import nltk
import requests
import schedule
import time
from datetime import datetime

# To use this code, make sure to install necessary libraries first.
# pip install nltk requests schedule

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download("punkt")


# Function to get the weather update for a given city
def get_weather(city_name):
    api_key = (
        "2746c82514c69e2d92fb707fd26c8964"  # Replace with your OpenWeatherMap API key
    )
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather_description = data["weather"][0]["description"]
        temperature = main["temp"]  # Temperature in Celsius

        print(f"Current Temperature in {city_name}: {temperature:.2f} °C")
        print(f"Weather Description: {weather_description.capitalize()}")
    else:
        print(
            f"City Not Found or API error. Please check the city name or your API key. Response: {response.text}"
        )


# Function to schedule reminders
def add_reminder(task, time_str):
    def reminder():
        print(f"Reminder: {task} at {time_str}")

    schedule_time = datetime.strptime(time_str, "%H:%M").time()
    schedule.every().day.at(schedule_time.strftime("%H:%M")).do(reminder)
    print(f"Reminder set for task '{task}' at {time_str}")


# Example of scheduling tasks
import threading


def schedule_task():
    print("Scheduling your tasks...")

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.daemon = True
    schedule_thread.start()


# Main function to demonstrate scheduling, reminders, and weather updates
def main():
    while True:
        print("\nAI Personal Assistant")
        print("1. Set a Reminder")
        print("2. Get Weather Update")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task you want to be reminded about: ")
            time_str = input("Enter the time for reminder (HH:MM format): ")
            add_reminder(task, time_str)

        elif choice == "2":
            city_name = input("Enter city name (e.g., 'Moscow'): ").strip()
            get_weather(city_name)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

        # Start the schedule task process in a non-blocking way
        try:
            schedule_task()
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
