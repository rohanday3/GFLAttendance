# GoFourthLearning Attendance Form Filler

## Description

This Python program automates the process of filling out the attendance form for GoFourthLearning using the Selenium WebDriver. It reads login credentials and the form URL from a JSON file and performs the necessary actions to submit attendance.

## Features

- Reads login credentials and form URL from a JSON file.
- Uses Selenium WebDriver to automate the form-filling process.
- Handles the Firefox binary location for Selenium WebDriver.

## Prerequisites

- Python 3.x
- Mozilla Firefox installed (Windows) or Chromium installed (Linux)
- Geckodriver executable (Windows) or Chromedriver executable (Linux)

## Setup

1. **Clone the repository or download the source code.**

2. **Install the required Python packages:**

   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Download and Install Mozilla Firefox (Windows):**

   - Download the latest version of Mozilla Firefox from [https://www.mozilla.org/firefox/](https://www.mozilla.org/firefox/).
   - Follow the installation instructions for your operating system.

4. **Install Chromium (Linux):**

   - Install Chromium using the package manager for your Linux distribution.
   - For example, on Ubuntu, run the following command:

     ```bash
     sudo apt-get install chromium-chromedriver xvfb
     ```

5. **Download Geckodriver (Windows):**

   - Download Geckodriver from [GeckoDriver releases](https://github.com/mozilla/geckodriver/releases).
   - Choose the appropriate version based on your operating system.
   - Extract the downloaded archive.

6. **Place Geckodriver in Firefox Binary Directory (Windows):**

   - Move the `geckodriver` executable to the same directory as your Firefox binary.
   - For example, if Firefox is installed in `C:/Program Files/Mozilla Firefox/`, move `geckodriver.exe` to `C:/Program Files/Mozilla Firefox/`.

7. **Update the JSON file (`login.json`) with your specific information.**

## Usage

Run the program by executing the following command in your terminal or command prompt:

```bash
python msformsfill.py
```

## Cron Job (Linux)

To automate the attendance form-filling process on Linux, you can use a cron job to run the Python script at a specific time.

1. **Make the Python script executable:**

   ```bash
   chmod +x msformsfill.py
   ```

2. **Open the crontab file:**

   ```bash
   crontab -e
   ```

3. **Add a new cron job to run the Python script at a specific time:**

   ```bash
   0 10 * * 1-5 /path/to/msformsfill.py
   ```

   This cron job will run the Python script at 10:00 AM from Monday to Friday.
