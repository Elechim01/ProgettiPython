
from pytube import YouTube


def AudioDownload(url, path):
    video = YouTube(url)
    audio = video.streams.filter(only_audio=True).first()
    try:
        audio.download(output_path=path)
        print(f"downlod completed\nfile saved in {path}")
    except Exception as errore:
        print("Errore nel download", errore)


if __name__ == '__main__':
    url = input("Inserisci l'url del video da scaricare\n")
    path = input("Inserisci il percorso della cartella dove salvare il file\n")
    AudioDownload(url=url, path=path)
