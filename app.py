from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/info/<split_name>')
def get_info(split_name):
    file_name = split_name+'.csv'
    df = pd.read_csv(f'annotations/raw_splits/{file_name}')
    num_total = len(df['image_id'])
    num_completed = 0
    if file_name in os.listdir('annotations/annotate/'):
        annotate = pd.read_csv(f"annotations/annotate/{file_name}")
        num_completed = len(annotate['image_id'])
    return {'numTotal' : num_total, 'numCompleted' : num_completed, 'splitName' : split_name}

@app.route('/annotate/<split_name>')
def annotate(split_name):
    return render_template('annotate.html')    

if __name__=="__main__":
    app.run(debug=True, )