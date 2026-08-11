# two_project_august_pair-programming

# 🍨 Açaí da Tia Lu & Co. - Cardápio Digital

Uma aplicação desktop simples e intuitiva desenvolvida em **Python** utilizando a biblioteca **Tkinter**. O aplicativo funciona como um PDV (Ponto de Venda) digital para pedidos de açaí, permitindo selecionar produtos, calcular o total em tempo real, alternar temas visuais e exportar o comprovante do pedido no formato **JSON**.

---

## 🚀 Funcionalidades

- **Categorias Organizadas:** Navegação por abas em estilo *Notebook* (Copos & Tigelas, Combos Especiais, Sucos & Vitaminas e Adicionais).
- **Cálculo Automático:** Atualização dinâmica do valor total conforme os itens são adicionados ou removidos via Spinbox.
- **Exportação para JSON:** Gera um ticket detalhado com data, hora, itens e valores.
  - Salva automaticamente na pasta `ticket/` do projeto.
  - Permite ao usuário escolher salvar uma cópia extra em outro diretório.
  - Tenta abrir o ticket diretamente no **VS Code** via terminal.
- **Alternância de Tema (Light/Dark Mode):** Suporte a Modo Claro e Modo Escuro com troca de paleta dinâmica para todos os componentes visuais.
- **Rolagem Suave:** Suporte a rolagem com a roda do mouse (*Scrollwheel*) dentro do menu de produtos.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.x](https://www.python.org/):** Linguagem base do projeto.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html):** Interface gráfica nativa.
- **[JSON](https://docs.python.org/3/library/json.html):** Formatação para exportação dos dados dos pedidos.
- **[Subprocess](https://docs.python.org/3/library/subprocess.html) & [OS](https://docs.python.org/3/library/os.html):** Manipulação de caminhos e execução de comandos do sistema.

---

## 📂 Estrutura de Arquivos Gerada

Ao finalizar um pedido, o aplicativo cria uma pasta `ticket/` na raiz do projeto (caso não exista) e grava o arquivo com a seguinte estrutura:

```text
nome_do_projeto/
│
├── main.py
├── README.md
└── ticket/
    └── ticket_YYYYMMDD_HHMMSS.json

```

---

## 📋 Pré-requisitos

Para executar o projeto, você precisa apenas do **Python 3** instalado na sua máquina, pois todas as bibliotecas utilitárias utilizadas (`tkinter`, `json`, `os`, `subprocess`, `datetime`) fazem parte da biblioteca padrão do Python.

*(Opcional)* Se desejar que o arquivo abra automaticamente após a exportação, certifique-se de ter o [Visual Studio Code](https://code.visualstudio.com/) instalado com o comando `code` configurado no PATH do sistema.

---

## 🖥️ Como Executar

1. **Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/acai-da-tia-lu.git](https://github.com/seu-usuario/acai-da-tia-lu.git)

```


2. **Navegue até o diretório do projeto:**
```bash
cd acai-da-tia-lu

```


3. **Execute o arquivo principal:**
```bash
python main.py

```



---

## 🎨 Paleta de Cores e Temas

O código possui gerenciamento centralizado de temas:

* **Modo Claro:** Tons vibrantes com fundo roxo/amarelo.
* **Modo Escuro:** Visual *Dark Mode* elegante com tons cinza-escuro e detalhes em âmbar/dourado.

```

```
