https://qiita.com/toshiyuki_tsutsui/items/f143946944a428ed105b
https://qiita.com/toshiyuki_tsutsui/items/19590b464f15f845efcd



# Mecabインストール
参考サイト
https://qiita.com/taroc/items/b9afd914432da08dafc8

brew install mecab
brew install mecab-ipadic


brew install git curl xz
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n


https://teratail.com/questions/163226
参考し、command line tools 9.4をインストール

brew install swig
/pip install mecab-python3
pip uninstall mecab-python3
pip install mecab-python3==0.7


echo `mecab-config --dicdir`"/mecab-ipadic-neologd"

```
import MeCab

#mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab = MeCab.Tagger('-d /Users/junnakano/git/machine-learning-sandbox/word2vec/mecab-ipadic-neologd/build/mecab-ipadic-2.7.0-20070801-neologd-20190228')


text = '解析したいテキスト'
mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    print('{0} , {1}'.format(word, pos))
    #次の単語に進める
```
