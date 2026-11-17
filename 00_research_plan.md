# 研究方針：圏論的 Fano 指数と非可換射影平面の認識

**2026-11-17 / v14（構成整理）**。再開時はこの文書を最初に読む。詳細な定理・仮定・証明状態は [研究方針の完全版](research/research_plan.tex)、[指数論文](papers/normalized_fano_index.tex)、[認識論文](papers/nc_dp9_recognition.tex)、[研究ノート](research/research_notes.tex) を参照する。GitHub `main` は TeX ソースの正本であり、旧版 ZIP や過去の会話なしに研究を再開できるようにする。

## I. 恒常的研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性に基づき、研究の目標と方法を柔軟に改める。重要な方針変更は現在有効な理由と旧目標の解決・未解決部分を説明し、時系列の履歴は蓄積しない。証明済み・追加仮定付き・未完成・予想・計算的観察を区別し、仮定、依存定理、証明の所在、新規性の確認状況を明示する。誤りが見つかれば依存する主張を修正し、有用な反例・障害だけを研究ノートに残す。一次資料を確認し、未確認書誌情報を推測しない。

論文は原則日本語・LuaLaTeXで、現在公表価値のある内容と証明を保持する。研究ノートは日誌ではなく現行知識を整理する。必要な再現コード・入力・証明書は残し、旧版 ZIP、PDF、ログ、キャッシュ、中間生成物を Git で追跡しない。研究の区切りでは**追加承諾なしに**現行の自己完結した軽量 bundle を Library に保存してよい。既存 Library ファイルは明示指示なしに削除しない。生成・検証・GitHub 反映・Library 保存は別々に確認して報告する。

## II. 現在の上位目標と達成基準

主目標は古典的 Fano 指数を忠実に拡張する圏論的指数を定義し、**数値的 Serre 根の exact 自己同値への持上げ障害**と、その非可換 Fano 圏への応用を明らかにすること。特に、正規化しない exact 指数と正規化指数の差、canonical class と有限位数自己同型の norm 方程式、非可換圏の heart-preserving 性を結び付ける。最大指数の認識へ進む際には、numerical root と full exceptional collection を混同しない。

元来の次数9認識は、六公理と exact 三乗根から三次元二次 AS-regular な `qgr` を認識する問題。有限障害への還元・可換特殊化・normal 境界での条件付き認識は保持されるが、**一般認識は未解決**。指数を定義へ加えたことで元問題を解決したことにはしない。

達成基準は (1) exact 根の持上げを判定する自然な十分必要条件、(2) 既知および新しい非可換 Fano 圏への実質的な適用、(3) 最大指数の認識または反例、(4) 一般認識の障害を実質的に縮小する条件付き定理。数値模型の実在圏への昇格は独立に証明する。

## III. 現行の主要到達点と状態

- **古典的回復（証明記載）**：数値群全体の unipotence で正規化した反Serre根の次数は、滑らかな複素 Fano 多様体の古典的指数の約数と一致する。構造対象の軌道だけの正規化とは許される根の集合が異なる。`papers/normalized_fano_index.tex` の `thm:classical`, `prop:orbit-classical`。
- **数値根の分類（証明記載・数値的主張）**：surface-like pseudolattice における rank-preserving 根は `t_H` と `F` の半直積で、`F^r=1`, `N_r(F)H=-K`。周期的 Euler 欠損と `r | K^2`。`thm:twisted-lattice-root` と `cor:periodic-deficit`。既知 Kuznetsov 理論に依存し、数値等長変換が exact 関手に持ち上がるとは主張しない。
- **del Pezzo の実例（証明記載・有限計算検証）**：次数 `d=1,...,9` における実現可能な最大 exact 指数は `1,2,3,4,5,6,1,4,3`。次数4一般の exact 指数は2だが、その共通の数値 Euler 格子には四乗根が存在する。`thm:delpezzo-exact-index-table`, `prop:degree-four-lifting-gap`。独立新規性は未確定。
- **三次元の整数値障害（条件付き定理）**：exceptional 標識・反標準 Euler 三次性・軌道正規化を仮定する。`thm:threefold-arithmetic`。圏や根の存在を示すものではない。
- **次数9の条件付き認識（証明記載）**：三次 normal 境界、滑らかな高 Veronese の復元、可換第三 Veronese の分類、有限生成障害の零性判定を `papers/nc_dp9_recognition.tex` に保持。全面的な独立再監査と新規性の網羅的確認は未了。

## IV. 優先順位の高い次の課題

1. **非可換圏の根の持上げ**：次数4 del Pezzo の数値四乗根と exact 二乗根を benchmark として、非可換二次・三次 AS-regular 圏で invertible bimodule の根と heart-exact 性を比較する。整数格子作用、自己同値群の像、Picard の norm 障害、root pair の生成仮定を分離する。
2. **内在的数値曲面性**：候補 heart から point-like 類、generic rank、characteristic canonical class を構成し、unimodularity と defect 条件をそれぞれ検証する。
3. **Kodaira 型消滅と full 性**：normal 元がない場合の漸近 Ext 消滅、第二 Bass 空間、負の Euler 窓、phantom 型残余を検討する。
4. **先行研究と公表準備**：Bondal--Orlov、Kuznetsov、Mori--Ueyama 最終稿、Loginov--Orlov、Hanihara、del Pezzo 自己同型群の一次資料を再確認し、新規な貢献と古典的幾何の組合せを明確に分ける。

## V. 再生成と検証

`requirements.txt` に Python 計算依存、`computations/` に四本の厳密算術コード、`scripts/verify_repository.py` にソース・参照・フォルダ構造の検査を置く。手順は [research/reproduce.md](research/reproduce.md) と [README.md](README.md) にまとめる。

```sh
python3 -m pip install -r requirements.txt
python3 scripts/verify_repository.py
bash scripts/check.sh
latexmk -lualatex papers/normalized_fano_index.tex
```

計算の PASS は圏論的存在や論文全証明の認証ではない。旧 ZIP との比較を再開の前提にしない。今回の構成整理は数学的主張を新しく証明する作業ではなく、TeX ソースの移動と入力パスの修正である。
