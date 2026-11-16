非可換9次del Pezzo認識：研究継続bundle
2026-11-17 / v10

再開順序と研究対象
最初に research_plan.pdf（または research_plan.tex）を読む。
次に nc_dp9_recognition.pdf、必要に応じて research_notes.pdf を参照する。
認識対象は、三次元二次AS-regular代数Sのqgr Sとexact同値なabel圏という標準ncP²のクラスである。
六公理はこのクラスの内在的な候補特徴付けであり、標準定義との同値は未証明である。
通常のgraded表示、構造対象、heart-exactな反Serre三乗根を選ぶことと、abel圏への所属を区別する。
六公理、現在の証明、未解決の核心と次の具体的な着手方法をこの一式に含む。
旧bundle・過去の会話・別途保存した旧ノートを研究再開の前提にしない。
主張の完全な仮定・証明・先行研究との関係は現行原稿と研究ノートに置く。

中心結果と状態
A=⊕_(n≥0) Hom(O,s^n O)、s^3≅S^(-1)[2]、E_n=Ext^1(O,s^n O)、
P(n)=(n+1)(n+2)/2とする。以下では結果ごとの追加仮定を区別する。

1. 可換特殊化と、標準クラスの内在的認識への橋渡し
   滑らかな連結射影複素多様体Xに対し(coh X,F)が六公理を満たせば、X≅P²でFは線束である。
   この可換特殊化には反Serre三乗根を仮定しない（主原稿 prop:v9-commutative-specialization）。
   標準ncP²では、AOUの有限長Serre filtrationによるrank-one torsion-free条件とχ(I,I)=1が
   標準対象πS(n)を内在的に識別し、exact自己同値はその順序集合Zに平行移動を誘導する
   （lem:v9-intrinsic-line-translation）。AOUのfiltrationは六公理のCat_0,Cat_1と同じである。
   従って六公理と固定した許容exact rootの下で、次は同値である：
     Catが標準ncP² ⇔ 固定したAが三次元二次Koszul AS-regular ⇔ E_-1=0かつ生成障害P=0。
   証明は標準クラスに属すると仮定した方向にAOUを適用し、標準full strong tripleを得てから
   既存の有限認識定理を使う（prop:v9-marking-independence）。
   この範囲では一つの許容rootの障害非消滅は、同じabel圏の別のAS-regular表示も排除する。
   heartを変更した導来同値や、rank-one条件を失う構造対象の変更についての主張ではない。

2. 六公理からの内在的線束対象と数値rank三での復元
   L(Cat)={rank-one torsion-free I : chi(I,I)=1}/isomorphism と置く。
   六公理だけでEnd(I)=C、Ext²(I,I)=0、chi(I,I)=1とexceptional性の同値、Hom非消滅による半順序が従う。
   この部分に三乗根は不要である（lem:v10-negative-line-hom、prop:v10-lines-exceptional-order）。
   任意のFについて反標準Hilbert関数は(9/2)rank(F)n²+O(n)である。
   homogeneous Ore局所化とfree部分加群のtorsion商から、generic rankとの一致を直接証明する
   （prop:v10-rank-hilbert-leading）。
   全対象の漸近Serre消滅(SV)の下でrankはK_numへ降下し、heartの非零対象は数値的に零にならず、
   L(Cat)の対象は数値類で一意に決まる（prop:v10-numerical-line-rigidity）。
   さらにexact rootと全K_numのQ-rank=3を仮定すると、L(Cat)={s^n O : n∈Z}、Hom順序は整数順序、
   exact反Serre根の可能次数は{1,3}となる（thm:v10-numerical-line-lattice）。
   全K_num rankとorbit rankは区別する。この段階では全E=0、Hom(O,sO)の次元3、生成障害P=0を結論しない。
   E_-1=0は得られるため、残る認識条件はP=0である。文献上の新規性は未確認。

