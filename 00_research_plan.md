# 研究方針：圏論的Fano指数・Serre根・非可換変形

**2026-11-17 / v16**。研究再開時はここを最初に読む。次に [Serre根と変形の論文](papers/fano_root_deformations.tex)、[先行研究と15の接続](research/fano_index_connections.md)、[数値指数論文](papers/normalized_fano_index.tex) を読む。詳細方針は [research/research_plan.tex](research/research_plan.tex)。GitHub `main` がソースの正本であり、旧bundle・過去の会話を再開の前提にしない。

## I. 恒常的研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し研究価値を最大化する。重要な方針変更は現時点の理由、元の目標の解決部分・未解決部分を整理して書き直し、履歴を蓄積しない。証明済み・追加仮定付き・未完成・予想・計算観察を区別し、仮定・依存結果・証明箇所・未解決点を明示する。既知結果と本研究の貢献を区別し、新規性や書誌情報を推測で補わない。誤りが判明したら依存する主張と要約・方針も訂正し、有用な障害だけをノートに残す。

公表原稿は原則日本語LuaLaTeX。既存の公表価値のある成果・十分な証明を削らず、現在の論理的まとまりに従って分割・統合する。ノートは日誌でなく有効な補助知識・反例・文献比較を保持する。現行ソース・PDF・文献・必要なコード・入力・証明書・再現手順だけで自己完結する軽量bundleを作り、旧ZIP・旧原稿・重複・バックアップ・ログ・キャッシュ・中間生成物は含めない。数学的内容や検証可能性を固定容量のために削らない。

研究の区切りには**追加承諾なしでLibraryに現行bundleを保存してよい**。既存Libraryファイルの削除は別操作であり、明示指示なしには行わない。生成・計算・組版・GitHub反映・Library保存を独立に確認し、未実行・失敗・制約を正確に報告する。Gitではソースと必要な再現資産だけを追跡し、PDF・ZIP・ログを追跡しない。

## II. 現在の目標と達成基準

主目標は、数値根・heart-exact根・根を保つ非可換変形を区別し、その差からFano幾何、表現論、Poisson幾何、残余圏へ具体的な定理を導くこと。現在は**tilting付き幾何の全Artin次数の根の持上げと、その代数化・同時根付きモジュライ**を中心にする。一次固定部分だけでは高次存在を保証できないが、相対Serreの構成と核の剛性によってその障害を解決できたためである。

達成基準は (1) 仮定が明示された持上げ・非存在定理、(2) 明示的非可換代数族と根、(3) 根付きモジュライの実際の高次構造、(4) 残余回転・root pair・HMSへの証明付き比較。元の六公理からの次数9一般認識は未解決であり、現行認識論文の全証明を保持する。形式近傍の相対Fano性を一般候補圏の認識と同一視しない。

## III. 到達点・証明の所在・適用範囲

中心論文は `papers/fano_root_deformations.tex`、全Artin証明の入力節は `papers/sections/root_artin_lifting.tex`。

- **全Artin根（証明記載・今回論理点検）**：tilting bundleとHH¹=HH³=0を持つ滑らかな射影Xで、指定したexact根を保つflat Abel変形は形式的に滑らか。接空間はHH²(X)^s。`thm:formal-roots`。相対Serreを双対化双加群から構成し（`prop:tilting-serre`）、核の一意性で冪関係を強制（`thm:artin-power`）する。小拡大の持上げtorsorへの再標識を平均化する。圏自体の有限群作用は仮定しない。
- **Fano性と生成（証明記載）**：相対反標準ample pair、軌道の自由Hilbert加群、既存full例外列と軌道関係の相対perfect圏への持上げ。`prop:relative-ample`, `prop:relative-exceptionals`。絶対C線形の有限homological dimensionを意味しない。
- **次数2（証明記載）**：任意のGeiser型根を保つ全形式Abel変形は、可換な幾何学的変形と同型類で一致。一次次元6。`cor:geiser-formal`。scalar慣性付きstack同型・代数化を主張しない。
- **次数4・三次曲面（証明記載・指標検算）**：次数4の各符号根の形式変形次元は3または5。一般曲面の許容一次集合は既存の10-plane配置。`cor:degree4-formal`。Fermat三次の三乗根は固定HH²が2次元（可換1、Poisson商1）で全形式次数へ延長。`prop:fermat-formal`。
- **保持する結果**：通常の線束根の全一次持上げ、P²の同数値根で固定HH²次元10/4、Gepner非存在、entropy=(0,dimX)。数値指数論文の古典回復・norm・格子・del Pezzo指数・三次元整数値条件、認識論文の全条件付き定理も保持する。

形式存在は有限型代数化ではない。異なる根の固定部分の同時線型化も未証明で、同じ接空間から高次固定部分が一致しない明示模型を `ex:nonlinear-fixed` に保持する。HH¹非零の場合、root pairの巡回coherence、一般の非可換KO上界は未解決。独立新規性は未確定。

## IV. 次の優先課題と着手方法

1. **明示的な代数化**：次数4の一つの符号根、またはFermat三次の固定2方向を選び、tilting quiverの関係式と可逆核の変形を計算する。Barmeier–Wangの有限型代数化条件を照合する。無限形式族だけで実際の一般ファイバーの指数を主張しない。
2. **同時根付き形式moduli**：同じfで異なるLの再標識作用、複数の符号根の合成を二次・三次まで計算する。一次10-plane配置から全根付きscheme構造を推測で補わない。
3. **HH¹非零とcoherence**：P²/quadricの恒等特殊化核を調べ、群norm補正と自然同型のscalar障害を分離する。Haniharaの巡回不変性は別に検証する。
4. **残余圏・HMS**：相対full例外列のmutationから回転を構成し、Geiserの残余Serre関係、HH–Serre代数、AKOのB+iωを比較する。一般認識の未解決点は保留するが削除しない。

## V. 再現・文献・状態

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
latexmk -lualatex papers/fano_root_deformations.tex
latexmk -lualatex papers/normalized_fano_index.tex
latexmk -lualatex papers/nc_dp9_recognition.tex
latexmk -lualatex research/research_plan.tex
latexmk -lualatex research/research_notes.tex
```

出力は `build/`。6本の検算コードは有限の恒等式・指標・配置を確認し、抽象的な形式持上げの証明を代替しない。32件の一次文献と15領域の関係を `research/fano_index_connections.md` に確認範囲別に整理する。全32論文の全証明の監査や網羅的な新規性認証を意味しない。生成・検証・GitHub・Libraryの実行状態はREADMEと最終報告で別々に記す。
