# nc-dp9 — 圏論的 Fano 指数と非可換射影平面の認識

**[研究方針](00_research_plan.md)から読む。** 独立した現行公表用原稿は [圏論的 Fano 指数](papers/normalized_fano_index.tex) と [次数9認識](papers/nc_dp9_recognition.tex)。前者は古典的指数の正規化、数値根の半直積分類と周期欠損、滑らかな del Pezzo 曲面の exact 根、三次元の整数値障害を扱う。後者は六公理に基づく AS-regular 認識、normal 境界、Ext と生成障害の条件付き定理を扱う。全一般認識と数値根の exact 自己同値への一般的持上げは **未解決**。

現行の詳細な方針は [research/research_plan.tex](research/research_plan.tex)、補助知識・反例・文献比較は [research/research_notes.tex](research/research_notes.tex)。[`AGENTS.md`](AGENTS.md) は研究・Codex 運用の規約。研究の再現情報は [research/reproduce.md](research/reproduce.md) にあり、`computations/` の四本の検算は厳密算術の確認であって抽象圏の存在や証明全体の認証ではない。

## 構成

```text
00_research_plan.md          研究再開時の入口・重要結果・優先課題
AGENTS.md                    Codex研究指示とGitHub運用
papers/
  normalized_fano_index.tex  圏論的Fano指数の公表用原稿
  nc_dp9_recognition.tex     次数9認識の公表用原稿（既存の全証明）
  preamble.tex               共通LuaLaTeX設定
  sections/numerical_rank_section.tex  認識論文の必要節
research/
  research_plan.tex          完全版研究方針
  research_notes.tex         研究ノート（有用な補題・反例・文献）
  reproduce.md               再生成・計算検証と状態の説明
computations/                独立の厳密計算コード4本
scripts/                     構造検査と一括検証
build/                       latexmk生成物（Git追跡外）
```

## 再生成（リポジトリルートから）

```sh
python3 -m pip install -r requirements.txt
python3 scripts/verify_repository.py
bash scripts/check.sh
latexmk -lualatex papers/normalized_fano_index.tex
latexmk -lualatex papers/nc_dp9_recognition.tex
latexmk -lualatex research/research_plan.tex
latexmk -lualatex research/research_notes.tex
```

LuaLaTeX、latexmk、TeX Live の `luatexja-fontspec`・Harano Aji 系フォントを利用する。VS Code LaTeX Workshop はルート起点で `build/` へ生成し、SyncTeX を有効化する。PDF、ZIP、aux、log、build、キャッシュは Git に入れない。GitHub `main` が現行の TeX 研究正本。Library bundle は現行版を自己完結させ、旧版を入れ子にしない。

## 検証と研究上の制約

構成整理前（2026-11-17 v14）には、四文書の LuaLaTeX 組版、四スクリプトの厳密算術計算、PDF 整合性が記録されている。構成整理後に四文書を LuaLaTeX/latexmk で再生成し、21・101・6・61ページを確認した。4本の計算スクリプトと TeX の入力参照・label・引用の構造検査も実行し、いずれも成功した。旧版 PDF と新 PDF の抽出テキストは4文書すべて完全一致し、TeX・計算コードは配置と入力パス以外変更していない。PDF バイナリはパス／組版メタデータ等の差により同一ではない。元の論文に記された条件付き定理はそのまま保持し、全証明の独立した再監査や新規性の網羅調査が完了したとは主張しない。
