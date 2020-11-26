from top2vec.top2vec import Top2Vec


#top2vec = Top2Vec(documents=arr, speed="learn", workers=4)

import pandas as pd
from underthesea import word_tokenize
df = pd.read_json("/home/thetamt3/docbao/src/backend/export/article_data.json")



# chuyển dạng list[dic] về dạng list[string]
def change_type(data):
    i = 0
    st = []
    for s in data:
        i += 1

        st.append([s[str(i)]])
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
    l = []
    for i in range(len(list_d_changed)):
        list_d_changed[i] = remove_pun(list_d_changed[i][0])
        l.append([list_d_changed[i]])

    return l





# tách từ cho mỗi doc trong tập dữ liệu data, input là dạng list đã được remove dấu câu
def tokenize(sentence):
    i = 0
    l = []
    for s in sentence:
        #print(word_tokenize(st))
        l.append(word_tokenize(s[0]))
    return l


# data dùng để làm input cho tập train
print("test")


#doc file
filename = 'vietnamese_stopwords.txt'
list_stopword = []
with open(filename) as fh:
    for line in fh:
        list_stopword.append(line.strip())
#
#
#
#
def remove_stopwords(texts):
    arr=[]
    for word in texts:
        word = word.lower()
        if word not in list_stopword and word.isdigit() == False:
            arr.append(word)
    return arr

# data2 = []
# for i in range(0, len(data_token)):
#     l = remove_stopwords(data_token[i])
#     data2.append(l)
# db2 = []
# for d2 in data2:
#     db2.append(" ".join(d2))
# print(db2[1])
# print(db2[0])
# print(db2[:1])
def list_to_string(data_token):
    db=[]
    for d in data_token:

        db.append(" ".join(d))
    return db




print("result")
def train_model(db):
    top2vec = Top2Vec(documents=db, speed="learn", workers=4)
    num = top2vec.get_num_topics()
    print("num" , num)
    topic_words, word_scores, topic_nums = top2vec.get_topics(num)
    print("topic words",topic_words)
    rs = []
    for topic in topic_words:
        l = remove_stopwords(topic)
        rs.append(l)
    print("RS\n")
    for r in rs:
        print(r)
    topic_sizes, topic_nums = top2vec.get_topic_sizes()
    print("topic sizes: ",topic_sizes)
    print(("topic nums", topic_nums))
    doc= top2vec.search_documents_by_topic(2, 10,return_documents=True,reduced=False)
    print(doc)
    print(doc[len(doc)-1])
    arr = doc[len(doc)-1]
    print(type(type(arr)))
    print(arr[1])
    return rs,top2vec
def api(df):
    data = list(df['article_list'])
    d_changed = change_type(data)
    list_data = change_remove(d_changed)
    data_token = tokenize(list_data)
    db = list_to_string(data_token)
    rs,top2vec = train_model(db)
    return  rs, top2vec
api,top2vec = api(df)
topic_sizes, topic_nums = top2vec.get_topic_sizes()
list_ds = []

data = list(df['article_list'])
print(data[2])
print(data[:3])
d_changed = change_type(data)
print(d_changed[1])
print(d_changed[:1])

for i in range(len(topic_nums)):
    doc = top2vec.search_documents_by_topic(topic_sizes[i], topic_nums[i], return_documents=True, reduced=False)
    list_ds.append(doc[len(doc)-1])
for j in list_ds:
    for k in j:
        print(data[k]['href'])
        break



