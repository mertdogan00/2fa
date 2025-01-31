import qrcode
import pyotp

def generate_qr_code(secret_key, filename="qrcode.png"):
    """
    Generate a QR code for the given secret key.
    
    :param secret_key: The secret key to encode.
    :param filename: Output filename for the QR image.
    """
    totp = pyotp.TOTP(secret_key)
    uri = totp.provisioning_uri(name="YourApp", issuer_name="2FA Generator")
    
    qr = qrcode.make(uri)
    qr.save(filename)
