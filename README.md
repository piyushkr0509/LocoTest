# Automated Login and Video Player Testing

This project uses Python and Appium to automate and validate login functionality and video player controls in a mobile application.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The project provides automated tests to ensure the robustness of the login feature and video player functionalities within the application. These tests include:
- Logging into the application.
- Navigating to a live streaming section.
- Performing video player actions like play, pause, forward, reverse, mute, etc.

## Prerequisites

To work with this project, you need the following installed on your local machine:

- Python 3.9.6
- pip (Python package installer)
- Appium server
- Java (for running Appium)
- Android SDK (if testing on Android)
- pytest

## Installation and Setup

Follow these steps to set up the project:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Appium server:**

    Follow the Appium documentation to install and start the Appium server.
    ```bash
    appium
    ```
