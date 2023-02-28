# jobboard
First api with technology FastApi

Install libraries:
* python -m pip install [libreria]

Work with requirements file:
* pip freeze > requirements.txt                 | Generar un archivo requirements.txt
* pip install -r requirements.txt               | Instalar todas las dependencias


Work with database migration:
* alembic init alembic                          | Migraciones usando alembic
* alembic revision --autogenerate -m “init”     | Generar primera migración
* alembic upgrade head                          | Aplicar primera migración
