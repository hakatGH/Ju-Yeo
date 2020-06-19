import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import cx_Oracle
import os
os.putenv('NLS_LANG','KOREAN_KOREA.KO16MSWIN949')
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

#전통주 술 정보 데이터베이스 호출
ora = cx_Oracle.connect("hr/hr@LocalHost:1521/XE")
tak = pd.read_sql("select * from liquorinfo",con=ora)
kwd = pd.read_sql("select * from keyword_set",con=ora)
kwd = kwd.sort_values(by='FREQ',ascending=False)


    


class sulrecom(): #본격적으로 추천을 위한 클래스
    def yoursul(self,kwd): #키워드 검색용 타겟 주류 추가 함수
        tak = pd.read_sql("select * from liquorinfo",con=ora)
        kwdtak = tak
        NEWDATA = {'IDX': 0, 'ALCOHOL_NAME': '당신의 술', 'ETC': kwd}
        kwdtak = kwdtak.append(NEWDATA,ignore_index=True)
        kwdtak = kwdtak.fillna('None')
        return kwdtak

    def removenan(self,li): #키워드 집합에서 결측치를 제거해주는 함수
        for i in range(len(li)):
            if(li.count('None') != 0):
                li.remove('None')
            else:
                return list(li)

    def method_pre(self,tak): #각각의 키워드들을 '키워드'라는 하나의 항목으로 모두 합치는 작업
        features = ['INCENSE','SWEET','ACIDITY','SKIPPING','ETC']
        tak['FLAVOR'] = tak['FLAVOR'].apply(lambda x: str(x))
        tak['KEYWORD'] = tak['FLAVOR'].apply(lambda x: x.split('/'))
        for ft in features:
            tak[ft] = tak[ft].apply(lambda x: str(x))
            tak[ft] = tak[ft].apply(lambda x: x.split('/'))
            tak['KEYWORD'] = tak['KEYWORD'] + tak[ft]
        tak['KEYWORD'] = tak['KEYWORD'].apply(self.removenan)
        tak['KEYWORD'] = tak['KEYWORD'].apply(lambda x : ' #'.join(x))
        return tak

    def method_recom(self,tak): #키워드 column을 이용해서 각 술별 유사도를 측정하는 함수
        tak = self.method_pre(tak)
        tfidf = TfidfVectorizer()
        kwd_mat = tfidf.fit_transform(tak['KEYWORD'])#각각의 키워드들을 가지고 tf-idf 가중치 설정
                                                    #각 키워드들의 중요도를 찾는 작업으로, 전체 문서에서 해당 키워드가 적게 쓰일수록 해당 문서의 고유한 특성으로 취급됨
        kwd_sim = cosine_similarity(kwd_mat, kwd_mat)#코사인 유사도를 이용해서 각 주류의 키워드 사이의 유사도 측정
        kwd_sim_sorted_ind = kwd_sim.argsort()[:, ::-1]# 그 유사도를 수치를 기반으로 정렬을 한 인덱스
        print(sorted(tfidf.vocabulary_.items()))
        print('##############################################')
        print(kwd_mat)
        print('##############################################')
        print(kwd_sim)
        return kwd_sim_sorted_ind # 그 정렬된 인덱스 반환

def simsul(sul,sim_name,sulname):#입력된 문자열이 포함된 술 이름들을 리스트로 묶어서 반환
    if sulname in sul:
        sim_name.append(sul)

def sulgle(df,title_name):#술의 이름을 입력받아서 검색을 하는 함수
    sim_name =[]
    df['ALCOHOL_NAME'].apply(lambda x: simsul(x,sim_name,title_name))
    print(df.loc[df['ALCOHOL_NAME'].isin(sim_name)])
    return df.loc[df['ALCOHOL_NAME'].isin(sim_name)]

        
def find_sim_ju(df, sorted_ind, title_name, top_n):#
    
    sulname = df[df['ALCOHOL_NAME'] == title_name]
    # sulname을 가진 DataFrame의 index 객체를 ndarray로 반환하고 
    # sorted_ind 인자로 입력된 genre_sim_sorted_ind 객체에서 유사도 순으로 top_n 개의 index 추출
    title_index = sulname.index.values
    similar_indexes = sorted_ind[title_index, :(top_n)+1]
    
    # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임. 
    #dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    similar_indexes = similar_indexes.reshape(-1)
    return df.iloc[similar_indexes]

def find_sim_ju1(df, sorted_ind, title_name, top_n):#
    
    sulname = df[df['ALCOHOL_NAME'] == title_name]
    # sulname을 가진 DataFrame의 index 객체를 ndarray로 반환하고 
    # sorted_ind 인자로 입력된 genre_sim_sorted_ind 객체에서 유사도 순으로 top_n 개의 index 추출
    title_index = sulname.index.values
    similar_indexes = sorted_ind[title_index, 1:(top_n)+1]
    
    # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임. 
    #dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    similar_indexes = similar_indexes.reshape(-1)
    return df.iloc[similar_indexes]
