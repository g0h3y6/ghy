import wordcloud
import jieba
import jieba.analyse
import numpy
from matplotlib import pyplot as plt
from nltk.text import TextCollection

def create_stopwordlist(location):#创建停用词表
    stop_word_list=[]#存储停用词的list
    with open(location,'r',encoding='UTF-8') as s:#遍历停用词表文档，构建停用词list
        slines=s.readlines()
        for line in slines:
            stop_word_list.append(line.strip())#strip是去除每行字词附带的回车符和空格之用，这是经过之前测试失败得到的方法
    stop_word_list.append('\n')#同时，上面的strip操作也不可避免地让停用词表少去了空格和回车符，现在需要再加上
    stop_word_list.append(' ')    
    return stop_word_list

def pre_segcut(a):
    pre=jieba.cut(a,cut_all=False)#精确模式
    return pre

def cn_divide(location,stop_word_list):
    segs=[]#用于存储分词后字段的list
    seg=[]#用于存储分词后各个句子的分词list的list
    all_sentences1=str()#将所有评论连接在一起的字符串
    with open(location,'r',encoding='UTF-8') as f:#遍历文本数据，经过分词构建词语汇总表
        flines=f.readlines()
        for line in flines:
            a=pre_segcut(line)
            seg_sub=[]
            for i in a:#在对每一条评论进行分词的同时，直接把分得的词汇使用停用词表筛选一遍
                if i not in stop_word_list:
                    all_sentences1+=i
                    seg_sub.append(i)
                    segs.append(i)
            seg.append(seg_sub)
    return segs,seg,all_sentences1

def en_divide(f_location,stop_word_list):
    segs1=[]#用于存储分词后字段的list
    seg1=[]#用于存储分词后各个句子的分词list的list
    with open(f_location,'r',encoding='UTF-8') as f:#遍历文本数据，经过分词构建词语汇总表
        flines=f.readlines()
        for line in flines:
            b=line.split()
            seg_sub1=[]
            for i in b:#在对每一条评论进行分词的同时，直接把分得的词汇使用停用词表筛选一遍
                if i not in stop_word_list:
                    seg_sub1.append(i)
                    segs1.append(i)
            seg1.append(seg_sub1)    
    return segs1,seg1

def en_keywords(segs1,seg1,topK1):
    segs_set1=set(segs1)#利用集合中不重复出现元素的特性，将原来的字段做成集合便于分类计算
    base=TextCollection(seg1)#根据语料构建语料库
    tf_idf_list=[]#存储各个词语的tf-idf值与其本身构成的元组，依据tf-idf值进行排序得到关键词
    for p in segs_set1:
        tf_idf_list.append((p,base.tf_idf(p,base)))
    for j in range(len(tf_idf_list)-1):#依然是冒泡排序
        for i in range(len(tf_idf_list)-1-j):
            if tf_idf_list[i][-1]<tf_idf_list[i+1][-1]:#取元组的末位，也就是说把tf-idf进行比较排序
                tf_idf_list[i],tf_idf_list[i+1]=tf_idf_list[i+1],tf_idf_list[i]
    keywords1=[]#英文关键词表
    for i in range(topK1):#按照tf-idf值从大到小的顺序构建关键词表
        temp=tf_idf_list[i][0]
        keywords1.append(temp)
    return keywords1

def frequency_write(location_w,segs):
    segs_set=set(segs)#利用集合中不重复出现元素的特性，将原来的字段做成集合便于分类计算
    frequency_list=[]#建立一个存储(词语,词频)元组的列表
    for p in segs_set:
        frequency_list.append((p,segs.count(p)))
    for j in range(len(frequency_list)-1):#大计基时代学的冒泡排序，因为是二元的元组，没有办法用Python内置的sort函数，那就用这个算法按词频给关键词排序吧
        for i in range(len(frequency_list)-1-j):
            if frequency_list[i][-1]<frequency_list[i+1][-1]:#取元组的末位，也就是说把词频进行比较排序
                frequency_list[i],frequency_list[i+1]=frequency_list[i+1],frequency_list[i]
    with open(location_w,'w',encoding='UTF-8') as w:#写入排序后的词频元组
        for i in frequency_list:
            w.write(str(i)+'\n')    

