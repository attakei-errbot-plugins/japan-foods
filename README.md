# 勝どきご飯 for Errbot

勝どきでご飯を食べたい人向けのErrbotプラグインです。

## 事前に用意するもの

* ぐるなびWebサービス用のAPIキー
* Recruit Web Services用のAPIキー

## Errbotへのインストール

### チャットから

基本的には、チャットツール上の管理コマンドで有効にしてください

```
!repos install https://github.com/attakei-errbot-plugins/kachidoki-foods 
```

### Git管理で

```
$ git submodule add plugins/kachidoki-foods https://github.co/attakei-errbot-plugins/kachidoki-foods
```

## 使い方

### 1. 事前にAPIキーをセットする

```
!plugin config KachidokiFoods {'RWS_API_KEY': 'yourkey', 'GNAVI_API_KEY': 'yourkey'}
```

### 2. キーワード検索する

```
!kachidoki_foods_search ラーメン
```

### 3. 雑に選んでほしいなら、キーワードからチョイスしてもらう


```
!kachidoki_foods_choice ラーメン
```

## FAQ

### RWSしか使わない・ぐるなびしか使わない

`plugin config KachidokiFoods` 実行の際に、使わないキーをから文字列にしてください。

例：`{'RWS_API_KEY': 'yourkey', 'GNAVI_API_KEY': ''}`

### 勝鬨周辺。。。？

各サービスにあわせて、雑にエリア指定しています。
「ここを足すと良いかも？」などがあれば、該当箇所を編集してPRをください。

