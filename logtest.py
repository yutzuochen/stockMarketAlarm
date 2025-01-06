import logging
import os
import sys
from datetime import datetime

def setup_logger():
    # Get today's date for the log file name
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file = f"logs/{current_date}.log"

    # Create a logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Configure the logger
    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,  # Capture only ERROR and higher levels
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger("UnexpectedErrorLogger")

# Set up the logger
logger = setup_logger()

# Define a function to handle unexpected exceptions
def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Ignore keyboard interrupts to allow graceful termination
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

# Override the default excepthook to log uncaught exceptions
sys.excepthook = log_uncaught_exceptions

# Example usage to demonstrate logging
def main():
    logger.info("Program started")
    
    # Simulate some operations
    logger.info("Simulating an operation")
    result = 1 / 0  # This will raise a ZeroDivisionError
    print(result)
    logger.info("Program ended")

if __name__ == "__main__":
    main()

    # Simulate an unhandled exception
    raise RuntimeError("This is an unexpected runtime error!")