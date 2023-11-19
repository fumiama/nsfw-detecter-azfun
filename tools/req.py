import azure.functions as func

import asyncio
import io
import aiohttp
from typing import List, IO, Union

import logging


async def download_from_url(url: str) -> IO:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return io.BytesIO(await resp.read())
    except aiohttp.ClientError as e:
        logging.error(e)


async def get_data(req: func.HttpRequest) -> Union[func.HttpResponse, List[IO]]:
    if req.method == "POST":
        data = [io.BytesIO(req.get_body())]
        logging.info("get_url: post body")
    else:
        url = req.params.get('url')
        if not url or len(url) == 0: url = req.params.get('pic')
        if not url or len(url) == 0: return func.HttpResponse(
                "400 BAD REQUEST: please specify an url to analyze",
                status_code=400
            )
        logging.info("get_url: " + str(url))
        data: List[IO] = (await asyncio.gather(
            *[asyncio.create_task(download_from_url(u)) for u in url.split(",")]
        ))
    return data
