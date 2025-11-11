<div align="center">

[Veja o estado atual do projeto aqui!](https://github.com/chEfInHO0/sample-auth-flask/tree/dev)

# 🔐 Flask Auth Demo

Uma **demo simples de autenticação** desenvolvida com **Flask** e **SQLite**, demonstrando o processo completo de **registro e login de usuários**, com boas práticas de **arquitetura backend**, **validação** e **tratamento de erros**.

---

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405e?logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-success)

</div>

---

## 🚀 Sobre o Projeto

Este projeto é uma **demo de autenticação baseada em Flask**, criada para ilustrar o fluxo completo de **cadastro, autenticação e gerenciamento de banco de dados**, utilizando uma **arquitetura modular limpa** e **tratamento personalizado de erros SQL**.

O objetivo principal é demonstrar como estruturar uma API backend **escalável, organizada e sustentável**, pronta para integrar com frameworks frontend como **React** ou **Vue**.

---

## 🧠 Funcionalidades

✅ Cadastro de usuários
✅ Login com verificação de credenciais
✅ Hash seguro de senhas
✅ Middleware para tratamento de erros SQL
✅ Sistema de logs centralizado
✅ Estrutura modular e escalável

---

## 🧩 Tecnologias Utilizadas

| Categoria          | Tecnologias              |
| ------------------ | ------------------------ |
| **Linguagem**      | Python 3.12+             |
| **Framework Web**  | Flask                    |
| **Banco de Dados** | SQLite                   |
| **ORM**            | SQLAlchemy               |
| **Validação**      | Pydantic                 |
| **Migrações**      | Flask-Migrate            |
| **Logs**           | Logging nativo do Python |

---

## 📂 Estrutura do Projeto

```bash
sample-auth-flask/
│
├── logs/                 # Arquivos de log (erros, eventos, etc.)
│
├── middleware/           # Middlewares personalizados
│   └── sqlErrorHandler.py
│
├── models/               # Modelos SQLAlchemy
│   └── user_model.py
│
├── schemas/              # Schemas Pydantic para validação
│   └── user_schema.py
│
├── __init__.py           # Marca o diretório como um pacote Python
├── .env.example          # Exemplo de configuração de variáveis de ambiente
├── .gitignore            # Arquivo de exclusões do Git
├── app.py                # Ponto de entrada da aplicação Flask
├── database.py           # Configuração e inicialização do banco
├── db_init.py            # Script de criação inicial das tabelas
├── README.md             # Documentação do projeto
└── requirements.txt      # Dependências do projeto
```

---

## ⚙️ Como Executar o Projeto

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seuusuario/flask-auth-demo.git
   cd flask-auth-demo
   ```

2. **Crie e ative o ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env`**

   Copie o arquivo `.env.example` para `.env` e ajuste as variáveis conforme seu ambiente:

   ```bash
   cp .env.example .env
   ```

   ### `.env.example`

   ```env
   # Chave secreta do Flask
   SECRET_KEY="sua_chave_secreta"

   # String de conexão com o banco de dados
   SQLALCHEMY_DATABASE_URI="sqlite:///seu_banco.db"

   # Configurações de sessão
   SESSION_COOKIE_HTTPONLY=True  # Protege os cookies contra scripts no cliente
   SESSION_COOKIE_SECURE=True    # Altere para False em ambiente de desenvolvimento
   SESSION_COOKIE_SAMESITE="Lax"

   # Configurações de login persistente
   REMEMBER_COOKIE_DURATION=7    # Dias
   REMEMBER_USER=True

   # Docker-Compose ENV

   MYSQL_ROOT_PASSWORD=MYSQL_PASSWORD
   MYSQL_DATABASE=MYSQL_DATABASE
   MYSQL_USER=MYSQL_USER
   MYSQL_PASSWORD=MYSQL_PASSWORD
   MYSQL_PORT=MYSQL_PORT
   ```

5. **Inicialize o banco de dados (se necessário)**

   ```bash
   python db_init.py
   ```

6. **Execute o servidor Flask**

   ```bash
   flask run
   ```

---

## 📬 Endpoints Principais

| Método | Endpoint    | Descrição                     |
| ------ | ----------- | ----------------------------- |
| `POST` | `/register` | Cria um novo usuário          |
| `POST` | `/login`    | Realiza login e retorna o JWT |

**Exemplo de requisição (cadastro):**

```json
{
  "email": "usuario@exemplo.com",
  "password": "123456"
}
```

**Exemplo de resposta (erro tratado):**

```json
{
  "message": "E-mail já cadastrado.",
  "error": "UNIQUE constraint failed: users.email",
  "status_code": 409
}
```

---

## 🧾 Tratamento de Erros e Logs

O projeto inclui um **middleware personalizado de tratamento de erros SQL**, que intercepta exceções do banco e retorna respostas JSON padronizadas, além de registrar os detalhes no console e em arquivo de log.

```python
class SqlErrorHandler:
    def __init__(self, error):
        self.error = error

    def errors(self):
        ...
        logger.error(f"[{code}] {error_type}: {error_msg}")
        return {"message": message, "status_code": code}
```

Os logs são salvos automaticamente dentro da pasta `/logs`.

---

## 🧭 Roadmap

- [ ] Adicionar autenticação JWT
- [ ] Implementar refresh tokens
- [ ] Criar testes unitários com `pytest`
- [ ] Configurar CI/CD com GitHub Actions
- [ ] Adicionar containerização com Docker

---

## 👨‍💻 Autor

**Luccas Santos**
Backend Developer • Python • Flask • FastAPI • Node.js

📧 [luccaselias0@gmail.com](mailto:luccaselias0@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/luccas-santos-3)

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

Feito com 💙 por **Luccas Santos**
Se gostou, ⭐ o repositório e contribua!

</div>

---
