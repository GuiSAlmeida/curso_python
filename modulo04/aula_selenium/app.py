from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.drive_path = 'modulo04/aula_selenium/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            'user-data-dir=modulo04/aula_selenium/Perfil')

        self.chrome = webdriver.Chrome(
            self.drive_path,
            options=self.options
        )
        self.chrome.set_window_size(1024, 768)

    def visit(self, url):
        self.chrome.get(url)

    def sign_in(self):
        try:
            input_matricula = self.chrome.find_element(By.ID, 'matricula')
            input_senha = self.chrome.find_element(By.ID, 'senha')
            btn_login = self.chrome.find_element(By.ID, 'login')

            input_matricula.send_keys('32010002737')
            input_senha.send_keys('Gui-dev87')

            btn_login.click()
        except Exception as e:
            print(f'Error on sign in: {e}')

    def classes(self):
        try:
            classes = self.chrome.find_element(
                By.CSS_SELECTOR,
                'a[href="aulas_ao_vivo.asp"]')

            self.chrome.execute_script("arguments[0].click();", classes)

        except Exception as e:
            print(f'Error on classes: {e}')

    def verify_email(self, email):
        user_email = self.chrome.find_element(By.ID, 'email-institucional')
        user_email_html = user_email.get_attribute('innerHTML')
        assert email in user_email_html

    def close_modal(self):
        try:
            btn_close_modal = self.chrome.find_element(
                By.CSS_SELECTOR,
                '.modal-content button.btn-danger')

            btn_close_modal.click()
            sleep(1)
            self.chrome.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            print(f'Error on close modal: {e}')

    def logout(self):
        try:
            btn_close_login = self.chrome.find_element(By.ID, 'btn-sair')
            btn_close_login.click()
        except Exception as e:
            print(f'Error on close login: {e}')

    def quit(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.visit('https://www.ies.edu.br/')
    chrome.sign_in()
    sleep(2)
    chrome.classes()
    sleep(2)
    chrome.close_modal()
    sleep(2)
    chrome.verify_email('guilherme.almeida22@aluno.ies.edu.br')
    sleep(2)
    chrome.logout()
    sleep(3)
    chrome.quit()
