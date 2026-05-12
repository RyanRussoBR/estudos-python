from fastapi import FastAPI
from datetime import UTC, datetime  

app = FastAPI()
fake_db = [
    {"title": f"Criando uma aplicação com DJANGO", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app FASTAPI", "date": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com FLASK", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app STARLETT", "date": datetime.now(UTC), "published": False},
]


# As query parameters são baseadas em números inteiros (não necessariamente), e tem os parâmetros skip e limit
# quando as query parameters estão em bool, podemos passar os parâmetros em 0 e 1, on e off, true ou false (True/False) ou yes e no
# Se eu remover o = True do bool, vai dar erro pois argumentos obrigatórios vem primeiro dos argumentos opcionais, no caso ali o skip e limit estão como argumentos opcionais

@app.get('/posts')
def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):
    return [post for post in fake_db[skip: skip + limit] if post ['published'] is published]


@app.get("/posts/{framework}") # Define uma rota
def read_framework_posts(framework: str): # Aqui define o método utilizado
    return {
        "posts": [ 
        {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
        {"title": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)}, 
        ]
    } # Criando um dicionário para json
# E aqui o parametro framework é recebido diretamente no path (endereço do navegador) - Vulgo PATH PARAMETER

# A estrutura básica de uma FastAPI é ter folders: models, controllers, bios, views e services :)
