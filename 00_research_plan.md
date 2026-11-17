# 研究方針：非可換9次del Pezzo圏・非可換射影平面の認識

**2026-11-18 / v18**。研究再開時に最初に読む。次に [認識論文](papers/nc_dp9_recognition.tex)、[研究ノート](research/research_notes.tex)、[再現手順](research/reproduce.md) を読む。圏論的Fano指数の正本は別リポジトリ [categorical-fano-index](https://github.com/uedakazushi/categorical-fano-index) へ移した。GitHub `main` は本研究のソース正本とする。

## I. 恒常的研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し研究価値を最大化する。重要な方針変更は現時点の理由、元の目標の解決部分・未解決部分を整理して書き直し、履歴を蓄積しない。証明済み・追加仮定付き・未完成・予想・計算観察を区別し、仮定・依存結果・証明箇所・未解決点を明示する。既知結果と本研究の貢献を区別し、新規性や書誌情報を推測で補わない。誤りが判明したら依存する主張と要約・方針も訂正し、有用な障害だけをノートに残す。

公表原稿は原則日本語LuaLaTeX。既存の公表価値のある成果・十分な証明を削らず、現在の論理的まとまりに従って分割・統合する。ノートは日誌でなく有効な補助知識・反例・文献比較を保持する。現行ソース・PDF・文献・必要なコード・入力・証明書・再現手順だけで自己完結する軽量bundleを作り、旧ZIP・旧原稿・重複・バックアップ・ログ・キャッシュ・中間生成物は含めない。数学的内容や検証可能性を固定容量のために削らない。

研究の区切りには**追加承諾なしでLibraryに現行bundleを保存してよい**。既存Libraryファイルの削除は別操作であり、明示指示なしには行わない。生成・計算・組版・GitHub反映・Library保存を独立に確認し、未実行・失敗・制約を正確に報告する。Gitではソースと必要な再現資産だけを追跡し、PDF・ZIP・ログを追跡しない。


## II. 現在の研究目標と達成基準

中心課題は、次数9の非可換del Pezzoの内在的六公理とheart-exactな反Serre三乗根から、三次元二次AS-regular代数のqgr圏として認識できるかを証明することである。認識対象への所属を公理として追加して問題をすり替えない。数学的重要性・正確性・実現可能性と最新の先行研究に応じ方針を見直す。

達成基準は、一般六公理における `E_{-1}=Ext^1(O,s^{-1}O)=0` と、生成障害 `P=L_O L_{sO} L_{s^2O}(s^3O)=0` の導出、または厳密な反例の構成である。条件付き認識定理はすでに多数あり、その仮定を落とすことを中心にする。標準クラスにおける非標識abel圏の認識と固定三乗根による認識の関係も保持する。

## III. 主要な到達点と証明の所在

- **六公理と三乗根からの有限判定**：`papers/nc_dp9_recognition.tex` の `thm:finite`。 `E_{-1}=0` と `s^3 O∈thick(O,sO,s²O)` を full geometric helix および三次元二次Koszul AS-regular座標環と同値にする。認識の生成障害 `P` は `def:defect` に定義。
- **可換特殊化と線束対象の内在的構造**：同論文の `prop:v9-commutative-specialization`、rank-one例外性とHom半順序、追加仮定下の線束列・数値rank三の復元。証明は本文。
- **Serre消滅の障害**：normal切断、第二Bass空間、残余mutationの純粋性による条件付き消滅・生成の判定。一般的な消滅とfullnessは未解決。
- **次数1・2・3の整なnormal境界**：次数1・2と一次生成された次数3の場合の認識。一般の三次domain境界では両側noetherian性、高Veronese、飽和後section Hilbert列 `3n`、Euler rank 3または5を得る。第三Veronese可換、または滑らかな高Veronese等の仮定下で認識が閉じる。
- **保存した計算・反例**：`research/research_notes.tex` に有限rank数値模型、退化Beilinson例、有限検査の限界、normal境界とstacky節点の局所障害等を保持。実現しない形式模型を六公理の反例と呼ばない。
- **新規性と監査**：公表用原稿の主張は条件を明記するが、全証明の独立監査と網羅的な先行研究調査は未完了。計算検算は証明を代替しない。

## IV. 最優先課題

1. **残余rank5とsection欠損 ε の排除**：三次domain境界で `ε=dim Ext¹(O,s^{-1}O)>0` が可能かを、Euler判別式、normal性、Veroneseの偏極で判定する。既存の `cor:cubic-defect-Euler-rank` と `prop:cubic-defect-mass` から開始。
2. **生成障害Pの消滅または反例**：二重mutationの純粋性・rank-one対象・残余圏の生成を利用する。Grothendieck群上の `[P]=0` を `P=0` と混同しない。
3. **normal元を仮定しないSerre消滅**：左右有限性・第二Bass空間を追跡し、有限検査の限界をノートの明示模型と照合。
4. **既知の非可換射影平面・Z-algebraとの比較**：Mori–Ueyamaのfull geometric helix仮定、AOUの線束復元の適用範囲を検証し、先行研究との新規性を確定する。

## V. 再現方法と関連リポジトリ

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
latexmk -lualatex papers/nc_dp9_recognition.tex
latexmk -lualatex research/research_notes.tex
```

出力は `build/`。TeX・Python・SymPyを用い、必要なHarano Ajiフォントは配布しない。理論的Fano指数・Serre根・Hesse–Sklyanin変形は [categorical-fano-index](https://github.com/uedakazushi/categorical-fano-index) で継続する。共通話題でも両リポジトリの数学的仮定と主張を混同しない。
