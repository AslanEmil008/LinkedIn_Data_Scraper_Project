# Linkedin Data

---

## 🧩 1. Company URLs Scraper

**Script:** `linkedin_company_data.py`  
**Description:** This script collects basic information about companies from LinkedIn search results.

**Extracted Fields:**
- `Company Name`
- `Company URL`
- `Company Type`
- `City`

**Output File:** `company-data.xlsx`

---

## 🕷️ 2. Company "About" Data Scraper

**Script:** `Scrapy` (Scrapy project)  
**Description:** A Scrapy-based spider that visits each company page URL and extracts detailed company info.

**Extracted Fields:**
- `Company URL`
- `Name`
- `Summary`
- `Industry`
- `Size`
- `Founded`
- `Website`
- `Headquarters`
- `Type`
- `Specialties`
- `Locations`
- `Employees`

**Output File:** `company_profiles.xlsx`

---

## 👥 3. Company Employees Scraper

**Script:** `linkedin_members_data`  
**Description:** This script collects public employee information from company LinkedIn pages.

**Extracted Fields:**
- `Company Name`
- `Member Name`
- `Title`
- `LinkedIn Profile URL`

**Output File:** `company_members.xlsx`

---

## 📌 Notes

- These are **initial results** and cover the first phase of scraping.
- More features and data may be added in future iterations.
- All data was collected using automation techniques with respect to LinkedIn's structure and dynamic loading.

---

## 📩 Contact / Feedback

If you have any questions, feedback, or would like to proceed with the next stage of the project, feel free to reach out!

📧 Email: aslanemil008@gmail.com

💻 GitHub: github.com/aslanemil008
