# 圏論的Fano指数・Serre根・非可換変形

**2026-11-17 / v16。最初に [研究方針](00_research_plan.md) を読む。** 現在の中心は、Hochschild不変な一次方向から、冪関係を保つ全Artin次数のSerre根へ進むことである。

## 現行原稿と到達点

[Fano圏のSerre根と非可換変形](papers/fano_root_deformations.tex)（17頁）は、tilting bundleと `HH¹=HH³=0` の下で根付きArtin変形の非障害性を証明する。相対Serre関手を有限代数の双対化双加群から構成し、`HH¹=0` で核の持上げの一意性と冪関係を得る。小拡大の持上げtorsorへの再標識作用が有限次数となることを証明してから平均化する。根自身を圏上の有限群作用とは扱わない。

次数2のGeiser根を保つ全形式変形は幾何学的な可換変形と一致する。次数4では各根の不変方向が全形式次数へ延長できるが、異なる根の高次固定部分を同時に線型化したとは主張しない。Fermat三次曲面には、可換1方向と非零Poisson商1方向を持つ2次元の根付き形式変形問題がある。相対ample pairと既存full exceptional collectionの持上げも扱う。

[数値指数論文](papers/normalized_fano_index.tex)（21頁）、[次数9認識論文](papers/nc_dp9_recognition.tex)（101頁）、[補助証明・反例ノート](research/research_notes.tex)（61頁）は有効な証明を保持する。[文献・15の接続](research/fano_index_connections.md)は32件の一次資料を確認範囲別に整理し、[詳細研究方針](research/research_plan.tex)（4頁）から次の課題へ進める。

**範囲**：全Artin次数の形式的存在と有限型代数化は異なる。一般の六公理の認識、`HH¹≠0` の場合、root pairの生成・巡回coherence、全根を忘れた高次moduliの同定は未解決。独立した新規性の網羅的確認も未完了。

## 再現

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
latexmk -lualatex papers/fano_root_deformations.tex
```

全5文書の組版コマンドは [再現手順](research/reproduce.md)。LuaLaTeX、latexmk、luatexja、Harano Aji、Python3、SymPyを使う。フォントは配布しない。出力は `build/`、SyncTeX有効。Gitはソース・必要な検算資産だけを追跡する。

## v16の検証範囲

構造・入力・ラベル・参照・引用の検査、6本の検算コード、5文書すべての再組版が成功した。最終ログに未定義参照・引用、missing-character、overfull、LaTeXエラーはない。中心論文17頁と方針4頁を画像化し、全体配置と主要証明のページを確認した。旧数値指数・認識・補助ノートの数学的ソースは保持しており、その全証明を今回独立に再監査したという意味ではない。

計算はaffine平均、数値恒等式、指標、配置、nilpotent scalar補正の検算であり、圏や一般定理の機械的形式証明ではない。外部文献の使用箇所の確認と全証明の監査を区別する。

## 正本・配布・保存

GitHub `uedakazushi/nc-dp9` の `main` をソース正本とする。今回の基準commitは `baffa16f914d315dc6ad54e102d603087eae4f19`。配布bundleはこの現行ソースと `pdf/` の5最終PDF、内容manifestからなる。旧版、外部文献PDF、build中間物、ログ、キャッシュを含めない。GitHub反映とLibrary保存の実行状態は、それぞれの成功応答を確認して別々に報告する。既存Libraryファイルを明示指示なく削除しない。
