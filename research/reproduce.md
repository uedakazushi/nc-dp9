# 再現手順

2026-11-17 / v17。リポジトリルートから実行する。

## 依存と計算

Python3、SymPy（requirements.txt）、LuaLaTeX、latexmk、luatexja/fontspec、Harano Ajiフォント。フォントファイルは配布しない。

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
```

構造検査と7本の検算を実行する。新しい `computations/verify_root_deformations.py` は、次数4の16指標・15ruling判定・全32support・10座標部分空間・Hilbert級数、P²の指標、Geiser作用、巡回norm補正を有理数／整数／記号計算する。圏の存在やrootの高次coherenceの証明ではない。

## 組版

```sh
latexmk -lualatex papers/fano_root_deformations.tex
latexmk -lualatex papers/normalized_fano_index.tex
latexmk -lualatex papers/nc_dp9_recognition.tex
latexmk -lualatex research/research_plan.tex
latexmk -lualatex research/research_notes.tex
```

`.latexmkrc` は出力・中間生成物をbuild/へ置く。VS Codeはリポジトリルートを開く。SyncTeXは有効。新しい中心論文は `fano_root_deformations.tex`。独立の数値指数論文と認識論文、その必要な補助証明は削除せず保持する。

## 配布前の検査

TeXの未定義参照・引用、missing character、overfull box、必要inputの欠落を確認する。新規／更新文書のPDFを画像化して組版を見る。計算PASSと証明監査を別状態として記す。旧来の数学本文を改めない場合、ソースの同一性を検査し、全証明を新たに監査したとはしない。

bundleは現在のソース・再現資産・pdf/内の5最終PDFと小さな内容manifestだけにする。build/、ログ、キャッシュ、外部文献PDF、旧ZIP・旧原稿は収録しない。manifestの各ファイルのSHA256とZIP CRCを確認する。GitにはPDF/ZIPを追跡しない。Library保存は実際の成功応答を確認し、既存ファイルを削除しない。

`computations/verify_artin_roots.py` はaffine巡回平均、Fermat三次の指標、非線型固定部分、nilpotent scalar補正を検算する。形式的な核・圏・ample pairの存在は本文の証明を用いる。

`computations/verify_root_packages.py` はD5格子、全1024個の五頂点グラフ（うち376個が二部、空グラフを含む）、375個の非空二部グラフの有限商・次元、量子PBW積、Nakayama、Hesse指標を検算する。一般の証明は新しい二つの入力節に置く。
