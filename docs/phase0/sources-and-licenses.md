# 取得元とライセンス一覧

確認日：2026年11月8日（日本時間）。本書は確認した公開条件の整理です。個別契約の対象範囲・価格は未確定です。

| ID | 提供元・根拠URL | データ／機能 | 条件・認証・頻度 | 本アプリでの判断 |
| --- | --- | --- | --- | --- |
| S01 | [京成電鉄バスグループ公式バスナビ](https://transfer-cloud.navitime.biz/keiseibus-group/)／[利用条件](https://transfer-cloud.navitime.biz/keiseibus-group/terms-of-use) | 時刻表・接近情報・検索画面 | 利用条件の禁止事項に自動収集、解析、複製、再配信等が記載。画面の30秒自動更新は第三者アプリへの許可ではない | 自動収集・内部API流用の提供元として不採用。正式な別途許諾があれば再検討 |
| S02 | [稲毛駅](https://transfer-cloud.navitime.biz/keiseibus-group/courses?busstop=00021389)／[長沼原町](https://transfer-cloud.navitime.biz/keiseibus-group/courses?busstop=00021830) | 対象停留所名・系統一覧・のりば | S01の条件。これらのIDは公式バスナビ内のID | 識別子・掲載範囲の確認のみ。GTFS stop_idと混同しない |
| S03 | [NAVITIME API案内](https://api-sdk.navitime.co.jp/api/)／[時刻表取得](https://api-sdk.navitime.co.jp/api/specs/api_guide/transport_diagram-segment.html)／[停車駅一覧取得](https://api-sdk.navitime.co.jp/api/specs/api_guide/transport_stops.html) | 正式JSON API。運行ID、停車順、許諾された時刻等 | 別途時刻表／バスデータのオプション契約が必要。両APIはAPIマーケットでは提供しないとの仕様。会社ごとに出力項目が制限される場合がある | 契約候補。対象路線、時刻項目、再表示・保存権限、実応答を未確認 |
| S04 | [CID](https://api-sdk.navitime.co.jp/api/specs/description/about_cid.html)／[デジタル署名による認証](https://api-sdk.navitime.co.jp/api/specs/description/about_signature.html)／[リクエスト数](https://api-sdk.navitime.co.jp/api/specs/description/about_rate_limit.html) | 正式APIへのアクセス条件 | CID等の契約認証。具体的なリクエスト数は営業担当への問い合わせが必要 | 秘密情報はサーバーの環境変数で管理。対象APIの30秒取得は未承認 |
| S05 | [乗換時刻表クラウド Web API仕様書](https://static-transfer-cloud.navitime.biz/external-api/redoc-static.html) | nodes候補JSON、courses／trips／approachings等のページ連携 | ホストは個別案内、顧客ID。ページ連携の応答は公式画面であり、自由に再配信できる到着予測JSON APIを意味しない | 技術資料として確認。公開資料の顧客IDを第三者資格として利用しない |
| S06 | [NAVITIME地図SDKのバスロケ機能](https://api-sdk.navitime.co.jp/api/specs/map_script_spec/functions/setBusLocationCondition.html) | バス位置描画・選択等のSDK機能 | 機能説明だけでは対象事業者の対応、データアクセス、Leaflet上への再表示許可は証明できない | リアルタイム契約の問い合わせ候補。対象実データで未検証 |
| S07 | [ODPT 静的データカタログ](https://ckan.odpt.org/dataset/keisei_transit_bus_all_lines) | 千葉ウエストの一般路線・市川市コミュニティバス等 | CC BY 4.0。ODPTデータセット単位で確認。カタログ検索は認証なしで成功 | 長沼営業所の対象ではないため不採用 |
| S08 | [ODPT リアルタイムカタログ](https://ckan.odpt.org/dataset/odpt_keisei_transit_bus_all_lines) | 同地域のVehiclePosition・TripUpdates・Alert | CC BY 4.0。公開API／認証APIの経路あり。カタログ閲覧成功は対象RT受信成功ではない | 対象地域が異なるため不採用。RTの取得・予測精度評価は未実施 |
| S09 | [GTFSデータリポジトリ](https://gtfs-data.jp/)／[API仕様](http://docs.gtfs-data.jp/api.v2.html)／[利用規約](http://docs.gtfs-data.jp/site/kiyaku.pdf) | feeds・filesの公開メタデータと登録GTFS | 規約第5条：GTFSは提供者指定ライセンス、付帯メタデータはCC BY 4.0。今回のAPI GETは認証なしで成功。公開資料から定量的レート上限は確定できず | カタログ調査に採用。対象フィードの発見には至らず |
| S10 | [実際に取得した塩浜営業所のGTFS ZIP](https://api.gtfs-data.jp/v2/organizations/keisei-transitbus/feeds/keiseitransitbus/files/feed.zip?uid=1cbf6425-88e7-41ea-8f83-bddacf7983e1) | 233停留所・16路線・802便。提供者は千葉ウエスト塩浜営業所 | CC BY 4.0。クレジット：京成バス千葉ウエスト株式会社 塩浜営業所／GTFSデータリポジトリ。今回の資料は検査件数等の集計で、元ZIPは同梱しない | 対象停留所・対象系統が一致しないことを実データで確認。不採用 |
| S11 | [ちばレインボーバスの登録メタデータを含む一覧](https://api.gtfs-data.jp/v2/feeds?pref=12) | 同一グループの別フィード | 一覧の表示はCC BY 4.0、有効期間末は2025-09-30。対象への対応は確認できず、期限切れ | 長沼営業所向けに流用しない |
| S12 | [OpenStreetMap著作権・ライセンス](https://www.openstreetmap.org/copyright)／[タイル利用方針](https://operations.osmfoundation.org/policies/tiles/) | 将来の背景地図候補 | OSMデータはODbL。クレジット・ライセンス案内が必要。タイル配信は別条件、Referer・キャッシュ・一括取得禁止等に従う | データ許諾後の候補。OSMからリアルタイムバス位置が得られるわけではない |

## 資料・証跡の扱い

同梱するカタログ証跡は、GTFSデータリポジトリ／一般社団法人社会基盤情報流通推進協議会（AIGID）が提供する付帯メタデータを選択・整形したものです（CC BY 4.0、連絡先項目を除外）。各フィード自体の利用条件は記載のライセンスを別途確認します。

公式バスナビのHTML、時刻表の全量、公式地図画像、内部APIの応答をリポジトリに転載しません。公式画面の観察事実と根拠URLを記録します。認証情報、期限付き署名ダウンロードURLも含めません。

S04の認証方式は契約・接続仕様に従って確定します。CIDの公開例や他の顧客用設定を本アプリの認証情報として使うことはありません。
