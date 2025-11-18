from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('5g_allocation.pkl', 'rb'))


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():

    application_type = request.form['at']
    if(application_type=="bd"):
        application_type=0
    elif(application_type=="es"):
        application_type=1
    elif(application_type=="fd"):
        application_type=2
    elif(application_type=="it"):
        application_type=3
    elif(application_type=="og"):
        application_type=4
    elif(application_type=="str"):
        application_type=5
    elif(application_type=="vc"):
        application_type=6
    elif(application_type=="vs"):
        application_type=7
    elif(application_type=="vpc"):
        application_type=8
    elif(application_type=="vic"):
        application_type=9
    elif(application_type=="wb"):
        application_type=10
    signal_strength = request.form['ss']
    latency = request.form['lt']
    required_bandwidth = request.form['rb']
    allocated_bandwidth = request.form['ab']

    t = [[float(application_type), float(signal_strength), float(latency), float(required_bandwidth), float(allocated_bandwidth)]]
    output = model.predict(t)
    print(output)


    return render_template('index.html', y = "The predicted Resource_Allocation is  "+str(np.round(output[0])))

if __name__ == '__main__':
    app.run(debug=True) 