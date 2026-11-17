# 圏論的 Fano 指数：先行研究・接続・証明境界

**2026-11-17 / v16**。これは作業日誌ではなく、現在の研究を再開するための文献比較と補助知識である。最初に `../00_research_plan.md`、次に `../papers/fano_root_deformations.tex` を読む。数値指数の完全な証明は `../papers/normalized_fano_index.tex`、次数9認識の既存証明は `../papers/nc_dp9_recognition.tex`、以前から有効な補助証明・反例は `research_notes.tex` に保持する。

## 1. 結論と証明状態

研究の中心を「指数の数値的整除性」だけでなく、**根の Hochschild 表現と、それを保つ非可換変形**へ広げる。既知の Serre 根・圏論的偏極の定義を新設したとは主張しない。

新論文の主張の所在は次のとおり。

| 主張 | ラベル | 状態・依存関係 |
|---|---|---|
| Serre 根の HH 作用は有限位数 | `prop:finite-hh` | Perry の既知定理からの帰結。圏自体の有限巡回群作用ではない。 |
| 指定した exact 関手の一次持上げは HH² の固定部分 | `thm:fixed` | Toda と Lowen–Van den Bergh に依存。heart-exact 性の継承を本文で証明。 |
| 相対Serreと冪関係 | `prop:tilting-serre`, `thm:artin-power` | tilting付き幾何のflat Abel変形では相対Serreを構成。HH¹=0なら関手の持上げが自動的に根となる。一般候補heartでは `cor:relative-root` の条件を残す。 |
| 根付き全Artin変形 | `thm:formal-roots` | tilting bundle・HH¹=HH³=0。小拡大の持上げtorsor上で再標識が有限次数となり平均化できる。代数化・巡回coherenceは含まない。 |
| 相対豊富性・例外列 | `prop:relative-ample`, `prop:relative-exceptionals` | nilpotent filtration・Serre消滅・derived Nakayamaによる直接証明。相対perfect圏の主張。 |
| 通常の反標準線束根による tensor は全一次変形へ持ち上がる | `thm:tensor-root` | Fano、HKR の三角作用、有限位数から直接証明。まず関手の持上げ。 |
| 次数2 Geiser根を保つ全形式変形は可換 | `thm:geiser`, `cor:geiser-formal` | 自然反標準指標と全Artin定理。幾何学的変形とのtorsor比較から全次数で可換。scalar慣性付きstack同型は未主張。 |
| 次数4の持上げ配置は C²×(10個の座標 C³ の和集合) | `thm:degree4-arrangement` | Aut=(Z/2)^4 の曲面。全符号群・全線束解を扱う。配置の被約イデアルを計算。`cor:degree4-formal` で各根の不変方向を全形式次数へ延長。異なる根の配置の同時線型化は未主張。 |
| Fermat三次曲面の三乗根 | `prop:fermat-formal` | HH²固有重複度(2,3,3)、固定空間2次元。可換1方向とPoisson商1方向を持つ。純粋なPoisson切断が固定とは限らない。 |
| P² の同じ数値根でも固定 HH² の次元が10/4に分かれる | `prop:plane` | 明示的な三次単項式計算。ある根の非持上げは全根の非存在ではない。 |
| Gepner位相の制約とFano全圏での非存在 | `prop:gepner`, `cor:no-gepner` | 固有値とsupport propertyによる直接の帰結。一般GL₂型のSerre不変性とは異なる。 |
| 全 heart-exact Fano 根の entropy=(0,n) | `prop:entropy` | vector-bundle generator、Serre 消滅、RR、DHKK/FFO の Ext-distance 表示。 |

本文に証明を書いたこと、主要な論理を今回点検したこと、有限計算で照合したことを分ける。外部文献の全証明を独立に再証明したのではない。新規性の不存在確認はできておらず、初等的帰結や既知理論の組合せを独立した新定理として過大評価しない。

## 2. 調査範囲と読み方

公開一次資料について、(A) 用いる定理と関連する証明箇所、(B) 定義・定理の主張と適用仮定、(C) abstract または導入だけ、を区別する。A も論文全体の監査を意味しない。下記の「継承」は既存原稿で確認範囲を記載しており、今回は全面再監査していない項目。2026年の preprint は公表された主張として比較し、未監査の定理を今回の証明に使用しない。

