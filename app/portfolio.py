from flask import(
    Blueprint, render_template, request, url_for
)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/mail', methods=['POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')
    return render_template('portfolio/sent_mail.html')



def send_email(name, email, message):
    # Configura los detalles de tu cuenta de Gmail
    gmail_user = 'kevinbarrantes02@gmail.com'  # Tu dirección de Gmail
    gmail_password = 'aoozdpexbixkqgom'    # Tu contraseña de Gmail

    # Configura la dirección de correo del visitante como el remitente
    from_email = email  # Usamos el correo proporcionado por el visitante

    # Configura tu dirección de correo como destinatario
    to_email = 'kevinbarrantes02@gmail.com'  # Tu dirección de correo

    # Configura el asunto del correo
    subject = 'Mensaje de contacto de tu portafolio'

    # Crea el objeto MIME para el correo electrónico con formato HTML
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Crea el cuerpo del correo electrónico en formato HTML con estilos
    html_body = f"""
    <html>
    <head>
        <style>
            /* Agrega tus estilos CSS aquí */
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                padding: 20px;
            }}
            .container {{
                background-color: #fff;
                border-radius: 5px;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Mensaje de contacto</h2>
            <p><strong>Nombre:</strong> {name}</p>
            <p><strong>Correo:</strong> {email}</p>
            <p><strong>Mensaje:</strong></p>
            <p>{message}</p>
        </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_body, 'html'))

    try:
        # Inicia una conexión con el servidor SMTP de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Inicia sesión en tu cuenta de Gmail
        server.login(gmail_user, gmail_password)

        # Envía el correo electrónico
        server.sendmail(from_email, to_email, msg.as_string())

        # Cierra la conexión con el servidor SMTP
        server.quit()

        print('Mensaje enviado con éxito')
        # El correo se ha enviado con éxito
        return True
    
    except Exception as e:
        # Maneja cualquier error que ocurra al enviar el correo
        print(f'Error al enviar el correo: {str(e)}')
        return False

