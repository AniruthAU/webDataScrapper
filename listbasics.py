from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url1 = 'https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analyst&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url1)

try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search-results')))

    job_elements = driver.find_elements(By.XPATH, '//li[contains(@class, "result-card")]')

    for job_element in job_elements:
        # Extract job name
        job_name_element = job_element.find_element(By.CLASS_NAME, 'result-card__title')
        job_name = job_name_element.text.strip()

        job_desc_element = job_element.find_element(By.CLASS_NAME, 'result-card__contents')
        job_desc = job_desc_element.text.strip()
        print(f"Job Title: {job_name}")
        print(f"Job Description:\n{job_desc}")
        print("=" * 50)

except TimeoutException:
    print("Timeout occurred while waiting for job listings to load.")

finally:
    driver.quit()
