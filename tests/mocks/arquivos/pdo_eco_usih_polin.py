MockPdoEcoUsihPolin = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  MODELO DESSEM     - VERSAO 19.4.1 -   Maio  de 2023 (CPLEX)                       *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA ONS                                                                                                                                                   \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    "  TE  PMO - JUNHO/23 - JULHO/23 - REV 2 - FCF COM CVAR - 12 REE - VALOR ESPERADO - Data do Caso: 13/06/2023                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "-----------------------------------------------------------------------\n",
    "Dados gerais das usinas hidroeletricas e da topologia dos reservatorios         \n",
    "-----------------------------------------------------------------------\n",
    "----------------------------------------------------------------------------------------\n",
    "USIH:                 Numero de cadastro da usina hidroeletrica                                                                                                                                         \n",
    "NomeUsih:             Nome de cadastro da usina hidroeletrica                                                                                                                                           \n",
    "ICOEF:                Indice do coeficiente do polinomio                                                                                                                                                \n",
    "Cota X Volume:        Coeficientes do polinomio Cota X Volume                                                                                                                                           \n",
    "Area X Cota:          Coeficientes do polinomio Area X Cota                                                                                                                                             \n",
    "Cota X Vazao (Hjus1): Coeficientes do polinomio Cota X Vazao para a Cota de jusante HJUS                                                                                                                \n",
    "Hjus1:                Cota de jusante de referencia para o polinomio Cota X Vazao                                                                                                                       \n",
    "Cota X Vazao (Hjus2): Coeficientes do polinomio Cota X Vazao para a Cota de jusante HJUS                                                                                                                \n",
    "Hjus2:                Cota de jusante de referencia para o polinomio Cota X Vazao                                                                                                                       \n",
    "Cota X Vazao (Hjus3): Coeficientes do polinomio Cota X Vazao para a Cota de jusante HJUS                                                                                                                \n",
    "Hjus3:                Cota de jusante de referencia para o polinomio Cota X Vazao                                                                                                                       \n",
    "Cota X Vazao (Hjus4): Coeficientes do polinomio Cota X Vazao para a Cota de jusante HJUS                                                                                                                \n",
    "Hjus4:                Cota de jusante de referencia para o polinomio Cota X Vazao                                                                                                                       \n",
    "Cota X Vazao (Hjus5): Coeficientes do polinomio Cota X Vazao para a Cota de jusante HJUS                                                                                                                \n",
    "Hjus5:                Cota de jusante de referencia para o polinomio Cota X Vazao                                                                                                                       \n",
    "Cota X Vazao (Hjus6): Coeficientes do polinomio Cota X Vazao para a Cota de jusante HJUS                                                                                                                \n",
    "Hjus6:                Cota de jusante de referencia para o polinomio Cota X Vazao                                                                                                                       \n",
    "----------------------------------------------------------------------------------------\n",
    "\n",
    "-----;--------------;-----;---------------------;---------------------;---------------------;-------;---------------------;-------;---------------------;-------;---------------------;-------;---------------------;-------;---------------------;-------;\n",
    "USIH ;   NomeUsih   ;ICOEF;    Cota X Volume    ;     Area X Cota     ;Cota X Vazao (Hjus1) ; Hjus1 ;Cota X Vazao (Hjus2) ; Hjus2 ;Cota X Vazao (Hjus3) ; Hjus3 ;Cota X Vazao (Hjus4) ; Hjus4 ;Cota X Vazao (Hjus5) ; Hjus5 ;Cota X Vazao (Hjus6) ; Hjus6 ;\n",
    "  -  ;      -       ;  -  ;  (m/((hm3)^(IND)))  ;  (m/((km2)^(IND)))  ;  (m/((km2)^(IND)))  ;  (m)  ;  (m/((km2)^(IND)))  ;  (m)  ;  (m/((km2)^(IND)))  ;  (m)  ;  (m/((km2)^(IND)))  ;  (m)  ;  (m/((km2)^(IND)))  ;  (m)  ;  (m/((km2)^(IND)))  ;  (m)  ;\n",
    "-----;--------------;-----;---------------------;---------------------;---------------------;-------;---------------------;-------;---------------------;-------;---------------------;-------;---------------------;-------;---------------------;-------;\n",
    " 001 ; CAMARGOS     ;  0  ;      0.89296997E+03 ;      0.13334300E+05 ;      0.88609998E+03 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 001 ; CAMARGOS     ;  1  ;      0.62089000E-01 ;     -0.32866089E+02 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 001 ; CAMARGOS     ;  2  ;     -0.11041000E-03 ;      0.20089300E-01 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 001 ; CAMARGOS     ;  3  ;      0.12469999E-06 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 001 ; CAMARGOS     ;  4  ;     -0.55512001E-10 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 002 ; ITUTINGA     ;  0  ;      0.88565863E+03 ;      0.15999990E+01 ;      0.85608978E+03 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 002 ; ITUTINGA     ;  1  ;      0.00000000E+00 ;      0.00000000E+00 ;      0.76499991E-02 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 002 ; ITUTINGA     ;  2  ;      0.00000000E+00 ;      0.00000000E+00 ;     -0.54500001E-05 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 002 ; ITUTINGA     ;  3  ;      0.00000000E+00 ;      0.00000000E+00 ;      0.26500000E-08 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 002 ; ITUTINGA     ;  4  ;      0.00000000E+00 ;      0.00000000E+00 ;     -0.45999999E-12 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 004 ; FUNIL-GRANDE ;  0  ;      0.80791309E+03 ;      0.37709991E+02 ;      0.76800000E+03 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 004 ; FUNIL-GRANDE ;  1  ;      0.00000000E+00 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 004 ; FUNIL-GRANDE ;  2  ;      0.00000000E+00 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 004 ; FUNIL-GRANDE ;  3  ;      0.00000000E+00 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 004 ; FUNIL-GRANDE ;  4  ;      0.00000000E+00 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 006 ; FURNAS       ;  0  ;      0.73524579E+03 ;      0.17882700E+06 ;      0.67163281E+03 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 006 ; FURNAS       ;  1  ;      0.34965801E-02 ;     -0.38527689E+03 ;      0.10173800E-02 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 006 ; FURNAS       ;  2  ;     -0.19743700E-06 ;      0.22135500E-01 ;     -0.17997191E-06 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 006 ; FURNAS       ;  3  ;      0.69170490E-11 ;      0.23279300E-03 ;      0.25132800E-10 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 006 ; FURNAS       ;  4  ;     -0.97736498E-16 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 007 ; M. DE MORAES ;  0  ;      0.64177490E+03 ;      0.66649600E+06 ;      0.61926593E+03 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 007 ; M. DE MORAES ;  1  ;      0.80881678E-02 ;     -0.29310000E+04 ;      0.17319800E-02 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 007 ; M. DE MORAES ;  2  ;     -0.36982399E-06 ;      0.42788501E+01 ;     -0.48919400E-07 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 007 ; M. DE MORAES ;  3  ;     -0.71105191E-10 ;     -0.20720400E-02 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 007 ; M. DE MORAES ;  4  ;      0.91237366E-14 ;      0.00000000E+00 ;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
    " 008 ; ESTREITO     ;  0  ;      0.10451660E+04 ;      0.46529999E+02 ;      0.55671777E+03 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;      0.00000000E+00 ;   0.00;\n",
]