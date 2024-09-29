from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class DragAndDropAutomation:
    def __init__(self):
        # Setup Chrome WebDriver options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)  # Wait for 10 seconds
        self.action = ActionChains(self.driver)  # ActionChains for performing drag-and-drop

    def open_url(self, url):
        """Open the provided URL."""
        self.driver.get(url)

    def perform_drag_and_drop(self):
        """Perform the drag-and-drop action from white box to yellow box."""
        # Switch to iframe where the drag-and-drop elements are located
        iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
        self.driver.switch_to.frame(iframe)

        # Locate the source (white box) and target (yellow box)
        source = self.wait.until(EC.presence_of_element_located((By.ID, "draggable")))
        target = self.wait.until(EC.presence_of_element_located((By.ID, "droppable")))

        # Perform drag-and-drop
        self.action.drag_and_drop(source, target).perform()

    def quit(self):
        """Close the browser."""
        self.driver.quit()

if __name__ == "__main__":
    automation = DragAndDropAutomation()
    try:
        # Step 1: Open the URL
        automation.open_url("https://jqueryui.com/droppable/")
        
        # Step 2: Perform drag-and-drop operation
        automation.perform_drag_and_drop()
        
    finally:
        # Step 3: Close the browser
        automation.quit()
