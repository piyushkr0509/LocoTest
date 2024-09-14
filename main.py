import pytest
from config.capabilities import start_appium, stop_appium

def run_tests():
    # Start the Appium server
    start_appium()

    try:
        # Run the pytest test suite
        pytest.main(["-v", "--html=reports/report.html", "--self-contained-html"])
    finally:
        # Stop the Appium server after tests are done
        stop_appium()

if __name__ == "__main__":
    run_tests()