検索は categorical polarization / roots of Serre functor / root pairs / noncommutative Fano / Hochschild deformation / Picard Morita / Nakayama twist / residual category / Gepner stability / polynomial entropy / del Pezzo automorphism / mirror symmetry の周辺を横断した。書誌には採用した一次資料と確認箇所を残す。検索結果や外部PDFをbundleに収録しない。網羅的な新規性認証は未達成である。

## 3. 十五の接続

### 3.1 古典的指数・自己同型群・巡回群コホモロジー

Bondal–Orlov [BO] により、Fano 上の heart-exact 根は L⊗f* と書ける。根の条件は f^r=1 と N_r(f*)L=−K。線束根 rL=−K との違いを消さない。固定した f の解を線束共役で割った集合は、非空なら H¹(C_r,Pic X) の torsor である [Milne]。これは通常の群コホモロジーの応用で、dg 根の cyclic invariance ではない。

新しい接続は、Pic の整数 norm 方程式を解いた後、同じ根の HH² 表現を調べる二段階の判定である。数値等長変換の存在、自己同型の実現、非可換変形上での持上げは三つの別問題。

### 3.2 surface-like 擬格子・Weyl 群・数値的 Riemann–Roch

[dTVdB, Kuz] は Serre 格子、標準類、defect の既存理論。本研究の数値論文はその枠内で unipotent 根を −K の整除性に同定し、非正規化根を半直積 t_H F で記述する。非正 defect と最大指数の P²/quadric 格子分類は既知の Kuznetsov 分類に帰着する。

次の計算は、W(E_n) 上の数値根の分類と、実際の Aut(X) の像を同時に保持すること。次数4では共通の格子に四乗根があっても一般の曲面には自己同値として持ち上がらない。今回の HH 配置は、さらにその上に一次変形の障害を重ねる。

### 3.3 Hochschild 変形・Serre 自明性・有限群の平均化

[Perry] の Serre 自明性から s_HH^r=1。HH² を有限巡回表現にできるため、固定部分は Reynolds 射影で計算できる。[Toda, LVdB] による一次変形の運搬と合成し、指定した根を自己同値として持ち上げられる方向を厳密に決定する。

ここでは s^r=τ≠id。圏上の C_r 作用を仮定して orbifold の公式を使ってはならない。全Artin定理では、相対Serreが全変形に持ち上がるため、**小拡大の持上げtorsorへの再標識作用**が有限次数になる。これはcochain上の厳密有限群作用や高次coherent actionの構成とは異なる。HH¹=0が核の一意性と冪関係を保証する。

### 3.4 Poisson 幾何・Picard re-marking・Morita / B-field 作用

線束 L の tensor による一次 Poisson→可換混合は δ_π(L)=H¹(π♯)c₁(L)。対象 L の持上げと、同じ変形を保つ tensor 自己同値の持上げを区別する。[BDW] の C∞ 形式的 star product ではこの現象は B-field による Morita 作用の一部であり、π♯(1+B♯π♯)⁻¹ という高次式を持つ。しかしこれは射影代数的 Abel 変形への無条件な定理ではない。

本研究では L^r=−K の場合、tensor の HH² 作用が unipotent かつ有限位数であるため恒等となる。通常の指数の根は一次方向を制限せず、混ざった自己同型 f が障害を生む。`nc-cubic-ambient-moduli` の Picard 障害と直接比較できる。別リポジトリの非常に一般の整数核=ZKという主張は研究方針で確認しただけで、今回の証明の入力にはしない。

### 3.5 del Pezzo モジュライ・自然な線型化・座標部分空間配置

[DM, HKT] の自己同型を使い、次数2と4を計算した。反標準写像の**射影**作用だけでは不十分である。Geiser involution は全反標準 divisor を保つが Poisson 切断には −1 として作用する。次数4では符号変換の determinant が反標準表現に掛かる。

一般次数4で根を許す一次Poisson集合は support≤3 の切断。10個の C³、被約イデアル (∏_{k≠i}a_k)_{i=0}^4、Hilbert 級数 (1+2t+3t²+4t³)/(1−t)³ を得る。これはStanley–Reisner型の座標配置だが、全高次の根モジュライのscheme構造・接錐とはまだ同定していない。各根の形式変形問題は滑らかで、符号1個なら3次元、2個なら5次元。可換変形C²は全て残る。異なる線束解の高次固定部分は接空間だけでは区別できない。

