from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils import appium_server
from utils.appium_server import AppiumServer


appium_server = AppiumServer()  # Initialize Appium server


def get_driver():
    # Start the Appium server
    appium_server.start()

    # Create UiAutomator2Options and set all the required capabilities
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "MediumPhone13"  # Replace with actual device name
    options.app_package = "com.showtimeapp"
    options.app_activity = "com.pocketaces.ivory.view.activities.SplashActivity"
    options.automation_name = "UiAutomator2"
    options.no_reset = True  # To keep the app in the same state after the session
    options.new_command_timeout = 300
    # Return the Appium driver with only `options`
    return webdriver.Remote('http://localhost:4723', options=options)

def stop_appium():
#Stop the Appium server after tests
    appium_server.stop()
