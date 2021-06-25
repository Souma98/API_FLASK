from flask import Flask, render_template, request
from FC import recommended_texts1
from FC import recommended_texts2


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/getRec')
def getRec():
	return render_template('getRec.html')

@app.route('/showRec',methods=['POST', 'GET'])
def showRec():
    if request.method == 'POST':  
        user_id = request.form.get('user_id')
        recommandations1=recommended_texts1(user_id)
        recommandations2=recommended_texts2(user_id)
        
    return render_template('showRec.html', user_id=user_id, recommandations1=recommandations1,recommandations2=recommandations2  )
        
@app.route('/getSim')
def getSim():
	return render_template('getSim.html')


@app.route('/showSim',methods=['POST', 'GET'])
def showSim():
    if request.method == 'POST':  
        title_text = request.form.get('title_text')
        #similarities=recommended_texts(user_id)
        similarities=""
    return render_template('showSim.html', title_text=title_text, similarities=similarities  )



if __name__ == '__main__':
   app.run(port = 5000, debug = True)
   print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
   #load_keras_model()