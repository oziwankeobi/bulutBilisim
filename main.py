from flask import Flask, request, jsonify

app = Flask(__name__)

def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                result += chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift_amount - 97) % 26 + 97)
        else:
            result += char
    return result

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data['text']
    shift = data['shift']
    encrypted_text = caesar_cipher(text, shift)
    return jsonify({"encrypted_text": encrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
