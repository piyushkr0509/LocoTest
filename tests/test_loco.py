import pytest
from webdriver_manager.core import driver

from config.capabilities import get_driver
from pages.login_page import LoginPage
from utils import helpers  # Import the Helpers class
from utils.helpers import Helpers


class TestLoco():

	@pytest.fixture(scope="class", autouse=True)
	def setup(self, request):
		# Initialize the driver and assign it to a class variable
		driver = get_driver()
		request.cls.driver = driver

		# Teardown: Quit the driver and stop Appium after tests complete
		def teardown():
			if driver:
				driver.quit()

		request.addfinalizer(teardown)

	def test_MediaPlayerPositive(self):
		# Create an instance of LoginPage
		login_page = LoginPage(self.driver)
		orientation = self.driver.orientation

		# Assert that the volume is zero (i.e., muted)

#        helpers.capture_screenshot_and_extract_text(self.driver, "after_login_attempt", "texts")

		# Perform login using methods from the LoginPage class
		login_page.click_streaming()
		assert login_page.is_live_successful()
		login_page.click_live_content()
		login_page.pausePlay_player()
		assert login_page.isVideo_paused()
		login_page.click_golive()
		login_page.forward_time()
		Helpers.assert_time_difference_by_10_seconds()
		login_page.reverse_time()
		Helpers.assert_time_difference_by_10_seconds()
		login_page.toggle_maxScreen()
		assert orientation == "LANDSCAPE", f"Expected device to be in landscape mode, but it is in {orientation} mode."
		login_page.toggle_maxScreen()
		assert orientation == "PORTRAIT", f"Expected device to be in portrait mode, but it is in {orientation} mode."
		login_page.mute_audio()
		assert Helpers.is_audio_muted(self)
		login_page.mute_audio()
		assert not Helpers.is_audio_muted(self)

	def test_MediaPlayerNegative(self):
			# Create an instance of LoginPage
			login_page = LoginPage(self.driver)



			#        helpers.capture_screenshot_and_extract_text(self.driver, "after_login_attempt", "texts")

			# Perform login using methods from the LoginPage class
			#login_page.click_streaming()
			Helpers.enable_airplane_mode()
			network_status = driver.network_connection
			assert network_status == 1, f"Expected Airplane mode ON, but got {network_status}"
			# assert login_page.is_live_successful()


# Parse the device_info to see if there's any indication of media playing/paused
		# Parse the system_bars information to see if any media control is shown

		# Use the Helpers class to take screenshot and extract text


		# Assert login success by checking if "Trending" appears in the page source
		#assert login_page.is_login_successful()


#To automate testing for a video player, both positive and negative test cases should cover aspects such as basic functionality, UI interactions, error handling, and performance. Here’s a detailed set of test cases:

