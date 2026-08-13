
---

# 🐍 Projetos Educacionais em Python - Finanças, História e Sistemas

Este repositório reúne quatro aplicações gráficas desenvolvidas em **Python** utilizando a biblioteca **Tkinter**. Os projetos foram elaborados com foco didático para alunos de programação, integrando conceitos de **programação procedural**, **educação financeira**, **história do Brasil** e **manipulação de dados com JSON**.

---

## 🎯 Objetivos Didáticos

* **Lógica Procedural & Estado:** Estruturação de código procedural facilitando a assimilação inicial de funções, parâmetros, variáveis globais (`global`) e gerenciamento de estado.
* **Interface Gráfica (GUI):** Construção de telas interativas com `tkinter` e componentes modernos (`ttk.Notebook`, `Canvas`, `Listbox`, `Spinbox`, alternância de temas claro/escuro).
* **Tratamento de Exceções & Validação:** Uso de blocos `try/except` para validação de entradas do usuário e prevenção de saques ou compras sem saldo.
* **Recursos Externos & Persistência:** Requisições HTTP (`requests`), manipulação de imagens (`Pillow`) e exportação/persistência de dados em arquivos `.json`.

---

## 🚀 Projetos Incluídos

### 1. 💵 Simulador de Rendas (`projeto1_simulador_rendas.py`)

Aplicação introdutória de fluxo de caixa para controle de saldo financeiro simples.

* **Destaques:**
* Controle e atualização dinâmica de saldo em tempo real.
* Validação de entradas para evitar valores nulos ou saques sem saldo.
* Uso de mensagens de aviso com `messagebox`.



---

### 2. 📊 Dashboard Financeiro - Padrão B3 (`projeto2_simulador_b3.py`)

Um painel financeiro completo com identidade visual inspirada na B3, organizado em abas interativas.

* **Destaques:**
* Uso de `ttk.Notebook` para abas de **Conta Corrente**, **Criptoativos** e **Extrato**.
* Simulação de compra de frações de Bitcoin (BTC).
* Histórico de transações em tempo real utilizando `Listbox`.



---

### 3. 📜 Linha do Tempo: Eufrásia Teixeira Leite (`projeto3_eufrasia_teixeira.py`)

Uma aplicação educativa sobre **Eufrásia Teixeira Leite** (1850–1930), a primeira investidora global do Brasil.

* **Destaques:**
* Download e exibição de imagem via requisição HTTP (`requests` e `PIL`/`Pillow`).
* Tratamento de falhas de conexão para manter a aplicação funcional mesmo offline.
* Botões interativos para exibição de acontecimentos históricos.



---

### 4. 🫐 Açai da Tia Lu & Co. — Cardápio Digital (`projeto4_cardapio_acai.py`)

Sistema de pedidos para loja de açaí, atuando como um cardápio digital completo com carrinho e geração de comprovantes.

* **Destaques:**
* Navegação por categorias em abas e cartões de produtos dinâmicos com `Canvas` e barra de rolagem.
* Alternância dinâmica entre **Modo Claro** e **Modo Escuro**.
* Exportação de pedidos com data e hora para arquivos `.json` salvos na pasta `ticket/` e integração com VS Code.



---

## 📊 Comparação dos Projetos

| Projeto | Principal Objetivo | Conceitos-Chave | Nível |
| --- | --- | --- | --- |
| **Projeto 1** | Simulador de Rendas | Variáveis globais, `messagebox`, validação simples | Básico |
| **Projeto 2** | Dashboard B3 | `ttk.Notebook`, abas, `Listbox`, simulação financeira | Intermediário |
| **Projeto 3** | História: Eufrásia | Requisições HTTP, `Pillow`, tratamento de exceções, dicionários | Intermediário |
| **Projeto 4** | Cardápio Digital | Exportação JSON, `Canvas`, temas (Light/Dark), `datetime`, `filedialog` | Avançado |

---

## 🛠️ Pré-requisitos e Instalação

Para executar os projetos, você precisará do **Python 3.10+** instalado em sua máquina.

### 1. Instalar as dependências do projeto

Abra o terminal ou prompt de comando e execute:

```bash
pip install requests pillow

```

ou

```bash
python -m pip install requests pillow

```

> **Nota:** O `tkinter` já vem instalado por padrão na maioria das instalações do Python para Windows/macOS. Caso esteja utilizando Linux (Ubuntu/Debian), instale-o via terminal:
> `sudo apt-get install python3-tkinter`

---

## 💻 Como Executar as Aplicações

Navegue até a pasta do projeto no seu terminal e rode o arquivo desejado:

```bash
# Executar o Simulador de Rendas
python projeto1_simulador_rendas.py

# Executar o Dashboard Financeiro B3
python projeto2_simulador_b3.py

# Executar a Aplicação do Eufrásia Teixeira Leite
python projeto3_eufrasia_teixeira.py

# Executar o Cardápio Digital Açai da Tia Lu
python projeto4_cardapio_acai.py

```

---

## 🗂️ Estrutura do Repositório

```text
.
├── projeto1_simulador_rendas.py   # Aplicação simples de depósitos e saques
├── projeto2_simulador_b3.py       # Dashboard financeiro com abas e extrato (B3)
├── projeto3_eufrasia_teixeira.py  # Aplicação educativa sobre Eufrásia Teixeira Leite
├── projeto4_cardapio_acai.py      # Cardápio digital com suporte a temas e exportação JSON
├── ticket/                        # Pasta gerada automaticamente para os comprovantes JSON
└── README.md                      # Documentação dos projetos

```

---

💙 *Projetos desenvolvidos para fins educacionais, capacitação profissional e prática de lógica de programação.*
