import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data


class UrbanRoutesPage:
    # --- LOCALIZADORES ---
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Pedir un taxi") or contains(text(), "Call a taxi")]')
    comfort_tariff_button = (By.XPATH, '//div[text()="Comfort"]')

    # Métodos de Pago y Tarjeta
    payment_method_button = (By.XPATH, '//div[@class="pp-button filled"]')
    add_card_button = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, '//input[@name="code"]')
    confirm_card_button = (By.XPATH, '//button[text()="Agregar"]')

    # Cierre de Modal de Método de Pago
    close_payment_modal_button = (By.XPATH,
                                  '//div[@class="payment-picker open"]//button[contains(@class, "close-button")]')
    overlay = (By.CLASS_NAME, 'overlay')

    # Mensaje al conductor
    driver_message_field = (By.ID, 'comment')

    # Requisitos del viaje
    blanket_tissue_switch = (By.XPATH, '//span[@class="slider round"]')

    # Localizador mejorado para el botón + del helado (busca el primer counter-plus del bloque)
    add_ice_cream_button = (By.XPATH,
                            '//div[contains(@class, "r-type-counter")]//div[contains(@class, "counter-plus")]')

    # Confirmar Pedido y Modal Conductor
    order_taxi_button = (By.XPATH, '//button[@class="smart-button"]')
    driver_info_modal = (By.XPATH, '//div[@class="order-header-title"]')

    def __init__(self, driver):
        self.driver = driver

    # --- MÉTODOS ---

    def set_route(self, from_address, to_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.call_taxi_button)
        ).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.comfort_tariff_button)
        ).click()

    def add_credit_card(self, number, code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.payment_method_button)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_card_button)
        ).click()

        card_num_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_number_field)
        )
        card_num_input.clear()
        card_num_input.send_keys(number)

        code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_code_field)
        )
        code_input.clear()
        code_input.send_keys(code)

        code_input.send_keys(Keys.TAB)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_card_button)
        ).click()

        close_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_payment_modal_button)
        )
        close_btn.click()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.overlay)
        )

    def set_driver_message(self, message):
        msg_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.driver_message_field)
        )
        msg_input.clear()
        msg_input.send_keys(message)

    def order_blanket_and_tissues(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.blanket_tissue_switch)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def add_ice_creams(self, count=2):
        # Desplazar hacia el elemento si es necesario
        plus_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.add_ice_cream_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", plus_btn)

        for _ in range(count):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_ice_cream_button)
            ).click()

    def submit_order(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_taxi_button)
        )
        btn.click()

    def wait_for_driver_info(self):
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.driver_info_modal)
        )


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        assert self.driver.find_element(*UrbanRoutesPage.from_field).get_attribute('value') == data.address_from
        assert self.driver.find_element(*UrbanRoutesPage.to_field).get_attribute('value') == data.address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card(data.card_number, data.card_code)

    def test_set_driver_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_driver_message(data.message_for_driver)

    def test_order_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_tissues()

    def test_add_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_creams(2)

    def test_submit_order(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.submit_order()

    def test_wait_for_driver_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.wait_for_driver_info() is not None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()