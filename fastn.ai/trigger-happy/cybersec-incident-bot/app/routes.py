from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.ai_agent import classify
from app.ucl_client import send_to_slack
from app.models import Incident
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/report", response_class=HTMLResponse)
async def report(request: Request, type: str = Form(...), desc: str = Form(...)):
    level = classify(type, desc)
    result = send_to_slack(type, desc, level)
    incident = Incident(type=type, desc=desc, level=level)
    return templates.TemplateResponse("success.html", {"request": request, "incident": incident, "result": result})
