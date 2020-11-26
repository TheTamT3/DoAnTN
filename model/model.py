from top2vec.top2vec import Top2Vec
from gensim.models.coherencemodel import CoherenceModel
import gensim.corpora as corpora
import pandas as pd
from underthesea import word_tokenize
import datetime
df = pd.read_json("/home/thetamt3/docbao/src/backend/export/article_data.json")

# chuyển dạng list[dic] về dạng list[string]
def change_type(data):
    i = 0
    st = []
    for s in data:
        i += 1
        st.append([s['content']])
    return st

# remove dấu câu
def remove_pun(sentence):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in sentence:
        if ele in punc:
            sentence = sentence.replace(ele, " ")
    return sentence
# remove dấu câu trong tất cả tập dữ liệu, d_changed đang là dạng list
def remove_pun_ele(list_ele):
    for i in range(len(list_ele)):
        list_ele[i] = remove_pun(list_ele[i])
    return list_ele
def change_remove(list_d_changed):
    list_removed = []
    for i in range(len(list_d_changed)):
        list_d_changed[i] = remove_pun(list_d_changed[i][0])
        list_removed.append([list_d_changed[i]])
    return list_removed

# tách từ cho mỗi doc trong tập dữ liệu data, input là dạng list đã được remove dấu câu
def tokenize(sentence):
    i = 0
    l = []
    for s in sentence:
        l.append(word_tokenize(s[0]))
    return l

def remove_stopwords(texts):
    # doc file
    filename = 'vietnamese_stopwords1.txt'
    list_stopword = []
    with open(filename) as fh:
        for line in fh:
            list_stopword.append(line.strip())
    arr=[]
    for word in texts:
        word = word.lower()
        if word not in list_stopword and word.isdigit() == False:
            arr.append(word)
    return arr

def token_to_stopword(data_token):
    data2 = []
    for i in range(0, len(data_token)):
        l = remove_stopwords(data_token[i])
        data2.append(l)
    db2 = []
    for d2 in data2:
        db2.append(" ".join(d2))
    return db2

def list_to_string(data_token):
    db=[]
    for d in data_token:

        db.append("_".join(d))
    return db


def train_model(db, numKey = 50):
    top2vec = Top2Vec(documents=db, speed="learn", workers=4)
    num = top2vec.get_num_topics()
    print("Number newspaper: " , num)
    topic_words, word_scores, topic_nums = top2vec.get_topics(num)
    # print("topic words",topic_words)
    rs = []
    for topic in topic_words:
        # l = remove_stopwords(topic)
        rs.append(topic[:15])
    # print("RS\n")
    for r in rs:
        print("_".join(r))
    # topic_sizes, topic_nums = top2vec.get_topic_sizes()
    # print("topic sizes: ",topic_sizes)
    # print(("topic nums", topic_nums))
    # doc= top2vec.search_documents_by_topic(2, 10,return_documents=True,reduced=False)
    # print(doc)
    return rs,top2vec
def api(df):
    data = list(df['article_list'])
    data_changed = change_type(data)
    list_data = change_remove(data_changed)
    data_token = tokenize(list_data)
    db = token_to_stopword(data_token)
    # db = list_to_string(data_token)
    rs,top2vec = train_model(db)
    return rs, top2vec
# datetime_object1 = datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S")
# print("INPUT TIME",datetime_object1)
# rs,top2vec = api(df)
# datetime_object2 = datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S")
# print("OUTPUT TIME",datetime_object2)
# def getTimeModel():
#     return datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S")
# # a = top2vec.generate_topic_wordcloud(10)
def document_similar_topic(top2vec,df):
    topic_sizes, topic_nums = top2vec.get_topic_sizes()
    print("topic", topic_nums)
    print("check", topic_sizes)
    num_list_ds = []
    score_list=[]
    for i in range(len(topic_nums)):
        doc = top2vec.search_documents_by_topic(topic_nums[i], topic_sizes[i], return_documents=True, reduced=False)

        num_list_ds.append(doc[len(doc) - 1])
        # score_list.append(doc[1][i])
    # for i in doc[1]:
    #     score_list.append(i)
    data = list(df['article_list'])
    ds_topic = []
    #
    for j in num_list_ds:
        count = 0
        ele_ds_topic = []
        for k in j:
            count += 1
            # print(data[k]['href'])
            ele_ds_topic.append({"topic": data[k]['topic'],
                                 "link": data[k]['href'],
                                 "sapo": data[k]['sapo'],
                                 "newspaper": data[k]['newspaper'],
                                 "publish": data[k]['publish_time'],
                                 "count":k

                                 })
        ds_topic.append(ele_ds_topic)
    return ds_topic,topic_nums,topic_sizes
rs,top2vec = api(df)
# document_similar_topic(top2vec,df)
def document_similar_document(top2vec,ID,df):
    data = list(df['article_list'])
    doc= top2vec.search_documents_by_documents([ID],20)
    ids_similar_doc = doc[2]
    score_doc_similar = doc[1]
    doc_similar=[]
    count = 0
    for i in ids_similar_doc:

        doc_similar.append({"topic":data[i]['topic'],
                            "link":data[i]['href'],
                            "score": score_doc_similar[count],
                            "newspaper": data[i]['newspaper'],
                            "publish": data[i]['publish_time'],

                            })
        count +=1
    return doc_similar



