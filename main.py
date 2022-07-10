from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request


async def homepage(request: Request):
    request.state.test = [x for x in range(999999)]
    return JSONResponse({'hello': 'world'})


app = Starlette(routes=[
    Route('/', homepage),
])