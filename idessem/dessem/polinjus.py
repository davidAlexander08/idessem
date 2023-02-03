from typing import Type, TypeVar, Optional, List, Union
from cfinterface.components.register import Register
from cfinterface.files.registerfile import RegisterFile
import pandas as pd  # type: ignore
from idessem.dessem.modelos.polinjus import (
    HidreletricaCurvaJusante,
    HidreletricaCurvaJusantePolinomioPorPartes,
)


class Polinjus(RegisterFile):
    """ """

    T = TypeVar("T")

    REGISTERS = [
        HidreletricaCurvaJusantePolinomioPorPartes,
        HidreletricaCurvaJusante,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="polinjus.csv"
    ) -> "Polinjus":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="polinjus.csv"):
        self.write(diretorio, nome_arquivo)

    def __registros_por_tipo(self, registro: Type[T]) -> List[T]:
        """
        Obtém os registro de um tipo, se houver algum no arquivo.

        :param registro: Um tipo de registro para ser lido
        :type registro: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int

        """
        return [b for b in self.data.of_type(registro)]

    def __obtem_registros(self, tipo: Type[T]) -> List[T]:
        return self.__registros_por_tipo(tipo)

    def __obtem_registros_com_filtros(
        self, tipo_registro: Type[T], **kwargs
    ) -> Optional[Union[T, List[T]]]:
        def __atende(r) -> bool:
            condicoes: List[bool] = []
            for k, v in kwargs.items():
                if v is not None:
                    condicoes.append(getattr(r, k) == v)
            return all(condicoes)

        regs_filtro = [
            r for r in self.__obtem_registros(tipo_registro) if __atende(r)
        ]
        if len(regs_filtro) == 0:
            return None
        elif len(regs_filtro) == 1:
            return regs_filtro[0]
        else:
            return regs_filtro

    def cria_registro(self, anterior: Register, registro: Register):
        """
        Adiciona um registro ao arquivo após um outro registro previamente
        existente.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.add_after(anterior, registro)

    def deleta_registro(self, registro: Register):
        """
        Remove um registro existente no arquivo.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.remove(registro)

    def append_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na última posição.
        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.append(registro)

    def preppend_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na primeira posição.
        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.preppend(registro)

    def hidreletrica_curvajusante(
        self,
        codigo_usina: Optional[int] = None,
        indice_familia: Optional[int] = None,
        nivel_montante_referencia: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaCurvaJusante,
            List[HidreletricaCurvaJusante],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que cadastram uma família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param nivel_montante_referencia: nível de montante de usina de
            jusante para cálculo da queda
        :type nivel_montante_referencia: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HidreletricaCurvaJusante` |
            list[:class:`HidreletricaCurvaJusante`] | None
        """
        if df:
            return self._as_df(HidreletricaCurvaJusante)
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaCurvaJusante,
                codigo_usina=codigo_usina,
                indice_familia=indice_familia,
                nivel_montante_referencia=nivel_montante_referencia,
            )

    def hidreletrica_curvajusante_polinomio(
        self,
        codigo_usina: Optional[int] = None,
        indice_familia: Optional[int] = None,
        numero_polinomios: Optional[float] = None,
        df: bool = False,
    ) -> Optional[
        Union[
            HidreletricaCurvaJusantePolinomioPorPartes,
            List[HidreletricaCurvaJusantePolinomioPorPartes],
            pd.DataFrame,
        ]
    ]:
        """
        Obtém registros que cadastram uma família de curvas
        de jusante para uma usina hidrelétrica. Opcionalmente,
        o retorno pode ser transformado em um `DataFrame`, apenas
        para leitura das informações.

        :param codigo_usina: código que especifica a usina
        :type codigo_usina: int | None
        :param indice_familia: índice da família de polinômios
        :type indice_familia: int | None
        :param numero_polinomios: número de polinômios da família
        :type numero_polinomios: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HidreletricaCurvaJusantePolinomioPorPartes` |
            list[:class:`HidreletricaCurvaJusantePolinomioPorPartes`] | None
        """
        if df:
            return self._as_df(HidreletricaCurvaJusantePolinomioPorPartes)
        else:
            return self.__obtem_registros_com_filtros(
                HidreletricaCurvaJusantePolinomioPorPartes,
                codigo_usina=codigo_usina,
                indice_familia=indice_familia,
                numero_polinomios=numero_polinomios,
            )