from fastapi import FastAPI
from mangum import Mangum
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication

app = FastAPI()
handler = Mangum(app)



models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
