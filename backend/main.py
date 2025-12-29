from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/square/{num}")
def square_number(num: int):
    return {"number": num, "square": num**2}


#Run Steps
# cd backend
# docker build -t fastapi-app .
# docker run -d -p 8000:8000 fastapi-app
# Visit http://localhost:8000