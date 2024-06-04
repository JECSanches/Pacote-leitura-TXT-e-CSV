class ArquivoCSV(object):

    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self._extrair_conteudo()
        self.colunas = self._extrair_nome_colunas()

    def _extrair_conteudo(self):
        conteudo = None
        with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
            conteudo = arquivo.readlines()
        return conteudo

    def _extrair_nome_colunas(self):
        return self.conteudo[0].strip().split(sep=',')

    def extrair_coluna(self, indice_coluna: str):
        coluna = []
        for elemento in self.conteudo:
            conteudo_elemento = elemento.strip().split(',')
            coluna.append(conteudo_elemento[indice_coluna])
        coluna.pop(0)
        return coluna
