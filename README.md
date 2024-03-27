# Projeto da Trilha Back-end ( Django )

Como usar o projeto?

```bash

# Crie um virtual env dentro da pasta CRM
python -m venv .venv

# Ative-o (windows)
.venv\Scripts\Activate.ps1

# Ative-o (linux)
source .venv/bin/activate

# Instale as dependencias
pip install -r requirements.txt

# Migre os dados
python manage.py migrate

# Criar um superuser
python manage.py createsuperuser

# Rode o projeto
python manage.py runserver

```

Para acessar o projeto localmente basta acessar <a href="http://localhost:8000/">http://localhost:8000/</a></p>