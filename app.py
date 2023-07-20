import os, sys
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from flask import Flask, escape, request,  Response, g, make_response
from flask.templating import render_template
import AI_model
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
app.debug=True
 
# Main page
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/nst_get',methods=['GET','POST'])
def nst_get():
    return render_template('nst_get.html')
 
 
@app.route('/nst_post', methods=['GET','POST'])
def nst_post():
    if request.method == 'POST':
        uploadedFiles = request.files.getlist("file[]")
        plist=[]
        for f in uploadedFiles:
            f.save('/Users/ihaemin/Desktop/codeep-flask2/vscode/static/images/'+str(f.filename))
            plist.append('/Users/ihaemin/Desktop/codeep-flask2/vscode/static/images/'+str(f.filename))

    resized_image = AI_model.preprocess(plist)
    resized_image.save('/Users/ihaemin/Desktop/codeep-flask2/vscode/static/images/final.png')
    resized_image_path= '/Users/ihaemin/Desktop/codeep-flask2/vscode/static/images/final.png'

    result = AI_model.main(resized_image_path)
    return render_template('nst_post.html',final_img=resized_image_path, result=result)

app.run()