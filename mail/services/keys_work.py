from mail.models import KeysStorage


def get_keys(from_: str, to_: str) -> dict | bool:
    if keys_objects := KeysStorage\
            .objects\
            .filter(from_email=from_,
                    to_email=to_):
        keys_obj = keys_objects[0]

        privKey, pubKey, tripleDesKey = keys_obj.privkey, keys_obj.pubkey, keys_obj.tripleDesKey

        # keys_obj.delete()

        return {'pubKey': pubKey,
                'privKey': privKey,
                'tripleDesKey': tripleDesKey}

    else:
        return False


def set_keys(from_: str, to_: str, privKey: str, pubKey: str, tripleDesKey: str):
    KeysStorage(from_email=from_,
                to_email=to_,
                privkey=privKey,
                pubkey=pubKey,
                tripleDesKey=tripleDesKey).save()
