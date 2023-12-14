from flask import Flask, render_template, request
from caesar_cipher import encrypt_caesar, decrypt_caesar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form['plaintext']
    shift = int(request.form['shift'])
    ciphertext = encrypt_caesar(plaintext, shift)
    return render_template('result.html', operation='Encrypt', text=ciphertext)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.form['ciphertext']
    shift = int(request.form['shift'])
    decrypted_text = decrypt_caesar(ciphertext, shift)
    return render_template('result.html', operation='Decrypt', text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
