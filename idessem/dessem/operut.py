from idessem.dessem.modelos.operut import (
    BlocoInitUT,
    BlocoOper,
    BlocoUctPar,
    BlocoUcTerm,
    BlocoPint,
    BlocoRegraNPTV,
)

from cfinterface.files.blockfile import BlockFile
from typing import Type, TypeVar, Optional, List
import pandas as pd  # type: ignore


class Operut(BlockFile):
    """
    Armazena os dados de entrada do DESSEM referentes às
    configurações da operação das usinas térmelétricas.

    """

    T = TypeVar("T")

    BLOCKS = [BlocoUctPar, BlocoUcTerm, BlocoPint, BlocoInitUT, BlocoOper]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="operut.dat") -> "Operut":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="operut.dat"):
        self.write(diretorio, nome_arquivo)

    def __bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.

        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        :return: O gerador de blocos, se houver
        :rtype: Optional[Generator[T], None, None]
        """
        try:
            return next(
                b
                for i, b in enumerate(self.data.of_type(bloco))
                if i == indice
            )
        except StopIteration:
            return None

    @property
    def condicoes_iniciais(self) -> Optional[pd.DataFrame]:
        """
        Tabela com as condições iniciais das UTEs.

        - indice_usina (`int`)
        - nome_usina (`str`)
        - indice_unidade_geradora (`int`)
        - estado (`int`)
        - geracao_inicial (`float`)
        - tempo_permanencia_estado (`int`)
        - meia_hora (`int`)
        - rampa_acionamento_desligamento (`int`)
        - titulacao_inicial (`int`)
        - inflexibilidade_titulacao (`float`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoInitUT, 0)
        if b is not None:
            return b.data[1]
        return None

    @condicoes_iniciais.setter
    def condicoes_iniciais(self, valor: pd.DataFrame):
        b = self.__bloco_por_tipo(BlocoInitUT, 0)
        if b is not None:
            b.data[1] = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def limites_e_condicoes_operativas(self) -> Optional[pd.DataFrame]:
        """
        Tabela com os limites e condições oeprativas das unidades.

        - indice_usina (`int`)
        - nome_usina (`str`)
        - indice_unidade_geradora (`int`)
        - dia_inicial (`int`)
        - hora_inicial (`int`)
        - meia_hora_inicial (`int`)
        - dia_final (`int`|`str`)
        - hora_final (`int`)
        - meia_hora_final (`int`)
        - geracao_minima (`float`)
        - geracao_maxima (`float`)
        - custo (`float`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoOper, 0)
        if b is not None:
            return b.data[1]
        return None

    @limites_e_condicoes_operativas.setter
    def limites_e_condicoes_operativas(self, valor: pd.DataFrame):
        b = self.__bloco_por_tipo(BlocoOper, 0)
        if b is not None:
            b.data[1] = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def uctpar(self) -> Optional[int]:
        """
        Número de threads utilizadas para o processamento paralelo.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.__bloco_por_tipo(BlocoUctPar, 0)
        if b is not None:
            return b.data
        return None

    @uctpar.setter
    def uctpar(self, valor: int):
        b = self.__bloco_por_tipo(BlocoUctPar, 0)
        if b is not None:
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def ucterm(self) -> Optional[int]:
        """
        Metodologia de solução para inclusão de rede e UCT.

        :return: O valor do flag
        :rtype: int | None
        """
        b = self.__bloco_por_tipo(BlocoUcTerm, 0)
        if b is not None:
            return b.data
        return None

    @ucterm.setter
    def ucterm(self, valor: int):
        b = self.__bloco_por_tipo(BlocoUcTerm, 0)
        if b is not None:
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def pint(self) -> Optional[str]:
        """
        Flag para ativar metodologia de pontos interiores.

        :return: O flag
        :rtype: str | None
        """
        b = self.__bloco_por_tipo(BlocoPint, 0)
        if b is not None:
            return "PINT"
        return None

    @property
    def regranptv(self) -> Optional[List[int]]:
        """
        Definição de valores default para a função de produção
        hidráulica.

        :return: Lista com os flag
        :rtype: list | None
        """
        b = self.__bloco_por_tipo(BlocoRegraNPTV, 0)
        if b is not None:
            return b.data
        return None

    @regranptv.setter
    def regranptv(self, valor: List[int]):
        b = self.__bloco_por_tipo(BlocoRegraNPTV, 0)
        if b is not None:
            b.data = valor
        else:
            raise ValueError("Campo não lido")