3. 標準クラスのexact反Serre指数
   Itaba–MatsunoのCY表示により、全標準ncP²には点ごとにheart-exactな三乗根が存在する。
   exact tについてt^r≅τ=S^(-1)[2]となる正整数rの集合は{1,3}であり、最大値i_ex(Cat)=3である
   （主原稿 cor:v9-exact-index）。CY表示ではτ=(3)、線対象の添字平行移動はr d(t)=3を満たす。
   AOUとItaba–Matsunoの既知結果の短い帰結であり、独立した新規性を主張しない。
   一つのgraded表示の標準shiftがそのままrootであるとは限らない。
   一般の六公理の候補圏のroot存在・指数上界・指数3による認識、族における互換的root選択は未証明。

4. 一般の整三次境界の標準section列
   ここからの三次境界の結果には、六公理・heart-exactな三乗根・非零normal元g∈A_3・
   domain商B=A/(g)を仮定する。
   全n>0でdim hatB_n=3n、全整数nでχ_qgrB(D,D(n))=3nが成立する
   （主原稿 thm:v8-cubic-standard-sections）。
   q_n=χ(O,s^n O)=P(n)-epsilon*1_(3∤n)、epsilon=dim E_-1=dim E_-2。
   Euler orbit rankは自動的に有限で、epsilon=0なら3、epsilon>0なら5である。
   有限rankを追加仮定しない。epsilon>0の排除と元の境界の一次生成性はこの定理の結論ではない。
   証明は、両側noetherian性、chi_1のVeroneseへの継承、高Veroneseの全THCR表示、
   構造対象からのcohomologyの自然な比較、正負両側のRiemann–Rochからなる。
   有限rankからの独立の準多項式による数値的証明も現行本文に保持する。

5. 滑らかな高Veroneseから元の境界heartとshiftを復元
   高Veronese B^(N)=B(C,M,rho)の曲線Cが滑らかなら、関数体の次数1自己同型sigmaはCへ延長し、
   全剰余層F_rは可逆である。deg F_r=3rと積の閉性から高次数の分数可逆層G_nはcocycleをなし、
   それを一次へ延長してdeg L=3のTHCR T=B(C,L,sigma)を構成する。
   B⊂Tは有限余次元で、(qgr B,D,(1))≅(coh C,O,sigma^(-1)*((- )⊗L))、hatB≅Tである
   （thm:v10-smooth-veronese-heart）。元のVeronese直像も同値となり、その核は零。
   singular Cでも、sigmaがCへ延長し、gcd(r,N)=1の一つのF_rが可逆なら同じ結論となる。
   特にF_1が可逆なら足りる（lem:v10-one-invertible-residue）。
   共通高次数idealによるtails同値、積のdense性まで本文で直接証明する。
   B=hatBやepsilon=0はこの復元だけでは結論しない。Artin–Staffordの分類との新規性比較は未完了。

6. 三次境界のEuler判別式による欠損消滅と認識
   五つの軌道類[L_0],...,[L_4]のEuler行列G_eはdet G_e=3^5*epsilon²を満たす。
   polynomialな三次元部分と周期的な二次元部分は左右双方に直交し、後者は9*epsilon*A_2型である
   （lem:v10-period-three-discriminant）。epsilon>0なら五次元軌道空間の判別式平方類は[3]。
   Euler形式を経由する整数格子Nのrank≤5、rank5なら判別式平方類≠[3]（または退化）であれば、
   epsilon=0、全E=0、B=hatBとなる。特にrank≤5かつunimodularで十分
   （prop:v10-unimodular-cubic-defect）。Nは全数値格子でよく、rank上界とunimodularityは追加仮定。
   高Veronese曲線が滑らか、または元の通常曲線triple表示がある場合には、この数値条件からAを認識する。
   具体的にはDb(Cat)に長さ5以下のfull exceptional collectionがあれば認識が成立する
   （cor:v10-five-exceptionals-recognition）。例外列のstrong性やrank-one性は仮定せず、認識後の長さは3。
   全rank≥6のunimodular格子はこの議論で排除できない。一般の数値モデルの位数6成分にも適用しない。

