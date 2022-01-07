from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from mail.services import mails


def get_messages(request: WSGIRequest):
    return JsonResponse({"status": "OK",
                         "messages": mails.get_messages(login=request.GET['login'],
                                                        password=request.GET['password'],
                                                        folder=request.GET['folder'])
                         },
                        # safe=False
                        )


def get_folders(request: WSGIRequest):
    return JsonResponse({"status": "OK",
                         "folders": mails.get_folders(login=request.GET['login'],
                                                      password=request.GET['password'])
                         },
                        # safe=False
                        )