### 3.6 AS-regular 代数・Nakayama 自己同型・Zhang twist

[RRZ] の左 graded twist 公式 μ_new=μ_A σ^ℓ ξ_hdet(σ)⁻¹ は、Gorenstein parameter と真の反Serre根の間に Nakayama 補正があることを示す。grading shift のℓ乗を反Serre関手と直ちに同一視しない。[MU] は canonical bimodule と ample full geometric relative helix を認識の仮定とする。訂正済みv4を使う。

優先実験：三次元 quadratic AS-regular 族の potential パラメータに対し、(i) Nakayama norm、(ii) HH² 指標、(iii) root が保つ変形 locus、を別々に計算する。P² の Hesse 型4次元不変空間は最初の明示基準となる。非可換平面全体の指数が落ちると結論してはならない。

### 3.7 ample 両側 tilting・高次表現論・preprojective / CY completion

[Minamoto] は ample two-sided tilting complex から noncommutative Proj を作り、Fano algebra を扱う。[Hanihara] は inverse dualizing dg bimodule の根と root pair による CY completion、folded cluster、Segre 構成を扱う。根に生成 thread を添えることで初めてこれらの構成へ進める。

段階を区別する：数値根 → heart-exact関手根 → invertible dg bimoduleの根 → root pair → cyclically invariant root pair。相対full exceptional collectionと軌道関係の持上げは `prop:relative-exceptionals` で確保した。既に生成threadを持つ場合に役立つが、任意の根にthreadがあることやcyclic invarianceは導いていない。

### 3.8 Lefschetz 分解・残余圏・fractional CY・Serre 次元

[KS] の残余回転 L_a s と [KP] の Serre/spherical twist 補正は、ambient Fano 指数から残余圏へ降りる方法を与える。例外 block の持上げは Ext² 障害が消えても、相対 semiorthogonality・fullness・mutation の base change を点検する必要がある。

根と既存の例外blockは相対perfect圏で同時に持ち上がる。次はその相対mutation回転の周期関係とcoherenceを比較する。一般の complete intersection では単一の純粋な fractional CY 関係にならないことがあり、Serre 次元の上下限との違いが重要。数値窓を full exceptional collection の代わりにしてはならない。

### 3.9 Hochschild–Serre 代数・categorical Torelli

[Lin] は twisted coefficients を含む Hochschild–Serre 代数の群作用と復元を扱う。[LRZ] は del Pezzo の残余圏、spinor modification、次数4の orbifold canonical ring と結び付ける。今回の通常 HH 上の Serre 自明性は、Serre 捩れ全係数での自明性ではない。

接続案：次数4の5個の自然な反標準 character と、pencil の5点からなる復元データを比較し、根の持上げ配置が復元圏から内在的に読めるかを調べる。2026年preprintの主張・定義を確認した段階で、全証明を監査しておらず、今回の定理の入力にはしていない。

### 3.10 Bridgeland / Gepner 安定性・matrix factorization

[TodaGepner] は grade shift ρ^d=[2] に対して位相2/dを考える。本稿の s^r=τ かつ τ_N unipotent は別の関係。数値安定性 sσ=σ·z には rz∈2Z、正規化根なら z∈2Z が必要。さらにsupport propertyを仮定すると、正次元Fanoの全導来圏にはその根に対するGepner型安定性はない。Gepner条件は反標準tensorのmassを一定にするが、support propertyは数値類のノルムをmassで抑え、c₁(ω⁻ᵐ)=m(−K)の増大と矛盾する。これは右C作用に関する結果であり、一般のGL₂型Serre不変性を禁止しない。独立新規性を主張しない。

[ALT] の2026年11月preprintは smooth hypersurface に対する一般の Gepner 構成を主張する。Theorem1.2を確認したが証明全体未監査。今回の結果はこの存在主張に依存しない。残余回転へ移った後に fractional phase が現れる仕組みを、ambient の HH 固定 locus と比較する。

### 3.11 圏論的 entropy・polynomial entropy・成長率

[DHKK, FFO] の Ext-distance 表示を用いる。Fano の heart-exact 根では h_t=0、h_t^pol=dimX。証明は指数ごとの剰余類で直接 Serre 消滅と RR を適用して行い、polynomial entropy の冪不変性を無条件に引用しない（FFO Lemma2.10 の一般形は不等式）。

