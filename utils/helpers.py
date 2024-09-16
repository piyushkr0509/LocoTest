import os
import time
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.core import driver


class Helpers:

    @staticmethod
    def ensure_directory_exists(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def take_screenshot(driver, name):
        Helpers.ensure_directory_exists('screenshots')
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = f"screenshots/{name}_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        return screenshot_path

    @staticmethod
    def extract_text(driver):
        elements = driver.find_elements_by_xpath("//*")
        return [el.text for el in elements if el.text]

    @staticmethod
    def save_extracted_texts(texts, file_name="texts"):
        Helpers.ensure_directory_exists('screenshots')
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        text_file_path = f"screenshots/{file_name}_{timestamp}.txt"
        with open(text_file_path, "w") as text_file:
            for line in texts:
                text_file.write(line + "\n")
        return text_file_path

    @staticmethod
    def capture_screenshot_and_extract_text(driver, screenshot_name, text_file_name):
        # Take screenshot
        screenshot_path = Helpers.take_screenshot(driver, screenshot_name)
        print(f"Screenshot saved at: {screenshot_path}")

        # Extract texts from the page
        extracted_texts = Helpers.extract_text(driver)

        # Save extracted texts
        text_file_path = Helpers.save_extracted_texts(extracted_texts, text_file_name)
        print(f"Extracted texts saved at: {text_file_path}")

        return screenshot_path, text_file_path

    def get_time_in_seconds(time_text):
        """Convert time in format mm:ss or hh:mm:ss to seconds."""
        parts = time_text.split(":")
        parts = [int(p) for p in parts]
        if len(parts) == 2:  # mm:ss
            return parts[0] * 60 + parts[1]
        elif len(parts) == 3:  # hh:mm:ss
            return parts[0] * 3600 + parts[1] * 60 + parts[2]

    def enable_airplane_mode(self,driver,condition):
        # Toggle the airplane mode ON
        driver.set_network_connection(condition)  # 1 stands for Airplane mode (all off)

        # Verify if Airplane mode is enabled (Optional)

    def assert_time_difference_by_10_seconds(driver, forward_button_locator):
        # Get the initial time
        initial_time_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(By.ID, "com.showtimeapp:id/exo_position")
        )
        initial_time_text = initial_time_element.text
        initial_time_seconds = driver.get_time_in_seconds(initial_time_text)
        print(initial_time_seconds)

        # Click the 10-second forward button
        forward_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(forward_button_locator)
        )
        forward_button.click()

        # Wait for the time to update and get the updated time
        updated_time_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(By.ID, "com.showtimeapp:id/exo_position", initial_time_text)
        )
        updated_time_text = updated_time_element.text
        updated_time_seconds = driver.get_time_in_seconds(updated_time_text)
        print(updated_time_seconds)

        # Assert that the time has increased by approximately 10 seconds
        assert updated_time_seconds - initial_time_seconds >= 10, f"Expected time increase of 10 seconds, but got {updated_time_seconds - initial_time_seconds} seconds."

    import subprocess

    def is_audio_muted():
        # Run an adb command to get the current volume state of the device
        result = subprocess.run(['adb', 'shell', 'media', 'volume', '--get'], capture_output=True, text=True)
        print(result.stdout)
        # Check if the output indicates the device is muted (depends on device)
        return 'mute' in result.stdout.lower()

    # Example usage
    if is_audio_muted():
        print("The audio is muted")
    else:
        print("The audio is not muted")
