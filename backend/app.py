from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, DateField, IntegerField, validators

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xza3363199--AIMI'
app.config['MYSQL_DB'] = 'flaskvuesite'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
CORS(app)
api = Api(app)

todos = {}



class ArticleForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    birth = DateField('Birth', [validators.Length(min=30)])
    score = IntegerField('Score', [validators.Length(min=0)])



class Helloworld(Resource):
    def get(self):
        form = ArticleForm(request.form)
        cur = mysql.connection.cursor()
        result_data = cur.execute("SELECT * FROM flaskvuesite")
        data = cur.fetchall()
        return jsonify({
            'result': "Score Table",
            'data': data
        })
    
    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}




api.add_resource(Helloworld, '/')

if __name__ == '__main__':
    app.run(debug=True)
