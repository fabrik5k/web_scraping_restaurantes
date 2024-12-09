from playwright.sync_api import sync_playwright
import time

def login_and_save_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.econodata.com.br/consulta-empresa")

        time.sleep(60)

        context.storage_state(path="storageState.json")
        browser.close()

def use_saved_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # Cria um novo contexto já com o estado salvo
        context = browser.new_context(storage_state="storageState.json")
        page = context.new_page()
        page.goto("https://www.econodata.com.br/consulta-empresa")

        # Se o estado foi salvo corretamente, a página deve já aparecer logada.
        # Teste algum elemento que só aparece depois do login.
        page.wait_for_selector("#elemento_logado")

        # Faça o que for necessário no estado logado
        print("Usuário logado com sucesso!")
        browser.close()

# Executa apenas uma vez para salvar o estado:
login_and_save_state()

# Depois, em execuções futuras, você só usa o estado salvo:
#use_saved_state()
