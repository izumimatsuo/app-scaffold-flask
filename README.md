# web-scaffold-flask

Python Flask で Web アプリケーションを開発する際の土台

## commands

環境起動
```
$ docker-compose -p $USER up -d
```

環境破棄
```
$ docker-compose -p $USER down
```

パッケージ追加
```
$ docker-compose -p $USER exec app pip install <package-name>
```

パッケージ反映
```
$ docker-compose -p $USER exec app pip freeze >requirements.txt
```

データベース接続
```
$ docker-compose -p $USER exec rdb psql -U <user-name> <database-name>
```

## Migrate

初期化
```
flask db init
```
マイグレーション作成
```
flask db migrate
```
マイグレーション実行
```
flask db upgrade
```
ロールバック
```
flask db downgrade
```

## test

登録
```
curl -X POST -H "Content-Type: application/json" -d '{"name":"momo-taro"}' localhost/izumi/api/v1/models
```
参照
```
curl localhost/izumi/api/v1/models
```
削除
```
curl -X DELETE localhost/izumi/api/v1/models/1
```
