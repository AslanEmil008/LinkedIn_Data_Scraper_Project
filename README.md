# LinkedIn Data Scraper Project
## Introduction
This project involves collecting data from LinkedIn about various companies.
It includes two Python scripts and one Scrapy project, which use ScrapeOps and Google APIs to gather LinkedIn data.<br>
The Python scripts collect data such as the company name, company URL, and employee information.<br>
The Scrapy project extracts information from the companies' 'About' sections.<br>
For more details, please refer to the section titled <b>Project Structure</b>.

##Project Sructure
### 1. **Company URLs Scraper**
- **Script**: `linkedin_company_data.py`
- **Description**: Retrieves company information, such as the company name and LinkedIn link.
- **Columns and Data**:
  - Company Name  
  - Company URL  
  - Company Type  
  - City
- **Output**: `company-data.xlsx`

### 2. **Company Data Scraper**
- **Script**: Scrapy
- **Description**: Enters company pages using the URLs from the company-data.xlsx file, located in the 'Company URL' column
- **Columns and Data**:
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
- **Description**: Using the company data from `company_data.xlsx`, it takes the company name, performs a specific search, and retrieves employee data.
- **Columns and Data**:
  - Company Name  
  - Member Name  
  - Title  
  - LinkedIn Profile URL
- **Output**: `company_members.xlsx`


# Getting Started
# Requirments 
Below is presented the correct order to run the code.<br>
For running this, you need to open two windows—one for running the linkedin_company_data.py,linkedin_members_data.py files and the other for running Scrapy.<br>
First, you need to run linkedin_company_data.py, then start Scrapy, and finally run linkedin_members_data.py
## Usage
### Clone the Repository
```bash
git clone https://github.com/AslanEmil008/LinkedIn_Data_Scraper_Project.git
cd linkedin-data-scraper
```
Then install requirments.txt
```bash
pip install -r requirements.txt
```

### Runing the codes
After cloning and downloading requirments.txt first you need to run <b>linkedin_company_data.py</b> <br>
for runing this code 
first you need in here:
email_field.send_keys("example@gmail.com")
password_field.send_keys("passwordexample")
chnge the email and password
then
for your nedded search you need do search the company types you want in linkedin then chooos from filters company after those copy the link and chnage it in
 linkedin_company_data.py file in <i>base_url = "https://www.linkedin.com/search/results/COMPANIES/?keywords=marketing&origin=SWITCH_SEARCH_VERTICAL&page={page}&sid=tHO"</i>
 instead <i>https://www.linkedin.com/search/results/COMPANIES/?keywords=marketing&origin=SWITCH_SEARCH_VERTICAL&page={page}&sid=tHO</i>
after doing changes you can run the code and get the datas.

Then you need to run the Scrapy



