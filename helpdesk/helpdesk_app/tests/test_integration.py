from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

class SeleniumIntegrationTest(TestCase):
    base_url = 'http://127.0.0.1:8000/'
    username = 'hd_yui'
    password = env('SELENIUM_TEST_PASSWORD')

    def setUp(self):
        self.driver = webdriver.Firefox()  
        self.driver.implicitly_wait(5)  # wait time

    def tearDown(self):
        self.driver.quit()

    def test_example(self):
        self.driver.get(self.base_url) 

    def authenticate_page(self):
        # Handle authentication prompt with separate text boxes for username and password
        username_input = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username_input.send_keys(self.username)

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(self.password)

        # Press Enter key to submit the credentials
        password_input.send_keys(Keys.RETURN)

    def test_create_ticket(self):
        # Example of navigating to a page
        self.driver.get(self.base_url + "/ticket/create_ticket/")

        self.authenticate_page() # login
        
        # Example of filling out form fields
        requester_input = self.driver.find_element(By.ID, "id_requester_name")
        requester_input.send_keys("John Doe")
        
        subject_input = self.driver.find_element(By.ID, "id_subject")
        subject_input.send_keys("Test Ticket")
        
        description_input = self.driver.find_element(By.ID, "id_description")
        description_input.send_keys("Test Description")
        
        assignee_input = self.driver.find_element(By.ID, "id_assignee")
        assignee_input.send_keys("Bob")
        
        priority_input = self.driver.find_element(By.ID, "id_priority")
        priority_input.send_keys("Highest")
        
        contact_email_input = self.driver.find_element(By.ID, "id_contact_email")
        contact_email_input.send_keys("johndoe@example.com")
        
        # Submit form
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        
        time.sleep(1) # Wait for the page to reload

        # Check for successful creation
        self.assertIn("Name on Ticket: John Doe", self.driver.page_source)
        self.assertIn("Test Ticket", self.driver.page_source)
        self.assertIn("Test Description", self.driver.page_source)
        self.assertIn("Bob", self.driver.page_source)
        self.assertIn("1", self.driver.page_source)

    def test_edit_ticket(self):
        # Navigate to the edit ticket page
        self.driver.get(self.base_url + "/tickets/19/update/") 

        self.authenticate_page() #login

        # Fill out the form with updated information
        subject_input = self.driver.find_element(By.ID, "id_subject")
        subject_input.clear()  # Clear existing subject
        subject_input.send_keys("Updated Ticket Subject")

        # Submit form
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        time.sleep(1)  # Wait for the page to reload

        # Check for successful update
        self.assertIn("Updated Ticket Subject", self.driver.page_source)

    def test_view_ticket(self):
        # Navigate to the ticket detail page
        self.driver.get(self.base_url + "/tickets/19") 

        time.sleep(1)  # Wait for the page to reload

        # Check for successful view
        self.assertIn("Name on Ticket:", self.driver.page_source)
        self.assertIn("Ticket Done:", self.driver.page_source)
        self.assertIn("Contact Email:", self.driver.page_source)
        self.assertIn("Subject:", self.driver.page_source)
        self.assertIn("Description:", self.driver.page_source)
        self.assertIn("Assignee:", self.driver.page_source)
        self.assertIn("Priority:", self.driver.page_source)