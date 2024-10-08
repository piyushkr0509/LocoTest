from multiprocessing.spawn import import_main_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.mobileby import MobileBy
from utils import helpers

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators on Media Player
    watch_Streams =(By.ID, "com.showtimeapp:id/watchStreamIntent")
    start_streaming=(By.ID, "com.showtimeapp:id/startStreamingIntent")
    rewards_giveaways=(By.ID, "com.showtimeapp:id/rewardsIntent")
    continue_login=(By.ID, "com.showtimeapp:id/continueBtn")
    google_login=(By.ID, "com.showtimeapp:id/googleLoginButton")
    login_button = (By.ID, "com.loco.play:id/login_button")
    streaming=(By.XPATH, "//android.widget.ImageView[@resource-id='com.showtimeapp:id/thumbnail'][1]")
    live_content=(By.XPATH, "//android.widget.FrameLayout[@resource-id='com.showtimeapp:id/exo_subtitles']/android.view.View")
    player_view=(By.XPATH, "//*[@content-desc='Show player controls']")
    play_pause_button = (MobileBy.ACCESSIBILITY_ID, "Pause")
    ad_overlay=(By.ID, "com.loco.play:id/exo_ad_overlay")
    go_live= (By.ID, "com.showtimeapp:id/goLiveIndicator")
    forward_seconds= (By.ID, "com.showtimeapp:id/exo_ffwd")
    reverse_seconds= (By.ID, "com.showtimeapp:id/exo_rew")
    time_duration= (By.ID, "com.showtimeapp:id/exo_position")
    mute_button= (By.ID, "com.showtimeapp:id/mutePlayer")
    toggle_max= (By.ID, "com.showtimeapp:id/minMaxToggle")
    pip_button= (By.ID, "com.showtimeapp:id/playerPIPButton")
    live_count= (By.ID, "com.showtimeapp:id/playerLiveCount")
    video_setting= (By.ID, "com.showtimeapp:id/videoSettings")
    progress_bar=(By.ID, "com.showtimeapp:id/exo_progress")

    # Methods to interact with elements
    def click_watchStreams(self):
        self.driver.find_element(*self.watch_Streams).click()
    def click_startStreaming(self):
        self.driver.find_element(*self.start_streaming).click()
    def click_rewardsGiveaways(self):
        self.driver.find_element(*self.rewards_giveaways).click()
    def click_continueLogin(self):
        self.driver.find_element(*self.continue_login).click()

    def click_streaming(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.streaming)).click()

    def is_live_successful(self):
        time.sleep(15)
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.player_view)).is_displayed()

    def click_live_content(self):
        time.sleep(15)
        self.driver.find_element(*self.player_view).click()

    def pausePlay_player(self):
        self.driver.find_element(*self.play_pause_button).click()

    def isVideo_paused(self):
        # 'play_button' is the locator for the play button
        play_button_locator = (By.XPATH, "//*[@content-desc='Show player controls']")

        # First, click to pause
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.player_view)).click()

        # Then, wait for the play button to become visible (this indicates the video is paused)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(play_button_locator))

        assert self.driver.find_element(
            *play_button_locator).is_displayed(), "Play button not displayed, video might not be paused."


    def click_golive(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.player_view)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.go_live)).click()
        time.sleep(15)

    def forward_time(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.player_view)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.forward_seconds)).click()

    def reverse_time(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.player_view)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.reverse_seconds)).click()

    def toggle_maxScreen(self):
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.player_view)).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.toggle_max)).click()

    def mute_audio(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.mute_button)).click()

    def spam_forward_time(self, num_taps):
        """
        Repeatedly taps the forward button to simulate excessive tapping for negative testing.

        :param num_taps: The number of times to tap the forward button (default: 10)
        """
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.player_view)).click()

        for _ in range(num_taps):
            try:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.forward_seconds)).click()
                print(f"Tapped forward {_ + 1} times")
            except Exception as e:
                print(f"Error occurred on tap {_ + 1}: {str(e)}")
                break