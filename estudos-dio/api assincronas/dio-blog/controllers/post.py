from datetime import UTC, datetime  
from typing import Annotated 

from fastapi import Response, FastAPI, Cookie, status, Header
from main import app
from schemas.post import PostIn  
from views.post import PostOut



fake_db = [
    {"title": f"Criando uma aplicação com DJANGO", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app FASTAPI", "date": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com FLASK", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app STARLETT", "date": datetime.now(UTC), "published": False},
]

@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump()) # Este model dump faz com que a representação na classe post esteja em formato de dicionario.
    return post
    
@app.get('/posts', response_model=list[PostOut])
def read_posts(response: Response, published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None, user_agent: Annotated[str | None, Header()] = None):
    response.set_cookie(key='user_six_seven', value='roro@hotmail.com') # Le um cookie
    print(f'Cookie: {ads_id}') # Define um cookie, é o numero la hehe
    print(f'User_Agent: {user_agent}')
    return [post for post in fake_db[skip: skip + limit] if post ['published'] is published]



@app.get("/posts/{framework}", response_model=PostOut) # Define uma rota
def read_framework_posts(framework: str): # Aqui define o método utilizado
    return {
        "posts": [ 
        {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
        {"title": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)}, 
        ]
    } # Criando um dicionário para json
# E aqui o parametro framework é recebido diretamente no path (endereço do navegador) - Vulgo PATH PARAMETER

# A estrutura básica de uma FastAPI é ter folders: models, controllers, bios, views e services :)


# As query parameters são baseadas em números inteiros (não necessariamente), e tem os parâmetros skip e limit
# quando as query parameters estão em bool, podemos passar os parâmetros em 0 e 1, on e off, true ou false (True/False) ou yes e no
# Se eu remover o = True do bool, vai dar erro pois argumentos obrigatórios vem primeiro dos argumentos opcionais, no caso ali o skip e limit estão como argumentos opcionais