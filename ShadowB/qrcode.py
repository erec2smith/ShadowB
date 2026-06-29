from ShadowB.Qrcode.generate import qr

def generate_qrcode(text, name="qrcode"):
    return qr(text,name)