従って同じ数値根、同じ entropy でも HH² 固定部分が違う。これは root の「次数」「動的成長」「変形を保つ対称性」を別の不変量として測る必要を示す。今後は残余圏に移ると entropy がどの程度根を区別するかを検討する。

### 3.12 HMS・Lefschetz fibration・B+iω と量子接続

[AKO] の del Pezzo HMS と非可換変形は、消滅サイクルと B+iω の変化を結ぶ。今回の根を保つ HH² 部分を mirror の period/area パラメータで記述する課題が生まれる。圏論的 mirror 同値から根を幾何学的 monodromy の分数へ自動同定したり、heart-exact 性を運んだことにしたりはしない。

[KRZ] の量子 central charge と quasi-convergent path は、Fano の semiorthogonal decomposition と安定性の接続候補。ここはabstract確認のみで、定理として使わない。数値Fano指数を量子微分方程式の回転対称性・Stokes構造に比較することは有望だが、今回は予想・計画に留める。

### 3.13 根付きモジュライ・慣性・equivariant deformation・高次障害

指定した根 s の一次空間は HH²^s だが、全根を忘れた locus はその和集合になり、自己同値群による quotient もさらに別である。次数4はそれを明示する例。root の自然同型も標識するなら、群の同型類だけではなく2-groupとcoherenceを扱う必要がある。

del PezzoでHH³=0、さらに次数≤5ではHH¹=0となる。tiltingを用いて相対inverse dualizing kernelを構成し、核の剛性と持上げtorsorのaffine平均化を組み合わせた `thm:formal-roots` が全Artin存在を与える。冪関係のscalarの選択は1+m上のr乗の可逆性で吸収できる。ただしroot pairの巡回不変性や全2-stackの慣性の消去を意味しない。

### 3.14 t-構造付き変形と一般のMorita変形の限界

[Iwanari] はleft/right complete t-構造を持つpresentable stable infinity-categoryの変形をHH cochainsで制御する。IntroductionとTheorems4.5/4.9/4.12の主張を確認したが、全証明は未監査で今回の入力にはしない。一般のnaive Morita変形はSchlessinger条件を満たさないことがある。本稿はflat Abel変形とtiltingモデルの比較 [BW] に限定し、任意のdg圏の変形へHH³消滅だけで結論を拡張しない。

### 3.15 原子的分解・Geiser involution・残余Serre関係

[ESS, Lemma3.17] は次数2の A=O^perp について S_A²=γ*[3] を述べ、Kuznetsov–Perryの二重被覆公式から導く。この一次本文の主張と短い帰着証明を確認した。本研究のambientの根は L⊗γ* で、その平方は反標準tensor。残余圏のS_A²[-3]と混同しない。根付き形式変形が可換に限られるという結果はambientの標準heartに関する制約であり、残余圏の全自己同値を禁止する定理ではない。相対mutationを介した両者の比較と、非可換変形で残余Serre関係がどう変わるかが次の課題。

## 有用な形式幾何上の障害

`ex:nonlinear-fixed`：a(x,y)=(x,−y), b(x,y)=(x,2x²−y) は同じ接作用を持つinvolutionだが固定形式部分はy=0とy=x²。b∘aは無限位数。各根の形式的滑らかさ・一次配置から、複数根の同時線型化や同じ線束解ごとの高次固定部分の一致は従わない。これはdel Pezzoの実現例でなく、誤った推論を防ぐ明示模型である。

## 4. 一次資料と確認範囲

各URLは再取得のための一次資料識別子。書誌の未確認の巻号・頁は補わない。

