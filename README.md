# 非可換9次del Pezzo圏の認識

**2026-11-18 / v18**。最初に [研究方針](00_research_plan.md) を読む。本リポジトリは、内在的六公理とheart-exactな反Serre三乗根から非可換射影平面を認識する研究の正本である。

## 論文と研究ノート

- [反Serre作用の三乗根による非可換射影平面の認識](papers/nc_dp9_recognition.tex)（101頁）：固定した三乗根に対するExtと生成の二障害による有限判定、非標識abel圏との関係、normal境界・高Veronese・飽和性・rank5の解析など条件付き認識結果を含む。元の六公理だけからの一般認識は**未解決**。
- [認識研究ノート](research/research_notes.tex)：既存の有効な数値模型、形式的な障害、明示的反例候補、文献比較、主論文に重複しない計算・証明を整理する。
- [再現手順](research/reproduce.md)：Python検算2本、TeX整合検査、LuaLaTeX組版。

現在の最優先課題は `E_{-1}=Ext¹(O,s^{-1}O)` の消滅と、`P=L_O L_{sO} L_{s²O}(s³O)` という生成障害の消滅、または厳密な反例の構成。一般の三次domain境界に残るrank5とsection欠損が中心的なテストケースである。

**研究の分離**：正規化された圏論的Fano指数、非正規化exact指数、Serre根と非可換変形、Hesse–Sklyanin族、二部グラフなどの正本は [categorical-fano-index](https://github.com/uedakazushi/categorical-fano-index) に移した。本認識研究に必要な概念・証明はこの論文とノートに保持する。

## 検算と組版

```sh
python3 -m pip install -r requirements.txt
bash scripts/check.sh
latexmk -lualatex papers/nc_dp9_recognition.tex
latexmk -lualatex research/research_notes.tex
```

Gitには原稿ソースと検算資産のみ追跡し、PDFやbuild中間物は追跡しない。本文に証明があること、検算したこと、今回独立に監査したことを区別する。mainに直接pushし、PR・Actions・force pushは使わない。
