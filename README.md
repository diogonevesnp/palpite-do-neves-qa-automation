## $\color{#4ac565}{\textsf{\textbf{🚀 AUTOMAÇÃO DE TESTES - PALPITE DO NEVES}}}$

>Projeto de automação de testes end-to-end (E2E) desenvolvido para validar as funcionalidades do web app **Palpite do Neves**, focado em garantir a estabilidade das previsões e navegação.

<h2 style="color: #4ac5b9;">🛠️ Tecnologias Utilizadas</h2>

* **Linguagem:** Python 3.12
* **Framework de Teste:** Pytest
* **Ferramenta de Automação:** Playwright

<h2 style="color: #4ac5b9;">💻 Ambiente de Testes</h2>

>Para garantir a qualidade em diferentes cenários, esta automação foi validada na seguinte infraestrutura:

* **Sistemas Operacionais:** Windows 11
* **Navegadores (Browsers):** 
    * Google Chrome
    * Microsoft Edge 
    * Mozilla Firefox
    * Safari (WebKit)
* **Resoluções:** Desktop (1920x1080)



<h2 style="color: #4ac5b9;">📋 Cenários de Teste Automatizados (Gherkin)</h2>

>Abaixo estão os fluxos principais validados nesta automação:

### Funcionalidade: Filtros de Palpites Por Data
**Cenário:** Validar carregamento de palpites do dia anterior dia atual e do próximo dia.

* **Dado** que acesso a página inicial
* **Quando** clico no filtro "Hoje"
* **Então** palpites devem ser exibidos do dia atual.

###
* **Dado** que acesso a página inicial
* **Quando** clico no filtro "Ontem"
* **Então** palpites devem ser exibidos com os resultados passados.

###
* **Dado** que acesso a página inicial
* **Quando** clico no filtro "Amanhã"
* **Então** palpites devem ser exibidos caso horário sejá após 21:00.

**Cenário:** Palpites não exibidos

* **Dado** que acesso a página inicial
* **Quando** clico no filtro "Hoje"
* **Então** palpites não devem ser exibidos.

###
* **Dado** que acesso a página inicial
* **Quando** clico no filtro "Ontem"
* **Então** palpites não devem ser exibidos com os resultados passados.

###
* **Dado** que acesso a página inicial
* **Quando** clico no filtro "Amanhã"
* **Então** palpites não devem ser exibidos em nehum horário.

<h2 style="color: #4ac5b9;">📋 Cenários de Teste Automatizados (Gherkin)</h2>

| Cenário de Teste | Status | Último Erro Detectado | Prioridade | Data |
| :--- | :--- | :--- | :--- | :--- |
| Filtro "Hoje": Exibição de palpites atuais | ✅ Passou | - | Alta | 18/01/2026 |
| Filtro "Ontem": Busca de resultados | ✅ Passou| - | Alta | 18/01/2026 |
| Filtro "Amanhã": Exibição de próximos palpites | ✅ Passou | - | Alta | 18/01/2026 |
|**⚠️ Cenário:** Palpites não exibidos | ⚠️ | | ⚠️ | ⚠️⚠️⚠️⚠️ |
| Filtro "Hoje": Não exibir palpites atuais | ✅ Passou | - | Alta | 18/01/2026 |
| Filtro "Ontem": Não exibir resultados | ✅ Passou| - | Alta | 18/01/2026 |
| Filtro "Amanhã": Não exibir próximos palpites | ✅ Passou | - | Alta | 18/01/2026 |

---

### Funcionalidade: Aba de Notícias
**Cenário:** Verificar navegação completa na aba de notícias
* **Dado** que estou na aba principal Home
* **Quando** navego até a aba de notícias
* **Então** devo conseguir ler os títulos e acessar os detalhes das matérias.

###
**Cenário:** Válidação do card de enquetes da semana
* **Dado** que estou na aba principal Home
* **Quando** navego até a aba de notícias
* **Então** não devo conseguir votar e ser redirecionado para criar conta ou fazer login

**Cenário:** Verificar visibilidade do card de curiosidades do futebol
* **Dado** que estou na aba principal Home
* **Quando** navego até a aba de notícias
* **Então** devo conseguir vizualizar o card e ler o título Curiosidades do Futebol.

###
**Cenário:** Verificar navegação nos ícones de rede sociais
* **Dado** que estou na aba principal Home
* **Quando** navego até a aba de notícias
* **Então** devo conseguir pasar o mause e ler o texto abaixo de cada ícone.

###
**Cenário:** Verificar cards de casa de apostas e redirecionamento correto
* **Dado** que estou na aba principal Home
* **Quando** navego até a aba de notícias
* **Então** ao clicar no botão do card devo ser redirecionado para a casa de apostas

<h2 style="color: #4ac5b9;"> 📊 Status de Qualidade Funcionalidade: Aba de Notícias</h2>

| Cenário de Teste | Status | Último Erro Detectado | Prioridade | Data |
| :--- | :--- | :--- | :--- | :--- |
| Carregamento dos cards de notícias | ✅ Passou | - | Alta | 18/01/2026 |
| Abertura de notícia | ✅ Passou | - | Alta | 18/01/2026 |
| Card de enquete da semana | ✅ Passou | - | Alta | 18/01/2026 |
| Card de curiosidades do futebol | ✅ Passou | - | Média | 18/01/2026 |
| Mensagem dos íncones de redes sociais | ✅ Passou | - | Média | 18/01/2026 |
| Card de casas de apostas e redirecionamento | ✅ Passou | - | Alta | 18/01/2026 |


>Testes negativos para a aba "Notícias" em andamento.

<h2 style="color: #4ac5b9;"> 📊 Status de Qualidade Geral do Projeto</h2>

| Funcionalidade | Status | Último Erro Detectado | Prioridade | Data |
| :--- | :--- | :--- | :--- | :--- |
| Filtro de Palpites Por Data | ✅ Aprovado | - | Alta | 18/01/2026 |
| Análise Detalhada dos Palpites | ✅ Aprovado | - | Alta | 18/01/2026 |
| Aba Notícias | ✅ Aprovado | - | Alta | 18/01/2026 |

>O projeto está com suporte para rodar no emulador para dispositivos mobile e difrentes sistemas operacionais, porém optei em realizar os testes apenas em desktop no momento.

<h2 style="color: #4ac5b9;"> 📅 Status do Projeto</h2>

* **Última atualização dos scripts:** 18/01/2026
* **Versão da Automação:** v1.0.0
