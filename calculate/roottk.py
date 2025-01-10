import tkinter as tk
from tkinter import font
import random


class Roottk():
    def __init__(self, g1, g2):
        self.g1 = g1
        self.g2 = g2
        self.root = tk.Tk()
        self.popup = tk.Toplevel(self.root)
    def move(self):
        self.popup.geometry(f'{str(self.g1)}x{str(self.g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
        # 決定窗格幾秒動次
        self.popup.after(3000, self.move)
    def exit_application(self):
        self.root.destroy()
    def on_close(self):
        print("Closing the window")
        self.root.destroy()
    def popUp(self, price, targetPrice, stockName, techIndex):
        # global g1, g2
        notification_title = f"{stockName} 目標 {techIndex} 已到達"
        notification_message = f"{stockName} {techIndex} is {price}.\n {techIndex} > {targetPrice}!"
        # logger.info(notification_message)
        print("notification_message: ", notification_message)
        # popup = tk.Toplevel(root)
        self.popup.title(notification_title)
        self.popup.geometry(f'{str(self.g1)}x{str(self.g2)}')
        custom_font = font.Font(family="Helvetica", size=16)

        label = tk.Label(self.popup, text=notification_message, height= 100, padx=40, pady=10, font=custom_font, relief="ridge")
        label.pack()
        self.popup.protocol("WM_DELETE_WINDOW", self.on_close)




class Roottk_report():
    def __init__(self, g1, g2):
        self.g1 = g1
        self.g2 = g2
        self.root = tk.Tk()
        self.popup = tk.Toplevel(self.root)
    def move(self):
        self.popup.geometry(f'{str(self.g1)}x{str(self.g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
        # 決定窗格幾秒動次
        self.popup.after(3000, self.move)
    def exit_application(self):
        self.root.destroy()
    def on_close(self):
        print("Closing the window")
        self.root.destroy()
    def popUp(self, s):
        # global g1, g2
        notification_title = f"結算報告"
        notification_message = s
        # logger.info(notification_message)
        print("notification_message: ", notification_message)
        # popup = tk.Toplevel(root)
        self.popup.title(notification_title)
        self.popup.geometry(f'{str(self.g1)}x{str(self.g2)}')
        custom_font = font.Font(family="Helvetica", size=16)

        label = tk.Label(self.popup, text=notification_message, height= 100, padx=40, pady=10, font=custom_font, relief="ridge")
        label.pack()
        self.popup.protocol("WM_DELETE_WINDOW", self.on_close)