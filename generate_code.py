from src.generate_2fa import generate_totp

def main():
    # get secret key from user
    secret_key = input("Enter your secret key: ").strip()

    # OTP code
    otp = generate_totp(secret_key)
    print(f"🔢 Your OTP Code: {otp}")

if __name__ == "__main__":
    main()
