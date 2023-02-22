  ## 【概要】
・コーディングテストで用いた素数判定アルゴリズムをメソッド化した。  
・ふと、隣合う素数同士の乖離率が気になり、pandasやpandas-ta(technical-analysis)を用いて分析し、  
  matplotlibでチャート出力できるようにした。  
・それらをAPIサーバとして利用できるよう、Fastapiでシンプルに実装した。  
## 【経緯】
コーディングテストに悔いが残ったので、追加で挑戦した。   
## 【/archive】
archiveディレクトリには、コーディングテストの記録が残っている。  
## 【/python/main.py】
PrimeNumberCheckerというクラスを作成した。 
   
is_primeメソッドやis_twin_primeメソッドを用いて、指定範囲の素数及び双子素数を取得することができる。  

### 前後の素数の乖離分析
また、primeNumber_pctChangeメソッドを用いることで、素数と次の素数の乖離比率を算出し、  
matplotlibを用いてチャート画像を生成することができる。 

![alt text](https://github.com/v3vapp/storage/blob/main/img/result.png?raw=true)
 (複数の一直線がなだらかに減少していることが伺える)  
   
・ピンクのドットは、前後の素数の乖離比率である。  
・素数の乖離比率の単純移動平均（SMA）を算出し青い線で表示している。   
・赤い線では、移動平均線の±1sigma（標準偏差）を計算し、表示している。   
 
出力したPNG画像は、staticディレクトリに保存される。  
    
## 【root/app.py】
ルートのapp.pyは、fastapiで実装したwebAPIである。  
ユーザーが素数検証範囲や単純移動平均データの取得数をカスタマイズすることができる。  
API利用時の認証やセキュリティについては、まだ手を加えられていない。  
動作確認する場合は、レポジトリをクローンし、下記のコマンドを用いる。  
```
uvicorn app:app --reload  
```
また、/docs へアクセスすることでswaggerでの動作検証を行える。  
```
http://localhost:8000/docs
```
エンドポイントは、以下のようになる。
```
http://127.0.0.1:8000/v1/prime_number
```
リクエストボディは、以下のように検証指数の最小値と最大値と、単純移動平均の参照数（オプション）が必要となる。  
単純移動平均の参照数（オプション）を省く場合、デフォルト数の30が適応される。  
```
{
  "minimum": 5000,
  "maximum": 8000,
  "sma_length": 30
}
```
リターンは「素数のリスト」「双子素数のペアのリストを内包するリスト」「乖離率の分析結果画像のパス情報」である。  
具体的には、以下のようになる。簡略化のため、上記のリクエストとは対応していない。  

```
{
  "prime_list": [2, 3, 5, 7], 
  "twin_prime_list": [[3, 5], [5, 7]], 
  "img_path": "static/result.png"
}
```
### ※ デプロイについて
このAPIを自力でコンテナ化してGCPへデプロイ（CDCIの構築）や、Heorkuに継続的にデプロイすることも可能である。  

### ※ 分析データの可視化について
分析結果のイメージを共有するには、いくつかの方法が考えられるが、最も理想的なのは、  
分析結果のデータをクライアントに返し、cahrtJS等でブラウザ上でチャートを表示させることだ。   
フロントエンドを実装時間すれば、このシステムでのmatplotlibは、本番環境でにおいて不要となる。  

## 【/examples】
examplesディレクトリには、ロジスティック回帰を用いて素数の発生予想を行うコードがある。  
これは、基本的にchatGPTが出力したものであり、あくまでサンプル・私の勉強用である。  
「エラトステネスのふるい」という素数判定法を、面接後に見つけ、組み合わせた。  
機械学習の本質を深く理解したいと思い、線形代数や確率統計や微分等の分野を基礎から学んでいる。  
 
## 【最後に】
冒頭でも記述しましたが、コーディング面接で満足いく回答ができず、悔しい気持ちが残ったためこのシステムを開発した。  
面接を受けた日の夜に、5-6時間で完成させたため、第三者がコードを参考にする際は、十分な注意が必要である。  
（利用機会はないとは思いますが...笑）    
   
以上。  
