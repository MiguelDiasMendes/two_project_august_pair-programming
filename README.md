# Projetos em Python com Tkinter

Este repositório reúne quatro projetos desenvolvidos em Python utilizando principalmente a biblioteca **Tkinter** para criação de interfaces gráficas. Cada aplicação trabalha conceitos diferentes de programação, como manipulação de variáveis, funções, eventos, abas, listas, dicionários, arquivos JSON, mudança de tema e integração com recursos externos.

---

## Projeto 1 — Simulador de Rendas

### Sobre o projeto

O **Simulador de Rendas** é uma aplicação simples para controlar um saldo financeiro. O usuário pode informar um valor e escolher entre realizar um depósito ou um saque.

### Para que serve

O projeto serve como uma introdução à criação de aplicações financeiras simples com interface gráfica, permitindo praticar:

- Variáveis globais;
- Funções;
- Entrada de dados pelo usuário;
- Conversão de texto para números;
- Operações matemáticas;
- Validação de valores;
- Mensagens de aviso e erro;
- Atualização dinâmica de elementos da interface.

### Principais funções

**Depositar:** recebe um valor digitado pelo usuário, verifica se ele é maior que zero e adiciona o valor ao saldo.

**Sacar:** verifica o valor informado e confirma se existe saldo suficiente antes de realizar a retirada.

**Atualizar saldo:** altera o texto exibido na tela para mostrar o saldo atual e limpa o campo de valor.

### Como funciona

A aplicação começa com saldo de **R$ 0,00**. O usuário digita um valor no campo de operação e utiliza um dos dois botões:

- **Depositar (+):** adiciona o valor ao saldo;
- **Sacar (-):** remove o valor do saldo, caso haja saldo suficiente.

Caso o usuário digite um valor inválido, menor ou igual a zero, a aplicação apresenta uma mensagem informativa.

### Tecnologias

- Python
- Tkinter
- `messagebox`

---

# Projeto 2 — Simulador Financeiro Padrão B3

## Sobre o projeto

O **Simulador Financeiro - Padrão B3** é uma versão mais completa do controle financeiro, organizada em três abas: **Conta Corrente, Criptoativos e Extrato**.

O projeto possui uma identidade visual baseada em azul, amarelo e outras cores de destaque, além de utilizar o componente `ttk.Notebook` para organizar as diferentes áreas da aplicação.

### Para que serve

O projeto foi desenvolvido para simular operações financeiras de forma educacional e praticar conceitos mais avançados de interfaces gráficas.

### Funcionalidades

#### Conta Corrente

Permite:

- Consultar o saldo disponível;
- Realizar entradas de dinheiro;
- Realizar saídas ou pagamentos;
- Impedir saques maiores que o saldo disponível;
- Registrar as operações realizadas.

O saldo inicial da aplicação é de **R$ 1.000,00**.

#### Criptoativos

A aplicação possui uma área de simulação de Bitcoin.

A cotação utilizada é fixa:

**1 BTC = R$ 300.000,00**

O usuário pode realizar uma compra simulada de **R$ 100,00 em BTC**, desde que tenha saldo suficiente.

A quantidade de Bitcoin adquirida é calculada automaticamente e adicionada ao saldo de criptoativos.

#### Extrato

Todas as movimentações realizadas são adicionadas a um histórico, incluindo:

- Depósitos;
- Saques/pagamentos;
- Compras de Bitcoin.

O extrato é exibido em uma lista dentro da terceira aba.

### Principais conceitos utilizados

- `ttk.Notebook`;
- Gerenciamento de estado;
- Variáveis globais;
- Listas;
- Funções;
- Validação de dados;
- Cálculos financeiros;
- Atualização dinâmica da interface;
- Componentes `Frame`, `Label`, `Entry`, `Button` e `Listbox`.

### Tecnologias

- Python
- Tkinter
- `ttk`
- `messagebox`

---

# Projeto 3 — História Financeira: Eufrásia Teixeira Leite

## Sobre o projeto

O terceiro projeto apresenta uma aplicação educativa sobre **Eufrásia Teixeira Leite**, utilizando uma interface gráfica com informações históricas organizadas em botões.

O programa também tenta carregar uma imagem de Eufrásia a partir de uma URL externa.

### Para que serve

O objetivo é transformar informações históricas e financeiras em uma aplicação interativa, permitindo que o usuário selecione acontecimentos e visualize detalhes sobre cada um.

### Funcionalidades

A aplicação apresenta eventos históricos como botões. Ao clicar em um evento, uma janela de informação é aberta utilizando `messagebox.showinfo()`.

Entre os eventos apresentados estão:

- **1850 — Nascimento:** informações sobre seu nascimento em Vassouras;
- **1872 — Herança & Europa:** informações sobre a mudança para Paris e gestão da fortuna familiar;
- **1873–1930 — Carteira Global:** informações sobre seus investimentos internacionais;
- **1930 — Legado:** informações sobre seu falecimento e legado;
- **1952 — Herança:** informação sobre a conclusão do inventário;
- **1873 — Relacionamento:** informação apresentada pelo projeto sobre seu relacionamento com Joaquim Nabuco.

