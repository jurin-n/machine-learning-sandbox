# 概要
下記２つのQiita記事参考にword2vec試してみた。ログをコミット。
https://qiita.com/toshiyuki_tsutsui/items/f143946944a428ed105b
https://qiita.com/toshiyuki_tsutsui/items/19590b464f15f845efcd

# 試した環境
* OSは、ubuntu 18.04.1
* ストレージは30GB
* メモリは4GB

# ubuntuセットアップ内容
### Mecabインストール
* 参考記事 https://qiita.com/ekzemplaro/items/c98c7f6698f130b55d53
* 参考記事のやり方だとmakeエラーになるので、この記事参考に対処。https://qiita.com/isogai3104/items/f9bfa23b850dd53a331a
* curl使ってるらしいのでインストール(sudo apt install curl) https://qiita.com/siraasagi/items/e07e0b271cb7cd679a70


### python周りセットアップ
```
sudo apt-get install python3-venv
sudo apt-get install swig
python3 -m venv ~/python_venv/sandbox_nlp
source ~/python_venv/sandbox_nlp/bin/activate
sudo apt install python3-pip
sudo pip3 install mecab-python3
```
