from playwright.sync_api import sync_playwright
import time
import json
import pandas as pd

NUM_RESULTADOS = 60

# Iniciar o Playwright
with sync_playwright() as p:
    # Inicializar o navegador (Chromium por padrão)
    browser = p.chromium.launch(headless=True)  # headless=False para ver o navegador em ação

    # Adicionando Estado da máquina
    context = browser.new_context(storage_state="./states/storageState2.json")

    # Acessar a página
    page = context.new_page()
    page.goto("https://www.econodata.com.br/empresas/todo-brasil?_gl=1*od5djw*_gcl_au*MTQ1OTE0MjY4OS4xNzMzNDQxMDg5*_ga*NjEwODg1NTQwLjE3MzM0NDEwODk.*_ga_BFMKLBFXM8*MTczMzQ0MTA4OS4xLjAuMTczMzQ0MTA4OS42MC4wLjA./")

    time.sleep(5)
    # Esperar até o campo de input estar visível
    input_xpath_restaurante = '//*[@id="buscador-inteligente-input-setor"]'
    input_xpath_regiao = '//*[@id="buscador-inteligente-input-regiao"]'
    input_xpath_botaoPesquisar = '//*[@id="ecdt-buscador-botao-pesquisar"]'


    page.wait_for_selector(input_xpath_restaurante, timeout=10000)
    page.fill(input_xpath_restaurante, "Restaurantes")
    
    page.wait_for_selector(input_xpath_regiao, timeout=10000)
    page.fill(input_xpath_regiao, "Belém")

    page.wait_for_selector(input_xpath_restaurante, timeout=10000)
    page.click(input_xpath_botaoPesquisar)

    span_xpath = '//*[@id="galhos-empresa-title-h1"]/span[1]'
    page.wait_for_selector(span_xpath, timeout=10000)
    valor_texto = page.locator(span_xpath).text_content().replace('.','')
    valor_de_resultados = int(valor_texto)
    print(f'O valor numérico é: {valor_de_resultados}')

    xpath_botao_ranking = '//*[@id="Maiores"]/div[3]/div[2]/div/a'
    page.wait_for_selector(xpath_botao_ranking, timeout=10000)
    page.click(xpath_botao_ranking)


    # Numero máximo de páginas que pode ter
    page_search_number = valor_de_resultados//20 + 1

    dados = []
    time.sleep(5)

    try:
        # Loop para pegar os dados
        for i in range(2, page_search_number):

            if NUM_RESULTADOS == len(dados):
                break

            print(len(dados))
            tbody_xpath = '//*[@id="ecdt-table-container"]/div/div/table/tbody'
            tbody = page.locator(tbody_xpath)
            tr_elements = page.locator(tbody_xpath).locator('tr')
            
            quantidade_elementos = tbody.locator('tr').count()
            print(quantidade_elementos)

            time.sleep(3)
            # Laço para iterar sobre os <tr> e clicar nos links dentro do primeiro <td>
            for j in range(quantidade_elementos):

                if NUM_RESULTADOS == len(dados):
                    break

                print(len(dados))

                link = tr_elements.nth(j).locator('td:nth-child(1) a')

                # Entrando nos sites das empresas
                link_url = link.get_attribute('href') 
                print(f'Clicando no link: {link_url}')
                link.click()

                time.sleep(5)
                # XPath do <p>
                xpath_Nome = '//*[@id="item-detalhe-valor-nome-fantasia"]'
                xpath_RazaoSocial = '//*[@id="item-detalhe-valor-razao-social"]'
                xpath_CNPJ = '//*[@id="item-detalhe-valor-cnpj"]'
                xpath_Situacao = '//*[@id="item-detalhe-valor-situacao"]'
                xpath_Logadouro = '//*[@id="__nuxt"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/span'
                xpath_Bairro = '//*[@id="__nuxt"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/span'
                xpath_Municipio = '//*[@id="detalhe-empresa-localizacao-cidade-uf"]'
                xpath_CEP = '//*[@id="__nuxt"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[4]/span'


                nome_fantasia = page.locator(xpath_Nome).text_content()
                razao_social = page.locator(xpath_RazaoSocial).text_content()
                cnpj = page.locator(xpath_CNPJ).text_content()
                situacao = page.locator(xpath_Situacao).text_content()
                logadouro = page.locator(xpath_Logadouro).text_content()
                bairro = page.locator(xpath_Bairro).text_content()
                municipio = page.locator(xpath_Municipio).nth(0).text_content()
                cep = page.locator(xpath_CEP).text_content()

                dicionario = {
                    'Nome': nome_fantasia,
                    'Razao Social': razao_social,
                    'CNPJ': cnpj,
                    'Situacao': situacao,
                    'Logadouro': logadouro,
                    'Bairro': bairro,
                    'Municipio/UF': municipio,
                    'CEP': cep
                }

                dados.append(dicionario)
                print(dicionario)
                page.go_back()
                
                with open('index.txt', 'w') as file:
                    file.write(f'i:{i}, j:{j}')
                file.close()
                
                time.sleep(6)
            page.goto(f"https://www.econodata.com.br/maiores-empresas/pa-belem/restaurantes?pagina={i}")
            time.sleep(3)
            
    except Exception as e:
        print('Erro:', e)
        
    df = pd.DataFrame(dados)
    df.to_excel('dados_empresas.xlsx', index=False)


    browser.close()