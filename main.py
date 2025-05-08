import data  # importa os dados de teste do arquivo data.py
import helpers  # importa a função is_url_reachable para verificar o servidor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.URBAN_ROUTES_URL)

    def test_set_route(self):
        from_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'from'))
        )
        to_field = self.driver.find_element(By.ID, 'to')

        from_field.click()
        from_field.clear()
        from_field.send_keys(data.ADDRESS_FROM)

        to_field.click()
        to_field.clear()
        to_field.send_keys(data.ADDRESS_TO)

        call_taxi_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Call a taxi")]')
        assert call_taxi_button is not None

    def test_select_plan(self):
        # Adicionar em S8
        print("Função criada para selecionar o plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("Função criada para preencher o número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("Função criada para preencher o cartão")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Função criada para adicionar comentário ao motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Função criada para pedir cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        print("Função criada para pedir sorvete")
        for i in range(2):
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Função criada para verificar se o modelo do carro aparece")
        pass
