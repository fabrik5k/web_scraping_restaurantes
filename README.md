# 📊 Projeto de Web Scraping e Geolocalização de Restaurantes em Belém do Pará

Este projeto realiza **web scraping** no site **EconoData** para coletar dados públicos sobre empresas de restaurantes localizadas em **Belém do Pará**. Além disso, gera um **mapa geográfico** utilizando as coordenadas obtidas por meio da API gratuita do **Nominatim** (OpenStreetMap) com a biblioteca **Geopy**.

## 📋 **Índice**

1. [Objetivo do Projeto](#objetivo-do-projeto)  
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
3. [Funcionamento do Projeto](#funcionamento-do-projeto)  
4. [Limitações](#limitações)  
5. [Como Executar o Projeto](#como-executar-o-projeto)  
6. [Resultados](#resultados)  
7. [Contribuições](#contribuições)  
8. [Licença](#licença)

---

## 🎯 **Objetivo do Projeto**

- Extrair dados públicos de empresas do setor de restaurantes na cidade de **Belém do Pará** usando web scraping.  
- Obter informações detalhadas como: **nome da empresa, endereço, razao social, CNPJ, e situacao**.  
- Geocodificar os endereços para obter **coordenadas geográficas (latitude e longitude)**.  
- Visualizar os dados coletados em um **mapa interativo** gerado com as coordenadas.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python**: Linguagem principal do projeto.  
- **playwright**: Biblioteca para fazer o scraping dos dados.  
- **Pandas**: Para manipulação e organização dos dados em tabelas.  
- **Geopy**: Para geocodificar os endereços usando a API do Nominatim (OpenStreetMap).  
- **Folium**: Para criar o mapa interativo com os dados coletados.  
- **Jupyter Notebook** *(opcional)*: Para documentação e execução interativa do código.

---

## ⚙️ **Funcionamento do Projeto**

1. **Coleta de Dados**:  
   - O script realiza scraping no site **EconoData**, coletando informações públicas sobre restaurantes em Belém do Pará.  
   - Dados coletados incluem:  
     - **Nome da Empresa**  
     - **Endereço Completo**  
     - **CNPJ**  
     - **Razao Social**
     - **Situacao**

2. **Geocodificação**:  
   - Os endereços coletados são convertidos em coordenadas geográficas (latitude e longitude) usando a API do **Nominatim** via biblioteca **Geopy**.  
   - Devido à limitação de uso da API (1 requisição por segundo), o processo inclui uma pausa entre as requisições para evitar bloqueios.

3. **Visualização no Mapa**:  
   - Utilizando a biblioteca **Folium**, os dados são plotados em um **mapa interativo**, mostrando a localização dos restaurantes coletados.

---

## 🚧 **Limitações**

- **Limite da API do Nominatim**:  
  - O Nominatim possui um limite de **1 requisição por segundo** para o serviço gratuito.  
  - Para grandes volumes de dados, esse processo pode ser demorado.  

- **Dependência do Site EconoData**:  
  - Mudanças no site podem quebrar o script de scraping.  
  - Sempre verifique a política de uso do site para garantir conformidade com os termos.

---

## 🚀 **Como Executar o Projeto**

1. **Clone o Repositório**:

   \`\`\`bash
   git clone https://github.com/seu-usuario/nome-do-projeto.git
   cd nome-do-projeto
   \`\`\`

2. **Instale as Dependências**:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Execute o Script**:

   \`\`\`bash
   python scraper.py
   \`\`\`

4. **Visualize o Mapa**:  
   - Após a execução, o mapa será salvo como um arquivo **HTML** (por exemplo, `mapa_restaurantes.html`).  
   - Abra o arquivo no navegador para visualizar os pontos no mapa.

---

## 📈 **Resultados**

Exemplo de dados coletados:

| **Nome**                  | **Razao Social**          | **CNPJ**            | **Situacao** | **Logadouro**        | **Bairro**       | **Municipio/UF** | **CEP**    | **Coordenadas**    |
|----------------------------|---------------------------|---------------------|--------------|---------------------|-----------------|------------------|------------|-------------------|
| Restaurante Sabor do Pará | Sabor do Pará Ltda.       | 12.345.678/0001-00  | Ativa        | Rua Exemplo, 123    | Batista Campos  | Belém/PA         | 66015-000  | -1.4556, -48.4902 |


**Mapa Exemplo**:  
![Mapa de Restaurantes](link_para_imagem_exemplo)

---

## 🤝 **Contribuições**

Contribuições são bem-vindas! Se quiser contribuir:

1. Faça um **fork** do projeto.  
2. Crie uma nova **branch**: `git checkout -b minha-branch`  
3. Faça as suas alterações e adicione commits: `git commit -m "Minha contribuição"`  
4. Envie um **pull request**.

---

## 📝 **Licença**

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

**Autor**: [Seu Nome](https://github.com/seu-usuario)  

---

### 🌟 **Agradecimentos**

- **OpenStreetMap** pelo serviço gratuito de geocodificação.  
- **EconoData** por disponibilizar dados públicos.  
- Comunidade de desenvolvedores e mantenedores das bibliotecas utilizadas.
