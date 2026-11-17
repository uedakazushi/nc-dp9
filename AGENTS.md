# Codex 研究指示 — nc-dp9

**まず `00_research_plan.md` を読む。** 詳細な数学的研究方針は `research/research_plan.tex`、公表用原稿は `papers/normalized_fano_index.tex` と `papers/nc_dp9_recognition.tex`、現行の補助結果は `research/research_notes.tex`、検算は `computations/`、再現は `research/reproduce.md` にある。古い会話や旧版の取得を前提にしない。

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し研究価値を最大化する。方針変更は現状の理由と残る問題を簡潔に書き換え、変更履歴を蓄積しない。証明済み・条件付き・未完成・予想・計算観察を区別し、本文に定理の仮定、依存文献、証明、未証明箇所を明示する。既知結果の新規性を推測で補わず、可能な限り一次資料の適用範囲を確認する。数学上の誤りは依存箇所まで正し、有用な反例・障害だけをノートに残す。

主軸は圏論的 Fano 指数、特に数値的根と heart-exact 自己同値の差、次数4 del Pezzo 持上げ障害、非可換 AS-regular 圏への適用。元の六公理からの一般認識は未解決であり、既存の長い論文・証明を削ったり新定義の仮定で置き換えたりしない。公表原稿は原則日本語 LuaLaTeX。論文は現行成果を読みやすい順序に維持する。

一つの Codex が継続研究し、約15分を目安に区切りのよい段階で `main` へ直接 fast-forward push する。PR・Actions・force push は使用しない。並行更新があれば fetch して統合する。検証は `python3 scripts/verify_repository.py`、`bash scripts/check.sh`、組版は `latexmk -lualatex papers/normalized_fano_index.tex`。`.latexmkrc` と VS Code はリポジトリルート起点、`build/` に PDF・中間ファイルを出す。Git ではソースと必要な再現資産のみを追跡し、旧版、PDF、ZIP、ログ、キャッシュは追跡しない。

研究の区切りには追加承諾なく現行 bundle を Library に保存してよい。既存 Library ファイルの削除は明示指示なしにしない。生成、計算、組版、GitHub 反映、Library 保存を別々の状態として正確に報告する。長い原稿の証明を実際に再監査していない場合はその旨を記す。
