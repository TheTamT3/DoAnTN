# from top2vec.top2vec import Top2Vec
#
#
# #top2vec = Top2Vec(documents=arr, speed="learn", workers=4)
#
# import pandas as pd
# from underthesea import word_tokenize
# df = pd.read_json("/home/thetamt3/docbao/src/backend/export/article_data.json")
#
#
#
# # chuyển dạng list[dic] về dạng list[string]
# def change_type(data):
#     i = 0
#     st = []
#     for s in data:
#         i += 1
#
#         st.append([s[str(i)]])
#     return st
#
# # remove dấu câu
# def remove_pun(sentence):
#     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     for ele in sentence:
#         if ele in punc:
#             sentence = sentence.replace(ele, " ")
#     return sentence
#
# # remove dấu câu trong tất cả tập dữ liệu, d_changed đang là dạng list
# def remove_pun_ele(list_ele):
#     for i in range(len(list_ele)):
#         list_ele[i] = remove_pun(list_ele[i])
#     return list_ele
#
#
# def change_remove(list_d_changed):
#     l = []
#     for i in range(len(list_d_changed)):
#         list_d_changed[i] = remove_pun(list_d_changed[i][0])
#         l.append([list_d_changed[i]])
#
#     return l
#
#
#
#
#
# # tách từ cho mỗi doc trong tập dữ liệu data, input là dạng list đã được remove dấu câu
# def tokenize(sentence):
#     i = 0
#     l = []
#     for s in sentence:
#         #print(word_tokenize(st))
#         l.append(word_tokenize(s[0]))
#     return l
#
#
# # data dùng để làm input cho tập train
# print("test")
#
#
# #doc file
# filename = 'vietnamese_stopwords.txt'
# list_stopword = []
# with open(filename) as fh:
#     for line in fh:
#         list_stopword.append(line.strip())
# #
# #
# #
# #
# def remove_stopwords(texts):
#     arr=[]
#     for word in texts:
#         word = word.lower()
#         if word not in list_stopword and word.isdigit() == False:
#             arr.append(word)
#     return arr
#
# def ds_no_stopword(data_token):
#     data2 = []
#     for i in range(0, len(data_token)):
#         l = remove_stopwords(data_token[i])
#         data2.append(l)
#     return data2
#
# print("result")
#
# def rs(df):
#     data = list(df['article_list'])
#     d_changed = change_type(data)
#     list_data = change_remove(d_changed)
#     data_token = tokenize(list_data)
#     ds = ds_no_stopword(data_token)
#     return ds,data_token
# ds,dt =rs(df)
#
#
#
#
print("HELLO WORD")