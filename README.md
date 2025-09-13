Optical Store Online System - Relatório de Atividades

Título do Relatório: Optical Store Online System - Gestão de Estoque e Registro de Produtos

Objetivo: O principal objetivo deste projeto é desenvolver um sistema online para uma ótica, facilitando o registro de produtos, a gestão de estoque e o acompanhamento de vendas.

2. Introdução

Objetivo Geral
O propósito deste projeto é criar um sistema web utilizando Flask para gerenciar eficientemente o estoque de uma ótica. O sistema permite o registro de produtos, a atualização das quantidades em estoque e o registro de transações de vendas.
Contexto
A gestão de estoque é um componente crítico para empresas de varejo, especialmente em setores que lidam com produtos de alto valor, como óculos e lentes. A implementação de uma solução digital pode otimizar o acompanhamento do inventário e melhorar o atendimento ao cliente, garantindo a disponibilidade dos produtos.

4. Descrição e Análise do Caso
Descrição do Caso
O sistema da ótica consiste nas seguintes funcionalidades principais:
Gestão de Produtos: Adicionar, excluir e listar produtos.


Gestão de Estoque: Monitorar a disponibilidade dos produtos.


Gestão de Vendas: Registrar transações e dados de vendas.


A implementação é baseada no framework Flask, utilizando um banco de dados relacional (SQLite) para armazenar informações de produtos e vendas.
Análise do Problema
Um controle de estoque eficiente garante que os produtos estejam sempre disponíveis quando necessário, reduzindo perdas devido ao excesso ou falta de estoque. O sistema aproveita os relacionamentos do banco de dados para gerenciar automaticamente as vendas e a atualização do estoque.

4. Implementação
Etapas de Execução
Configuração do Projeto:


Instalado Flask e SQLAlchemy.


Criado um esquema de banco de dados para produtos e vendas.


Módulo de Produtos:


Implementados endpoints para adicionar, excluir e listar produtos.


Integrados templates HTML para visualização dos produtos.


Módulo de Vendas:


Criado um modelo para armazenar registros de vendas.


Desenvolvidas visualizações para exibição de transações de vendas.


Desafios e Decisões
Desafio: Garantir a consistência dos dados entre o estoque de produtos e as transações de vendas.


Decisão: Implementação de restrições de chave estrangeira no banco de dados para manter a integridade referencial.



5. Resultados
Testes e Validação
Foram realizados testes unitários para validar a criação e exclusão de produtos.


Simuladas transações de vendas para confirmar a atualização do estoque.


Implementada validação no frontend para evitar registros incorretos de produtos.


Interpretação
Os resultados confirmam que o sistema gerencia corretamente o estoque e o rastreamento de vendas. Os usuários podem adicionar novos produtos, monitorar os níveis de estoque e registrar transações de vendas de forma eficiente.

6. Conclusão
Aprendizados
Experiência adquirida no desenvolvimento de operações CRUD utilizando Flask e SQLAlchemy.


Compreensão da importância dos relacionamentos entre tabelas para a gestão de estoque.


Aplicações Futuras
Implementação de autenticação de usuários para acesso seguro.


Adição de funcionalidades de relatórios e análises para insights sobre vendas.



7. Impacto no Mundo Real
Aplicações Práticas
Varejistas podem acompanhar a disponibilidade de produtos de forma eficiente.


Registros de vendas podem ser usados para otimizar ciclos de reposição de estoque.


Oportunidades de Expansão
O sistema pode ser expandido para integração com plataformas de e-commerce.


Implementação de modelos de machine learning para prever tendências de demanda.



8. Desafios Futuros e Melhorias
Aprimoramento da interface do usuário para melhor interação.


Otimização de consultas ao banco de dados para implantações em grande escala.


Automação de notificações de reposição de estoque com base em limites predefinidos.


9. Configuração Técnica Adicional
Arquivos e Diretórios Relevantes
.venv


.pytest_cache


pycache


populate_db.py


Serviços
services:
  db:
    image: mysql:8.0
    container_name: optical_store_db
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: optical_store
    ports:
      - "3306:3306"
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      retries: 5
    volumes:
      - db_data:/var/lib/mysql


  web:
    build: .
    container_name: optical_store_web
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    command: flask run --host=0.0.0.0 --port=5000
    depends_on:
      - db
volumes:
  db_data:

Arquivo Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "run.py"]

Dependências do Projeto
alembic==1.12.1
click==8.1.8
colorama==0.4.6
Flask==2.2.5
Flask-Migrate==4.1.0
Flask-SQLAlchemy==3.0.5
greenlet==3.1.1
importlib-metadata==6.7.0
importlib-resources==5.12.0
itsdangerous==2.1.2
Jinja2==3.1.6
Mako==1.2.4
MarkupSafe==2.1.5
mysql-connector-python==8.0.33
protobuf==3.20.3
SQLAlchemy==2.0.39
typing_extensions==4.7.1
Werkzeug==2.2.3
zipp==3.15.0




