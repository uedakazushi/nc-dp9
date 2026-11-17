# 圏論的Fano指数・Serre根・非可換変形

**2026-11-17 / v17。最初に [研究方針](00_research_plan.md) を読む。** 現在の中心は、一つのSerre根から複数の根の同時持上げへ進み、反Serre商の有限性をPicard格子で判定することである。

## 現行の主結果と範囲

[Fano圏のSerre根と非可換変形](papers/fano_root_deformations.tex)（22頁）は、tilting bundleと `HH¹=HH³=0` の下で、自己同値群の部分群Γがτを含みΓ/〈τ〉が有限なら、指定生成元の同時Artin持上げが非障害的であることを証明する。一次空間は `HH²(X)^Γ`。群関係は自然同型まで保つが、coherentな群作用を構成したとはしない。

次数4の符号二乗根を五頂点グラフの辺に対応させる。全ての線束norm解を整係数で記述し、可換な根を選べること、反Serre商を有限にできること、グラフの二部性が同値となる。選んだ根が可換なら商は `(Z/2)^(|V_E|-c_E)`、形式変形の次元は `7-|V_E|`。全五頂点を覆えば、これらの根を同時に保つ形式変形は幾何学的な可換変形と一致する。二部グラフ上の任意の線束解が可換とは主張しない。

既知のskew polynomial族 `yz=qzy, zx=qxz, xy=qyx` では三つの三乗根を全fiberで明示した。これは共通Hesse不変空間の `xyz` 方向の実際の代数化であり、次数4やFermat三次の形式族を代数化したものではない。元の単一根の全Artin定理、次数2の形式的可換性、次数4・Fermat三次の形式族、相対ample pair、例外列、Gepnerとentropyの結果を保持する。

[数値指数論文](papers/normalized_fano_index.tex)（21頁）、[次数9認識論文](papers/nc_dp9_recognition.tex)（101頁）、[補助証明・反例ノート](research/research_notes.tex)（61頁）は数学的本文を変更せず保持する。[文献・16の接続](research/fano_index_connections.md)は34件の一次資料を確認範囲別に整理する。[詳細研究方針](research/research_plan.tex)は4頁。

**未解決**：無限反Serre商、HH¹非零の場合の一般定理、複数根のcoherence、全根を忘れた高次moduli、次数4/Fermatの明示代数化、一般六公理の認識。独立新規性の網羅的確認も未完了。

## 再現

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
latexmk -lualatex papers/fano_root_deformations.tex
```

全5文書の組版は [再現手順](research/reproduce.md)。LuaLaTeX、latexmk、luatexja、Harano Aji、Python3、SymPyを使用し、フォントは配布しない。出力はbuild/、SyncTeX有効。Gitはソースと必要な再現資産だけを追跡する。

## 今回の検証

ソース・入力・ラベル・参照・引用の検査、7本の検算コード、5文書すべての再組版が成功した。最終ログに未定義参照・引用、missing-character、overfull、LaTeXエラーはない。日本語italicのfont-shape情報は通常体への代替であり、missing-characterとは異なる。中心論文の新規節と研究方針の主要ページを画像で点検した。

新しいコードは全1024グラフ、376個の二部グラフ（空を含む）、全非空有限商と変形次元、Picard整性、45個の交換子、量子平面の3280語の二通りの正規化、Nakayama係数、Hesse指標を厳密計算する。有限検算は一般の圏論的存在・形式的滑らかさの証明ではない。既存の長い論文・ノートの全証明を今回独立に再監査したという意味ではない。

## 正本と配布

GitHub `uedakazushi/nc-dp9` mainをソース正本とする。配布bundleには現行ソース、pdf/の5最終PDF、内容manifestだけを収録し、旧版、外部文献PDF、build中間物、ログ、キャッシュを含めない。GitHub反映・Library保存は各成功応答を確認して独立に報告する。既存Libraryファイルを明示指示なく削除しない。
