from flask import Flask, request, jsonify
import base64
import os
from Crypto.Cipher import AES

app = Flask(__name__)

secret = 'TESTTESTTESTTEST'

@app.route("/ping")
def ping():
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

def get_decoded_secret():
    decoded_string = base64.b64decode(secret)
    return decoded_string

def decrypt_message(msg, key):
	decoded_encrypted_msg = base64.b64decode(msg)
	cipher = AES.new(key)
	decrypted_msg = cipher.decrypt(decoded_encrypted_msg)
	unpadded_private_msg = decrypted_msg.rstrip(padding_character)
	return unpadded_private_msg