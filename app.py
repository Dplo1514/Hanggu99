from flask import Flask , render_template ,jsonify ,request
import pymongo 
import certifi

#데이터베이스 import
ca = certifi.where()
client = pymongo.MongoClient('mongodb+srv://plo:1514@cluster0.eakep.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.Hangu99

app = Flask(__name__)
#templates html 반환 부분
@app.route('/')
def home():
   return render_template("index.html")

@app.route("/border")
def border():
    return render_template("border.html")
 
@app.route("/border_write")
def border_write():
    return render_template("border_write.html")
 
@app.route("/login_page")
def login_page():
    return render_template("login.html")
 
@app.route("/sing-up")
def sign_up():
    return render_template("sign_up.html")
 
 #회원가입 기능 구현
@app.route("/save_member", methods=["POST"])
def save_member():
    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    b_receive = request.form['b_give']
    
    doc = {
      'Name': name_receive,
      'ID':id_receive,
      'B': b_receive
    }
    
    db.users.insert_one(doc)
    return render_template("index.html") , jsonify({'msg': '회원가입이 완료되었습니다!'})
 
 #로그인 기능 구현
@app.route("/login",methods=["POST" , "GET"])
def login():
    user_list = list(db.users.find({},{'_id':False}))
    user_id = user_list[0]["ID"]
    user_b = user_list[0]["B"]
    user = {user_id : user_b}
    id = request.form['id_give']
    b = request.form['b_give']
    doc = {id : b}
    if user["user_id" : "user_b"] == doc[id : b]:
       return render_template("index.html") , jsonify({'user': user_list})       

if __name__ == '__main__':  
   app.run('0.0.0.0',port=8000,debug=True)