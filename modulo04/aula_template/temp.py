from string import Template
from datetime import datetime
from email_data import email, senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('./modulo04/aula_template/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')

    dados = {
        'nome': 'Gui',
        'data': data_atual
    }

    corpo_msg = template.substitute(dados)


msg = MIMEMultipart()
msg['from'] = 'Gui Almeida'
msg['to'] = 'ga.designer.art@gmail.com'
msg['subject'] = 'Atenção este é email de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('./modulo04/aula_template/thumb_home.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha)
        smtp.send_message(msg)
        print('Email enviado com sucesso!')
    except Exception as e:
        print('Email não enviado: ')
        print(e)
