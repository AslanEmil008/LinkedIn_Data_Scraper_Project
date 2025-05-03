# 🔗 LinkedIn Data Scraper Project

A multi-phase Python-based project that automates the process of collecting company and employee data from LinkedIn. This tool is designed for researchers, recruiters, or analysts who need structured LinkedIn data at scale.

---

## 📁 Project Structure

### 1. **Company URLs Scraper**
- **Script**: `linkedin_company_data.py`
- **Function**: Collects basic company information from LinkedIn search results.
- **Extracted Fields**:
  - Company Name  
  - Company URL  
  - Company Type  
  - City
- **Output**: `company-data.xlsx`

### 2. **Company "About" Data Scraper**
- **Script**: Scrapy-based project
- **Function**: Visits company pages from `company-data.xlsx` and extracts detailed company descriptions.
- **Extracted Fields**:
  - Company URL  
  - Name  
  - Summary  
  - Industry  
  - Size  
  - Founded  
  - Website  
  - Headquarters  
  - Type  
  - Specialties  
  - Locations  
  - Employees
- **Output**: `company_profiles.xlsx`

### 3. **Company Employees Scraper**
- **Script**: `linkedin_members_data.py`
- **Function**: Gathers public employee details listed on company LinkedIn pages.
- **Extracted Fields**:
  - Company Name  
  - Member Name  
  - Title  
  - LinkedIn Profile URL
- **Output**: `company_members.xlsx`

---

## 💡 Technologies Used

- **Python**: Core language for automation scripts.
- **Selenium**: For interacting with LinkedIn’s dynamically loaded content.
- **Scrapy**: Efficient web crawling and structured data extraction.
- **Pandas**: Handling and exporting data in Excel format.
- **OpenPyXL / XlsxWriter**: For writing Excel files.
- **XPath / CSS Selectors**: DOM navigation and targeted data scraping.

These tools were chosen for their reliability, ability to handle JavaScript-heavy websites like LinkedIn, and compatibility with structured data workflows.

---

## 🚀 Getting Started

### 📦 Clone the Repository
```bash
git clone https://github.com/aslanemil008/linkedin-data-scraper.git
cd linkedin-data-scraper
```

### 🛠️ Install Dependencies
Make sure you have Python 3 installed. Then run:
```bash
pip install -r requirements.txt
```

### ▶️ How to Run

#### 1. Scrape Company URLs
```bash
python linkedin_company_data.py
```

#### 2. Scrape Company About Info (Scrapy)
```bash
cd company_about_scraper
scrapy crawl company_about
```

#### 3. Scrape Company Employees
```bash
python linkedin_members_data.py
```

> Ensure all scripts are configured with your Selenium WebDriver, valid LinkedIn login credentials (if needed), and proxy settings if scraping in volume.

---

## 📌 Notes

- These are early-phase scrapers. More features and data fields may be added in future updates.
- All data is gathered via automation with respect to LinkedIn’s public structure and dynamic content behavior.
- Use responsibly and ethically. Comply with LinkedIn’s [Terms of Service](https://www.linkedin.com/legal/user-agreement).

---

## 📩 Contact / Feedback

Have questions or suggestions? Want to collaborate or extend the functionality?

- 📧 Email: [aslanemil008@gmail.com](mailto:aslanemil008@gmail.com)  
- 💻 GitHub: [github.com/aslanemil008](https://github.com/aslanemil008)
