from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import jwt

pages_router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="app/templates")

def get_current_user(request: Request) -> dict | None:
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=["HS256"])
    except jwt.PyJWTError:
        return None
    return payload 

@pages_router.get("/invite")
async def invite_page(request: Request):
    return templates.TemplateResponse(request, "auth/invite.html")

@pages_router.get("/register")
async def register_page(request: Request, invite_code: str = ""):
    return templates.TemplateResponse(request, "auth/register.html", {"invite_code": invite_code})

@pages_router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(request, "auth/login.html")
