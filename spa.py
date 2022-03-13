from glob import glob
from typing import Union
from pathlib import Path
from os import walk, path
from importlib import import_module

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException

def SPA(app: FastAPI, build_dir: Union[Path, str]) -> FastAPI:
    # Serves a React application in the root directory

    @app.exception_handler(StarletteHTTPException)
    async def _spa_server(req: Request, exc: StarletteHTTPException):
        if exc.status_code == 404:
            return FileResponse('index.html', media_type='text/html')
        else:
            return await http_exception_handler(req, exc)

    if isinstance(build_dir, str):
        build_dir = Path(build_dir)

    for r in [y for x in walk('routers') for y in glob(path.join(x[0], '*.py')) if not '__init__' in y]:
        parts = Path(r).parts
        impmod = '.'.join(parts)[:-3]
        prefix = '/' + parts[1] if not '.py' in parts[1] else ''
        app.include_router(getattr(import_module(impmod), 'router'), prefix=prefix)

    return app
