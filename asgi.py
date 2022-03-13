from glob import glob
from typing import Union
from pathlib import Path
from os import walk, path
from importlib import import_module

import uvicorn
from spa import SPA

from fastapi import FastAPI


app: FastAPI = FastAPI()

for r in [y for x in walk('routers') for y in glob(path.join(x[0], '*.py')) if not '__init__' in y]:
    parts = Path(r).parts
    impmod = '.'.join(parts)[:-3]
    prefix = '/' + parts[1] if not '.py' in parts[1] else ''
    app.include_router(getattr(import_module(impmod), 'router'), prefix=prefix)

if __name__ == '__main__':
    uvicorn.run('asgi:app', host='0.0.0.0', port=8000, reload=True)
