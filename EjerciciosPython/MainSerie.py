import Serie

serie1 = Serie.Serie("Serie 1", 10, False, "Genero 1", "Creador 1")
serie2 = Serie.Serie("Serie 2", 2, False, "Genero 2", "Creador 2")
serie3 = Serie.Serie("Serie 3", 3, False, "Genero 3", "Creador 3")
serie4 = Serie.Serie("Serie 4", 5, False, "Genero 4", "Creador 4")
serie5 = Serie.Serie("Serie 5", 25, False, "Genero 5", "Creador 5")

juego1 = Serie.Videojuego("Juego 1", 1, False, "Genero 1", "Compañia 1")
juego2 = Serie.Videojuego("Juego 2", 600, False, "Genero 2", "Compañia 2")
juego3 = Serie.Videojuego("Juego 3", 2, False, "Genero 3", "Compañia 3")
juego4 = Serie.Videojuego("Juego 4", 250, False, "Genero 4", "Compañia 4")
juego5 = Serie.Videojuego("Juego 5", 300, False, "Genero 5", "Compañia 5")

juego1.entregar()
juego3.entregar()
juego5.entregar()

serie1.entregar()
serie3.entregar()
serie5.entregar()

listaSeries = [serie1, serie2, serie3, serie4, serie5]
listaJuegos = [juego1, juego2, juego3, juego4, juego5]

seriesEntregadas=0
juegosEntregados=0
nTemporadas=0
nHoras=0
serieConMasTemporadas=""
juegoConMasHoras=""

for e in listaSeries:
    if e.entregado is True:
        seriesEntregadas=seriesEntregadas+1
        print(e.getTitulo()+" entregada.")
    if e.getNTemporadas() > nTemporadas:
        nTemporadas=e.getNTemporadas()
        serieConMasTemporadas=e.getTitulo()


for e in listaJuegos:
    if e.entregado is True:
        juegosEntregadas=juegosEntregados+1
        print(e.getTitulo()+" entregado.")
    if e.getHorasEstimadas() > nHoras:
        nHoras=e.getHorasEstimadas()
        juegoConMasHoras=e.getTitulo()

print("El juego con mas horas es: "+juegoConMasHoras+" con "+str(nHoras)+" horas.")
print("La serie con mas temporadas es: "+serieConMasTemporadas+" con "+str(nTemporadas)+" temporadas.")