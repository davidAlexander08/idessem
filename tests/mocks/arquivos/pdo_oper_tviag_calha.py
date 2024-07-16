MockPdoOperTviagCalha = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  MODELO DESSEM     - VERSAO 20.3 - Junho  de 2024 (CPLEX)                          *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA ONS                                                                                                                                                   \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    " TE  PMO - SETEMBRO/22 - OUTUBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPE - Data do Caso: 03/09/2022                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "------------------------------------------------------------------\n",
    "Operacao dos volumes na calha do rio no fim do horizonte de estudo              \n",
    "------------------------------------------------------------------\n",
    "----------------------------------------------------------------------------------------------\n",
    "IPER:         Indice do periodo.                                                                                                                                                                        \n",
    "Dur:          Duracao                                                                                                                                                                                   \n",
    "USIHMON:      Numero de cadastro da usina hidreletrica de montante                                                                                                                                      \n",
    "NomeUsihMont: Nome da usina hidreletrica de montante                                                                                                                                                    \n",
    "TPELEMJUS:    Tipo de elemento de jusante                                                                                                                                                               \n",
    "              USIH: Usina hidreletrica                                                                                                                                                                  \n",
    "              SECR: Secao de Rio                                                                                                                                                                        \n",
    "NUMELEMJUS:   Numero do elemento de jusante                                                                                                                                                             \n",
    "NomeElemJus:  Nome do elemento de jusante                                                                                                                                                               \n",
    "TempViag:     Tempo de viagem da agua                                                                                                                                                                   \n",
    "TpTviag:      Tipo de modelagem para tempo de viagem                                                                                                                                                    \n",
    "              TRANSL: Translacao                                                                                                                                                                        \n",
    "              PROPAG: Curva de propagacao                                                                                                                                                               \n",
    "TacumFim:     Tempo que falta do inicio do periodo para o final do estudo.                                                                                                                              \n",
    "FatCalha:     Percentual do volume defluente no periodo que estara na calha do rio no final do                                                                                                          \n",
    "Vol.Calha:    Volume na calha do rio.                                                                                                                                                                   \n",
    "----------------------------------------------------------------------------------------------\n",
    "\n",
    "-----;-----;-------;--------------;---------;----------;--------------;--------;-------;--------;--------;----------;\n",
    "IPER ; Dur ;USIHMON; NomeUsihMont ;TPELEMJUS;NUMELEMJUS; NomeElemJus  ;TempViag;TpTviag;TacumFim;FatCalha;Vol.Calha ;\n",
    "  -  ; (h) ;   -   ;      -       ;    -    ;    -     ;      -       ;  (h)   ;   -   ;  (h)   ;        ;  (hm3)   ;\n",
    "-----;-----;-------;--------------;---------;----------;--------------;--------;-------;--------;--------;----------;\n",
    "   1 ;  0.5;  066  ; ITAIPU       ;  SECR   ;        1 ;          R11 ;   24.00;PROPAG ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  083  ; BAIXO IGUACU ;  SECR   ;        1 ;          R11 ;   15.00;PROPAG ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  002  ; ITUTINGA     ;  USIH   ;        4 ; FUNIL-GRANDE ;   12.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  004  ; FUNIL-GRANDE ;  USIH   ;        6 ; FURNAS       ;   23.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  006  ; FURNAS       ;  USIH   ;        7 ; M. DE MORAES ;    6.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  007  ; M. DE MORAES ;  USIH   ;        8 ; ESTREITO     ;    2.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  008  ; ESTREITO     ;  USIH   ;        9 ; JAGUARA      ;    2.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  009  ; JAGUARA      ;  USIH   ;       10 ; IGARAPAVA    ;    5.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  010  ; IGARAPAVA    ;  USIH   ;       11 ; VOLTA GRANDE ;    2.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  011  ; VOLTA GRANDE ;  USIH   ;       12 ; P. COLOMBIA  ;    6.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  012  ; P. COLOMBIA  ;  USIH   ;       17 ; MARIMBONDO   ;    6.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  014  ; CACONDE      ;  USIH   ;       15 ; E. DA CUNHA  ;   12.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  015  ; E. DA CUNHA  ;  USIH   ;       16 ; A.S.OLIVEIRA ;    3.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  016  ; A.S.OLIVEIRA ;  USIH   ;       17 ; MARIMBONDO   ;   72.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  017  ; MARIMBONDO   ;  USIH   ;       18 ; A. VERMELHA  ;    6.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  018  ; A. VERMELHA  ;  USIH   ;       34 ; I. SOLTEIRA  ;    6.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  020  ; BATALHA      ;  USIH   ;       21 ; SERRA FACAO  ;    8.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
    "   1 ;  0.5;  021  ; SERRA FACAO  ;  USIH   ;       24 ; EMBORCACAO   ;   11.00;TRANSL ;  168.0 ;   0.00 ;     0.0  ;\n",
]