def vector_list_write(location_w,seg,keywords,topK):
    vector_list=[]#存储生成的向量表示
    with open(location_w,'a',encoding='UTF-8') as w:#按行写入生成的向量
        w.write('关键词：'+str(keywords)+'\n')
        for i in seg:#借助每一行数据分词后提取的list生成向量
            vector=numpy.array([0 for i in range(topK)])
            for j in range(topK):
                if keywords[j] in i:
                    vector[j]=i.count(keywords[j])
            vector_list.append(vector)
            w.write(str(vector)+'\n')
    return vector_list

def write_sentence(location,location_w,vector_list):
    all_vaild_num=len(vector_list)#测算向量个数
    vector_list=numpy.array(vector_list)
    G_vector=numpy.array(numpy.sum(vector_list,axis=0))/all_vaild_num#计算列和平均以得出重心向量
    distances=[]#采取欧氏距离并按序存储
    for i in vector_list:
        dis=(sum((G_vector-i)**2))**(1/2)
        distances.append(dis)
    min_dis=min(distances)#取最小距离

    sp_num=[]#最终具有代表性话语所在的行数
    for i in range(all_vaild_num):#遍历寻找最小值所在位置
        if min_dis==distances[i]:
            sp_num.append(i)

    with open(location,'r',encoding='UTF-8') as f:#重新读取文件，根据存储的索引找到所在行
        with open(location_w,'a',encoding='UTF-8') as w:#写入代表性的语句
            flines=f.readlines()
            for p in sp_num:
                w.write(flines[p])    

def main():
    stop_words=r"D:/Files/计算机程序设计/现代程序设计技术/作业数据/stopwords_list.txt"#停用词表的路径
    stop_word_list=create_stopwordlist(stop_words)

    location=r"D:/Files/计算机程序设计/现代程序设计技术/作业数据/online_reviews_texts.txt"#处理文件的路径
    location_w=r'D:/Files/计算机程序设计/现代程序设计技术/作业/中文.txt'
    segs,seg,all_sentences1=cn_divide(location,stop_word_list)

    frequency_write(location_w,segs)
    
    topK=30#关键词个数
    keywords=jieba.analyse.extract_tags(all_sentences1,topK=topK)#直接使用jieba内置的TF-IDF算法生成关键词列表以作为特征集
    vector_list=vector_list_write(location_w,seg,keywords,topK)

    write_sentence(location,location_w,vector_list)


    f_location=r"D:/Files/计算机程序设计/现代程序设计技术/作业数据/tweets_apple_stock.txt"
    f_location_w=r'D:/Files/计算机程序设计/现代程序设计技术/作业/english.txt'
    segs1,seg1=en_divide(f_location,stop_word_list)

    frequency_write(f_location_w,segs1)
    topK1=30#关键词个数
    keywords1=en_keywords(segs1,seg1,topK1)

    vector_list1=vector_list_write(f_location_w,seg1,keywords1,topK1)

    write_sentence(f_location,f_location_w,vector_list1)

    #开始做词云
    font=r'C:/Windows/Fonts/XBSJT.ttf'
    font1=r'C:/Windows/Fonts/cambria.ttc'

    wcd1=wordcloud.WordCloud(font_path=font,background_color='orange',width=800,height=1000).generate(' '.join(segs))
    plt.imshow(wcd1)
    plt.axis('off')
    plt.show()

    wcd2=wordcloud.WordCloud(font_path=font1,background_color='orange',width=800,height=1000).generate(' '.join(segs1))
    plt.imshow(wcd2)
    plt.axis('off')
    plt.show()

if __name__=='__main__':main()