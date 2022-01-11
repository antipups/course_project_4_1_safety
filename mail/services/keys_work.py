from mail.models import KeysStorage


def get_keys(from_: str, to_: str) -> dict:
    keys_obj = KeysStorage.objects.get(from_email=from_,
                                       to_email=to_)

    privKey, pubKey, tripleDesKey = keys_obj.privkey, keys_obj.pubkey, keys_obj.tripleDesKey

    # keys_obj.delete()

    return {'pubKey': pubKey,
            'privKey': privKey,
            'tripleDesKey': tripleDesKey}


def set_keys(from_: str, to_: str, privKey: str, pubKey: str, tripleDesKey: str):
    KeysStorage(from_email=from_,
                to_email=to_,
                privkey=privKey,
                pubkey=pubKey,
                tripleDesKey=tripleDesKey).save()
