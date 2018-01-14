import os
from app import appObj
from flask import render_template, request, jsonify
from uuid import uuid4
from werkzeug import secure_filename

BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPDIR = os.path.join(BASEDIR, 'static', 'user_data')

@appObj.route("/")
def index():
    return render_template('index.html', uid=uuid4())

@appObj.route('/fnupload', methods=['POST'])
def fnupload():
    uid = uuid4()
    if request.method == 'POST':
        try:
            files = request.files
        except:
            return False
        else:
            if len(files) != 3:
                return False
            for i in files:
                file = files[i]
                filename = secure_filename(file.filename)
                if filename.split('.')[-1] not in appObj.config['ALLOWED_EXTENSIONS']:
                    return False
            for i in files:
                save_dir = 
                os.mkdir('')
                file = files[i]
                file.save(os.path.join(UPDIR, secure_filename(file.filename)))
            return jsonify(hi='hi')
    else:
        return False
