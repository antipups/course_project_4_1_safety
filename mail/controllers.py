from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from mail.services import mails, keys_work, messagesigns


def get_messages(request: WSGIRequest):
    return JsonResponse({"status": "OK",
                         "messages": mails.get_messages(login=request.GET['login'],
                                                        password=request.GET['password'],
                                                        folder=request.GET['folder'])
                         },)


def get_folders(request: WSGIRequest):
    return JsonResponse({"status": "OK",
                         "folders": mails.get_folders(login=request.GET['login'],
                                                      password=request.GET['password'])
                         },)


def get_keys(request: WSGIRequest):
    return JsonResponse({"status": "OK",
                         "keys": keys_work.get_keys(from_=request.GET['from_'],
                                                    to_=request.GET['to_'])
                         },)


@csrf_exempt
def set_keys(request: WSGIRequest):
    get_args = json.loads(request.body.decode())
    keys_work.set_keys(from_=get_args['from_email'],
                       to_=get_args['to_email'],
                       privKey=get_args['privKey'],
                       pubKey=get_args['pubKey'],
                       tripleDesKey=get_args['tripleDesKey'],)
    return JsonResponse({"status": "OK"},)


def get_sign(request: WSGIRequest):
    return JsonResponse({"status": "OK",
                         "sign": messagesigns.get_sign(from_=request.GET['from_'],
                                                       to_=request.GET['to_'])
                         },)


@csrf_exempt
def set_sign(request: WSGIRequest):
    get_args = json.loads(request.body.decode())
    messagesigns.set_sign(from_=get_args['from_email'],
                          to_=get_args['to_email'],
                          sign=get_args['sign'],)
    return JsonResponse({"status": "OK"},)


def set_seen(request: WSGIRequest):
    mails.set_seen(login=request.GET['login'],
                   password=request.GET['password'],
                   uid=request.GET['uid'])
    return JsonResponse({"status": "OK"},)
