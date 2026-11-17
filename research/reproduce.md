# 再現手順

2026-11-18 / v18。リポジトリルートから実行。

## 依存と検査

Python3、SymPy（requirements.txt）、LuaLaTeX、latexmk、luatexja-fontspec、Harano Aji。検算は次数9認識に固有の二本。圏論的Fano指数の六本の検算は別リポジトリ categorical-fano-index にある。

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
latexmk -lualatex papers/nc_dp9_recognition.tex
latexmk -lualatex research/research_notes.tex
```

`scripts/verify_repository.py` は論文・ノートのinput、label、ref、citeの整合をチェックする。`computations/verify_identities.py` は明示数値・形式モデルと変形障害に関する有限恒等式、`computations/verify_toric.py` はsemigroup環の例の格子点計算を検算する。これらは六公理からの一般認識の証明ではない。

出力はbuild/、SyncTeX有効。配布前には未定義参照・引用、missing character、overfull boxとPDF描画を別に確認。現行bundleには研究方針、認識論文、研究ノート、必要な二本の計算コードと再現手順、生成できた最終PDFだけを含める。旧版・ログ・キャッシュを含めない。
