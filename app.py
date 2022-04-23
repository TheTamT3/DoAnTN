from flask import Flask,request, render_template
import  pandas as pd
from model import model
import threading
from threading import Timer
import datetime
from apscheduler.schedulers.background import BackgroundScheduler


#app
app = Flask(__name__)
def getData():
    df = pd.read_json("/home/thetamt3/docbao/src/backend/export/article_data_13_11.json")
    result, top2vec = model.api(df)
    time = datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S")
    print("GET DATA OK")
    return  result,top2vec,df,time

result,top2vec,df,time = getData()


@app.route('/',methods = ['POST','GET'])
def index():
    dic ={}
    date_time = time
    # print(result)
    ds,topic_nums,topic_sizes =  model.document_similar_topic(top2vec,df)
    legend = "month"
    if request.method == "POST":
        numKey = int(request.form['numKey'])
        for i in range(len(result)):
            dic[i] = " - ".join(result[i][:numKey])
        return render_template('index.html', array=dic, date_time=date_time,labels = topic_nums,values1 = topic_sizes,legend=legend)
    for i in range(len(result)):
        dic[i] = " - ".join(result[i][:10])

    return render_template('index.html', array=dic, date_time=date_time, labels=topic_nums, values=topic_sizes)


@app.route('/listdoc/<id>',methods = ['POST','GET'])
def doc_topic(id):
    list_topic,top_nums,top_sizes = model.document_similar_topic(top2vec,df)
    data = list(df['article_list'])
    list_new_newspaper = data[:10]
    return render_template('index2.html',list_topic = list_topic[int(id)],list_new_newspaper=list_new_newspaper)


@app.route('/doc/<id_news>',methods = ['POST','GET'])
def doc_to_doc(id_news):
    list_doc_similar = model.document_similar_document(top2vec,int(id_news),df)
    return render_template('index3.html',list_doc_similar = list_doc_similar)


if __name__ == '__main__':
        app.run(debug=True)
