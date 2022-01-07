from imap_tools import MailBox, AND
from mail.services.config import Servers, MaxOutMessages


def get_server(email: str) -> str:
    return Servers.Mail if 'mail' in email else Servers.Yandex


def get_messages(login: str, password: str, folder: str) -> list:
    messages = []
    with MailBox(get_server(login))\
            .login(login, password) as mail:

        if folder:
            mail.folder.set(folder=folder)

        for message in mail.fetch(limit=MaxOutMessages):
            attachs = [{'name': attach.filename, 'content': attach.payload} for attach in message.attachments]
            messages.append({'subject': message.subject,
                             'date': message.date_str,
                             'body': message.text,
                             'from': message.from_,
                             'flags': message.flags,
                             'id': int(message.uid)
                             # 'attachments': attachs,
                             })

    return messages[::-1]


def get_folders(login: str, password: str) -> tuple:
    with MailBox(get_server(login))\
            .login(login, password) as mail:
        return tuple({"id": folder.name,
                      "title": folder.name} for folder in mail.folder.list())


if __name__ == '__main__':
    ...
