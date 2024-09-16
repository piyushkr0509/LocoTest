import pytest
from config.capabilities import get_driver
from pages.login_page import LoginPage
from utils.helpers import Helpers


class TestLoco:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        """
        Setup method to initialize the driver before the tests and quit it after.
        """
        driver = get_driver()  # Get the driver from capabilities
        request.cls.driver = driver

        def teardown():
            """
            Teardown method to quit the driver after the tests are complete.
            """
            if driver:
                driver.quit()

        request.addfinalizer(teardown)

    def test_MediaPlayerPositive(self):
        """
        Test to verify positive cases for the media player functionality.
        """
        # Initialize LoginPage object
        login_page = LoginPage(self.driver)

        # Save the initial orientation of the device
        initial_orientation = self.driver.orientation

        # Navigate through the media player functionalities
        login_page.click_streaming()
        assert login_page.is_live_successful(), "Live streaming failed to start."

        login_page.click_live_content()

        # Pause and verify the video is paused
        login_page.pausePlay_player()
        assert login_page.isVideo_paused(), "Video is not paused."

        # Resume playback and verify it resumes
        login_page.click_golive()

        # Verify forwarding the video by 10 seconds
        login_page.forward_time()
        Helpers.assert_time_difference_by_10_seconds(self.driver, "forward")

        # Verify reversing the video by 10 seconds
        login_page.reverse_time()
        Helpers.assert_time_difference_by_10_seconds(self.driver, "reverse")

        # Toggle fullscreen mode and verify the orientation is landscape
        login_page.toggle_maxScreen()
        assert self.driver.orientation == "LANDSCAPE", f"Expected landscape mode, but got {self.driver.orientation}."

        # Toggle back to portrait mode and verify
        login_page.toggle_maxScreen()
        assert self.driver.orientation == "PORTRAIT", f"Expected portrait mode, but got {self.driver.orientation}."

        # Mute the audio and verify it is muted
        login_page.mute_audio()
        assert Helpers.is_audio_muted(self.driver), "Audio is not muted."

        # Unmute the audio and verify it is unmuted
        login_page.mute_audio()
        assert not Helpers.is_audio_muted(self.driver), "Audio is still muted."

    def test_MediaPlayerNegative(self):
        """
        Test to verify negative cases, such as network issues, for the media player.
        """
        # Initialize LoginPage object
        login_page = LoginPage(self.driver)

        # Enable airplane mode to simulate network disconnection
        Helpers.enable_airplane_mode(self.driver,1)

        # Get the current network connection status
        network_status = self.driver.network_connection

        # Assert that airplane mode is enabled (network connection should be 1)
        assert network_status == 1, f"Expected Airplane mode ON, but got {network_status}."

        # Try to interact with the video player and verify that actions fail due to network issues
        with pytest.raises(Exception, match="No network connection"):
            login_page.click_live_content()