from twilio.rest import Client

# Vos informations d'authentification Twilio
account_sid = 'AC4c0653f793cfe944cd0d8f7e36311cf0'
auth_token = '9502ec355dff0d29be7bd2a005605646'
twilio_phone_number = '+12296290660'  

# Créez un client Twilio
client = Client(account_sid, auth_token)

# Utilisez le client pour envoyer des SMS
message = client.messages.create(
    body='Ceci est un message de test.',
    from_=twilio_phone_number,
    to='+22956543880'  
)
