from ShadowB.Qrcode.generate import qr

def generate_qrcode(text, name="qrcode", path=""):
    return qr(text, name, path)