7. 第三Veroneseが可換な境界の認識
   B^(3)可換 ⇔ A^(3)可換 ⇔ A≅C[x_0,x_1,x_2]^sigma、sigmaは線形でsigma^3=id
   （主原稿 thm:v8-commutative-veronese-boundary）。
   (Cat,O,s)≅(coh P²,O,alpha^*(-)⊗O(1))、alpha^3=idという、構造対象と固定したshiftを含む認識である。
   E=0、B=hatB、Aは三次元二次Koszul AS-regular、Bはintegral plane cubicのTHCRとなる。
   境界の生成次数・飽和性・幾何学的表示・gの中心性を追加仮定しない。
   B自体が可換ならAは通常の三変数多項式環となる（thm:v7-commutative-cubic-recognition）。
   既知のskew Fermat例により、B^(3)だけの可換性はBの可換性より真に弱い。
   sigmaとalphaの位数は3を割ればよく、恒等自己同型も含む。

8. 幾何学的境界の中心化と一つの障害への還元
   追加的に(qgr B,D,(1))≅(coh C,O,L⊗sigma^*(-))、p_a(C)=1、deg L=3があるとする。
   Bの飽和性は仮定せず、U=A^(3)をZhang twistして、同じ非可換THCRを商に持つ中心的な次数9被覆Vを得る
   （主原稿 prop:v8-geometric-central-reduction）。
   この幾何学的表示の下では、epsilon=0、B=hatB、B一次生成、AのAS-regular性、
   Euler rank=3、Euler rank≤4、dim A_1=3、dim A_2=6が同値である
   （cor:v8-geometric-one-obstruction）。
   Vの圏が標準ncP²と認識できれば、標識非依存命題から元の固定したAも認識できる。
   この境界設定ではK_0のrankによる独立な数値的証明も保持する。
   RSSの認識には特定のg-divisible ideal・overmodule・endomorphism Hilbert級数・divisor等式がさらに必要。
   次数9と有限qgr homological dimensionだけでは適用しない。

9. 環論的な補助帰結
   一般の三次domain境界でAとBはともに両側noetherian、各Veronese上で左右有限である
   （主原稿 cor:v8-cubic-ambient-noetherianほか）。
   Aの左noetherian性はgr_(g)A≅B[z;nu_bar]と固定全次数内で停止する初期項消去から従う。
   研究ノート prop:v8-boundary-full-chi / cor:v8-ambient-full-chi はAとBの両側full chiを証明する。
   両側torsion functorのcohomological dimensionはBで2以下、Aで3以下
   （同 prop:v8-ambient-local-cd）。chiの持上げと、local cohomologyの右有界性・次数周期性を直接証明する。
   これらの有限性を、epsilon=0や一次生成性と取り違えない。

10. 数値と有限の例外列だけによる定義の限界
   三頂点、各段三本の矢v_i,w_j、関係w_0 v_i=0の退化Beilinson代数Lambdaは、
   smooth properな導来圏とP²のEuler行列を持つfull strong tripleを持つが、
   (dim HH^0,dim HH^1,dim HH^2)=(1,14,16)である。
   全標準ncP²ではdim HH^2≤10なので、そのいずれとも導来同値でない。
   指定tripleのhelixにも負次数Homが現れる。
   研究ノート ex:v9-degenerate-beilinson / prop:v9-degenerate-beilinson-hochschild に
   完全なbimodule分解と証明を置く。verify_identities.pyにはnormalized relative bar複体による独立検算を含む。
   これは六公理全体への反例ではない。smooth proper dg性やfull strong tripleとEuler行列だけを
   geometric helix、heartの正値性、AZ生成の代わりにする定義を排除する例である。

現行原稿の他の主要到達点
・有限認識：E_-1=0と生成障害P=0による判定。
  残余回転のSerre関係と一対象の軌道生成、二重mutationのheart内純粋性による生成判定。
・実局所cohomologyの左右作用、Bass空間による有限性の判定。
  AまたはA^(3)に正次数normal元があればE有限。飽和normal商があれば全E=0。
  normal切断の構造対象の双対性、support障害、高次Ext周期性。
・数値rank条件、低次数増大制約、normal半群型の最小増大の排除。
・次数1または2のnormal元の商がdomainなら、三次元二次Koszul AS-regular認識。
・一次生成・両側noetherian・双有理的に幾何的という追加条件の下での曲面認識。
・三次境界の有限section欠損の質量、Extの復元、Laurent多項式とmoment公式。
  一次生成されたintegral genus-one THCR境界のnormal被覆はAS-regular型または分裂Ore型。
  後者は有限qgr homological dimensionと両立しない。この被覆定理は六公理を必要としない。
  重み付き完全交叉境界の全normal被覆の分類・排除も、弱い仮定での独立した結果として保持する。
  局所平面性、忠実な方程式指標、conductor次数式、整数次数の忠実な偏極によるstackの排除。
