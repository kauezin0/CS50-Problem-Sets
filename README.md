# 🏅 CS50 – Problem Sets

Este repositório contém ALGUNS dos exercícios do curso CS50
(Obs.: Na maioria dos exercícios, foi utilizado o inglês nos comentários e na descrição do README, para que os avaliadores do CS50 consigam entender.) 

# Exercícios

# 1. Scratch

Introdução à lógica de programação com sequências de comandos, loops e condições.

Arquivo: Trying to Get to Julia's House_Scratch.sb3

# 2. Cash.c

Programa em C para calcular o troco mínimo.

Pratica loops, condicionais e manipulação de variáveis.

Arquivo: cash.c

# 3. MarioLess

Construção de pirâmides no terminal.

Exercita loops aninhados e padrões de saída formatada.

Arquivo: mario.c

# 4. Scrabble

Programa em C que simula o jogo Scrabble, atribuindo pontuações às palavras digitadas pelos jogadores com base nas letras utilizadas.

Exercita o uso de arrays, loops, condicionais, funções e manipulação de strings.

Arquivo: scrabble.c

# 5. Readability

Programa em C que calcula o nível de leitura de um texto usando o índice Coleman-Liau.
Analisa o número de letras, palavras e frases para estimar o grau escolar necessário para compreender o texto.

Exercita manipulação de strings, contagem de caracteres, expressões matemáticas e estruturas condicionais.

Arquivo: readability.c

# 6. Caesar

Programa em C que implementa a cifra de César, um método clássico de criptografia.
O usuário fornece uma chave numérica, e o programa aplica um deslocamento nas letras do texto, gerando a mensagem criptografada.

Exercita manipulação de strings, funções, conversão de caracteres, loops, argumentos de linha de comando e criptografia básica.

Arquivo: caesar.c

# 7. Runoff

Programa em C que simula um sistema de votação por turno instantâneo (runoff).
Os eleitores classificam os candidatos por preferência, e o programa elimina o candidato com menos votos a cada rodada, redistribuindo os votos até que haja um vencedor.

Exercita arrays, matrizes, loops aninhados, estruturas condicionais, funções, comparação de strings e lógica de algoritmos.

Arquivo: runoff.c

# 8. Speller

Programa em C que verifica a ortografia de palavras a partir de um dicionário.
Neste exercício, foi implementada apenas a parte solicitada pelo CS50, focando na criação das funções responsáveis por carregar o dicionário, verificar palavras, calcular o tamanho e liberar a memória.

Exercita estruturas de dados, tabelas hash, manipulação de strings, ponteiros, alocação e liberação de memória, além de análise de desempenho.

Pasta: speller/

# 9. Recover

Programa em C que recupera arquivos de imagem (JPEG) a partir de um cartão de memória.
Neste exercício, foi implementada apenas a parte solicitada pelo CS50, focando na leitura de blocos de dados, identificação das assinaturas de arquivos JPEG e escrita dos arquivos recuperados no disco.

Exercita manipulação de arquivos, leitura binária, ponteiros, buffers, controle de fluxo e uso de estruturas básicas em C.

Pasta: recover/

# 10. Homepage

Projeto de site pessoal desenvolvido com HTML, CSS e JavaScript, com o objetivo de praticar conceitos básicos de desenvolvimento web.
Inclui estruturação de páginas, estilização visual e interatividade simples com o usuário.

Exercita HTML semântico, CSS, JavaScript, organização de arquivos, design básico e fundamentos de front-end.

Pasta: homepage/

# 11. Finance

Aplicação web desenvolvida com Python (Flask), SQL, HTML e CSS que simula uma plataforma de compra e venda de ações.
Neste exercício, foi implementada apenas a parte solicitada pelo CS50, focando na lógica do backend, manipulação do banco de dados, autenticação de usuários e processamento das transações.

Exercita desenvolvimento web, Flask, SQL, integração entre frontend e backend, autenticação, manipulação de dados e boas práticas de programação.

Pasta: finance/

# Descrição do Projeto Final

Este projeto é uma aplicação web desenvolvida com Flask, Python, SQL, HTML, CSS e Bootstrap, focada em autenticação de usuários e busca de jogos de forma segura e organizada.

No arquivo helpers.py, foi implementada a função login_required, responsável por proteger rotas sensíveis da aplicação, garantindo que determinadas ações só possam ser realizadas por usuários autenticados.
O banco de dados games.db armazena informações dos jogos e dos usuários, utilizando hash de senhas para maior segurança.

No app.py, são utilizados recursos essenciais do Flask, SQL e werkzeug.security. A função after_request foi implementada para impedir o cache do navegador, evitando que páginas sensíveis possam ser acessadas após o logout, aumentando a segurança da aplicação.

A autenticação utiliza generate_password_hash e check_password_hash, garantindo que as senhas reais não sejam armazenadas no banco de dados.
O frontend foi desenvolvido com Bootstrap, adotando um tema escuro com estética gamer. A página principal utiliza Flexbox para alinhamento preciso dos elementos e consultas SQL com LIKE para tornar a busca mais flexível.

A página de resultados exibe capas dos jogos, horas de gameplay e nível de dificuldade. As imagens são vinculadas automaticamente aos jogos por meio de IDs do banco de dados e renderizadas com Jinja2.
Em caso de erros, a página apology.html fornece feedback visual claro ao usuário por meio de alertas do Bootstrap.

# Estrutura do Projeto

app.py: Controlador principal da aplicação Flask, responsável pelas rotas, autenticação e consultas ao banco de dados.

helpers.py: Funções auxiliares, incluindo o decorator login_required.

games.db: Banco de dados SQLite com tabelas de usuários e jogos.

static/img/: Armazena as capas dos jogos, nomeadas conforme o ID do banco de dados.

templates/layout.html: Estrutura base do site (navbar e layout geral).

templates/index.html: Página inicial com barra de busca e layout responsivo.

templates/busca.html: Exibição dos resultados da busca com informações detalhadas dos jogos.

templates/login.html & register.html: Formulários de autenticação e registro de usuários.

templates/apology.html: Página de erros com mensagens amigáveis ao usuário.

# ⚠️ Como rodar os programas em C

Estes programas utilizam a biblioteca CS50 (cs50.h). Para compilar e executar:

# Opção 1 – Usando CS50 IDE

Abra o CS50 IDE
.

Clone este repositório no IDE.

Compile e execute normalmente.

# Opção 2 – Instalar CS50 Library localmente

macOS: brew install cs50

Linux: sudo apt install libcs50-dev

Compile usando:

clang -o cash cash.c -lcs50
./cash

# Habilidades Desenvolvidas

.Lógica de programação

.Linguagem C

.Scratch

.Loops e loops aninhados

.Condicionais

.Resolução de problemas
