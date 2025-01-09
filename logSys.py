import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime
import sys
from playsound import playsound
import threading
import time
import tkinter as tk
from tkinter import font
import random
class Roottk_log():
    def __init__(self, g1, g2):
        self.g1 = g1
        self.g2 = g2
        self.root = tk.Tk()
        self.popup = tk.Toplevel(self.root)
    def move(self):
        self.popup.geometry(f'{str(self.g1)}x{str(self.g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
        self.popup.after(1000, self.move)
    def exit_application(self):
        self.root.destroy()
    def on_close(self):
        print("Closing the window")
        self.root.destroy()
    def popUp(self):
        # global g1, g2
        notification_title = "程式發生錯誤!!!"
        notification_message = f"程式發生錯誤，請將 log 檔案傳給開發工程師!!"
        # logger.info(notification_message)
        print("notification_message: ", notification_message)
        # popup = tk.Toplevel(root)
        self.popup.title(notification_title)
        self.popup.geometry(f'{str(self.g1)}x{str(self.g2)}')
        custom_font = font.Font(family="Helvetica", size=16)

        label = tk.Label(self.popup, text=notification_message, height= 100, padx=40, pady=10, font=custom_font, relief="ridge")
        label.pack()
        self.popup.protocol("WM_DELETE_WINDOW", self.on_close)



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
    # 跳出窗格提醒用戶
    roottk = Roottk_log(3000, 3000)
    roottk.popUp()
    roottk.move()
    roottk.popup.mainloop()
    print("掛了啦啦啦_2")
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