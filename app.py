from flask import Flask, render_template, send_file, request
import pandas as pd
import os
import json

app = Flask(__name__, static_url_path="/static/")

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

def get_split_info(split_name):
    file_name = split_name+'.csv'
    df = pd.read_csv(f'annotations/raw_splits/{file_name}')
    num_total = len(df['image_id'])
    num_completed = 0
    if file_name in os.listdir('annotations/annotate/'):
        annotate = pd.read_csv(f"annotations/annotate/{file_name}")
        num_completed = len(annotate['image_id'])
    return {'numTotal' : num_total, 'numCompleted' : num_completed, 'splitName' : split_name}

@app.route('/info/<split_name>', methods=['GET', 'POST'])
def get_info(split_name):
    return get_split_info(split_name)

def getImage(split_name):
    file_name = split_name+'.csv'
    df = pd.read_csv(f'annotations/raw_splits/{file_name}')
    if file_name in os.listdir('annotations/annotate/'):
        print('present')
        annotate = pd.read_csv(f"annotations/annotate/{file_name}")
        imgs_ = list(set(df['image_id']).difference(set(annotate['image_id'])))
        print(len(imgs_))
    else:
        imgs_ = list(df['image_id'])
    img_id = imgs_[0]
    row = df[df['image_id'] == img_id]
    if len(row) > 0:
        row = row.to_dict(orient='records')[0]
        row['image_id'] = row["image_id"]+".jpg"
    else:
        row = None
    return row

@app.route('/save_info/<split_name>', methods = ['GET', 'POST'])
def save_info(split_name):
    file_name = split_name+'.csv'
    data = {
        'age' : request.form['age'],
        'dataset' : request.form['dataset'],
        'dx' : request.form['dx'],
        'dx_type' : request.form['dx_type'],
        'image_id' : request.form['image_id'].split('.')[0],
        'lesion_id' : request.form['lesion_id'],
        'localization' : request.form['localization'],
        'sex' : request.form['sex'],

        'dark_corner' : request.form['dark_corner'],
        'hair' : request.form['hair'],
        'gel_border' : request.form['gel_border'],
        'bubble' : request.form['bubble'],
        'ruler' : request.form['ruler'],
        'ink' : request.form['ink'],
        'patches' : request.form['patches'],
    }

    if file_name in os.listdir('annotations/annotate/'):
        df = pd.read_csv(f'annotations/annotate/{file_name}')
        df_dictionary = pd.DataFrame(data, index=[0])
        df = pd.concat([df, df_dictionary], ignore_index=True)
    else:
        df = pd.DataFrame(data, index=[0])

    df.to_csv(f'annotations/annotate/{file_name}', index=False)
    return "updated"

@app.route('/get_image/<image_name>')
def get_image(image_name):
    image_path = 'data/imgs/'+image_name
    return send_file(image_path, mimetype='image/jpeg')

@app.route('/annotate/<split_name>', methods=['GET', 'POST'])
def annotate(split_name):
    data = get_split_info(split_name)
    img_info = getImage(split_name)
    return render_template('annotate.html', 
                           fileName=data['splitName'], 
                           numCompleted=data['numCompleted'],
                           numTotal = data['numTotal'], 
                           imgInfo= img_info
                           )    

if __name__=="__main__":
    app.run(debug=True, )