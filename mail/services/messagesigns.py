from mail.models import MessagesSigns


def get_sign(from_: str, to_: str) -> dict:
    sign_obj = MessagesSigns.objects.get(from_email=from_,
                                         to_email=to_)

    sign = sign_obj.sign

    sign_obj.delete()

    return {'sign': sign}


def set_sign(from_: str, to_: str, sign: str):
    MessagesSigns(from_email=from_,
                  to_email=to_,
                  sign=sign).save()
