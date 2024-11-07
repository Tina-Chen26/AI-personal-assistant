# AI-personal-assistant

## Overview
This AI Personal Assistant is a Python-based application designed to provide basic functionality to assist users in their daily activities. It can schedule reminders and provide weather updates for any city. This script utilizes several libraries, including `nltk`, `requests`, and `schedule`.

### Features:
1. **Set a Reminder**: Users can add a reminder for a specific task at a given time each day.
2. **Get Weather Update**: Users can get the current weather update for any city using OpenWeatherMap API.
3. **Interactive Menu**: The application has an interactive command-line interface where users can select desired options.

## Prerequisites
To run this project, you need to have Python 3 installed on your system. The following libraries are required for the assistant to work:

- `nltk`
- `requests`
- `schedule`

You can install these libraries using the following command:

```sh
pip install nltk requests schedule
```

Make sure to also set the `OpenSSL` context correctly for `nltk` downloads to avoid SSL issues.

## Setup
1. **Clone or Download the Repository**:
   Clone this project repository or download the source files.

2. **Install Dependencies**:
   After cloning, install the required dependencies by running:
   
   ```sh
   pip install nltk requests schedule
   ```

3. **Obtain an API Key for Weather**:
   The assistant uses OpenWeatherMap for weather updates. You need to register at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get an API key. Once you have the key, replace the `api_key` variable in the script:
   
   ```python
   api_key = "YOUR_API_KEY_HERE"
   ```

4. **Running the Script**:
   You can run the script with the following command:
   
   ```sh
   python ai_personal_assistant.py
   ```

## Usage
After running the script, an interactive menu will appear with the following options:

1. **Set a Reminder**:
   - Enter the task name and the time in `HH:MM` format when prompted. The reminder will repeat every day.

2. **Get Weather Update**:
   - Enter the name of the city for which you want to get a weather update. The temperature and weather description will be provided in response.

3. **Exit**:
   - Exits the application.

## Important Notes
- **Threading**: The reminder system is implemented using Python's `threading` module to run the reminders concurrently in the background.
- **Weather API**: Make sure to replace the placeholder API key in the script with your valid API key to avoid API errors.
- **SSL Fix**: There is a section to disable SSL verification for `nltk` downloads to avoid SSL errors. If not required, you can comment it out.

```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

## Dependencies
- `nltk`: Used for natural language processing tasks. Here, it's used to download the "punkt" tokenizer.
- `requests`: For making HTTP requests to get weather data from OpenWeatherMap.
- `schedule`: A lightweight job scheduling library for Python.
- `threading`: Handles background tasks to ensure reminders run without blocking the main program.

## License
This project is licensed under the MIT License.

## Contact
For issues or suggestions, feel free to contact me through the GitHub repository's issue tracker or email.

## Contributions
Contributions are welcome! Feel free to fork the repository, make modifications, and create pull requests.

---

Enjoy using your AI Personal Assistant!
