import requests
import time
import openpyxl
import re
from openpyxl import Workbook

# Google API Key & Custom Search Engine ID
API_KEY = "AIzaSyAgGV4pzTPcdrbx5Ne5bb0GW-XYS1B3jok"
CX = "25409c5e0557e48ef"


# Function to use Google Custom Search API with pagination
def google_search(query, api_key, cx, start_index=1):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}&start={start_index}"
    response = requests.get(url)
    return response.json()

# Function to process the results from the API
def process_results(data, company_name):
    results = []
    for item in data.get("items", []):
        title = item.get("title", "")
        link = item.get("link", "")

        if "LinkedIn" not in title:
            continue

        # Remove anything after '|'
        title_clean = title.split("|")[0].strip()

        # Skip titles that are just 'LinkedIn', 'Airbnb', etc.
        if title_clean.lower() in ["linkedin", "airbnb", "gerente"]:
            continue

        # Remove company name (case-insensitive)
        title_clean = re.sub(re.escape(company_name), "", title_clean, flags=re.IGNORECASE).strip(" -")

        # Split into name and title
        if " - " in title_clean:
            name, title_part = title_clean.split(" - ", 1)
        else:
            name = title_clean
            title_part = ""

        name = name.strip()
        title_part = title_part.strip()

        if name:
            results.append((name, title_part, link))

    return results

# Function to search and gather multiple pages
def search_and_print_profiles(query, api_key, cx, company_name, max_pages=3):
    all_results = []
    start_index = 1

    for page in range(max_pages):
        print(f"Fetching page {page + 1} with start_index = {start_index}...")

        data = google_search(query, api_key, cx, start_index)

        if "items" not in data:
            print("No more results or API issue.")
            break

        results = process_results(data, company_name)
        all_results.extend(results)

        start_index += 10
        time.sleep(2)

    return all_results

# Read company names from Excel
company_names = []
wb = openpyxl.load_workbook("company_data_1.xlsx")
sheet = wb.active

for i in range(2, 22):  # Read rows 2 to 20 (i.e., first 19 companies)
    company_name = sheet[f"A{i}"].value
    if company_name:
        company_names.append(company_name)

# Prepare output workbook
output_wb = Workbook()
output_sheet = output_wb.active
output_sheet.append(["Company Name", "Member Name", "Title", "LinkedIn Profile URL"])

# Loop through companies and perform search
for company_name in company_names:
    print(f"\nScraping data for company: {company_name}")
    
    query = f'"{company_name}" -intitle:"profiles" -inurl:"dir/" site:linkedin.com/in/ OR site:linkedin.com/pub/'
    profiles = search_and_print_profiles(query, API_KEY, CX, company_name)

    for name, title, link in profiles:
        output_sheet.append([company_name, name, title, link])

# Save results
output_wb.save("company_members.xlsx")
print(f"\nScraped data has been saved to company_members.xlsx.")
