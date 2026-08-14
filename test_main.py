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

    # Método de Pago y Tarjeta
    payment_method_button = (By.XPATH, '//div[@class="pp-button filled"]')
    add_card_button = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, '//input[@name="code"]')
    confirm_card_button = (By.XPATH, '//button[text()="Agregar"]')
    close_payment_modal_button = (By.XPATH,
                                  '//div[@class="payment-picker open"]//button[contains(@class, "close-button")]')
    overlay = (By.CLASS_NAME, 'overlay')

    # Mensaje y Requisitos
    driver_message_field = (By.ID, 'comment')
    blanket_tissue_switch = (By.XPATH, '//span[@class="slider round"]')
    add_ice_cream_button = (By.XPATH,
                            '//div[contains(@class, "r-type-counter")]//div[contains(@class, "counter-plus")]')

    # Pedido y Conductor
    order_taxi_button = (By.XPATH, '//button[@class="smart-button"]')
    driver_info_modal = (By.XPATH, '//div[@class="order-header-title"]')

    def __init__(self, driver):
        self.driver = driver

    # --- MÉTODOS DE LA PÁGINA ---
    def set_route(self, from_address, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button)).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.comfort_tariff_button)).click()

    def add_credit_card(self, number, code):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_method_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_card_button)).click()

        card_num_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_number_field))
        card_num_input.clear()
        card_num_input.send_keys(number)

        code_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_code_field))
        code_input.clear()
        code_input.send_keys(code)
        code_input.send_keys(Keys.TAB)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_card_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_payment_modal_button)).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.overlay))

    def set_driver_message(self, message):
        msg_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.driver_message_field))
        msg_input.clear()
        msg_input.send_keys(message)

    def order_blanket_and_tissues(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.blanket_tissue_switch))
        self.driver.execute_script("arguments[0].click();", element)

    def add_ice_creams(self, count=2):
        plus_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.add_ice_cream_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", plus_btn)
        for _ in range(count):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_ice_cream_button)).click()

    def submit_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_taxi_button)).click()

    def wait_for_driver_info(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.driver_info_modal))


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_order_taxi_e2e(self):
        # 1. Abrir la página y configurar la ruta
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)

        assert self.driver.find_element(*UrbanRoutesPage.from_field).get_attribute('value') == data.address_from
        assert self.driver.find_element(*UrbanRoutesPage.to_field).get_attribute('value') == data.address_to

        # 2. Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()

        # 3. Agregar tarjeta de crédito
        routes_page.add_credit_card(data.card_number, data.card_code)

        # 4. Escribir mensaje al conductor
        routes_page.set_driver_message(data.message_for_driver)

        # 5. Solicitar manta y pañuelos
        routes_page.order_blanket_and_tissues()

        # 6. Agregar helados
        routes_page.add_ice_creams(2)

        # 7. Confirmar el pedido
        routes_page.submit_order()

        # 8. Validar modal del conductor
        driver_info = routes_page.wait_for_driver_info()
        assert driver_info is not None

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()