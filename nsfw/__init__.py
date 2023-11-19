import azure.functions as func

from json import dumps

from tools import get_data

from .crud import classify, model


async def main(req: func.HttpRequest) -> func.HttpResponse:
    data = await get_data(req)
    if isinstance(data, func.HttpResponse): return data
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
