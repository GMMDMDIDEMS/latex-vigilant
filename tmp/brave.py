from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import csv
import time

def get_result():
    try:
        result = driver.find_element(By.XPATH,'//*[@id="result-titlecase"]')
        print(result.text)
        return result
    except StaleElementReferenceException:
        get_result()

chromedriver_autoinstaller.install()
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

driver = webdriver.Chrome(options = options)
wait = WebDriverWait(driver, 10)
time.sleep(5)

def read_file(file_path):
    with open(file_path, 'r') as file:
        for row in file:
            yield row.strip()

# Specify the CSV file path
csv_file = "titlecase_data.csv"

# Example usage
file_path = 'unittests/data/headings.txt'


driver.get("https://titlecase.com/titlecase")


all_iframes = driver.find_elements(By.TAG_NAME,"iframe")
if len(all_iframes) > 0:
    print("Ad Found\n")
    driver.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)
    print('Total Ads: ' + str(len(all_iframes)))
else:
    print('No frames found')

# Wait until the contenteditable div is visible
try:
    div_element = wait.until(
        EC.visibility_of_element_located((By.ID, "to_convert"))
    )
except TimeoutException:
    pass


# # Prompt the user for input
# user_input = input("Enter several sentences: ")

# # Clear the existing content in the div element
# driver.execute_script("arguments[0].textContent = '';", div_element)
# Write the data to the CSV file
try:
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Input", "Converted Input"])
        
        for row in read_file(file_path):
            time.sleep(1)
            
            try:
                div_element = wait.until(
                    EC.visibility_of_element_located((By.ID, "to_convert"))
                )
            except TimeoutException:
                pass
            # driver.execute_script("arguments[0].scrollIntoView();", div_element)
            driver.execute_script("arguments[0].textContent = arguments[1];", div_element, str(row))
            # Find and click the submit button
            # submit_button = driver.find_element_by_xpath("//button[@type='submit' and @class='btn btn-primary-outline convert-button' and @name='convert-button']")
            # submit_button.click()

            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @class='btn btn-primary-outline convert-button' and @name='convert-button']"))).click()
            except TimeoutException:
                pass

            time.sleep(1)

            # Wait until the converted text is visible
            # WebDriverWait(driver, 10).until(
            #     EC.visibility_of_element_located((By.ID, "result-titlecase"))
            # )
            try:
                wait.until(EC.visibility_of_element_located((By.ID, "result-titlecase")))
            except TimeoutException:
                pass
            
           
            converted_text_element = get_result()
            # driver.execute_script("arguments[0].scrollIntoView();", converted_text_element)
            
            # driver.execute_script("arguments[0].scrollIntoView();", converted_text_element)
            print(converted_text_element.text)
            # Get the converted text
            converted_text = converted_text_element.text.strip()

        # Create a list of dictionaries with the input and converted input
            data = [
                {"Input": row, "Converted Input": converted_text},
            ]

            writer.writerows(data)



        print(f"Data has been written to {csv_file}.")

finally:
    # Quit the browser
    driver.quit()



import os
from tex2py import tex2py

LATEX_PROJECT_PATH = "latex"

def get_tex_files(project_path):
    tex_files = []
    
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(".tex"):
                tex_files.append(os.path.join(root, file))
    
    return tex_files

tex_files = get_tex_files(LATEX_PROJECT_PATH)

for file_path in tex_files:
    print(file_path)
    with open(file_path) as f:
        data = f.read()

    soup = tex2py(data)
    print(soup.branches)