| ID | 一次資料・識別子 | 具体的な確認範囲 |
|---|---|---|
| BO | Bondal–Orlov, *Reconstruction of a variety from the derived category and groups of autoequivalences*, https://arxiv.org/abs/alg-geom/9712029 | Theorem3.1；既存原稿の確認を継承。 |
| KS | Kuznetsov–Smirnov, *On residual categories for Grassmannians*, https://arxiv.org/abs/1802.08097v3 | B：Definition2.1、Example2.2、Theorem2.8と残余回転。 |
| Minamoto | *Ampleness of two-sided tilting complexes*, 著者版2009-03-07, https://www.math.kyoto-u.ac.jp/preprint/2009/11minamoto.pdf | B：Definition0.1/2.6、Theorem0.2/2.8、Fano algebraの導入。 |
| MU | Mori–Ueyama, *A categorical characterization of quantum projective spaces*, https://arxiv.org/abs/1708.00167v4 | B：Theorem1.2=4.1のAS1/AS2。abstractの訂正告知を再確認。 |
| LO | Loginov–Orlov, *Non-commutative Fano varieties and three-dimensional minifolds*, https://arxiv.org/abs/2609.39766 | B：Definitions2.1,2.3,2.6、Propositions2.7–2.8。 |
| Hanihara | *Calabi–Yau completions for roots of dualizing dg bimodules*, https://arxiv.org/abs/2412.18753v1 | B：Definition2.5、Definitions3.1–3.2、Theorem3.3、後半応用の範囲。 |
| Perry | *Hochschild cohomology and group actions*, https://arxiv.org/abs/1807.09268v2 | A：Proposition1.2、§5.2の証明（Lemma5.3–5.4とtrace）。 |
| Toda | *Deformations and Fourier–Mukai transforms*, JDG81(2009)197–224, https://arxiv.org/abs/math/0502571v3 | B：Theorem1.1のpushforwardとrestrictionの可換図式、HH/HT、§4の変形。 |
| LVdB | Lowen–Van den Bergh, *Hochschild cohomology of abelian categories and ringed spaces*, https://arxiv.org/abs/math/0405227 | B：Theorem3.1のHH³障害・HH²torsor、§4.1。 |
| BDW | Bursztyn–Dolgushev–Waldmann, *Morita equivalence and characteristic classes of star products*, https://arxiv.org/abs/0909.4259 | B：Proposition3.7、Theorem3.11。C∞形式設定を確認。 |
| DM | Dolgachev–Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, https://arxiv.org/abs/2303.16170v2 | B：§2.3の二重被覆と§4のGeiser/自己同型群。 |
| HKT | Hassett–Kresch–Tschinkel, *On the moduli of degree 4 Del Pezzo surfaces*, AS Pure Math69(2016)349–386, https://cims.nyu.edu/~tschinke/papers/yuri/13noheighttwo/noheighttwo13.pdf | B：導入の2次元moduliと一般Aut、§2のpencil・conic・D5。 |
| TodaGepner | *Gepner type stability conditions on graded matrix factorizations*, https://arxiv.org/abs/1302.6293 | B：Definition2.3、grade shiftと位相の規約。 |
| ALT | Aravena–Liu–Tevelev, *Gepner stability conditions on hypersurface categories*, https://arxiv.org/abs/2611.05350 | B：2026-11-03提出、Theorem1.2の主張。全証明未監査・不使用。 |
| DHKK | Dimitrov–Haiden–Katzarkov–Kontsevich, *Dynamical systems and categories*, https://arxiv.org/abs/1307.8418v1 | A/B：Lemma2.5、Theorem2.6のExt-distance表示と使用条件。 |
| FFO | Fan–Fu–Ouchi, *Categorical polynomial entropy*, AdvMath383(2021)107655, https://irma.math.unistra.fr/~lfu/articles/CatPolyEntropy.pdf | A/B：Lemmas2.7/2.10、Proposition6.4、Theorem6.7、line-bundle tensorの証明箇所。 |
| RRZ | Reyes–Rogalski–Zhang, *Skew Calabi–Yau algebras and homological identities*, https://arxiv.org/abs/1302.0437v2 | B：Theorems0.3–0.4、left twistとhdetの規約。 |
| KP | Kuznetsov–Perry, *Serre functors and dimensions of residual categories*, https://arxiv.org/abs/2109.02026 | B：導入、complete intersectionのSerre/spherical twist、§6の帰結。 |
| Lin | *Group action of Hochschild–Serre algebra and categorical reconstruction*, https://arxiv.org/abs/2609.07562 | B：§2–3の定義・Theorem2.8、主結果の適用範囲。全証明未監査。 |
| LRZ | Lin–Rampazzo–Zhang, *Categorical reconstruction of del Pezzo surfaces: Hochschild–Serre algebras and spinor modifications*, https://arxiv.org/abs/2609.10344 | B：Introduction、次数4のorbifold canonical ringの記述。全証明未監査。 |
| AKO | Auroux–Katzarkov–Orlov, *Mirror symmetry for Del Pezzo surfaces: Vanishing cycles and coherent sheaves*, https://arxiv.org/abs/math/0506166 | B：Theorems1.4/1.6、非可換変形とB+iωの範囲。 |
| KRZ | Karube–Robotis–Zuliani, *Toward the noncommutative minimal model program for Fano varieties*, https://arxiv.org/abs/2601.20739 | C：abstractの量子central charge・準収束経路のみ。 |
| dTVdB | de Thanhoffer de Volcsey–Van den Bergh, *On an analogue of the Markov equation for exceptional collections of length 4*, https://arxiv.org/abs/1607.04246 | 継承：§3.2–3.3のSerre lattice。 |
| Kuz | Kuznetsov, *Exceptional collections in surface-like categories*, https://arxiv.org/abs/1703.07812 | 継承：標準類、defect、公刊版Theorem5.12（arXivv2では5.11）。 |
| Keeler | *Criteria for sigma-ampleness*, https://arxiv.org/abs/math/9912051 | 継承：Theorems1.2–1.3。quasi-unipotenceと根のunipotenceを区別。 |
| Milne | *Class Field Theory*, v4.03, https://www.jmilne.org/math/CourseNotes/CFT.pdf | 継承：II, Example1.20の巡回H¹とnorm核。 |
| HP | Hille–Perling, *Tilting Bundles on Rational Surfaces and Quasi-Hereditary Algebras*, AIF64(2014)625–644, https://arxiv.org/abs/1110.5843 ; DOI:10.5802/aif.2860 | B：Theorem1.1の仮定と主張、導入の構成。出版社書誌確認。全構成証明は未監査。 |
| BW | Barmeier–Wang, *Deformations of categories of coherent sheaves via quivers with relations*, Algebraic Geometry11(2024)1–36, https://arxiv.org/abs/2107.07490 ; DOI:10.14231/AG-2024-001 | A/B：Theorems3.1/3.18、Proposition3.21とその証明・依存先。出版社pp.18–19画像も確認。 |
| LowenOb | Lowen, *Obstruction theory for objects in abelian and derived categories*, Comm.Algebra33(2005)3195–3223, https://arxiv.org/abs/math/0407019 | B：TheoremsA/B、有限coflat/Tor次元、核Ext¹/²の範囲を本文・画像確認。全証明未監査。 |
| KellerDIH | Keller, *Derived invariance of higher structures on the Hochschild complex*, 2003, revised2018, https://webusers.imj-prg.fr/~bernhard.keller/publ/dih.pdf | B：Theorem3.2と§4.6、cofibrancy・両側fully faithfulの条件。画像確認。 |
| Iwanari | *Hochschild cohomology and deformation theory of stable infinity-categories with t-structures*, https://arxiv.org/abs/2506.21867v1 | B：Introduction、Theorems4.5/4.9/4.12。一般Morita変形との区別。証明未監査・本稿の入力ではない。 |
| ESS | Elagin–Schneider–Shinder, *Atomic decompositions for derived categories of G-surfaces*, https://arxiv.org/abs/2512.05064v1 | B：Lemma3.17とそのKPへの短い帰着。全原子的分解定理は未監査。接続に限り引用。 |

