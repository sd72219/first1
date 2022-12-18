from flask import Flask,jsonify,request, render_template
import units

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict',methods = ['POST'])
def pred():
    
    data = request.form
    if request.method == 'POST':
        print('Input data is:',data)
        x = int(data['x'])
        y = int(data['y'])
        z = int(data['z'])
        

        msg = units.pred_class(x,y,z)

        return render_template('after.html', data=int(msg))
    else:
        return jsonify({"message":"unsuccessful"})
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)  