### Carregamento da imagem

O programa utiliza uma URL para tentar baixar a imagem.

Para isso, utiliza:

- `requests` para realizar a requisição;
- `io.BytesIO` para trabalhar com os dados recebidos;
- `PIL.Image` para abrir e redimensionar a imagem;
- `ImageTk.PhotoImage` para exibir a imagem no Tkinter.

Caso a imagem não possa ser carregada, o programa apresenta uma mensagem indicando que a foto está indisponível sem internet.

### Principais conceitos utilizados

- Interface gráfica;
- Eventos e botões;
- Dicionários;
- Funções;
- `messagebox`;
- Requisições HTTP;
- Manipulação de imagens;
- Tratamento de exceções com `try/except`.

### Tecnologias

- Python
- Tkinter
- Requests
- Pillow (PIL)

---

# Projeto 4 — Açai da Tia Lu & Co. — Cardápio Digital

## Sobre o projeto

O **Açai da Tia Lu & Co.** é o projeto mais completo dos quatro. Ele funciona como um **cardápio digital com carrinho**, permitindo selecionar produtos, definir quantidades, calcular o valor total e exportar o pedido em formato JSON.

O cardápio é dividido em categorias, como:

- Copos & Tigelas;
- Combos Especiais;
- Sucos & Vitaminas;
- Adicionais Extra.

Os produtos possuem identificador, nome, preço e descrição.

### Para que serve

O projeto simula um sistema de pedidos para uma loja de açaí, permitindo praticar conceitos de programação e desenvolvimento de interfaces mais completas.

### Funcionalidades

#### Cardápio por categorias

Cada categoria é apresentada em uma aba do `ttk.Notebook`.

Os produtos aparecem em cartões contendo:

- Nome;
- Descrição;
- Preço;
- Campo para selecionar a quantidade.

A interface também possui barra de rolagem para permitir a visualização de todos os produtos.

#### Cálculo automático do pedido

O programa verifica a quantidade selecionada de cada produto e calcula o subtotal:

**quantidade × preço**

Depois, soma todos os subtotais para gerar o valor total do pedido.

#### Limpar pedido

O botão **Limpar** redefine todas as quantidades para zero e atualiza o total para **R$ 0,00**.

#### Exportação para JSON

Ao finalizar o pedido, o sistema:

1. Verifica se existe pelo menos um produto selecionado;
2. Cria uma lista com os itens escolhidos;
3. Registra categoria, quantidade, preço unitário e subtotal;
4. Calcula o total geral;
5. Registra data e horário do pedido;
6. Cria um arquivo `.json`;
7. Salva automaticamente o arquivo dentro da pasta `ticket`;
8. Oferece a opção de salvar uma cópia em outro local;
9. Tenta abrir o arquivo diretamente no VS Code.

Os arquivos recebem nomes padronizados com data e horário, por exemplo:

`ticket_20260813_135400.json`

### Modo claro e modo escuro

O sistema possui um botão para alternar entre dois temas visuais:

- **Modo Claro**
- **Modo Escuro**

A troca altera as cores da janela, abas, cartões, textos, campos e rodapé.

### Estrutura dos dados

O cardápio é armazenado em um dicionário chamado `CARDAPIO`.

Cada produto possui informações como:

- `id`;
- `nome`;
- `preco`;
- `desc`.

As quantidades escolhidas são armazenadas em variáveis associadas ao ID de cada produto.

### Principais conceitos utilizados

- Dicionários e listas;
- Funções;
- Variáveis de controle;
- `IntVar`;
- `Spinbox`;
- `Canvas`;
- Barras de rolagem;
- Abas com `ttk.Notebook`;
- Manipulação de arquivos;
- JSON;
- Data e hora;
- `filedialog`;
- `subprocess`;
- Tratamento de exceções;
- Alternância de temas;
- Interface gráfica dinâmica.

### Tecnologias

- Python
- Tkinter
- `ttk`
- JSON
- Pillow não é utilizado neste projeto
- `datetime`
- `filedialog`
- `subprocess`

---

# Comparação dos Projetos

| Projeto | Principal objetivo | Nível de complexidade |
|---|---|---|
| Projeto 1 | Controle simples de saldo | Básico |
| Projeto 2 | Simulação financeira com abas, Bitcoin e extrato | Intermediário |
| Projeto 3 | Aplicação educativa sobre Eufrásia Teixeira Leite | Intermediário |
| Projeto 4 | Cardápio digital com pedidos e exportação JSON | Avançado |

---

# Conclusão

Os quatro projetos demonstram uma evolução no uso do Python e do Tkinter, começando por uma aplicação simples de controle de saldo e avançando para sistemas com múltiplas abas, gerenciamento de estado, integração com recursos externos, manipulação de arquivos JSON e interfaces mais completas.

Em conjunto, os projetos permitem demonstrar conhecimentos de **Python, lógica de programação, programação orientada a eventos, interfaces gráficas, tratamento de erros, manipulação de dados e persistência de informações em arquivos**.
