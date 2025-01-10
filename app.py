from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = 'media'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'message': 'Отсутствует файл для загрузки'}), 401
    
    f = request.files['file']
    if f.filename == '':
        return jsonify({'message': 'Отправленный файл содержит пустое имя'}), 401

    f.save(app.config['UPLOAD_FOLDER'] + '/' + f.filename)
    return jsonify({'status': 'success'})
        
if __name__ == '__main__':
    app.run(debug=True)