未取得・未確認の文献内容は、推測で補わず証明の入力にしない。旧認識論文のAZ/Artin–Stafford等に関する確認限界は `research_notes.tex` の文献節に保持している。最新の全研究動向の網羅性を保証するものではない。

## 5. 次の課題：具体的な着手順

1. **代数化と明示式**。次数4の固定した根、またはFermat三次の2次元固定変形でtilting quiverを選び、根のinvertible bimoduleと積の変形を有限次数で明示する。全形式次数の存在は証明したが有限型代数化は別。BWのalgebraization条件との照合を最初に行う。
2. **同時根付き変形**。同じfを持つ異なるL、複数符号根について、再標識作用の合成をHH以外の高次へ持ち上げて比較する。10-plane配置を完成した根moduliの接錐とはしない。
3. **HH¹が非零の場合**。P²とquadricの自己同値核を非可換unipotent群として扱い、norm補正とscalar coherenceの障害を分離する。HH¹=0の核一意性をそのまま使わない。
4. **残余圏・HMS・root pair**。相対例外列の存在からmutation回転を構成し、ESS/KPのGeiser関係、Haniharaのcyclic invariance、AKOのB+iωパラメータへ実際の比較写像を作る。

元の六公理からの一般認識、一般の非可換KO上界、normal元なしの消滅、生成障害の零性は依然未解決。tilting付き幾何の形式近傍で得た相対ample性を、これらの一般問題の解決と取り違えない。
