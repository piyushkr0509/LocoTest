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
- Navigating to a live streaming section.
- Performing video player actions like play, pause, forward, reverse, mute, etc.
- Putting device in flight mode and test video player

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
   
5. **Set up the Android device or emulator:**

    Ensure your device/emulator is connected and recognized by the system: Add your device name in config.capabilities.py { options.device_name = "YOUR DEVICE NAME"  } 
    ```bash
    adb devices
    ```

## Project Structure

```plaintext
.
├── helpers.py                # Helper functions
├── login_page.py             # Page Object Model (POM) for login page interactions
├── test_login.py             # Test cases for login and video player functionalities
├── requirements.txt          # List of dependencies
└── README.md                 # This readme file
```

## Running Tests

Execute the tests using the following command:

```bash
pytest
```

This will automatically discover and run the tests in the `test_login.py` file.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b your-feature-name`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin your-feature-name`.
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Appium](http://appium.io/)
- [pytest](https://pytest.org/)
- [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)

---
