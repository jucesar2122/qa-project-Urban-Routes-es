import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_open_application(self):
        # 1. Abrir la página
        self.driver.get(data.urban_routes_url)
        
        # 2. Validar que la página cargó correctamente
        assert self.driver.title is not None

    def test_driver_initialization(self):
        # Validar que el navegador está activo
        assert self.driver.current_url.startswith('http')

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

