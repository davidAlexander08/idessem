MockPdoOperTerm = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  MODELO DESSEM     - VERSAO 19.3 - Janeiro de 2023 (CPLEX)                         *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA ONS                                                                                                                                                   \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    "  TE  PMO - AGOSTO/22 - SETEMBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPER- Data do Caso: 11/08/2022                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "----------------------------------------------\n",
    "Geracao e custos marginais por unidade termica                                  \n",
    "----------------------------------------------\n",
    "------------------------------------------------------\n",
    "IPER:      Indice do periodo.                                                                                                                                                                           \n",
    "USIT:      Numero de cadastro da usina termoeletrica                                                                                                                                                    \n",
    "UNIDT:     Numero de cadastro da unidade termoeletrica                                                                                                                                                  \n",
    "Nome Usit: Nome da usina termoeletrica                                                                                                                                                                  \n",
    "NomeSist:  Nome do subsistema                                                                                                                                                                           \n",
    "NumBarra:  Numero da barra da rede eletrica                                                                                                                                                             \n",
    "GTER:      Geracao Termoeletrica                                                                                                                                                                        \n",
    "ClinGter:  Custo linear de geracao da unidade termica                                                                                                                                                   \n",
    "CMO:       Custo marginal de operacao                                                                                                                                                                   \n",
    "CMB:       Custo marginal de operacao da barra                                                                                                                                                          \n",
    "------------------------------------------------------\n",
    "\n",
    "-----;-----;------;--------------;--------;--------;---------;---------;----------;------------;\n",
    "IPER ;USIT ;UNIDT ;  Nome Usit   ;NomeSist;NumBarra;  GTER   ;ClinGter ;   CMO    ;    CMB     ;\n",
    "  -  ;  -  ;  -   ;      -       ;   -    ;   -    ;  (MW)   ; ($/MWh) ; (R$/MWh) ;  (R$/MWh)  ;\n",
    "-----;-----;------;--------------;--------;--------;---------;---------;----------;------------;\n",
    "   1 ; 001 ; 001  ; ANGRA 1      ; SE     ;    10  ;   582.00;    31.17;    71.48 ;      71.48 ;\n",
    "   1 ; 108 ; 001  ; XAVANTES     ; SE     ;  2979  ;     0.00;  2637.13;    71.48 ;      71.48 ;\n",
    "   1 ; 108 ; 002  ; XAVANTES     ; SE     ;  2979  ;     0.00;  2637.13;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 001  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 002  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 003  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 004  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 005  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 006  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 007  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 008  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 009  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 010  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 011  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 012  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 013  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 014  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 110 ; 015  ; N.PIRATININ  ; SE     ;   404  ;     0.00;   654.42;    71.48 ;      71.48 ;\n",
    "   1 ; 012 ; 001  ; CUIABA G CC  ; SE     ;  4596  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 012 ; 002  ; CUIABA G CC  ; SE     ;  4596  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 012 ; 003  ; CUIABA G CC  ; SE     ;  4596  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 013 ; 001  ; ANGRA 2      ; SE     ;    11  ;  1350.00;    20.12;    71.48 ;      71.48 ;\n",
    "   1 ; 137 ; 001  ; GNA          ; SE     ;    53  ;     0.00;  1116.41;    71.48 ;      71.48 ;\n",
    "   1 ; 146 ; 001  ; STA VITORIA  ; SE     ;  7160  ;    14.00;   134.46;    71.48 ;      71.48 ;\n",
    "   1 ; 015 ; 001  ; LINHARES     ; SE     ;  9026  ;     0.00;   887.97;    71.48 ;      71.48 ;\n",
    "   1 ; 015 ; 002  ; LINHARES     ; SE     ;  9026  ;     0.00;   887.97;    71.48 ;      71.48 ;\n",
    "   1 ; 015 ; 003  ; LINHARES     ; SE     ;  9026  ;     0.00;   887.97;    71.48 ;      71.48 ;\n",
    "   1 ; 015 ; 004  ; LINHARES     ; SE     ;  9026  ;     0.00;   887.97;    71.48 ;      71.48 ;\n",
    "   1 ; 153 ; 001  ; DAIA         ; SE     ;  3004  ;     0.00;  1831.16;    71.48 ;      71.48 ;\n",
    "   1 ; 153 ; 002  ; DAIA         ; SE     ;  3004  ;     0.00;  1831.16;    71.48 ;      71.48 ;\n",
    "   1 ; 155 ; 001  ; GOIANIA II   ; SE     ;  3017  ;     0.00;  1931.55;    71.48 ;      71.48 ;\n",
    "   1 ; 155 ; 002  ; GOIANIA II   ; SE     ;  3017  ;     0.00;  1931.55;    71.48 ;      71.48 ;\n",
    "   1 ; 182 ; 001  ; PALMEIRAS GO ; SE     ;  3740  ;     0.00;  1495.97;    71.48 ;      71.48 ;\n",
    "   1 ; 182 ; 002  ; PALMEIRAS GO ; SE     ;  3740  ;     0.00;  1495.97;    71.48 ;      71.48 ;\n",
    "   1 ; 194 ; 001  ; T.NORTE 2    ; SE     ;  6913  ;     0.00;   910.86;    71.48 ;      71.48 ;\n",
    "   1 ; 194 ; 002  ; T.NORTE 2    ; SE     ;  6913  ;     0.00;   910.86;    71.48 ;      71.48 ;\n",
    "   1 ; 194 ; 003  ; T.NORTE 2    ; SE     ;  6912  ;     0.00;   910.86;    71.48 ;      71.48 ;\n",
    "   1 ; 194 ; 004  ; T.NORTE 2    ; SE     ;  6912  ;     0.00;   910.86;    71.48 ;      71.48 ;\n",
    "   1 ; 194 ; 005  ; T.NORTE 2    ; SE     ;  6912  ;     0.00;   910.86;    71.48 ;      71.48 ;\n",
    "   1 ; 194 ; 006  ; T.NORTE 2    ; SE     ;  6912  ;     0.00;   910.86;    71.48 ;      71.48 ;\n",
    "   1 ; 194 ; 007  ; T.NORTE 2    ; SE     ;  6912  ;     0.00;   910.86;    71.48 ;      71.48 ;\n",
    "   1 ; 211 ; 001  ; BAIXADA FLU  ; SE     ;  9627  ;     0.00;   560.62;    71.48 ;      71.48 ;\n",
    "   1 ; 211 ; 002  ; BAIXADA FLU  ; SE     ;  9627  ;     0.00;   560.62;    71.48 ;      71.48 ;\n",
    "   1 ; 211 ; 003  ; BAIXADA FLU  ; SE     ;  9627  ;     0.00;   560.62;    71.48 ;      71.48 ;\n",
    "   1 ; 229 ; 001  ; ONCA PINTADA ; SE     ;  7646  ;    30.00;   124.48;    71.48 ;      71.48 ;\n",
    "   1 ; 230 ; 001  ; PREDILECTA   ; SE     ;  2117  ;     0.00;   175.91;    71.48 ;      71.48 ;\n",
    "   1 ; 247 ; 001  ; LINHARES PCS ; SE     ;  9026  ;     8.70;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 247 ; 002  ; LINHARES PCS ; SE     ;  9026  ;     8.30;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 247 ; 003  ; LINHARES PCS ; SE     ;  9026  ;     9.00;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 247 ; 004  ; LINHARES PCS ; SE     ;  9026  ;     9.00;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 248 ; 001  ; PAULINIA     ; SE     ;  4137  ;    15.95;  3958.84;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 001  ; POVOACAO 1   ; SE     ; 45063  ;     8.48;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 002  ; POVOACAO 1   ; SE     ; 45063  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 003  ; POVOACAO 1   ; SE     ; 45063  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 004  ; POVOACAO 1   ; SE     ; 45063  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 005  ; POVOACAO 1   ; SE     ; 45063  ;     8.30;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 006  ; POVOACAO 1   ; SE     ; 45063  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 007  ; POVOACAO 1   ; SE     ; 45063  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 251 ; 008  ; POVOACAO 1   ; SE     ; 45063  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 253 ; 001  ; VIANA 1      ; SE     ;  8910  ;     8.30;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 253 ; 002  ; VIANA 1      ; SE     ;  8910  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 253 ; 003  ; VIANA 1      ; SE     ;  8910  ;     9.37;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 253 ; 004  ; VIANA 1      ; SE     ;  8910  ;     8.96;  4166.49;    71.48 ;      71.48 ;\n",
    "   1 ; 334 ; 001  ; W ARJONA     ; SE     ;  1890  ;     0.00;  2326.88;    71.48 ;      71.48 ;\n",
    "   1 ; 334 ; 002  ; W ARJONA     ; SE     ;  1890  ;     0.00;  2326.88;    71.48 ;      71.48 ;\n",
    "   1 ; 334 ; 003  ; W ARJONA     ; SE     ;  1890  ;     0.00;  2326.88;    71.48 ;      71.48 ;\n",
    "   1 ; 334 ; 004  ; W ARJONA     ; SE     ;  1890  ;     0.00;  2326.88;    71.48 ;      71.48 ;\n",
    "   1 ; 334 ; 005  ; W ARJONA     ; SE     ;  1890  ;     0.00;  2326.88;    71.48 ;      71.48 ;\n",
    "   1 ; 383 ; 001  ; ATLANTICO    ; SE     ;  9603  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 383 ; 002  ; ATLANTICO    ; SE     ;  9615  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 383 ; 003  ; ATLANTICO    ; SE     ;  9600  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 383 ; 004  ; ATLANTICO    ; SE     ;  9603  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 383 ; 005  ; ATLANTICO    ; SE     ;  9600  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 383 ; 006  ; ATLANTICO    ; SE     ;  9600  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 383 ; 007  ; ATLANTICO    ; SE     ;  9600  ;   420.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 004 ; 003  ; ST.CRUZ 34   ; SE     ;    30  ;     0.00;   310.41;    71.48 ;      71.48 ;\n",
    "   1 ; 004 ; 004  ; ST.CRUZ 34   ; SE     ;    30  ;     0.00;   310.41;    71.48 ;      71.48 ;\n",
    "   1 ; 434 ; 001  ; W ARJONA 2   ; SE     ;  1890  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 434 ; 002  ; W ARJONA 2   ; SE     ;  1890  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 434 ; 003  ; W ARJONA 2   ; SE     ;  1890  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 434 ; 004  ; W ARJONA 2   ; SE     ;  1890  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 434 ; 005  ; W ARJONA 2   ; SE     ;  1890  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 001  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 002  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 003  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 004  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 005  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 006  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 007  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 008  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 009  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 010  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 011  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 012  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 013  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 014  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 015  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 016  ; TERMORIO     ; SE     ;  4203  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 017  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 018  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 019  ; TERMORIO     ; SE     ;  4207  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 020  ; TERMORIO     ; SE     ;  4207  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 021  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 022  ; TERMORIO     ; SE     ;  4207  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 023  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 024  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 025  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 026  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 027  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 028  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 029  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 030  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 047 ; 031  ; TERMORIO     ; SE     ;  4205  ;     0.00;   380.20;    71.48 ;      71.48 ;\n",
    "   1 ; 049 ; 003  ; VIANA        ; SE     ;  8910  ;     0.00;  1397.63;    71.48 ;      71.48 ;\n",
    "   1 ; 049 ; 004  ; VIANA        ; SE     ;  8910  ;     0.00;  1397.63;    71.48 ;      71.48 ;\n",
    "   1 ; 049 ; 001  ; VIANA        ; SE     ;  8910  ;     0.00;  1397.63;    71.48 ;      71.48 ;\n",
    "   1 ; 049 ; 002  ; VIANA        ; SE     ;  8910  ;     0.00;  1397.63;    71.48 ;      71.48 ;\n",
    "   1 ; 050 ; 001  ; PIRAT.12 G   ; SE     ;   403  ;     0.00;   470.34;    71.48 ;      71.48 ;\n",
    "   1 ; 050 ; 002  ; PIRAT.12 G   ; SE     ;   404  ;     0.00;   470.34;    71.48 ;      71.48 ;\n",
    "   1 ; 054 ; 001  ; JUIZ DE FORA ; SE     ;  4100  ;     0.00;   522.96;    71.48 ;      71.48 ;\n",
    "   1 ; 054 ; 002  ; JUIZ DE FORA ; SE     ;  4180  ;     0.00;   522.96;    71.48 ;      71.48 ;\n",
    "   1 ; 060 ; 001  ; NORTEFLU     ; SE     ;  3962  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 060 ; 002  ; NORTEFLU     ; SE     ;  3962  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 060 ; 003  ; NORTEFLU     ; SE     ;  3962  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 060 ; 004  ; NORTEFLU     ; SE     ;  3962  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 060 ; 005  ; NORTEFLU     ; SE     ;  3962  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 060 ; 006  ; NORTEFLU     ; SE     ;  3962  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 060 ; 007  ; NORTEFLU     ; SE     ;  3962  ;     0.00;     0.00;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 001  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 002  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 003  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 004  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 005  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 006  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 007  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 062 ; 008  ; SEROPEDICA   ; SE     ;  3974  ;     0.00;   468.21;    71.48 ;      71.48 ;\n",
    "   1 ; 063 ; 001  ; IBIRITE      ; SE     ;  1585  ;     0.00;  2376.35;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 001  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 002  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 003  ; TRES LAGOAS  ; SE     ;  4301  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 004  ; TRES LAGOAS  ; SE     ;  4301  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 005  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 006  ; TRES LAGOAS  ; SE     ;  4301  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 007  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 008  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 009  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 010  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 011  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 012  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 013  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 014  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 068 ; 015  ; TRES LAGOAS  ; SE     ;  4300  ;     0.00;   318.54;    71.48 ;      71.48 ;\n",
    "   1 ; 086 ; 011  ; ST.CRUZ NOVA ; SE     ;    32  ;     0.00;   567.02;    71.48 ;      71.48 ;\n",
    "   1 ; 086 ; 021  ; ST.CRUZ NOVA ; SE     ;    32  ;     0.00;   567.02;    71.48 ;      71.48 ;\n",
    "   1 ; 009 ; 001  ; R.SILVEIRA   ; SE     ;   201  ;     0.00;   978.10;    71.48 ;      71.48 ;\n",
    "   1 ; 009 ; 002  ; R.SILVEIRA   ; SE     ;   203  ;     0.00;   978.10;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 001  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 002  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 003  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 004  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 005  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 006  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 007  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 008  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 009  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 010  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 011  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 012  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 013  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 014  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 015  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 016  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 017  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 018  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 019  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 090 ; 020  ; TERMOMACAE   ; SE     ;  3977  ;     0.00;   885.63;    71.48 ;      71.48 ;\n",
    "   1 ; 097 ; 001  ; CUBATAO      ; SE     ;  9100  ;     0.00;   392.78;    71.48 ;      71.48 ;\n",
    "   1 ; 097 ; 002  ; CUBATAO      ; SE     ;  9101  ;     0.00;   392.78;    71.48 ;      71.48 ;\n",
    "   1 ; 097 ; 003  ; CUBATAO      ; SE     ;  9100  ;     0.00;   392.78;    71.48 ;      71.48 ;\n",
    "   1 ; 107 ; 001  ; PAMPA SUL    ; S      ;   998  ;     0.00;    77.19;    71.44 ;      71.44 ;\n",
    "   1 ; 149 ; 001  ; SAO SEPE     ; S      ; 10170  ;     4.00;    97.11;    71.44 ;      71.44 ;\n",
    "   1 ; 156 ; 001  ; CANDIOTA 3   ; S      ;  1173  ;   240.00;   101.78;    71.44 ;      71.44 ;\n",
    "   1 ; 169 ; 001  ; CISFRAMA     ; S      ;  9839  ;     2.00;   360.51;    71.44 ;      71.44 ;\n",
    "   1 ; 024 ; 007  ; J.LACERDA C  ; S      ;   913  ;     0.00;   285.18;    71.44 ;      71.44 ;\n",
    "   1 ; 025 ; 005  ; J.LACERDA B  ; S      ;   911  ;     0.00;   331.67;    71.44 ;      71.44 ;\n",
    "   1 ; 025 ; 006  ; J.LACERDA B  ; S      ;   911  ;     0.00;   331.67;    71.44 ;      71.44 ;\n",
    "   1 ; 026 ; 001  ; J.LACERDA A1 ; S      ;   907  ;     0.00;   392.82;    71.44 ;      71.44 ;\n",
    "   1 ; 026 ; 002  ; J.LACERDA A1 ; S      ;   907  ;     0.00;   392.82;    71.44 ;      71.44 ;\n",
    "   1 ; 027 ; 003  ; J.LACERDA A2 ; S      ;   909  ;     0.00;   333.15;    71.44 ;      71.44 ;\n",
    "   1 ; 027 ; 004  ; J.LACERDA A2 ; S      ;   909  ;     0.00;   333.15;    71.44 ;      71.44 ;\n",
    "   1 ; 028 ; 001  ; FIGUEIRA     ; S      ;  2481  ;     0.00;   475.68;    71.44 ;      71.44 ;\n",
    "   1 ; 028 ; 003  ; FIGUEIRA     ; S      ;  2481  ;     0.00;   475.68;    71.44 ;      71.44 ;\n",
    "   1 ; 035 ; 001  ; URUGUAIANA   ; S      ;  1164  ;     0.00;     0.00;    71.44 ;      71.44 ;\n",
    "   1 ; 035 ; 002  ; URUGUAIANA   ; S      ;  1164  ;     0.00;     0.00;    71.44 ;      71.44 ;\n",
    "   1 ; 035 ; 003  ; URUGUAIANA   ; S      ;  1164  ;     0.00;     0.00;    71.44 ;      71.44 ;\n",
    "   1 ; 048 ; 001  ; ARAUCARIA    ; S      ;   802  ;     0.00;     0.00;    71.44 ;      71.44 ;\n",
    "   1 ; 048 ; 002  ; ARAUCARIA    ; S      ;   802  ;     0.00;     0.00;    71.44 ;      71.44 ;\n",
    "   1 ; 048 ; 003  ; ARAUCARIA    ; S      ;   802  ;     0.00;     0.00;    71.44 ;      71.44 ;\n",
    "   1 ; 064 ; 001  ; CANOAS       ; S      ;  1152  ;     0.00;   698.14;    71.44 ;      71.44 ;\n",
    "   1 ; 106 ; 001  ; ERB CANDEIAS ; NE     ;  6611  ;     4.00;    97.18;    71.46 ;      71.46 ;\n",
    "   1 ; 109 ; 001  ; ALTOS        ; NE     ;  5503  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 111 ; 001  ; ARACATI      ; NE     ;  5453  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 112 ; 001  ; CURUMIM      ; NE     ;  5802  ;     0.00;  1495.67;    71.46 ;      71.46 ;\n",
    "   1 ; 112 ; 002  ; CURUMIM      ; NE     ;  5802  ;     0.00;  1495.67;    71.46 ;      71.46 ;\n",
    "   1 ; 112 ; 003  ; CURUMIM      ; NE     ;  5802  ;     0.00;  1495.67;    71.46 ;      71.46 ;\n",
    "   1 ; 113 ; 001  ; BATURITE     ; NE     ;  5453  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 117 ; 001  ; CAMPO MAIOR  ; NE     ;  5503  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 119 ; 001  ; CAUCAIA      ; NE     ;  5453  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 121 ; 001  ; CRATO        ; NE     ;  5453  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 125 ; 001  ; ENGUIA PECEM ; NE     ;  5453  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 127 ; 001  ; IGUATU       ; NE     ;  5453  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 133 ; 001  ; JUAZEIRO N   ; NE     ;  5453  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 135 ; 001  ; MARAMBAIA    ; NE     ;  5503  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 138 ; 001  ; NAZARIA      ; NE     ;  5503  ;     0.00;     0.00;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 001  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 002  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 003  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 004  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 005  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 006  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 007  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 144 ; 008  ; PETROLINA    ; NE     ;  6314  ;     0.00;  2018.59;    71.46 ;      71.46 ;\n",
    "   1 ; 147 ; 001  ; PROSPERIDADE ; NE     ;  6104  ;     0.00;   183.28;    71.46 ;      71.46 ;\n",
    "   1 ; 147 ; 002  ; PROSPERIDADE ; NE     ;  6104  ;     0.00;   183.28;    71.46 ;      71.46 ;\n",
    "   1 ; 147 ; 003  ; PROSPERIDADE ; NE     ;  6104  ;     0.00;   183.28;    71.46 ;      71.46 ;\n",
    "   1 ; 151 ; 001  ; POTIGUAR     ; NE     ;  5240  ;     0.00;  2034.43;    71.46 ;      71.46 ;\n",
    "   1 ; 151 ; 002  ; POTIGUAR     ; NE     ;  5240  ;     0.00;  2034.43;    71.46 ;      71.46 ;\n",
    "   1 ; 151 ; 003  ; POTIGUAR     ; NE     ;  5240  ;     0.00;  2034.43;    71.46 ;      71.46 ;\n",
    "   1 ; 151 ; 004  ; POTIGUAR     ; NE     ;  5240  ;     0.00;  2034.43;    71.46 ;      71.46 ;\n",
    "   1 ; 152 ; 001  ; TERMOCABO    ; NE     ;  5134  ;     0.00;  1380.24;    71.46 ;      71.46 ;\n",
    "   1 ; 152 ; 002  ; TERMOCABO    ; NE     ;  5134  ;     0.00;  1380.24;    71.46 ;      71.46 ;\n",
    "   1 ; 152 ; 003  ; TERMOCABO    ; NE     ;  5134  ;     0.00;  1380.24;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 001  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 002  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 003  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 004  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 005  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 006  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 007  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 008  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 009  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 010  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 011  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 159 ; 012  ; TERMOMANAUS  ; NE     ;  5188  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 160 ; 001  ; PAU FERRO I  ; NE     ;  5187  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 160 ; 002  ; PAU FERRO I  ; NE     ;  5187  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 160 ; 003  ; PAU FERRO I  ; NE     ;  5187  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 160 ; 004  ; PAU FERRO I  ; NE     ;  5187  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 160 ; 005  ; PAU FERRO I  ; NE     ;  5187  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 160 ; 006  ; PAU FERRO I  ; NE     ;  5187  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 160 ; 007  ; PAU FERRO I  ; NE     ;  5187  ;     0.00;  2278.98;    71.46 ;      71.46 ;\n",
    "   1 ; 161 ; 001  ; POTIGUAR III ; NE     ;  5242  ;     0.00;  2034.41;    71.46 ;      71.46 ;\n",
    "   1 ; 161 ; 002  ; POTIGUAR III ; NE     ;  5242  ;     0.00;  2034.41;    71.46 ;      71.46 ;\n",
    "   1 ; 161 ; 003  ; POTIGUAR III ; NE     ;  5242  ;     0.00;  2034.41;    71.46 ;      71.46 ;\n",
    "   1 ; 161 ; 004  ; POTIGUAR III ; NE     ;  5242  ;     0.00;  2034.41;    71.46 ;      71.46 ;\n",
    "   1 ; 161 ; 005  ; POTIGUAR III ; NE     ;  5242  ;     0.00;  2034.41;    71.46 ;      71.46 ;\n",
    "   1 ; 161 ; 006  ; POTIGUAR III ; NE     ;  5242  ;     0.00;  2034.41;    71.46 ;      71.46 ;\n",
    "   1 ; 163 ; 001  ; P. PECEM II  ; NE     ;  5659  ;     0.00;  1148.05;    71.46 ;      71.46 ;\n",
    "   1 ; 164 ; 001  ; APOENA       ; NE     ;  5764  ;     0.00;  1839.87;    71.46 ;      71.46 ;\n",
    "   1 ; 164 ; 002  ; APOENA       ; NE     ;  5764  ;     0.00;  1839.87;    71.46 ;      71.46 ;\n",
    "   1 ; 164 ; 003  ; APOENA       ; NE     ;  5764  ;     0.00;  1839.87;    71.46 ;      71.46 ;\n",
    "   1 ; 164 ; 004  ; APOENA       ; NE     ;  5764  ;     0.00;  1839.87;    71.46 ;      71.46 ;\n",
    "   1 ; 164 ; 005  ; APOENA       ; NE     ;  5764  ;     0.00;  1839.87;    71.46 ;      71.46 ;\n",
    "   1 ; 164 ; 006  ; APOENA       ; NE     ;  5764  ;     0.00;  1839.87;    71.46 ;      71.46 ;\n",
]
