# 🔐 2FA Code Generator with QR Code Support

This project is a **Two-Factor Authentication (2FA) code generator** written in Python. It allows you to:

✅ **Generate a secure TOTP secret key**  
✅ **Create a QR code for easy setup**  
✅ **Generate OTP codes from an existing secret key**  
✅ **Works with Google Authenticator, Authy, and similar apps**  

---

## 📌 Features
- 🔑 **Secure Secret Key Generation**
- 📸 **QR Code Generation for Easy Authentication**
- ⏳ **Time-based One-Time Password (TOTP) Code Generation**
- 🛠 **Minimal Dependencies & Easy Setup**
- 🔒 **Works with any 2FA-enabled service**

---

## 🚀 Installation

1️⃣ **Clone the repository**
```sh
git clone https://github.com/mertdogan00/2fa-toolkit.git
cd 2fa
```

2️⃣ **Install dependencies**
```sh
pip install -r requirements.txt
```

---

## ⚡ Usage

### 🔑 **1. Generate a New Secret Key and QR Code**
Run the following command to create a **new 2FA secret key and QR code**:
```sh
python main.py
```
✅ **Output Example:**
```
🔑 Your Secret Key: ABCDEFGHIJKLMNOP
📸 QR Code saved as: 2fa_qr.png
🔢 Your OTP Code: 123456
```
✅ **Scan the `2fa_qr.png` QR Code** using **Google Authenticator, Authy, or another 2FA app**.

---

### 🔢 **2. Generate OTP Code from a Saved Secret Key**
If you already have a secret key and need to generate a **TOTP code**, run:
```sh
python generate_code.py
```
It will prompt you to **enter your secret key**, then display a valid **OTP**.

✅ **Example:**
```
Enter your secret key: ABCDEFGHIJKLMNOP
🔢 Your OTP Code: 654321
```

---

## 🛠 Code Structure

### **Secret Key & OTP Generation**
📄 [`src/generate_2fa.py`](src/generate_2fa.py)
```python
import pyotp

def create_secret_key():
    return pyotp.random_base32()

def generate_totp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()
```

### **QR Code Generation**
📄 [`src/generate_qr.py`](src/generate_qr.py)
```python
import qrcode
import pyotp

def generate_qr_code(secret_key, filename="qrcode.png"):
    totp = pyotp.TOTP(secret_key)
    uri = totp.provisioning_uri(name="YourApp", issuer_name="2FA Generator")
    
    qr = qrcode.make(uri)
    qr.save(filename)
```

### **Main Execution File**
📄 [`main.py`](main.py)
```python
from src.generate_2fa import generate_totp, create_secret_key
from src.generate_qr import generate_qr_code

def main():
    secret_key = create_secret_key()
    print(f"🔑 Your Secret Key: {secret_key}")

    qr_filename = "2fa_qr.png"
    generate_qr_code(secret_key, qr_filename)
    print(f"📸 QR Code saved as: {qr_filename}")

    otp = generate_totp(secret_key)
    print(f"🔢 Your OTP Code: {otp}")

if __name__ == "__main__":
    main()
```

---

## 🛠 Dependencies
The project uses the following Python libraries:
- `pyotp` – Generates **TOTP** codes.
- `qrcode[pil]` – Creates **QR codes**.
- `pillow` – Handles QR code image processing.

Install them with:
```sh
pip install pyotp qrcode[pil] pillow
```

---

## 🔗 References
- [PyOTP (Python OTP Library)](https://github.com/pyotp/pyotp)
- [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en)
- [QR Code Python Documentation](https://pypi.org/project/qrcode/)
- [RFC 6238 - TOTP: Time-Based One-Time Password Algorithm](https://tools.ietf.org/html/rfc6238)

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
🚀 **Contributions are welcome!**  
Feel free to fork this repository, create a branch, and submit a **pull request**.

💡 **Stay secure with Two-Factor Authentication!** 🔒
