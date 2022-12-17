from flask import Flask,render_template

from flask import request as rq
from keras.models import load_model
import numpy as np
from keras_preprocessing.sequence import pad_sequences
from underthesea import word_tokenize
from static.connect_SQL_server import *

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" # disable gpu

max_len = 78
# my model
# model = load_model('model_3_BiLSTM.h5')
model = load_model('static/2_cnn.h5')

decode = {
    0 : 'sản phẩm xấu chất lượng kém',
    1 : 'sản phẩm tạm chấp nhận',
    2 : 'chất lượng sản phẩm tuyệt vời',
    3 : 'cửa hàng phục vụ quá tệ',
    4 : 'cửa hàng phục vụ tốt chăm sóc khách hàng tuyệt vời'
}
word_id = {}


# Load từ điển
with open('word (1).txt','r',encoding='utf-8') as f:
    dem = 1
    for word in f.read().split('\n'):
        word_id[word] = dem
        dem += 1

def process(text):
    text = text.lower()
    text = word_tokenize(text,format='text')
    text = text.strip()
    return text
def chuyenCauThanhSo(cau):
    return [word_id[word] for word in cau.split() if word in word_id.keys()]

def predict(model,text):
    arr = []
    for cau in text.split('.'):
        cau = process(cau)
        print(cau)
        s = chuyenCauThanhSo(cau)
        if len(s)>0:
            s = pad_sequences([s],maxlen=max_len,padding='post')
            pre = model.predict(s)
            print(pre.max())
            arr.append(np.argmax(pre))
    return arr
def insert_comment(comment):
    cnxn,cursor = connection_SQL();
    try:
        insert_DATA(comment,result,cnxn,cursor)
    except ValueError:
        print(ValueError)
    cursor.close()
    cnxn.close()

app = Flask(__name__,template_folder='template',static_folder='static')

@app.route("/",methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route("/predict",methods=['GET','POST'])

def r_predict():
    try:

        if 'comment' in rq.form.keys():
            print('-----------------------------------------')
            text_post = rq.form['comment']
            label_arr = predict(model,text_post)
            kq = [decode[i] for i in label_arr]
            print(kq)
            result = ', '.join(kq) if (len(', '.join(kq).strip())>0) else 'thong tin khong hop le'
            print(result)
            #insert_comment(result)
            cnxn,cursor = connection_SQL();
            try:
                insert_DATA(text_post,result,cnxn,cursor)
            except ValueError:
                print(ValueError)
            
            print('-----------------------------------------')
            return result
        return 'thong tin khong hop le'
    except Exception as e:
        return str(e)


if __name__ == "__main__":


    app.run(debug=True)