from crypt import methods
from flask import Flask, request, jsonify
import base64
import os
from Crypto.Cipher import AES

app = Flask(__name__)

secret = 'TESTTESTTESTTEST'

def unpad_str(msg):
    msg = msg.decode('utf-8')
    msg = msg.rstrip('%')
    return msg

def decrypt_message(msg, key):
	decoded_encrypted_msg = base64.b64decode(msg)
	cipher = AES.new(key)
	decrypted_msg = cipher.decrypt(decoded_encrypted_msg)
	unpadded_private_msg = unpad_str(decrypted_msg)
	return unpadded_private_msg

@app.route("/decrypt", methods=['GET'])
def decrypt():
    args = request.args
    encrypted_string = args.get('enc_str')
    dec_str = decrypt_message(encrypted_string, secret) 
    return jsonify({"status": str(dec_str)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)