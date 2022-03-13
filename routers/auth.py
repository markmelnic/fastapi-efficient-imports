from . import *

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.get('/auth_test')
async def auth_test():
    return Response(status_code=status.HTTP_200_OK)
