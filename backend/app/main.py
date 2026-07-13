from fastapi import FastAPI, Request
from app.api.thermometr import thermometr_router
from app.api.pages import pages_router
from app.database import SessionDep
from fastapi.responses import RedirectResponse
from fastapi import Depends
import jwt
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="app/templates")

def get_current_user(request: Request) -> dict | None:
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=["HS256"])
    except jwt.PyJWTError:
        return None
    return payload  # тут будет username и что ещё положили в claims

app = FastAPI()
app.include_router(thermometr_router)
app.include(pages_router)

@app.get("/dashboard")
async def dashboard(
    request: Request,
    session: SessionDep,
    user: dict | None = Depends(get_current_user),
):
    if not user:
        return RedirectResponse("/login")
    return templates.TemplateResponse("dashboard.html", {"request": request, "username": user["username"]})