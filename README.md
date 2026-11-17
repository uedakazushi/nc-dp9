# 圏論的Fano指数・Serre根・非可換変形

**2026-11-18 / v18。最初に [研究方針](00_research_plan.md) を読む。** 現在の中心は、Hesse不変二方向をSklyanin族で同時代数化し、次数4の奇閉路の無限反Serre商を正確に計算することである。

## 現行の主結果と範囲

[Fano圏のSerre根と非可換変形](papers/fano_root_deformations.tex)（25頁）は、tilting bundleと `HH¹=HH³=0` の下で、自己同値群の部分群Γがτを含みΓ/〈τ〉が有限なら、指定生成元の同時Artin持上げが非障害的であることを証明する。一次空間は `HH²(X)^Γ`。群関係は自然同型まで保つが、coherentな群作用を構成したとはしない。

次数4の符号二乗根を五頂点グラフの辺に対応させる。全ての線束norm解を整係数で記述し、可換な根を選べること、反Serre商を有限にできること、グラフの二部性が同値となる。選んだ根が可換なら商は `(Z/2)^(|V_E|-c_E)`、形式変形の次元は `7-|V_E|`。全五頂点を覆えば、これらの根を同時に保つ形式変形は幾何学的な可換変形と一致する。二部グラフ上の任意の線束解が可換とは主張しない。

既知のskew polynomial族は共通Hesse不変空間の `xyz` 方向を実現する。より広いSklyanin族 `S(a,b,c)` は三つの三乗根を全fiberで保ち、可換点の二パラメータKodaira--Spencer写像は `span{xyz,x³+y³+z³}` への同型となる。これは既知の代数族を使った接空間の全代数化であり、全根付きmoduliの形式同型ではない。次数4の三角形で選んだ根の反Serre商はrank三の平行移動格子（同parityの三つ組）を持つKlein四元群の拡大。一次共通固定空間は4次元だが、全Artin持上げは未解決。元の単一根の全Artin定理、次数2の形式的可換性、次数4・Fermat三次の形式族、相対ample pair、例外列、Gepnerとentropyの結果を保持する。

[数値指数論文](papers/normalized_fano_index.tex)（21頁）、[次数9認識論文](papers/nc_dp9_recognition.tex)（101頁）、[補助証明・反例ノート](research/research_notes.tex)（61頁）は数学的本文を変更せず保持する。[文献・17の接続](research/fano_index_connections.md)は37件の一次資料を確認範囲別に整理する。[詳細研究方針](research/research_plan.tex)は4頁。

**未解決**：無限反Serre商、HH¹非零の場合の一般定理、複数根のcoherence、全根を忘れた高次moduli、次数4/Fermatの明示代数化、一般六公理の認識。独立新規性の網羅的確認も未完了。

## 再現

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
latexmk -lualatex papers/fano_root_deformations.tex
```

全5文書の組版は [再現手順](research/reproduce.md)。LuaLaTeX、latexmk、luatexja、Harano Aji、Python3、SymPyを使用し、フォントは配布しない。出力はbuild/、SyncTeX有効。Gitはソースと必要な再現資産だけを追跡する。

## 今回の検証

ソース・入力・ラベル・参照・引用の検査と8本の計算検証は成功。中心論文25ページ・研究方針4ページは今回LuaLaTeXで再組版し、主張のあるページを画像で点検した。数値指数論文21ページ・認識論文101ページ・従来研究ノート61ページは数学的ソースに変更がないため、検証済みの現行PDFを保持した。中心論文と方針の最終ログに未定義参照・引用、missing-character、overfull、LaTeXエラーは見られない。日本語italicのfont-shape情報は通常体への代替であり、missing-characterとは異なる。

コードは全1024グラフ、376個の二部グラフ（空を含む）、全非空有限商と変形次元、Picard整性、45個の交換子、Hesseのcyclic potential・2つのKodaira--Spencer方向、三角形のaffine平行移動格子、量子平面の3280語の二通りの正規化、Nakayama係数、Hesse指標を厳密計算する。有限検算は一般の圏論的存在・形式的滑らかさの証明ではない。既存の長い論文・ノートの全証明を今回独立に再監査したという意味ではない。

## 正本と配布

GitHub `uedakazushi/nc-dp9` mainをソース正本とする。配布bundleには現行ソース、pdf/の5最終PDF、内容manifestだけを収録し、旧版、外部文献PDF、build中間物、ログ、キャッシュを含めない。GitHub反映・Library保存は各成功応答を確認して独立に報告する。既存Libraryファイルを明示指示なく削除しない。
