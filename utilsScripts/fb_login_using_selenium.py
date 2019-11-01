from selenium import webdriver

# Step 1) Open Firefox
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_id("loginbutton")
username.send_keys("you@email.com")
password.send_keys("yourpassword")
# Step 4) Click Login
submit.click()
