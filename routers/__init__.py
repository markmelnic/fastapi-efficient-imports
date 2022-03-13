from os import getenv
from typing import Any
from requests import post
from jose import jwt, JWTError

from fastapi import status, APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette.responses import HTMLResponse, FileResponse, RedirectResponse, Response

from db import *
from utils import *
from schemas import *
