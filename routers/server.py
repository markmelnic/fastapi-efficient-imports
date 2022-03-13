from . import *

router = APIRouter(tags=['Server'])

@router.get('/status')
async def status():
    return {
        'status': 'Live',
    }
