from starlette.responses import PlainTextResponse

def start_test_point(request):
    return PlainTextResponse("Welcome to GuruKul")