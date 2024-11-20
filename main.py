from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import random

app = FastAPI()

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE"])
async def handle_request(request: Request, path: str):
    # Получаем информацию о запросе
    method = request.method
    url = str(request.url)
    headers = dict(request.headers)
    body = await request.body()
    print(path)
    api_box = ['http://localhost:8001/' , 'http://localhost:8002/' , 'http://localhost:8003/']
    api = f'{api_box[random.randint(0 , len(api_box)-1)]}{path}'
    print(api)

    # Отправляем запрос на другой сервер
    try:
        if method == "GET":
            response = requests.get(api, headers=headers)
        elif method == "POST":
            response = requests.post(api, headers=headers, data=body)
        elif method == "PUT":
            response = requests.put(api, headers=headers, data=body)
        elif method == "DELETE":
            response = requests.delete(api, headers=headers)
        elif method == "OPTIONS":
            response = requests.options(api, headers=headers)
        elif method == "HEAD":
            response = requests.head(api, headers=headers)
        elif method == "PATCH":
            response = requests.patch(api, headers=headers, data=body)
        elif method == "TRACE":
            response = requests.request("TRACE", api, headers=headers)
        else:
            return JSONResponse(content={"error": "Unsupported method"}, status_code=405)

        # Проверка статуса ответа
        if response.status_code == 200:
            # Если запрос успешен, выводим содержимое ответа
            print("Ответ сервера:")
            return JSONResponse(content=response.json())
        else:
            # Если запрос не успешен, выводим сообщение об ошибке
            print(f"Ошибка: {response.status_code}")
            return JSONResponse(content={"error": f"Error: {response.status_code}"}, status_code=response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

    # Формируем ответ
    response_data = {
        "method": method,
        "endpoint": path,  # Добавляем конечную точку в ответ
        "url": url,
        "headers": headers,
        "body": body.decode("utf-8") if body else None,
    }

    return JSONResponse(content=response_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)