各結果の正確な仮定・証明所在は研究方針と主原稿に記す。本文にある証明、独立点検、計算検証は別に扱う。

未解決の核心と次の着手
六公理だけで内在的線束対象の例外性・Hom半順序、SVの下で数値的一意性まで得た。
SV・exact root・全K_num rank3なら線束列とexact指数も復元済みであるが、全導来圏の生成が残る。
この範囲では隣接対象の評価射、kernel/cokernelのrankとtorsion、二重mutationの純粋性を調べ、P=0へ結び付ける。
数値的に零のheart対象がないことから、導来残余圏の消滅を推論しない。
一般の六公理からSV・全数値rank3・root存在が従うかは別の未解決問題として保持する。

具体的な第一の路線は、第三Veroneseも非可換な三次domain境界でのepsilon>0の排除と元の一次生成性である。
高Veroneseの通常曲線表示、標準section列、有限Euler rank、両側noetherian・chi・有限torsion次元は確保済み。
高Veroneseの曲線が滑らかな場合、元のheartとshiftの復元は解決した。
この範囲では、Euler格子のrank上界・判別式・unimodularityを六公理と境界構造から導くことを優先する。
特異曲線では、関数体自己同型sigmaが曲線へ延長することと、一つの原始剰余層F_rの可逆性を調べる。
これらが得られれば同じ復元・認識判定へ進める。cohomology保存だけから同値を推論しない。
中心的次数9被覆のidealやdivisorを用いる経路ではRSSの追加仮定を個別に検証する。
normal元を仮定しない範囲では、E有限性、E_-1=0、mutation純粋性・生成障害の消滅が残る。
AZ1を評価射の核・余核に使い、数値・smooth proper性だけでは見えない生成を検出する。
一般の六公理の候補圏におけるrootの存在、exact指数上界、三乗根を仮定しない認識は未解決。
全六公理を満たす非AS型の実構成は得ていない。中心結果の文献上の新規性は未確定である。

研究ノートの役割
現行の例・反例・別証明・文献比較を収め、作業履歴は含めない。
可換射影空間の認識との比較、AS-regular/Z-algebra/geometric helixによる定義、
形式abel変形と導来同値の区別、退化Beilinson代数のHochschild障害を整理する。
A_*の実乗法と全反標準Hilbert列、normal半群環A(q)、weighted stackの生成障害、
形式Ext双加群、分裂conicの頂点Ext、B_nodeとcyclic stack境界族、有限欠損のambient実現、
無限位数の非可換境界、Koszul持上げ、Zhang twistの規約、局所高次cuspの障害を保持する。
weighted stack P(1,1,4)はAZ1以外の公理とexact rootを満たし、E=0、q=Pでも生成障害が残る。
これは反標準のAZ生成を省けないことを示し、粗weighted projective schemeとは区別する。
これらを六公理全体の反例と扱わず、欠けている仮定を各例に記す。
負次数derivationの消滅から中心被覆の自己同型が恒等となる補助補題も完全証明を収録する。
主原稿に完全証明がある結果は、ノートで証明全文を重複させず参照する。

構成
  research_plan.tex / .pdf       現行研究方針・一般8原則・保存許可（最初に読む）
  nc_dp9_recognition.tex / .pdf   日本語LuaLaTeXの主原稿
  numerical_rank_section.tex    主原稿から読み込む数値rank節
  research_notes.tex / .pdf      現行の具体例・補助証明・文献確認範囲
  preamble.tex                  共通LuaLaTeX設定
  .latexmkrc                    latexmk設定
  verify_identities.py           数値・Hilbert恒等式・conic行列・三次境界・Hochschildの厳密検算
  verify_toric.py                A_*の全積表と半群環A(q)の厳密有限検算
  README.txt                    本文書
以上12ファイルを収録する。外部文献PDF、旧版、ログ、キャッシュ、組版中間生成物は含めない。

