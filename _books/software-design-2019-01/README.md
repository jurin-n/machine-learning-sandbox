## 概要 
機械学習勉強用。
雑誌 Software Design 2019年1月号[https://gihyo.jp/magazine/SD/archive/2019/201901](https://gihyo.jp/magazine/SD/archive/2019/201901) 
の第一特集 "ITエンジニアのための機械学習と線形代数入門"に掲載のコードを写経。

## 環境作成
#### バーチャル環境作成 *初回のみ
```
conda create --name ml-sandbox
```

#### バーチャル環境へ切り替え
```
source activate ml-sandbox
```

#### 作成したバーチャル環境をjupyterのkernelとして使えるように設定
```
ipython kernel install --user --name=ml-sandbox --display-name=ml-sandbox
```

#### Jupyter Notebook起動
```
jupyter notebook  --no-browser
```

#### バーチャル環境無効化
```
source deactivate
```

