from crypt import methods
from this import s
from flask import Flask, request, jsonify
import base64
import os
from Crypto.Cipher import AES
from urllib.parse import unquote

app = Flask(__name__)

secret = 'TESTTESTTESTTEST'

p_char = '%'


def unpad_str(msg):
    msg = msg.decode('utf-8')
    msg = msg.rstrip('%')
    return msg


def decrypt_message(msg, key):
    decoded_encrypted_msg = base64.b64decode(msg)
    cipher = AES.new(key)
    try:
        decrypted_msg = cipher.decrypt(decoded_encrypted_msg)
    except:
        raise Exception('Error Decrypting')
    else:
        unpadded_private_msg = unpad_str(decrypted_msg)
        return unpadded_private_msg


def decode_str(msg):
    msg = msg.rstrip(p_char)
    splitted = msg.split(':')
    splitted_bev = splitted[4].split(';')
    resp_dect = {}
    resp_dect['id'] = int(float(splitted[0]))
    resp_dect['name'] = splitted[1]
    resp_dect['email'] = splitted[2]
    resp_dect['emp_no'] = 'N/A' if (splitted[3] == '0.0') else splitted[3]
    resp_dect['beverages'] = splitted_bev
    resp_dect['food_preference'] = splitted[5]
    return resp_dect


@app.route("/decrypt", methods=['GET'])
def decrypt():
    args = request.args
    encrypted_string = args.get('enc_str')
    dec_str = ''
    try:
        dec_str = decrypt_message(encrypted_string, secret)
    except:
        return jsonify({'error': 'Invalid User!!'}), 400, {'ContentType': 'application/json'}
    else:
        processed_res = decode_str(dec_str)
        return jsonify({'data': processed_res}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
