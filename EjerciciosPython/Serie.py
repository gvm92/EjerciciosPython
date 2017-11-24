class Serie:
    def __init__(self, titulo, nTemporadas, entregado, genero, creador):
        self.titulo=titulo
        self.nTemporadas=nTemporadas
        self.entregado=entregado
        self.genero=genero
        self.creador=creador

    def getTitulo(self):
        return self.titulo

    def getNTemporadas(self):
        return self.nTemporadas

    def getGenero(self):
        return self.genero

    def getCreador(self):
        return self.creador

    def setTitulo(self, titulo):
        self.titulo=titulo

    def setNTemporadas(self, nTemporadas):
        self.nTemporadas=nTemporadas

    def setGenero(self, genero):
        self.genero=genero

    def setCreador(self, creador):
        self.creador=creador

    def entregar(self):
        self.entregado=True

class Videojuego:
    def __init__(self, titulo, horasEstimadas, entregado, genero, compania):
        self.titulo=titulo
        self.horasEstimadas=horasEstimadas
        self.entregado=entregado
        self.genero=genero
        self.compania=compania

    def getTitulo(self):
        return self.titulo

    def getHorasEstimadas(self):
        return self.horasEstimadas

    def getGenero(self):
        return self.genero

    def getCompania(self):
        return self.compania

    def setTitulo(self, titulo):
        self.titulo=titulo

    def setHorasEstimadas(self, horasEstimadas):
        self.horasEstimadas=horasEstimadas

    def setGenero(self, genero):
        self.genero=genero

    def setCompania(self, compania):
        self.compania=compania

    def entregar(self):
        self.entregado=True
