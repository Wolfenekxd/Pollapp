from Crypto.PublicKey import RSA

key = RSA.generate(2048)

def generate_private_key():
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    file_out.close()
    return private_key

def generate_public_key():
    public_key = key.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()
    return public_key

public_key = generate_public_key()
private_key = generate_private_key()
print(public_key)
print(private_key)