from fastapi import FastAPI  
from controllers import post
# import sqlalchemy as sa

# metadata = sa.MetaData()

app = FastAPI()
app.include_router(post.router)