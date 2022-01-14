from pytube import Youtube

link = input("Link do vídeo: ")
path = input("Diretório para salvar: ")
yt = Youtube(link)

print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")
print("Avaliação do vídeo: ", yt.rating)

ys = yt.streams.get_highest_resolution()

print("Baixando...")
ys.download(path)
print("Download completo!")