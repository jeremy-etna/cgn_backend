from django.http import JsonResponse


def api_test(request):
    data = {
        'msg': 'bar'
    }
    return JsonResponse(data)
