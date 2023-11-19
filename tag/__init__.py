import azure.functions as func

from json import dumps

from tools import get_data

from .crud import predict_file


async def main(req: func.HttpRequest) -> func.HttpResponse:
    data = await get_data(req)
    if isinstance(data, func.HttpResponse): return data
    limit = req.params.get('limit')
    if not limit or len(limit) == 0: limit = 0.7
    else:
        try:
            limit = float(limit)
        except:
            return func.HttpResponse(
             "400 BAD REQUEST: limit is not a float number",
             status_code=400
        )
    return func.HttpResponse(dumps(predict_file(data, limit)))
