import subprocess
import time
import os
import signal

class AppiumServer:
    def __init__(self):
        self.process = None

    def start(self):
        # Start the Appium server programmatically
        print("Starting Appium server...")
        self.process = subprocess.Popen(["appium"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)  # Allow some time for the server to start

    def stop(self):
        # Stop the Appium server programmatically
        if self.process:
            print("Stopping Appium server...")
            os.kill(self.process.pid, signal.SIGTERM)
            self.process = None