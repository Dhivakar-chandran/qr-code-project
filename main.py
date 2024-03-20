from flask import Flask,render_template,request
import qrcode

app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        #print(request.form ['qrinput'])
        img=qrcode.make(request.form ['qrinput'])
        img.save('static/qr code/out.jpg')
        return render_template('home.html', image="True")
    return render_template('home.html', image="")

if __name__== "__main__":
   app.run(debug=True, host="0.0.0.0")