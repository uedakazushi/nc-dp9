# Codex研究指示 — nc-dp9

**2026-11-18 / v18。まず `00_research_plan.md` を読む。** 次に `papers/fano_root_deformations.tex`、`research/fano_index_connections.md`、数値指数論文を読む。詳細方針は `research/research_plan.tex`。認識の全証明は `papers/nc_dp9_recognition.tex`、補助証明・反例は `research/research_notes.tex`。旧会話・旧bundleなしで再開する。

主軸はSerre根のHH作用と非可換変形への持上げ。指定した関手の持上げ、冪関係を保つ根、root pair、cyclic coherenceを区別する。tiltingとHH¹=HH³=0の下でrelative Serre、冪関係、根付き全Artin変形の非障害性は現行原稿に証明した。有限反Serre商を持つ複数根の同時持上げ、次数4の二部グラフ判定と全頂点被覆による形式的可換性が現行結果。優先はrank三の無限反Serre商を持つ三角形の高次障害と、Hesse型Sklyanin二方向の根付きモジュライ・慣性、次数4・Fermat三次の具体的代数化である。既知のSklyanin族はHesseの共通二方向を一次で全て代数化する。ただしHH¹(P²)非零のためmoduliの形式普遍性までは主張せず、次数4の形式族の代数化とも混同しない。三角形の無限商はrank三の平行移動格子であり、有限平均法を適用しない。HH³=0から根付き変形の非障害性を無条件に推論しない。通常のHHでのSerre自明性をHochschild–Serre代数全体へ拡張しない。

数学的重要性、新規性、理解、応用、正確性、実現可能性を総合して目標を柔軟に改め、現行方針を書き換える。証明済み・条件付き・未完成・予想・計算観察を区別する。一次資料と適用仮定を確認し、未確認の書誌・新規性を推測しない。2026年preprintの主張確認と証明監査を混同しない。誤りは依存箇所まで訂正する。

論文は原則日本語LuaLaTeX。原稿の分割・統合は論理的まとまりによる。既存の有効な結果・十分な証明を削らず、ノートは日誌にしない。元の六公理からの認識、消滅、fullnessの未解決箇所を新定義で置き換えない。他研究用リポジトリは比較のために読み、明示指示なしに内容を同期・変更しない。

約15分を目安に切りのよいところでmainへfast-forwardで直接pushする。PR・Actions・force pushは使わない。並行更新があればfetchして差分を読み統合する。計算は `bash scripts/check.sh`、組版は `latexmk -lualatex papers/fano_root_deformations.tex`。詳細は `research/reproduce.md`。ルートから実行し出力はbuild/。Gitはソースと必要な再現資産だけを追跡する。

研究区切りには追加承諾なく現行bundleをLibraryに保存してよい。既存Libraryファイルは明示指示なしに削除しない。bundleには現在の論文・方針・ノート・最終PDF・必要な計算資産を収録し、旧版・旧ZIP・ログ・キャッシュを除く。生成、検証、GitHub反映、Library保存を別々に報告し、未実行や未監査は明記する。

tiltingとHH¹=HH³=0の定理を一般候補heartへ無断で拡張しない。`papers/sections/root_artin_lifting.tex` を先に点検する。
