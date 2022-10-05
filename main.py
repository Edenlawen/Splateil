import deplacement as dp
import bonus




a=dp.creerGrille(10)
a,zz=dp.creerPion1(a)
bonus.poserBonus(a,4,5)
dp.afficherGrille(a)
dp.multimove1(a,zz)

dp.afficherGrille(a)