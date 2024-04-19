#from django.contrib.auth.models import User
#from django.urls import reverse

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

#from webdriver_manager.firefox import GeckoDriver
#from selenium.webdriver.firefox.service import Service as FirefoxService



'''
driver = webdriver.Firefox()
browser = webdriver.Firefox(
    service = FirefoxService(GeckoDriverManager().install())
)


#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

class IntegrationTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        self.browser.get(self.live_server_url)  # Point to the live server URL

    def tearDown(self):
        self.browser.quit()

def test_create_ticket(self):
    # Example of navigating to a page
    self.browser.get(self.live_server_url + "/ticket/create_ticket/")
    
    # Example of filling out form fields
    requester_input = self.browser.find_element(By.ID, "id_requester_name")
    requester_input.send_keys("John Doe")
    
    subject_input = self.browser.find_element(By.ID, "id_subject")
    subject_input.send_keys("Test Ticket")
    
    description_input = self.browser.find_element(By.ID, "id_description")
    description_input.send_keys("Test Description")
    
    assignee_input = self.browser.find_element(By.ID, "id_assignee")
    assignee_input.send_keys("Bob")
    
    priority_input = self.browser.find_element(By.ID, "id_priority")
    priority_input.send_keys("1")
    
    contact_email_input = self.browser.find_element(By.ID, "id_contact_email")
    contact_email_input.send_keys("johndoe@example.com")
    
    # Submit form
    submit_button = self.browser.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    
    # Check for successful creation
    self.assertIn("Ticket created successfully", self.browser.page_source)
   ''' 
'''from helpdesk_app.models import Ticket

class TestName(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        super(TestName, self).setUp()

        test_user = User.objects.create(username='Testuser')
        test_user.set_password('senha8dg')
        test_user.save()
        
        # Login the user
        self.assertTrue(self.client.login(username='Testuser', password='senha8dg'))
        # Add cookie to log in the browser
        cookie = self.client.cookies['sessionid']
        self.browser.get(self.live_server_url) # visit page in the site domain so the page accepts the cookie
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})


def testTicketCreation(self):
    ticket = Ticket.objects.create(
        requester_name="John Doe",
        subject="Test Ticket",
        description="This is a test ticket.",
        assignee="Bob",
        priority="3",
        contact_email="john.doe@example.com"
    )
    self.browser.get(self.live_server_url)
    self.browser.get(self.live_server_url + reverse('index')
    wait = WebDriverWait(self.browser, 10)'''
    #click on manage tickets tab (second fram the left on nav bar)
    #click create new ticket button
    #enter requester name in requester name field of the form
    #enter contact email in contact email field of the form
    #enter subject in subject field of the form
    #enter Description in Description field of the form
    #enter Assignee in Assignee field of the form
    #enter Priority in Priority field of the form
    #click submit button
    #success when Ticket in in databse with correct attrbutes
