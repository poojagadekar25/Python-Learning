from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Directory where HTML files are stored

@app.get("/")
def read_root(request: Request):
    # Render 'index.html' with a variable passed to the template
    return templates.TemplateResponse("index.html", {"request": request, "username": "John Doe"})
