from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time, os
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
#scraping yt studio with Firefox (geckodriver)

# Set Firefox options
options = Options()
options.binary_location = r'/opt/firefox/firefox'

# Set the Firefox profile
profile = webdriver.FirefoxProfile('/home/toukoum/.mozilla/firefox/0he3tt71.default-release/')
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()

# Set the desired capabilities of the Firefox driver
desired = DesiredCapabilities.FIREFOX

# Instantiate the Firefox driver with the defined options and capabilities
driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired, options=options, executable_path=r'/opt/geckodriver')




#for all videos in the videos folder
dir_path = '/home/toukoum/chatGptApi/Youtube-Shorts-Bot/videos'
count = 0
for path in os.listdir(dir_path): 
if os.path.isfile(os.path.join(dir_path, path)): 
count += 1
print(" ", count, " Videos found in the videos folder, ready to upload...")
time.sleep(6)


#on upload all the videos that are in the /video folder
for i in range(count): 

# ========================================= 
# Set here your Youtube studio Url 
# =======================================

driver.get('https://studio.youtube.com/channel/UCzpIAsd_bGAwxVMEFk3HK7w')

time.sleep(3)

# Click the upload button
upload_button = driver.find_element(By.XPATH, '//*[@id="upload-icon"]')
upload_button.click()

# Wait 5 seconds
time.sleep(5)

file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')

# represents the relative path of the video file to upload
simp_path = 'videos/vid{}.mp4'.format(str(i+1))

# represents the Absolute path of the video file to upload
abs_path = os.path.abspath(simp_path)

print(abs_path)

file_input.send_keys(abs_path)

time.sleep(7)

#upload button
next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')

    # to do 3 times
    next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')

    #you have to click 3 times on the next button (we check the error which clicks in the 2nd step)
    for l in range (3):
        while True:
            try:
                next_button.click()
                time.sleep(3)
                break
            #if weird mistake, we wait... I don't know if that's the best way
            except ElementClickInterceptedException:
                time.sleep(10)   
            except ElementNotInteractableException:
                 time.sleep(10)

    done_button = driver.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)

    os.remove(abs_path)
    

driver.quit()


