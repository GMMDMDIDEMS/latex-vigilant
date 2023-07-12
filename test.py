from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

def read_file(file_path):
    with open(file_path, 'r') as file:
        for row in file:
            yield row.strip()

# Example usage
file_path = 'unittests/data/headings.txt'


try:
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Load the webpage
    driver.get("https://titlecase.com/titlecase")

    # Wait until the contenteditable div is visible
    div_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "to_convert"))
    )



    # Enter the user input into the div element
    driver.execute_script("arguments[0].textContent = arguments[1];", div_element, "amk")

    time.sleep(2)

    # Enter the user input into the div element
    driver.execute_script("arguments[0].textContent = arguments[1];", div_element, "it works")


    # Find and click the submit button
    submit_button = driver.find_element_by_xpath("//button[@type='submit' and @class='btn btn-primary-outline convert-button' and @name='convert-button']")
    submit_button.click()


    # Wait until the converted text is visible
    converted_text_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result-titlecase"))
    )

    # Get the converted text
    converted_text = converted_text_element.text.strip()

    # Create a list of dictionaries with the input and converted input
    data = [
        {"Input": "amk", "Converted Input": converted_text},
    ]

    # Specify the CSV file path
    csv_file = "titlecase_data.csv"

    # Write the data to the CSV file
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Input", "Converted Input"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Data has been written to {csv_file}.")

finally:
    # Quit the browser
    driver.quit()
