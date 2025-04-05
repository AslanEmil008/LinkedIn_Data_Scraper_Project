from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import openpyxl

# Set up the driver (make sure to have ChromeDriver installed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Log in to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Enter login credentials (replace 'your_email' and 'your_password' with actual credentials)
email_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

email_field.send_keys("anderstomm6@gmail.com")
password_field.send_keys("aslanemil0616//")
password_field.send_keys(Keys.RETURN)
time.sleep(3)

# Base URL for LinkedIn search results
base_url = "https://www.linkedin.com/search/results/COMPANIES/?keywords=marketing&origin=SWITCH_SEARCH_VERTICAL&page={page}&sid=tHO"

company_data = []

# Loop through pages 1 to 10
for page_num in range(1, 11):
    # Construct the URL for the current page
    url = base_url.format(page=page_num)
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    # Parse the page source using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all divs with class 'mb1' that contain company information
    companies = soup.find_all("div", class_="mb1")

    # Extract the company name, URL, and location
    for company in companies:
        company_name_tag = company.find("a", class_="dgePcUVTyZcmWIuOySyndWdGoBMukAZsio")
        location_tag = company.find("div", class_="mTjnOwtMxHPffEIRcJLDWXTPzwQcTgTqrfveo t-14 t-black t-normal")
        
        if company_name_tag and location_tag:
            company_name = company_name_tag.get_text(strip=True)
            company_url = company_name_tag["href"]
            location = location_tag.get_text(strip=True)

            # Split the location into company type and city
            location_parts = location.split('•')
            company_type = location_parts[0].strip() if len(location_parts) > 1 else ""
            city = location_parts[-1].strip() if len(location_parts) > 1 else location.strip()

            # Create the People URL by appending '/people/' to the company URL
          #  people_url = company_url + "/people/"

            company_data.append({
                "name": company_name,
                "url": company_url,
                "company_type": company_type,
                "city": city,
                #"people_url": people_url  # Add people URL
            })

# Create a new workbook and select the active sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Company Data"

# Define column headers
headers = ["Company Name", "Company URL", "Company Type", "City"] #"People URL"]
ws.append(headers)

# Write the data to the Excel sheet
for data in company_data:
    ws.append([data["name"], data["url"], data["company_type"], data["city"]]) #data["people_url"]])

# Save the workbook to an XLSX file
wb.save("company_data.xlsx")

# Close the browser after scraping
driver.quit()

print("Data has been saved to company_data.xlsx")