再生成
TeX LiveのLuaLaTeX、LuaTeX-ja、AMS・geometry・mathtools・enumitem・booktabs・hyperref・fix-cm、
Noto Serif CJK JP / Noto Sans CJK JPを用意する。
フォントがない場合は導入するか、preamble.texのフォント名を利用可能な日本語フォントへ置き換える。
数学的ソースに外部データ依存はない。このディレクトリで以下を実行する。

  latexmk -lualatex research_plan.tex
  latexmk -lualatex nc_dp9_recognition.tex
  latexmk -lualatex research_notes.tex
  python3 verify_identities.py
  python3 verify_toric.py

PDFはTeXと同じディレクトリへ出力される。二つの検算コードはPython 3標準ライブラリだけを使用する。
環境のcacheは再現入力ではなく、配布しない。

検算の対象と数学的証明との区別
verify_identities.pyはrank5モデルの行列式・漸化式、Hilbert恒等式、四候補、位数6の証明書、
weighted stackのmutation係数、C_ex、conic行列、三次境界の完全交叉・二項形式を厳密検算する。
B_nodeの生成元の像は次数0..12、有限欠損モデルは次数30まで、五つの形式欠損分布の
Laurent恒等式・telescoping・一次momentは全support、Hilbert/Euler式は次数0..34と対応する負次数を対象とする。
退化Beilinson代数については基底の乗法を実装し、normalized relative bar複体とその微分を構成して
HH^0,HH^1,HH^2の次元(1,14,16)を独立に検算する。
三次Euler判別式については、パラメータepsilonの多項式としてT^t G_e Tの全25成分、
左右直交ブロックの消滅、det T=27、det H_e=3^6、det G_e=3^5*epsilon²を厳密検算する。
verify_toric.pyはA_*の次数0..60、全36積、自由基底、pairing、非normal性証明書とface quotientを対象とする。
A(q)はq=2..8について、次数0..6qの格子点、3q個の自由基底、次数3q+1までの最小生成元を対象とする。
無限個のパラメータや全次数の結論には本文の証明を用い、有限検算で代用しない。
可換特殊化、標識非依存、exact指数、標準section列、Veronese cohomology比較、局所・大域境界幾何、
第三Veronese可換認識等は数学的証明であり、これらのコードによる形式的認証ではない。
未構成の圏の存在を計算で確認したという意味でもない。

生成・確認・保存の状態（2026-11-17 / v10）
・生成：日本語LuaLaTeXで主原稿101頁、研究ノート60頁、研究方針14頁を生成した。
・組版：各文書の最終ソースを3回処理。最終ログの警告、未解決参照、重複ラベル、文献キー欠落、
  Overfull/Underfull、文字欠落はいずれも0。入力ファイルの存在も確認した。
・視覚確認：3文書の全175頁を画像化し、全頁の一覧と主要な数学頁・長い数式を単頁拡大で点検した。
  研究ノートの文献項目の頁分断を調整し、影響した最終4頁を再確認した。
  変更のない先行56頁は画像のbyte一致も確認した。切れ・重なり・欠字・版面はみ出しは認めなかった。
・数学的点検：内在的lineの負方向Hom・例外性・数値一意性、generic rankと最高次係数、
  全数値rank3の整数格子・線束列、余有限cocycle・原始剰余の可逆性・tails同値、
  cubic判別式と認識への帰結の証明を記述し、仮定と各推論を点検した。
  line/rankとheart復元の主要証明は別担当でも独立に監査した。
  外部文献の全証明や、既存本文の全結果を今回一から再証明したという意味ではない。
・verify_identities.py：全検算に成功。三次Euler行列の全25成分の基底変換と判別式は
  有理係数の多項式恒等式として検証した。既存のHilbert・conic・Hochschild等の検算も保持し実行した。
・verify_toric.py：本書に記した範囲の厳密有限検算を全て実行し成功した。
・保存許可を含む一般8原則は2819 bytesをbyte同一に保持した。
・配布ZIP：現行12項目だけを収録し、CRC検査と全項目の内容・配布元ファイルとのbyte一致を確認した。
・永続保存の成否は、以上の生成・検証と区別し、実際の保存応答に基づいて配布時に報告する。

