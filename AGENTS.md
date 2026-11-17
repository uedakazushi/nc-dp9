# Codex研究指示 — nc-dp9

**2026-11-18 / v18**。まず `00_research_plan.md`、次に `papers/nc_dp9_recognition.tex` と `research/research_notes.tex` を読む。研究継続に旧会話・旧bundleを要求しない。

中心課題は六公理とheart-exactな三乗根からの一般認識。有限判定は `thm:finite`、主障害は `E_{-1}` と `P`。追加normal境界、飽和、full exceptional collection等を仮定した条件付き結果は既存の本文で証明済みとして区別し、一般公理から導出したと誤認しない。現在の優先は三次domain境界のrank5・section欠損、全Serre消滅、二重mutationの純粋性。 `research/research_notes.tex` の反例候補は六公理の真の反例とは限らない。

圏論的Fano指数・Serre根・非可換変形の別研究は `uedakazushi/categorical-fano-index` に移動済み。認識論文への必要な引用は保持するが、同じ研究本文の複製や別リポジトリの無断編集をしない。

研究価値最大化のため方針を柔軟に改め、現時点の理由と未解決核心を書く。証明済み、条件付き、未証明、予想、計算を区別する。先行研究の一次資料を照合し、書誌と新規性の未確認点を明示する。誤りを発見したら依存主張まで直す。公表原稿は日本語LuaLaTeX、著者は空欄とし、推敲で数学的内容を削らない。

検算は `bash scripts/check.sh`。組版は `latexmk -lualatex papers/nc_dp9_recognition.tex` と `latexmk -lualatex research/research_notes.tex`。ルートから実行しbuild/出力、SyncTeX有効。PDF、ログ、旧ZIP、キャッシュをGitに入れない。

切りのよい約15分ごとにmainへfast-forwardで直接push。PR・Actions・force pushは使わない。競合があれば差分を調べる。研究区切りには、現行論文・方針・ノート・必要なPDF/コードだけの軽量bundleを追加承諾なくLibraryに保存してよい。既存Libraryファイルは明示指示なしに削除しない。生成・検証・GitHub反映・Library保存は別に報告する。
