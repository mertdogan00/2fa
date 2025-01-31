import pyotp

def create_secret_key():
    """
    Generate a new base32 secret key.
    :return: A random secret key
    """
    return pyotp.random_base32()

def generate_totp(secret_key):
    """
    Generate a TOTP (Time-based One-Time Password).
    
    :param secret_key: The secret key for OTP generation.
    :return: OTP code
    """
    totp = pyotp.TOTP(secret_key)
    return totp.now()
