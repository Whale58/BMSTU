from crypt import methods
import flask
from flask import render_template
import pickle
import sklearn
from sklearn.linear_model import LinearRegression
import tensorflow as tf

app = flask.Flask(__name__, template_folder = 'templates')


@app.route('/')
def choose_prediction_method():
    return render_template('main.html')


def mu_prediction(params):
    model = tf.keras.models.load_model('models/model_3')
    pred = model.predict([params])
    return pred



@app.route('/', methods=['POST', 'GET'])
def mu_predict():
    message = ''
    if request.method == 'POST':
        mf = request.form.get('mf')
        
        pl = request.form.get('pl')
        
        mup = request.form.get('mup')
        
        ko = request.form.get('ko')
        
        seg = request.form.get('seg')
        
        tf = request.form.get('tf')
        
        pp = request.form.get('pp')
        
        ps = request.form.get('ps')
        
        an = request.form.get('an')
        
        shn = request.form.get('shn')
        
        pn = request.form.get('pn')
        
        params = [mf, pl, mup, ko, seg, tf, pp, ps, an, shn, pn]
        params = [float(i) for i in params]

        message = f'Прогноз Модуля упругости при растяжении для введенных параметров: {mu_prediction(params)} ГПа'
    return render_template('main.html', message=message)

if __name__ == '__main__':
    app.run()
