import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
# from general_config import Recipients, mail_user, mail_password
from mailing_api.config import SERVER_SITE


def get_text_from_dict(data: dict) -> str:
    result = ''
    for key, value in data.items():
        result += key + ': ' + value + '\n'
    return result


def check_mail(login: str, password: str):
    mail = smtplib.SMTP_SSL(SERVER_SITE)

    try:
        mail.login(login, password)
        mail.quit()

    except Exception as e:
        return e.args[1]



# def send_mail(data: dict):
#
#     sender = mail_user
#     subject = 'Новая заявка из бота central_tur_bot'
#
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subject
#     msg['From'] = 'Python script <' + sender + '>'
#     msg['To'] = ', '.join(Recipients)
#     msg['Reply-To'] = sender
#     msg['Return-Path'] = sender
#     msg['X-Mailer'] = 'Python/' + (python_version())
#
#     text = get_text_from_dict(data=data)
#     part_text = MIMEText(text, 'plain')
#
#     msg.attach(part_text)
#
#     try:
#         mail = smtplib.SMTP_SSL(server)
#         mail.login(mail_user, mail_password)
#         mail.sendmail(sender, Recipients, msg.as_string())
#         mail.quit()
#
#     except Exception as e:
#         logger.exception(f'Error in mailing sending - {e}')
#
#     else:
#         logger.success(f'Success send mail')
