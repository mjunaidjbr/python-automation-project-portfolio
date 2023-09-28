from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import pyautogui
import pyperclip
from bs4 import BeautifulSoup
def getTextFromImage(image_path):\
    # driver_path = r".\chromedriver.exe"  # Update with your actual path
    # Configure Chrome to run in headless mode
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_experimental_option("detach", True)  # Keep the browser open after script execution
    # Set the logging level to suppress debug logs
    chrome_options.add_argument('--log-level=3')  # 3 corresponds to WARNING level
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--disable-extensions')
    # Create a Chrome WebDriver instance with headless mode
    driver = webdriver.Chrome(options=chrome_options)


    # Open the website
    url = "https://imagestotext.io/"
    driver.get(url)
    # time.sleep(10)


    try:
        # Wait for the "browse0" button to become available
        button1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/main/article/div/div/div[1]/div/div/div[3]/div/button[2]")))
        # Once the button is available, click it
        button1.click()
        # Optionally, you can perform other actions or interact with the website here
    except:
        driver.quit()
        return None


    # Close the browser when done
    # driver.quit()
    # Simulate pressing "Ctrl + V" using PyAutoGUI
    pyperclip.copy(str(image_path))
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    #press enter


    pyautogui.press('enter')

    #hit the get text button

    try:
        # Wait for the "browse0" button to become available
        button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/main/article/div/div/div[1]/div/div/div[4]/div[1]/button")))
        # Once the button is available, click it
        button2.click()
        # Optionally, you can perform other actions or interact with the website here
    except:
        driver.quit()
        return None

    # time.sleep(5)


    try:
        # Wait for the "browse0" button to become available
        getData = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "copytext")))
        # getData = driver.find_element(By.CLASS_NAME, "copytext")
        # Once the button is available, click it
        getData.click()
        # Optionally, you can perform other actions or interact with the website here
    except:
        driver.quit()
        return None
        
    
    if driver:
        driver.quit()

    return pyperclip.paste()


# # Specify the path to your Chrome WebDriver executable

# image_path = r"C:\Users\rao\Desktop\Freelance\python_scripts\python Automation scripts\project_script_29\pdf_data_extraction\cropped_images\piece_1.png"
# data = getTextFromImage(image_path=image_path)

# print(data)