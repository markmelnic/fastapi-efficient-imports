from . import *

router = APIRouter(tags=['Dashboard'])

@router.get('/dashboard')
async def dashboard():
    return Response(status_code=status.HTTP_200_OK)
