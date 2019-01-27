# 日本でご飯 for Errbot

日本でご飯を食べたい人向けのErrbotプラグインです。

## 事前に用意するもの

* ぐるなびWebサービス用のAPIキー
* Recruit Web Services用のAPIキー

## Errbotへのインストール

### チャットから

基本的には、チャットツール上の管理コマンドで有効にしてください

```
!repos install https://github.com/attakei-errbot-plugins/jp-foods
```

### Git管理で

```
$ git submodule add plugins/kachidoki-foods https://github.co/attakei-errbot-plugins/kachidoki-foods
```

## 使い方

### 1. 事前に「APIキー」「エリア情報」をセットする

```
!plugin config JapanFoods {'RWS_API_KEY': 'yourkey', 'GNAVI_API_KEY': 'yourkey', 'GNAVI_AREA_CODE': 'AREAS2111', 'RWS_AREA_CODE': 'X025,X026,XA34,XA35'}
```

### 2. キーワード検索する

```
!jp_foods_search ラーメン
```

### 3. 雑に選んでほしいなら、キーワードからチョイスしてもらう


```
!jp_foods_choice ラーメン
```

## FAQ

### RWSしか使わない・ぐるなびしか使わない

`plugin config JapanFoods` 実行の際に、使わないキーを空文字列にしてください。

例:

```
!plugin config JapanFoods {'RWS_API_KEY': 'yourkey', 'GNAVI_API_KEY': 'yourkey', 'GNAVI_AREA_CODE': 'AREAS2111', 'RWS_AREA_CODE': 'X025,X026,XA34,XA35'}
```

