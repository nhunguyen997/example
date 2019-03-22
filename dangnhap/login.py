import MySQLdb

from flask import Flask, render_template, request
app = Flask(__name__)

db = MySQLdb.connect(port=3306, user="NhuNguyen", passwd="250897250897", db="login", host="localhost")
cursor = db.cursor()


@app.route('/')
def login():
    return render_template('giaodien.html')


@app.route('/ketqua', methods=['POST', 'GET'])
def ketqua():
    if request.method == 'POST':
        if request.form['password'] == cursor.execute('select password from login where username =?', request.form['username']):
            result = request.form
            return render_template("ketqua.html", result=result)

        else:
            error = "thong tin dang nhap khong chinh xac"
            return error


if __name__ == '__main__':
    app.run(debug=True)

