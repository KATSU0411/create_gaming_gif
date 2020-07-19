なんでもゲーミング○○のgifにしちゃうやーつ
====
![sushi](https://github.com/KATSU0411/create_gaming_gif/blob/master/imgs/gaming_sushi.gif?raw=true)
![vim](https://github.com/KATSU0411/create_gaming_gif/blob/master/imgs/gaming_vim.gif?raw=true)

こんな感じで、指定した色のみを虹色に光らせるgifを作れます  
discordやslackの治安を悪くすることができます

## 概要
HSVで指定した領域の色のHを変化させて、gifを作るだけのプログラムです  
pngにしか対応していません(多分)

## 環境
Python 3.7  
Pycharm Community Edition

## 使用方法
`filepath`と`imgname`でゲーミング化させたい画像を指定して、hsvLとhsvUを設定することで指定の色の範囲をゲーミング化させます。  
HSVの範囲は[0~180, 0~255, 0~255]ですが、hsvLのHはマイナスを指定しても問題ないです。そのうちhsvHも180超えて大丈夫なようにすると思います

そしたらoutputフォルダにゲーミングgifが保存されます  

細かいパラメータについて
- frame ・・・虹が一周するまでのフレーム数を指定できます
- duration　・・・ 1フレームの表示ミリ秒を指定できます

## ライセンス
オールフリーです。画像のライセンスにだけは気を付けてください

## 雑談
唐突にゲーミング寿司が作りたくなったから5時間くらいで作った。後悔はしてる  
気が向いたらマウス指定でゲーミング化したい場所選択できるようにするとかやるかも。気が向いたら  

あとslack等の治安悪くしたいだけならこっち使ったほうが多分いいです
https://qiita.com/zk_phi/items/8a24b8ad9d1eabd364aa
