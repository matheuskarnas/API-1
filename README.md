<div align="center">
    <img src="./src/app/front/static/images/debuggers.png">
</div>

# Índice

- [Objetivo do Projeto](#objeto-do-produto)
- [Vídeos e Apresentações](#vídeos-e-apresentações)
- [Backlog do Produto](#backlog-do-produto)
- [Backlog da Sprint](#backlog-da-sprint)
- [Autores](#autores)

# Objetivo do Projeto

Oferecer aos eleitores dados claros e acessíveis que ajudem a tomar decisões informadas nas eleições municipais
que se aproximam. A plataforma permitirá que os cidadãos visualizem a atuação dos vereadores, incluindo:

1. Presença nas Sessões: Percentual de presença e faltas, justificadas ou não.
2. Proposições Apresentadas: Projetos de lei, requerimentos e moções que o vereador apresentou
durante o mandato.
3. Projetos de Lei Aprovados: Detalhamento das propostas aprovadas, com links para o conteúdo
completo.
4. Posicionamento em Votações: Como o vereador votou em questões-chave.
5. Participação em Comissões: Informações sobre o envolvimento do vereador em comissões
especiais e permanentes

# Vídeos e Apresentações

## Sprint 1

### Objetivo da Sprint
Criar as páginas do site e sua estrutura permitindo a navegação entre elas

[![MVP - Sprint 1](https://img.youtube.com/vi/En5hxTBmlNE/0.jpg)](https://youtu.be/En5hxTBmlNE)

## Sprint 2

### Objetivo da Sprint
Adicionar Tailwind para deixar as páginas resposivas e começar a integração das páginas com o banco de dados

[![MVP - Sprint 2](https://img.youtube.com/vi/xRuLMWFXutc/0.jpg)](https://youtu.be/xRuLMWFXutc)

## Tecnologias

<div align="center">
  <table>
  <tr>
    <td align="center" width="96">
      <img src="documentation/images/html5.svg" width="48" height="48" alt="HTML" />
      <span>HTML</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/css3.svg" width="48" height="48" alt="CSS" />
      <span>CSS</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/figma.svg" width="48" height="48" alt="Figma" />
      <span>Figma</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/python.svg" width="48" height="48" alt="Python" />
      <span>Python</span>
     </td>
    <td align="center" width="96">
      <img src="documentation/images/github.png" width="48" height="48" alt="GitHub" />
      <span>GitHub</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/mysql.png" width="48" height="48" alt="MySQL" />
      <span>MySQL</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/flask.svg" width="48" height="48" alt="Flask"/>
      <span>Flask</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/discord.png" width="48" height="48" alt="Discord"/>
      <span>Discord</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/jira.png" width="48" height="48" alt="Jira"/>
      <span>Jira</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/jupyter.svg" width="48" height="48" alt="Jira"/>
      <span>Jupyter</span>
    </td>
    <td align="center" width="96">
      <img src="documentation/images/tailwind.png" width="48" height="48" alt="Jira"/>
      <span>Tailwind</span>
    </td>
  </tr>
</table>
</div>

# Backlog do produto

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #ddd;">Requisito</th>
            <th style="border: 1px solid #ddd;">User Story</th>
            <th style="border: 1px solid #ddd;">Prioridade</th>
            <th style="border: 1px solid #ddd;">Estimativa</th>
            <th style="border: 1px solid #ddd;">Sprint</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd;">Lista completa de todos os vereadores atuais</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar uma lista completa de todos os vereadores em atuação.</td>
            <td style="border: 1px solid #ddd;">Alta</td>
            <td style="border: 1px solid #ddd;">1</td>
            <td style="border: 1px solid #ddd;">1</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Perfil individual de cada vereador</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar o perfil individual de cada vereador, sendo que neste perfil deverá conter: dados biográficos, histórico político, presença nas sessões, proposições apresentadas, Projetos de Lei aprovados, posicionamento em votações, participação em comissões.</td>
            <td style="border: 1px solid #ddd;">Alta</td>
            <td style="border: 1px solid #ddd;">8</td>
            <td style="border: 1px solid #ddd;">1</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Painel de estatísticas</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar um painel de estatísticas contendo a atuação geral de cada vereador na Câmara, comparando o desempenho entre eles.</td>
            <td style="border: 1px solid #ddd;">Média</td>
            <td style="border: 1px solid #ddd;">5</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Presença nas Sessões</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar o percentual de presença de cada vereador nas sessões da Câmara e, caso existam faltas, se estas foram justificadas e qual foi a justificativa.</td>
            <td style="border: 1px solid #ddd;">Baixa</td>
            <td style="border: 1px solid #ddd;">3</td>
            <td style="border: 1px solid #ddd;">2</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Participação em Comissões</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar a participação de cada vereador nas comissões, com destaque para a forma como cada um se manifestou nas comissões especiais e permanentes.</td>
            <td style="border: 1px solid #ddd;">Média</td>
            <td style="border: 1px solid #ddd;">3</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Proposições apresentadas</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar os Projetos de Lei, requerimentos e moções que cada vereador apresentou durante o seu mandato.</td>
            <td style="border: 1px solid #ddd;">Média</td>
            <td style="border: 1px solid #ddd;">5</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Projetos de Lei aprovados</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar os Projetos de Lei aprovados de cada vereador e o detalhamento das propostas aprovadas, com acesso ao conteúdo completo.</td>
            <td style="border: 1px solid #ddd;">Baixa</td>
            <td style="border: 1px solid #ddd;">5</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Posicionamento em votações</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar o posicionamento de cada vereador nas votações de questões-chave para o município.</td>
            <td style="border: 1px solid #ddd;">Baixa</td>
            <td style="border: 1px solid #ddd;">3</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Ferramenta de busca e filtros</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de um recurso que permitisse buscar o perfil de cada vereador por nome, partido e atuação em temas específicos.</td>
            <td style="border: 1px solid #ddd;">Baixa</td>
            <td style="border: 1px solid #ddd;">5</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Informação sobre reeleição de vereadores</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de saber quais vereadores estão se reelegendo.</td>
            <td style="border: 1px solid #ddd;">Média</td>
            <td style="border: 1px solid #ddd;">1</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Feedback do eleitorado</td>
            <td style="border: 1px solid #ddd;">Eu, como cidadão, gostaria de visualizar comentários relevantes do eleitorado sobre cada vereador, assim como a classificação atribuída a cada um deles.</td>
            <td style="border: 1px solid #ddd;">Baixa</td>
            <td style="border: 1px solid #ddd;">3</td>
            <td style="border: 1px solid #ddd;">3</td>
        </tr>
    </tbody>
</table>

# Backlog da Sprint

## Sprint 1

- Criar repositório no GitHub
- Padronizar pastas do GitHub
- Backlog do Produto
- Validação do Backlog do Produto
- Criação do Jira
- Criar wireframes
- Validar wireframes
- Raspagem de dados - Estudo
- Raspagem de dados
- Modelagem do banco de dados
- Script do banco de dados
- Página Home
- Página Informativa
- Página Comparação
- Modal

## Sprint 2

- Adicionar TailwindCSS
- Adicionar Tailwind na página Home
- Deixar a página Home responsiva
- Adicionar Tailwind na página Perfil
- Deixar a página Perfil responsiva
- Adicionar Tailwind na página Comparação
- Deixar a página Comparação responsiva
- Coletar informções sobre os vereadores
- Finalizar o Banco de Dados
- Implementar Tailwind no Header
- Estudar/escolher biblioteca de gráficos
- Continuar raspagem

# Autores

| Foto | Função |Nome |                                                                                                                                                    LinkedIn & GitHub                                                                                                                                                    |
| :---------: | :-----------: | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="./documentation/integrantes/lucasm.jpg" width=50px> | Product Owner | Lucas Martins |        [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)]() [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/LucasMSCarmo)        |
| <img src="./documentation/integrantes/matheus.jpg" width=50px> | Scrum Master  | Matheus Karnas   |    [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/matheuskarnas/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/matheuskarnas)    |
| <img src="./documentation/integrantes/marcos.jpg" width=50px> |  Scrum Team  | Marcos Yudi    |    [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/antonio-nepomuceno-04943720a/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/marcosyudi)    |
| <img src="./documentation/integrantes/julia.jpg" width=50px> |  Scrum Team  | Julia Rosa    |       [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/julia-da-rosa-silva-26455bb0/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/juliaroosas)        |
| <img src="./documentation/integrantes/victor.jpg" width=50px> |  Scrum Team  | Victor Chagas   | [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)]() [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/victorchagas-93) |
| <img src="./documentation/integrantes/lucasa.jpg" width=50px> |  Scrum Team  | Lucas Araujo   |         [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lucas-araujo-448115329/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/LucasAraujo1016)          |
| <img src="./documentation/integrantes/gabriel.jpg" width=50px> |  Scrum Team  | Gabriel Robert   |         [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)]() [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/LittleRob120)          |
| <img src="./documentation/integrantes/pedro.jpg" width=50px> |  Scrum Team  | Pedro Rosa   | [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)]() [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/PedHr) |
| <img src="./documentation/integrantes/thomaz.jpg" width=50px> |  Scrum Team  | Thomaz Feitosa   | [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)]() [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/PedHr) |
