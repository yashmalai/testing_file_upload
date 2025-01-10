from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = 'media'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/upload', methods=['POST'])
def upload():
    # if 'file' not in request.files:
    #     return jsonify({'message': 'Отсутствует файл для загрузки'}), 401
    
    f = request.files['file']
    # if f.filename == '':
    #     return jsonify({'message': 'Отправленный файл содержит пустое имя'}), 401

    # f.save(app.config['UPLOAD_FOLDER'] + '/' + f.filename)

    # Вывод всех заголовков запроса
    print("Headers:", request.headers)
    
    # Вывод данных формы (если отправлены)
    print("Form Data:", request.form)
    
    # Вывод переданных файлов (если есть)
    if 'file' in request.files:
        f = request.files['file']
        print("File Name:", f.filename)
    else:
        print("No file uploaded.")
    
    # Вывод JSON-данных (если переданы)
    if request.is_json:
        print("JSON Data:", request.get_json())
    else:
        print("No JSON data sent.")
    
    # Вывод строки запроса (если есть)
    print("Query String:", request.args)
    
    # Вывод сырого тела запроса
    print("Raw Body:", request.data)
    return jsonify({'status': 'хз',
                    "Headers:": request.headers,
                    "Form Data:": request.form,
                    "JSON Data:": request.get_json(),
                    "Query String:": request.args,
                    "Raw Body:": request.data,
                    'filename': f.filename, 
                    })
        
if __name__ == '__main__':
    app.run(debug=True)
