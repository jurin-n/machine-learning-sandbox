import numpy as np
import pandas as pd
import pickle
from gensim.models import word2vec
import MeCab

tagger = MeCab.Tagger('-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

def tokenize_ja(text, lower):
    node = tagger.parseToNode(str(text))
    while node:
        if lower and node.feature.split(',')[0] in ["名詞","形容詞"]:#分かち書きで取得する品詞を指定
            yield node.surface.lower()
        node = node.next
def tokenize(content, token_min_len, token_max_len, lower):
    return [
        str(token) for token in tokenize_ja(content, lower)
        if token_min_len <= len(token) <= token_max_len and not token.startswith('_')
    ]

#学習データの読み込み

df = pd.read_csv('output/tokyo_ramen_review.csv')
df_ramen = df.groupby(['store_name','score','review_cnt'])['review'].apply(list).apply(' '.join).reset_index().sort_values('score', ascending=False)

#コーパス作成
wakati_ramen_text = []
for i in df_ramen['review']:
    txt = tokenize(i, 2, 10000, True)
    wakati_ramen_text.append(txt)
np.savetxt("output/ramen_corpus.txt", wakati_ramen_text, fmt='%s', delimiter=',')
# モデル作成
word2vec_ramen_model = word2vec.Word2Vec(wakati_ramen_text, sg=1, size=100, window=5, min_count=5, iter=100, workers=3)
#sg（0: CBOW, 1: skip-gram）,size（ベクトルの次元数）,window（学習に使う前後の単語数）,min_count（n回未満登場する単語を破棄）,iter（トレーニング反復回数）

# モデルのセーブ
word2vec_ramen_model.save("output/word2vec_ramen_model.model")

