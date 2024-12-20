from pytube import YouTube

def baixar_audio(video_url, caminho_destino="./"):
    try:
        # Cria o objeto YouTube
        yt = YouTube(video_url)
        
        # Seleciona o stream de áudio com a maior taxa de bits
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Faz o download do áudio
        print(f"Baixando: {yt.title}")
        audio_stream.download(output_path=caminho_destino, filename=f"{yt.title}.mp4")
        print(f"Download concluído! Arquivo salvo em: {caminho_destino}{yt.title}.mp4")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# URL do vídeo do YouTube
url = input("Digite a URL do vídeo do YouTube: ")
caminho = input("Digite o caminho para salvar (pressione Enter para usar o padrão): ")
if not caminho:
    caminho = "./"

baixar_audio(url, caminho)
