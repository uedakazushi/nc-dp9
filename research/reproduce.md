# 再生成手順と検証範囲

研究再開は [`00_research_plan.md`](../00_research_plan.md) から始める。TeX と計算はすべて **リポジトリルート** から実行する。共通入力は `papers/preamble.tex`、認識論文の追加節は `papers/sections/numerical_rank_section.tex`。PDF と SyncTeX は `build/` に生成し、Git には追跡しない。

```sh
python3 -m pip install -r requirements.txt
python3 scripts/verify_repository.py
python3 computations/verify_normalized_index.py
python3 computations/verify_del_pezzo_roots.py
python3 computations/verify_identities.py
python3 computations/verify_toric.py
latexmk -lualatex papers/normalized_fano_index.tex
latexmk -lualatex papers/nc_dp9_recognition.tex
latexmk -lualatex research/research_plan.tex
latexmk -lualatex research/research_notes.tex
```

`bash scripts/check.sh` は構造確認と四つの Python コードをまとめて実行する（組版は独立に実行）。外部 PDF、旧 bundle、旧会話は必要ない。SymPy が Python の依存パッケージ。LuaLaTeX に luatexja-fontspec・Harano Aji 字体が必要。フォントのバイナリは bundle に同梱しない。

数値恒等式・有限代数例の検算と、圏の存在・強い認識定理の証明は異なる。研究の新規性の完全確定、引用文献の全証明の監査は未完了。原稿全体に直接証明があることと、今回その全証明を独立再監査したことは混同しない。bundle は現行ソース・必要なコード・PDF のみを含め、履歴、キャッシュ、旧 ZIP を含めない。
