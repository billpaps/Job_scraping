import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 
def job_description_text_scrape(job_description_frame: WebElement): # ID = 'vjs-container-iframe'
    try:
        # Switch to description frame
        driver.switch_to_frame(job_description_frame)
        # job_description_text = description_element.find_element_by_id('jobDescriptionText')
        print(driver.find_element_by_id('jobDescriptionText').get_attribute('innerHTML'))
    except NoSuchElementException:
        print('Exception Raised')
    driver.switch_to_default_content()
    return

# This functions is scraping every job card withing a web page
def scrape_job_posts_in_page():
    try:
        # Wait request. Set to 5 seconds
        wait = WebDriverWait(driver, 5)

        # Return all the job cards elements
        # job_cards = driver.find_elements_by_xpath('//*[contains(@id, "job_")]')
        job_cards = driver.find_elements_by_class_name('slider_container')
        print(len(job_cards))

        # Extract job title
        job_title = driver.find_elements_by_xpath('//*[contains(@id, "job_")]/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/span')

        for i in job_cards:
            i.click()
            print('clicks')
            try:
                ''' 
                Selects the job description element which shows on the right. 
                This window contains usefull informations about that specific job.
                After selecting it we further process it in the @job_description_editing function
                '''
                
                job_description_frame = wait.until(EC.presence_of_element_located((By.ID, 'vjs-container-iframe')))
                job_description_text_scrape(job_description_frame)

            except TimeoutException:
                print('Couldnt open job description panel')
    finally:
        print('shit yooo')
    return


website = "https://www.indeed.com"
driver = webdriver.Chrome('C:/Users/billonios/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(website)
driver.set_window_size(2000, 1500)

print(website.title())


search_bar_job = driver.find_element_by_id('text-input-what')   # Select the 'Job Search' text field
search_bar_location = driver.find_element_by_id('text-input-where') # Select the location text field


search_bar_job.clear()
search_bar_job.send_keys('Analyst')

search_bar_location.clear()
search_bar_location.send_keys('America')
search_bar_job.send_keys(Keys.RETURN)

# Redirect to other location. If you entered an abroad place then this is crucial
national_search = driver.find_element_by_xpath('//*[@id="resultsCol"]/div[2]/div/p/a')
national_search.send_keys(Keys.RETURN)

scrape_job_posts_in_page()

driver.close()
