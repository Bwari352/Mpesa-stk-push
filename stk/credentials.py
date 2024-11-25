import json
import base64
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

class Credentials:
    consumer_key = "vh9rrzYjcCElJWz9cFiVAjXyeKOmdY7zGFQ3auVaymjA4SV0"
    consumer_secret = "b1VSUobBefy2TKuT6K1bDRIncQhLEJJjbV0prUyM9kiKU8GuPDPjPuas2ZZdnSb9"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


class MpesaAccessToken:
    token = requests.get(Credentials.api_url, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
    access_token = json.loads(token.text)
    validated_token = access_token['access_token']

class MpesaPassword:
    timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    shortcode = "174379"
    passkey = Credentials.passkey

    encode_str = shortcode + passkey + timestamp

    encoded = base64.b64encode(encode_str.encode())

    decoded_password = encoded.decode('utf-8')






