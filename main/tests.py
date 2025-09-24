from django.test import TestCase, Client
from .models import Product
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User

class MainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        logged_in = self.client.login(username='testuser', password='testpass')

    def test_main_url_is_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_product_creation(self):
        product = Product.objects.create(
            name="Jersey Club X",
            price=250000,
            description="Jersey resmi klub X",
            thumbnail="https://example.com/jersey.jpg",
            category="jersey",
            is_featured=True
        )
        self.assertEqual(product.name, "Jersey Club X")
        self.assertEqual(product.price, 250000)
        self.assertEqual(product.category, "jersey")
        self.assertTrue(product.is_featured)

    def test_product_default_values(self):
        product = Product.objects.create(
            name="Sepatu Latihan",
            price=350000,
            description="Sepatu training serbaguna"
        )
        # Sesuaikan expected default category jika kamu mengubah default di model
        self.assertEqual(product.category, "jersey")
        self.assertFalse(product.is_featured)
        # thumbnail pada model diset blank=True, null=True -> bila tidak diisi, seharusnya None
        self.assertIsNone(product.thumbnail)

class ProductFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create single browser instance for all tests
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Close browser after all tests complete
        cls.browser.quit()

    def setUp(self):
        # Create user for testing
        self.test_user = User.objects.create_user(
            username='testadmin',
            password='testpassword'
        )

    def tearDown(self):
        # Clean up browser state between tests
        self.browser.delete_all_cookies()
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.execute_script("window.sessionStorage.clear();")
        # Navigate to blank page to reset state
        self.browser.get("about:blank")

    def login_user(self):
        """Helper method to login user"""
        self.browser.get(f"{self.live_server_url}/login/")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpassword")
        password_input.submit()

    def test_login_page(self):
        # Test login functionality
        self.login_user()

        # Check if login is successful
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        # App name should be displayed as H1 on the main page
        self.assertEqual(h1_element.text, "GoalGear")

        logout_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.assertTrue(logout_link.is_displayed())

    def test_register_page(self):
        # Test register functionality
        self.browser.get(f"{self.live_server_url}/register/")

        # Check if register page opens
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Register")

        # Fill register form
        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("newuser")
        password1_input.send_keys("complexpass123")
        password2_input.send_keys("complexpass123")
        password2_input.submit()

        # Check redirect to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        login_h1 = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(login_h1.text, "Login")

    def test_create_product(self):
        # Test create product functionality (requires login)
        self.login_user()

        # Go to create product page via "Add Product" button/link
        add_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Add Product")
        add_button.click()

        # Fill form (fields based on ProductForm: name, price, description, thumbnail, category, is_featured, ...)
        name_input = self.browser.find_element(By.NAME, "name")
        price_input = self.browser.find_element(By.NAME, "price")
        description_input = self.browser.find_element(By.NAME, "description")
        thumbnail_input = self.browser.find_element(By.NAME, "thumbnail")
        category_select = self.browser.find_element(By.NAME, "category")
        is_featured_checkbox = self.browser.find_element(By.NAME, "is_featured")

        name_input.send_keys("Test Product Name")
        price_input.send_keys("100000")
        description_input.send_keys("Test product description for selenium testing")
        thumbnail_input.send_keys("https://example.com/image.jpg")

        # Set category (select 'jersey' for example)
        select = Select(category_select)
        select.select_by_value("jersey")

        # Check is_featured checkbox
        is_featured_checkbox.click()

        # Submit form
        name_input.submit()

        # Check if returned to main page and product appears
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "GoalGear"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "GoalGear")

        # Check if product name appears on page
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Test Product Name")))
        product_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Test Product Name")
        self.assertTrue(product_link.is_displayed())

    def test_product_detail(self):
        # Test product detail page

        # Login first because some views may require authentication
        self.login_user()

        # Create product for testing (no user field on Product model)
        product = Product.objects.create(
            name="Detail Test Product",
            price=50000,
            description="Content for detail testing",
            category="jersey"
        )

        # Open product detail page
        self.browser.get(f"{self.live_server_url}/product/{product.id}/")

        # Check if detail page opens correctly
        self.assertIn("Detail Test Product", self.browser.page_source)
        self.assertIn("Content for detail testing", self.browser.page_source)

    def test_logout(self):
        # Test logout functionality
        self.login_user()

        # Click logout button - text is inside button, not link
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        logout_button.click()

        # Check if redirected to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Login")

    def test_filter_main_page(self):
        # Test that products are shown on main page (no specific filter UI assumed)
        Product.objects.create(
            name="My Test Product",
            price=20000,
            description="My product content",
            category="jersey"
        )
        Product.objects.create(
            name="Other Product", 
            price=30000,
            description="Other content",
            category="jersey"
        )

        self.login_user()

        # Wait until main page loads and check both products are present
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        page_source = self.browser.page_source
        self.assertIn("My Test Product", page_source)
        self.assertIn("Other Product", page_source)