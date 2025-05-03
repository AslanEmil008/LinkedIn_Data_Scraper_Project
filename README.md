# LinkedIn Data Scraper Project
## Introduction
This project involves collecting data from LinkedIn about various companies.
It includes two Python scripts and one Scrapy project, which use ScrapeOps and Google APIs to gather LinkedIn data.<br>
The Python scripts collect data such as the company name, company URL, and employee information.<br>
The Scrapy project extracts information from the companies 'About' sections.<br>
For more details, please refer to the section titled **[Project Structure](#project-structure)**.

## Project Structure
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
- **Script**: `Scrapy`
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
## Requirments 
Below is the order in which the code should be run and instructions on how to run it<br>
First, you need to run linkedin_company_data.py, then start Scrapy, and finally run linkedin_members_data.py<br>
For running this project, you need to open two windows—one for running the linkedin_company_data.py,linkedin_members_data.py files and the other for running Scrapy.<br>
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

### How to run
After cloning the repository and installing the requirements from `requirements.txt`<br>
<br>
<b>First run `linkedin_company_data.py`</b>
#### To run this code you need:
<b>1.</b>Locate the following lines:
```bash
email_field.send_keys("example@gmail.com")
password_field.send_keys("passwordexample")
```
Replace the email and password with your own LinkedIn credentials.<br>


<b>2.</b>To perform a search:<br>
Go to LinkedIn and search for the company types you need.<br>
Use the filters to select "Companies".<br>
Copy the resulting URL and in code locate this line:
```bash
base_url = "https://www.linkedin.com/search/results/COMPANIES/?keywords=marketing&origin=SWITCH_SEARCH_VERTICAL&page={page}&sid=tHO"
```
 Replace the value of your <b>base_url</b> <br>
 <b>3.</b>Run the script:
 ```bash
python3 linkedin_company_data.py
```
After this step, you'll get data with the columns defined in the **[Project Structure](#project-structure)**


<b>Next, you need to run the Scrapy spider:</b><br>
<b>1.</b>Open the Scrapy folder in a new terminal window<br>
<b>2.</b>In terminal run:
```bash
source venv/bin/activate
cd Scrapy
```
<b>3.</b>`Open settings.py` and update this line with your own ScrapeOps API key
```bash
SCRAPEOPS_API_KEY = 'your-api-key-here'
```
<b>4.</b>Run the spider:
```bash
scrapy crawl basic_scrapy_spider
```
After this step, you'll get data with the columns defined in the **[Project Structure](#project-structure)**

<b>Lastly, run `linkedin_members_data.py`.</b><br>
<b>1.</b>In the script,locate and update the following with your own credentials:
```bash
API_KEY = "your-google-api-key"
CX = "your-custom-search-engine-id"
```
- To get the API key, go to [Google Cloud Console](https://console.cloud.google.com/), create a project, and generate an API key.
- To get the CX (Custom Search Engine ID), go to [Programmable Search Engine](https://programmablesearchengine.google.com/about/), create a project, and obtain the CX ID.<br>
<b>2.</b>Run the script.<br>
```bash
python3 linkedin_members_data.py
```
After running it, you will receive the member data as specified in the **[Project Structure](#project-structure)**





