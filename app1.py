from flask import Flask,jsonify

app = Flask(__name__)

notes = [
    {"id":1,"Title":"Study Flask","Content":"start with basics"},
    {"id":2,"Title":"Study Github","Content":"start with repo"}
]

@app.route("/api",methods=["GET"])
def get_notes():
    return success_response(data=notes,status=200)

#helper
def success_response(data=None,message="Success",status=200):
    return jsonify({"success":True,"message":message,"data":data})

if __name__=="__main__":
    app.run(debug=True)