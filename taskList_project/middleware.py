

def open_access_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = 'Origin', 'Content-Type', 'Accept','Authorization'
        response["Access-Control-Allow-Methods"] = "GET", "HEAD","PUT", "POST", "PATCH", "DELETE"
        response["Access-Control-Max-Age"] = "86400"
        return response
    return middleware