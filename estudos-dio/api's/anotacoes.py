# Introdução a desenvolvimento web
# É o processo de criação de web sites e aplicações na internet(informações públicas) e na intranet(inforamções privadas)
# Nas empresas pode ter pessoas com funções sobrecarregadas, dependendo do conhecimento do profissional, ele pode ficar com mais de uma função ou ficar com uma por inteiro.
# Na web temos o desenvolvimento front-end: Tudo que o usuário vai ver e interagir, é usado o HTML, CSS e JavaScript
# Já no desenvolvimento back-end, é o chamado "bastidor" que é a lógica, controle de servidor de um site e processamento de dados. Feito geralmente em Python, Java, PHP, JavaScript, etc...
# 20%  DE UMA APLICAÇÃO É FRONT END, JÁ 80% É O BACK-END. (não é geral, mas a maioria é desse jeito, bom, segundo o que eu entendi hahahah :P)

# Como a web funciona?
# A internet é uma rede global de computadores interconectados, já a web (Word Wide Web) transmite dados, sendo um sistema de informação construído sob a internet, construido no protocolo HTTP
# HTTP (Hypertext Transfer Protocol) é o prótocolo fundamental da web, quando um usuário acessa um site, é enviada uma solicitação HTTP ao servidor do site, respondendo com os dados do site, sendo assim, serve para transferência de dados.
# A url (domínio) quando usada para acessar um site, é traduzida pelo DNS (Domain Name System) pelo ip do servidor que hospeda o site, processando a solicitação HTTP, enviando de volta os dados em forma de HTML, CSS E JavaScript, no final o navegador interpreta os arquivos e exibe ao usuário.
# Também tem outras tecnologias envolvidas na web como o TLS/SSL (segurança), achei bacana nisso que descobri o porque do HTTPS, pois esse s vem do TLS, que faz a criptografia da circulação de dados. E também API's para o gerenciamento e aramazenamento de banco de dados e interatividade.

# API - Conceitos fundamentais
# Conjunto de regra ou definições que permite diferentes aplicações de softwares ou componentes se comuniquem entre si, é como se fosse o intermediário desse rebolation todo. É importante para a flexbilidade e facilitar o desenvolvimento de funcionalidades da aplicação.

# Tipos de API
# RESTful: É uma API que trabalha com os príncipios do REST(Representational State Transfer). Baseada em padrões HTTP e usada em interações web.
# - Usa métodos HTTP (GET, POST, PUT, DELETE) para operações CRUD
# - Curva de aprendizado menor 
# - Fácil de implementar e entender

# API SOAP: Simple Object Acess Protocol, vulgo SOAP, é um protocolo que define um padrão para a troca de mensagens (ou dados) em XML (uma linguagem de marcação mais superior ao HTML :P)
# - Mais difícil de entender, porém mais "descritivo"
# - Independente de linguagem e plataforma de transporte
# - Suporte para operações complexas e segurança avançada.

# GraphQL - É uma linguagem de consulta para a sua API, um servidor capaz de realizar essas consultas, retornando dados especificados.
# - Permite que clientes especifiquem o tipo de dado que querem
# - Eficiente na redução de solicitações e no tamanho dos dados transferidos
# - Flexivel e muito tipada, importante para a evolução das minhas API's (nem tenho ainda isadjhfgiasdjxoig)    
# - Aumenta a velocidade do site, ao invés de fazer duas ou três solicitações como o REST, o GraphQL exibe tudo de uma vez só.

# A escolha da API vai depender da funcionalidade da aplicação e as suas necessidades (propostas).

# Verbos HTTP - GET, PUT, PATCH, POST E DELETE :)
# Os verbos HTTP na API RESTful é importante para tornar uma API padronizada, abordagem essa que torna intuitiva e previsível, facilitando a interação entre sistemas e aplicações.
# GET - LEITURA
# POST - CRIAÇÃO
# PUT/PATCH - ATUALIZAÇÃO
# DELETE - REMOÇÃO

# Importante para o design de uma API bem projetada 
