from imap_tools import MailBox
from mail.services.config import Servers, MaxOutMessages


def get_server(email: str) -> str:
    return Servers.Mail if 'mail' in email else Servers.Yandex


def get_messages(login: str, password: str) -> list:
    messages = []
    with MailBox(get_server('imap.mail.com'))\
            .login(login, password) as mail:
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
    print(messages)

    return messages
