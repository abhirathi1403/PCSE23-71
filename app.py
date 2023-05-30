from flask import *
import numpy as np
import pickle

with open('mysaved.pkl', 'rb') as file:
    model = pickle.load(file)
app=Flask(__name__)
@app.route('/')
def main():
    #return " hello"
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict1():

    age=int(request.form['age'])
    km=int(request.form['driven'])
    fuel=int(request.form['fuel'])
    seller=int(request.form['seller'])
    trans=int(request.form['transmission'])
    owner=int(request.form['owner'])
    milage=int(request.form['Milage'])
    engine=int(request.form['engine'])
    power=int(request.form['power'])
    seat=int(request.form['Seat'])
    name=int(request.form['name'])
    print(fuel)
    lis=[age,km,fuel,seller,trans,owner,milage,engine,power,seat,name]
    npar=np.array(lis)
    res1=model.predict(np.reshape(npar,(-1,11)))
    res=f"your car price is  {res1}"
    return render_template('index.html',result=res)

    '''
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],"filename.jpg"))
    #file.save("filename.jpg")
	#print('upload_image filename: ' + filename)
    #flash('Image successfully uploaded and displayed below')
    res=output('static/filename.jpg')
    res=f"Digit In Image is {res[0]}"
    return render_template('result.html',result=res)
    '''

if __name__=='__main__':
    print("app is running")
    app.run(debug=True)
    
