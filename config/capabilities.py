import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import WebDriverException

from utils import appium_server
from utils.appium_server import AppiumServer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

appium_server = AppiumServer()  # Initialize Appium server


def get_driver():
    # Start the Appium server
    try:
        logger.info("Starting Appium server...")
        appium_server.start()
        if not appium_server:
            logger.error("Failed to start Appium server.")
            logger.info("Appium server started successfully.")

    # Create UiAutomator2Options and set all the required capabilities
        logger.info("Setting up device capabilities...")
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "MediumPhone13"  # Replace with actual device name
        options.app_package = "com.showtimeapp"
        options.app_activity = "com.pocketaces.ivory.view.activities.SplashActivity"
        options.automation_name = "UiAutomator2"
        options.no_reset = True  # To keep the app in the same state after the session
        options.new_command_timeout = 300

        # Return the Appium driver with only `options`
        logger.info("Starting WebDriver session...")
        return webdriver.Remote('http://localhost:4723', options=options)
    except WebDriverException as e:
        logger.error(f"Failed to start WebDriver session: {e}")

def stop_appium():
#Stop the Appium server after tests
     appium_server.stop()