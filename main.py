from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Chrome
driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdM9YYdGh60QX9NXmHw_JzvNahZyE99vGIpEzeBp5Bt-FB1Zw/viewform")
wait = WebDriverWait(driver, 10)

try:
    # == Wait for form to fully load == #
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    time.sleep(1)

    # == Question 1: Industry (Text Input) == #
    industry_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    industry_input.send_keys("Roofing")

    time.sleep(1)
    # == Question 2: Ad Spend (Radio Option) == #
    ad_option = driver.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
    ad_option.click()

    # == Question 3: Ad spend (dropdown) == #
    drop_down = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]')
    drop_down.click()

    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="listbox"]')))
    dropdown.click()
    time.sleep(1)

    # === Click "$100-$1000" from dropdown ===
    option = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="option"]//span[contains(text(), "$100-$1000")]')))
    option.click()

    # == Business Listed == #
    gmb = wait.until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "i45"] / div[2]')))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", gmb)
    time.sleep(0.5)
    gmb.click()

    fb = driver.find_element(By.XPATH, '//*[@id="i48"]/div[2]')
    fb.click()

    ig = driver.find_element(By.XPATH, '//*[@id="i51"]/div[2]')
    ig.click()

    ind_dir = driver.find_element(By.XPATH, '//*[@id="i57"]/div[2]')
    ind_dir.click()

    other = driver.find_element(By.XPATH, '//*[@id="i60"]/div[2]')
    other.click()

    other_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[6]/div/div/div/div/div[1]/input')
    time.sleep(0.5)
    other_box.send_keys("Local magazine")
    time.sleep(0.5)

    # == Get Started == #
    yes_asap_radio = driver.find_element(By.XPATH, '//*[@id="i68"]/div[3]/div')
    yes_asap_radio.click()

    time.sleep(1)
    # == Submit Button == #
    submit_button = driver.find_element(By.XPATH, '// *[ @ id = "mG61Hd"] / div[2] / div / div[3] / div[1] / div[1] / div / span / span')
    submit_button.click()

    # == Confirmation == #
    print("Form submitted successfully")

finally:
    time.sleep(2)
    driver.quit()
