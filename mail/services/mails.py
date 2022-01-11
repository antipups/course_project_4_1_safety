from imap_tools import MailBox, AND, MailMessageFlags
from mail.services.config import Servers, MaxOutMessages
import base64


def get_server(email: str) -> str:
    return Servers.Mail if 'mail' in email else Servers.Yandex


def get_messages(login: str, password: str, folder: str) -> list:
    messages = []
    with MailBox(get_server(login))\
            .login(login, password) as mail:

        if folder:
            mail.folder.set(folder=folder)

        for message in mail.fetch(limit=MaxOutMessages,
                                  reverse=True,
                                  mark_seen=False):
            attachs = [{'name': attach.filename,
                        'content': base64.b64encode(attach.payload).decode()}
                       for attach in message.attachments]

            messages.append({'subject': message.subject,
                             # 'date': "",
                             'date': message.date_str,
                             'body': message.html,
                             'from': message.from_,
                             'flags': message.flags[:1],
                             'id': int(message.uid),
                             'attachments': attachs,
                             })
    return messages


def get_folders(login: str, password: str) -> tuple:
    with MailBox(get_server(login))\
            .login(login, password) as mail:
        return tuple({"id": folder.name,
                      "title": folder.name} for folder in mail.folder.list())


def set_seen(login: str, password: str, uid: str):
    with MailBox(get_server(login))\
            .login(login, password) as mail:
        mail.flag(uid_list=(uid, ),
                  flag_set=(MailMessageFlags.SEEN,),
                  value=True)


if __name__ == '__main__':
    ...
