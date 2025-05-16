from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import openpyxl
import re

# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Log in to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Enter credentials
email_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
email_field.send_keys("jastinbrendon@gmail.com")
password_field.send_keys("aslanemil0616//")
password_field.send_keys(Keys.RETURN)
time.sleep(20)

# Base URL for LinkedIn search
base_url = "https://www.linkedin.com/search/results/COMPANIES/?keywords=marketing&origin=SWITCH_SEARCH_VERTICAL&page={page}"

# Dictionary to store unique company data
company_data = {}

# Loop through pages
for page_num in range(1, 101):  # Adjust page range as needed
    url = base_url.format(page=page_num)
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract all <a> tags that point to company pages
    for a in soup.find_all("a", attrs={"data-test-app-aware-link": True}):
        href = a.get("href")
        name = a.get_text(strip=True)

        # Validate it's a clean company page URL and name is non-empty
        if (
            href and name and
            href.startswith("https://www.linkedin.com/company/") and
            re.match(r"^https://www\.linkedin\.com/company/[^/]+/?$", href)
        ):
            if href not in company_data:
                company_data[href] = {
                    "name": name
                }

# Create Excel workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Company Data"

# Headers
ws.append(["Company Name", "Company URL"])

# Write data
for url, data in company_data.items():
    ws.append([data["name"], url])

# Save file
wb.save("company_data.xlsx")

# Close browser
driver.quit()

print("✅ Unique company names and URLs saved to company_data.xlsx")
