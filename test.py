import pickle
from selenium import webdriver

# Path to ChromeDriver


driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin")

# Wait for manual login
input("Log in manually and press Enter here to save cookies...")

# Save cookies to a file
with open("cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)

driver.quit()