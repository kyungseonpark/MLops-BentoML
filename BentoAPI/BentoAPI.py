from fastapi import FastAPI

bentoml = FastAPI(
    title='BentoML_API',
    description=f'BentoML API Set 🍱'
)

TAGS = []


@bentoml.post("/hello")
async def hello_world(api_body: dict):
    return {"return": "Hello World!"}