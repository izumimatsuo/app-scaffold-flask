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

データベース接続
```
$ docker-compose -p $USER exec rdb psql -U <user-name> <database-name>
```

## Migrate

初期化
```
$ docker-compose -p $USER exec app flask db init
```
マイグレーション作成
```
$ docker-compose -p $USER exec app flask db migrate
```
マイグレーション実行
```
$ docker-compose -p $USER exec app flask db upgrade
```
ロールバック
```
$ docker-compose -p $USER exec app flask db downgrade
```

## test

登録
```
curl -X POST -H "Content-Type: application/json" -d '{"name":"momo-taro"}' localhost/${USER}/api/v1/users
```
参照
```
curl localhost/${USER}/api/v1/users
```
削除
```
curl -X DELETE localhost/${USER}/api/v1/users/1
```
## gitlab-runner
```
gitlab-runner exec docker test
```
