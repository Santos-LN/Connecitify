# 📱 Connectify – Loja de Smartphones (Projeto Fictício)

**Connectify** é uma empresa fictícia do varejo de smartphones e acessórios, com operações físicas no **Rio de Janeiro** e **São Paulo**, além de presença **online**. Este projeto simula o funcionamento real da empresa utilizando tecnologias como **Python**, **MySQL**, **Excel/CSV** e **Power BI** para criar um modelo completo de Business Intelligence.

---

## 🎯 Objetivo

Demonstrar a aplicação prática dos seguintes conceitos e tecnologias:

- Modelagem de dados relacional
- ETL (Extração, Transformação e Carga) com Python
- Estruturação de banco de dados SQL com chaves estrangeiras
- Criação de dashboards interativos com Power BI conectados ao banco MySQL

---

## 🧱 Modelo Relacional (RDM)

O banco de dados relacional do projeto é composto por **quatro tabelas principais** com os seguintes relacionamentos:

**Relacionamentos:**

- A tabela **VENDAS** se relaciona com:
  - **FUNCIONARIOS** através de `id_funcionario`
  - **PRODUTOS** através de `id_produto`
  - **CANAIS_VENDAS** através de `id_loja`

**Estrutura das tabelas:**

| Tabela         | Colunas                               | Chaves            | Descrição                              |
|----------------|-------------------------------------|-------------------|--------------------------------------|
| **FUNCIONARIOS** | `id_funcionario` (INT, PK)          | PK                | Identificador do funcionário          |
|                | `nome` (VARCHAR)                    |                   | Nome do funcionário                   |
|                | `idade` (INT)                      |                   | Idade do funcionário                  |
|                | `sexo` (ENUM)                      |                   | Sexo do funcionário                   |
|                | `whatsapp` (VARCHAR)               |                   | Contato WhatsApp                      |
| **PRODUTOS**    | `id_produto` (INT, PK)              | PK                | Identificador do produto              |
|                | `produto` (VARCHAR)                |                   | Nome do produto                      |
|                | `valor` (DECIMAL)                  |                   | Preço do produto                      |
| **CANAIS_VENDAS** | `id_loja` (INT, PK)                 | PK                | Identificador do canal/loja           |
|                | `endereco` (VARCHAR)               |                   | Endereço da loja/canal                |
|                | `telefone` (VARCHAR)               |                   | Telefone de contato                   |
| **VENDAS**      | `id_venda` (INT, PK)                | PK                | Identificador da venda                |
|                | `data_venda` (DATE)                |                   | Data da venda                        |
|                | `id_produto` (INT, FK)             | FK → PRODUTOS     | Produto vendido                      |
|                | `id_funcionario` (INT, FK)         | FK → FUNCIONARIOS | Funcionário que realizou a venda      |
|                | `id_loja` (INT, FK)                | FK → CANAIS_VENDAS | Canal/loja onde ocorreu a venda      |

---

## 💻 Tecnologias Utilizadas

- **Python** (com pandas para manipulação e tratamento de dados)
- **MySQL** (banco de dados relacional para armazenamento estruturado)
- **Power BI** (ferramenta de Business Intelligence para criação de dashboards e relatórios)
- **Excel e CSV** (formatos para exportação e manipulação intermediária dos dados)
- **GitHub** (controle de versão e hospedagem do código e documentação)

---

## ⚙️ Etapas Técnicas Desenvolvidas

- Criação e manipulação de DataFrames em Python para dados de vendas, funcionários, produtos e canais
- Leitura e limpeza dos dados brutos, incluindo conversão de colunas de datas para o formato adequado
- Realização de merges entre DataFrames para composição da base final unificada (`df_connectify`)
- Exportação dos dados tratados para arquivos Excel (.xlsx) e CSV
- Criação das tabelas no banco MySQL com definição das chaves primárias e estrangeiras
- Importação dos arquivos Excel/CSV para as respectivas tabelas MySQL
- Estabelecimento da conexão entre Power BI e o banco de dados MySQL para consulta direta
- Desenvolvimento de visualizações e indicadores no Power BI para análise e tomada de decisão

---

## 📊 Insights Extraídos

- Identificação dos **produtos mais vendidos**
- Ranking dos **funcionários com maior volume de vendas**
- Comparativo entre desempenho das **lojas físicas** e canal **online**
- Evolução mensal das vendas com análise temporal
- Cálculo do ticket médio por canal de venda para avaliação da performance

---

## 👤 Autor

**Lucas Santos**  
Desenvolvedor focado em dados, SQL, Python e Business Intelligence.

- [LinkedIn](https://www.linkedin.com/in/lucass-dados)  
- [GitHub](https://github.com/Santos-LN)

