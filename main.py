import os
from google.adk.cli.fast_api import get_fast_api_app
import logging
from fastapi.middleware.cors import CORSMiddleware
from ui import ui_router

logging.basicConfig(level=logging.DEBUG)

try:
    app = get_fast_api_app(agents_dir=".", web=False,session_db_url=os.getenv("SESSION_DB_URL"))
except Exception as e:
    print(repr(e))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(ui_router, prefix="")