文献と公表前の確認課題
必要な書誌情報・識別子・リンク・参照箇所は主原稿と研究ノートの文献表にある。
標準クラスの定義にはATV、Bondal–Polishchuk、Van den Bergh、Mori–Ueyamaを用い、
regular Z-algebraの点別1周期性と、変形族全体の互換的なgraded表示の存在を区別する。
AOUのDefinition A.3、Corollary A.7、Theorems A.8・7.1とAppendix A、
Itaba–MatsunoのTheorems1.1・4.4とLemma2.5、BelmansのTable1・Propositions3・17・19・Corollary20・§4.1を本文で確認した。
AOUはarXiv:1411.7770 (2014)のプレプリントとして引用し、未確認の刊行情報を補わない。
BelmansのHH²上界は代数閉体・標数≠2,3で、全退化cubic型とlinear caseを含む標準クラス全体に適用される。
通常のabel圏のHHと標準dg enhancementのHHの一致、および有限次元tilting代数のderived invarianceを用いる。
標準クラスのexact指数3と標識非依存の橋渡しについて、独立した新規性を主張しない。

可換認識の比較ではKachi–Kollár、Sieder、Kebekus、K. Fujita、Liu、Vialの該当本文を確認した。
T. Fujitaは出版社公開のChapter I冒頭のTheorem(1.1)と証明冒頭を確認し、書籍全文は未取得。
Kobayashi–Ochiai、Mori、CMSBの原論文本文は未取得で、確認済みの強化版または明示的再掲を根拠とする。
既知の可換認識定理を本研究の新規な成果として扱わない。

Bondal–Van den Bergh §4.1の式(4.1)、Lemmas4.1.4–4.1.6と証明を一次資料で確認した。
chi判定のLemma4.2.1には後続節の仮定が引き継がれるため、境界の有限torsion次元を先に証明して適用する。
Baumann–Belmans–van GarderenのarXiv:2410.07620v1 §6.1、Proposition50、Lemma52を本文で確認した。
同論文はTrans.AMS379(2026),3537–3589, DOI10.1090/tran/9571として出版されており、著者の公開一覧で書誌を確認。
参照番号・頁は確認済みarXiv版による。出版社最終版本文は未取得。
RSSのNotation3.2、Theorem4.3、条件(4.1)–(4.2)、Remark4.13を一次本文で確認した。
Rainsの負次数derivation・filtered deformationの結果とConjecture1を確認し、既知結果と未解決の認識を区別した。
Artin–Stafford原論文本文は未取得。出版社abstractと共著者Stafford–Van den Berghの
Theorems5.1・5.2・5.5・5.6で正確な定理文・適用条件を照合し、原典全証明の点検とは区別する。
Artin–Zhang原論文全文も未取得であり、再構成・chiの定理文は再掲資料と照合した。
Zhangのtwist原論文は書誌とabstractを確認し、必要な同値・三乗根の識別は本文で直接証明した。
ATV、Cassidy–Shelton、Iyudu–Shkarin、Gulliksen、Levchenko、Nironi、Smyth、
Stacks、Dolgachev–Martin等の確認済み箇所と残る未確認点は研究ノートへ集約する。
既知の曲線分類・局所特異点分類・twist一般論・del Pezzo分類を本研究の独自成果とは扱わない。
THCRの積と右/左規約はChirvasitu–Kanda–Smith, arXiv:1908.06525v3 (2021), §2.3、
Proposition2.2、Theorem2.4の一次本文を確認した。同所はArtin–Van den BerghのTheorems1.3–1.4を再掲する。
Artin–Van den Bergh原論文の全証明を直接点検したという意味ではない。
内在的lineの候補圏での復元と、余有限cocycleによるheart復元の先行研究比較は未完了。
原典の未確認箇所の解消と、中心定理の系統的な新規性比較を公表前の課題とする。

保存権限と現行版の方針
研究の区切りごとのLibrary保存は許可済み。既存項目の削除はこの許可に含まない。
このbundleは現在の研究だけを含み、過去版の保存・復元を目的とした資料を含めない。
生成、検証、保存は別々の状態として扱い、保存の成否は実際の操作結果に基づいて報告する。
