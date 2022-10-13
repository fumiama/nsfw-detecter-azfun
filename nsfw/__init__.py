import azure.functions as func

from typing import List, IO
import asyncio
from json import dumps

from .crud import classify, model, download_from_url

async def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "POST":
        data = req.get_body()
    else:
        url = req.params.get('url')
        if not url or len(url) == 0: url = req.params.get('pic')
        if not url or len(url) == 0: return func.HttpResponse(
                "400 BAD REQUEST: please specify an url to analyze",
                status_code=400
            )
        data: List[IO] = await asyncio.gather(asyncio.create_task(download_from_url(url)))
    size = req.params.get('size')
    if not size or len(size) == 0: size = 224
    else:
        try:
            size = int(size)
        except:
            return func.HttpResponse(
             "400 BAD REQUEST: size is not a int number",
             status_code=400
        )
    return func.HttpResponse(dumps(classify(model, data, size)))
