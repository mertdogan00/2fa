from src.generate_2fa import generate_totp, create_secret_key
from src.generate_qr import generate_qr_code

def main():
    # new secret key
    secret_key = create_secret_key()
    print(f"🔑 Your Secret Key: {secret_key}")

    # QR code create
    qr_filename = "2fa_qr.png"
    generate_qr_code(secret_key, qr_filename)
    print(f"📸 QR Code saved as: {qr_filename}")


if __name__ == "__main__":
    main()
