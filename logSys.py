import logging
from logging.handlers import TimedRotatingFileHandler
import os


def setup_logger():
    # Create a logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Create a logger
    logger = logging.getLogger("DailyLogger")
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create a TimedRotatingFileHandler to rotate logs daily
    handler = TimedRotatingFileHandler(
        filename="logs/daily.log",  # Base filename for logs
        when="midnight",           # Rotate logs at midnight
        interval=1,                # Rotate every day
        backupCount=7              # Keep logs for the last 7 days
    )

    # Define the log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

Logger = setup_logger()
# def main():
#     # Set up the logger
#     logger = setup_logger()

#     # Example usage of the logger
#     logger.debug("=========Debugging information")
#     logger.info("=========This is an informational message")
#     logger.warning("=========Warning: Something might be wrong!")
#     logger.error("Error: Something went wrong!")
#     logger.critical("Critical: Serious problem occurred!")

# if __name__ == "__main__":
#     main()