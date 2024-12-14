from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.calculator.route import router as calculator_router
from mangum import Mangum

app = FastAPI()

# CORS Middleware (allow all origins for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {"message": "Server is running"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

# Convert FastAPI app to a serverless function using Mangum
handler = Mangum(app)
