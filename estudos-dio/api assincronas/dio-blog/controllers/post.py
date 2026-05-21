from fastapi import Response, status, APIRouter
from schemas.post import PostIn, PostUpdateIn  
from views.post import PostOut
from models.post import posts   
from database import database

from databases.interfaces import Record

router = APIRouter(prefix="/posts")
service = PostService()

@router.get('/', response_model=list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0) -> list[Record]:
    return await service.read_all(published=published, limit=limit, skip=skip)
    
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    query = posts.insert().values(title = post.title, content = post.content, published_at=post.published_at, published = post.published)
    last_id = await database.execute(query)
    return {**post.model_dump(), "id": last_id}

@router.get('/{id}', response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)

@router.patch('/{id}', response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id= id, post=post)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT_, response_model=None)
async def delete_post(id:int):
    return await service.read(id)
    

 # Criando um dicionário para json
# E aqui o parametro framework é recebido diretamente no path (endereço do navegador) - Vulgo PATH PARAMETER

# A estrutura básica de uma FastAPI é ter folders: models, controllers, bios, views e services :)


# As query parameters são baseadas em números inteiros (não necessariamente), e tem os parâmetros skip e limit
# quando as query parameters estão em bool, podemos passar os parâmetros em 0 e 1, on e off, true ou false (True/False) ou yes e no
# Se eu remover o = True do bool, vai dar erro pois argumentos obrigatórios vem primeiro dos argumentos opcionais, no caso ali o skip e limit estão como argumentos opcionais