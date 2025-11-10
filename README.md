<div align="center">

# 🔐 Flask Auth Demo

Uma aplicação simples de autenticação desenvolvida com **Flask** e **SQLite**, demonstrando o processo completo de **registro e login de usuários** com boas práticas de arquitetura, validação e tratamento de erros no backend.

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

Este projeto é uma **demo de autenticação com Flask**, ideal para quem deseja compreender o fluxo completo de **cadastro, login e manipulação de banco de dados** com **tratamento de erros personalizado** e **estrutura limpa e modular**.

O foco está na clareza e na organização, simulando uma base sólida para projetos de APIs REST.

---

## 🧠 Funcionalidades

✅ Registro de usuários  
✅ Login com verificação de credenciais  
✅ Hash seguro de senhas  
✅ Middleware para tratamento de erros SQL  
✅ Logging detalhado de exceções  
✅ Estrutura modular e escalável  

---

## 🧩 Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| **Linguagem** | Python 3.12+ |
| **Framework Web** | Flask |
| **Banco de Dados** | SQLite |
| **ORM** | SQLAlchemy |
| **Validação** | Pydantic |
| **Migrações** | Flask-Migrate |
| **Logs** | Logging nativo do Python |

---

## 📂 Estrutura do Projeto

```bash
sample-auth-flask/
│
├── app.py                # Ponto de entrada da aplicação Flask
├── database.py           # Configuração e inicialização do banco
├── db_init.py            # Script de criação inicial das tabelas
│
├── models/               # Modelos SQLAlchemy
│   └── user_model.py
│
├── schemas/              # Schemas Pydantic para validação
│   └── user_schema.py
│
├── middleware/           # Middlewares personalizados
│   └── sqlErrorHandler.py
│
├── routes/               # Rotas e controladores da API
│   └── auth_routes.py
│
└── .env.example          # Exemplo de variáveis de ambiente
````

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

   ```bash
   FLASK_ENV=development
   DATABASE_URL=sqlite:///auth.db
   SECRET_KEY=sua_chave_secreta
   ```

5. **Inicie o servidor**

   ```bash
   flask run
   ```

---

## 📬 Endpoints Principais

| Método | Endpoint    | Descrição                    |
| ------ | ----------- | ---------------------------- |
| `POST` | `/register` | Cria um novo usuário         |
| `POST` | `/login`    | Realiza o login e gera token |

**Exemplo de payload (registro):**

```json
{
  "email": "user@example.com",
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

O projeto inclui um **middleware de tratamento de erros SQL**, que intercepta exceções do banco e gera respostas JSON estruturadas, além de salvar os logs em arquivo e console.

```python
class SqlErrorHandler:
    def __init__(self, error):
        self.error = error

    def errors(self):
        ...
        logger.error(f"[{code}] {error_type}: {error_msg}")
        return {"message": message, "status_code": code}
```

---

## 🧭 Roadmap

* [ ] Adicionar autenticação JWT
* [ ] Implementar refresh tokens
* [ ] Criar testes unitários com `pytest`
* [ ] Adicionar CI/CD com GitHub Actions
* [ ] Criar container com Docker

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
```