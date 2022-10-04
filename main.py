import deplacement as dp

a=dp.creerGrille(20)
a,zz=dp.creerPion2(a)
dp.afficherGrille(a)
dp.multimove2(a,zz)
dp.afficherGrille(a)