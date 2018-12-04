import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, DateTimeField, IntegerField, validators

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

# 创建用户表
class UserForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    birth = DateTimeField('Birth', [validators.Length(min=30)], format="%Y-%m")
    score = IntegerField('Score', [validators.Length(min=0)])


# 用户表API
class UserList(Resource):

    def get(self):
        form = UserForm(request.form)
        cur = mysql.connection.cursor()
        result_data = cur.execute("SELECT * FROM flaskvuesite")
        data = cur.fetchall()

        return jsonify({
            'data': data
        })

# 成都市数据API（暂时使用）
class Chengdu(Resource):
    
    def get(self):
        with open('./data.json', 'r', encoding='utf-8') as f:
            table = json.load(f)
            # print(table)
            f.close()
        # 数据备份
        with open('./data2.json', 'w', encoding="utf-8") as f:
            json.dump(table, f)
            print('Opened.')
            f.close()

        return jsonify({
            'table': table
        })

# 上海市数据API（暂时使用）
class Shanghai(Resource):
    
    def get(self):
        with open('./shanghai.json', 'r', encoding="utf-8") as f:
            table = json.load(f)
            f.close()

        return jsonify({
            'table': table
        })

api.add_resource(UserList, '/v1/userlist')
api.add_resource(Chengdu, '/v1/成都')
api.add_resource(Shanghai, '/v1/上海')


if __name__ == '__main__':
    app.run(debug=True)
