import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime
import sys
from playsound import playsound
import threading
import time

def setup_logger():
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{current_date}.log"

    # Create a logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Full path for the log file
    log_file_path = os.path.join("logs", log_file)

    # Create a logger
    logger = logging.getLogger("DailyLogger")
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Configure the logger
    logging.basicConfig(
        filename=log_file_path,
        level=logging.DEBUG,  # Set the logging level
        format="%(asctime)s - %(levelname)s - %(message)s",  # Include timestamp in log entries
        datefmt="%Y-%m-%d %H:%M:%S"  # Timestamp format
    )

    return logger

# Define a function to handle unexpected exceptions
def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Ignore keyboard interrupts to allow graceful termination
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    Logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

    plan_A_thread = threading.Thread(target = alertProcessErr)
    # 語音提醒
    plan_A_thread.start()
    print("掛了啦啦啦_1")
    time.sleep(2)
    # Override the default excepthook to log uncaught exceptions

def alertProcessErr():
    playsound("sound/processError.mp3")

Logger = setup_logger()
sys.excepthook = log_uncaught_exceptions

def main():
    # Set up the logger
    logger = setup_logger()

    # Example usage of the logger
    logger.debug("Debugging information")
    logger.info("This is an informational message")
    logger.warning("Warning: Something might be wrong!")
    logger.error("Error: Something went wrong!")
    logger.critical("Critical: Serious problem occurred!")

if __name__ == "__main__":
    main()