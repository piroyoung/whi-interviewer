# whi-interviewer

Teamsのランダムな複数ユーザにランダムな質問を配信するバッチアプリケーションです．

１０秒程度で答えられる簡単な質問から，社内の新しい繋がりが生まれるかも！？

## 基本動作

Dockerhubにてイメージを公開しています．

https://hub.docker.com/repository/docker/piroyoung/whi-interviewer

```shell
docker run -it piroyoung/whi-interviewer:latest \
  -e TEAMS_INCOMING_WEB_HOOK="https://<incoming_webhook>" \
  -e MSSQL_CONNECTION_STRING="Driver={ODBC Driver 17 for SQL Server};<connection_string>" \
  -e NUMBER_OF_USERS "5"
```

## 環境変数

### TEAMS_INCOMING_WEBHOOK

Teamsから発行したIncomingWebhookを`https://`から全て指定してください．

* [受信 Webhook を作成する](https://learn.microsoft.com/ja-jp/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

### MSSQL_CONNECTION_STRING

SQL ServerへのConnectionStringを指定してください．認証方法は色々なものが使えますが， 公開しているDockerイメージを使用する際はODBCには `ODBC Driver 17 for SQL Server`
を指定してください．

* [Azure Active Directory 認証を使用して接続する](https://learn.microsoft.com/ja-jp/sql/connect/jdbc/connecting-using-azure-active-directory-authentication?view=sql-server-ver16)

### NUMBER_OF_USERS

１つの質問に対して複数名に対してメンションします．`NUMBER_OF_USERS` ではその人数を指定します．

## データベース
バッチはSQLServerを参照します．一度実行すると，最初は実行が失敗しますが（直せよ）以下の２つのテーブルが作成されます．
データの追加などはPowerAppsなどで適当にどうぞ

### dba.Users

| フィールド名     | 概要                         |
|------------|----------------------------|
| id         | 整数値の主キー                    |
| name       | メンションに使用する表示               |
| email      | ActiveDirectoryに紐づくメールアドレス |
| created_at | 登録日時（UTC)                  |
| updated_at | 更新日時（UTC）|

### dbo.Messages

| フィールド名     | 概要        |
|------------|-----------|
| id         | 整数値の主キー   |
| message    | 質問本文      |
| created_at | 登録日時（UTC) |
| updated_at | 更新日時（UTC） |


## 定期的に実行したい

Azureで定期的にコンテナを実行するには以下のようなものを使用します．

大まかには，Logic Apps を用いてスケジュールされたトリガを作成して，Container Instances のコンテナをKickするといいと思います．

### Azure Container Instances

* [Azure Container Instances とは](https://learn.microsoft.com/ja-jp/azure/container-instances/container-instances-overview)

### Azure Logic Apps

* [Azure Logic Apps とは](https://learn.microsoft.com/ja-jp/azure/logic-apps/logic-apps-overview)

