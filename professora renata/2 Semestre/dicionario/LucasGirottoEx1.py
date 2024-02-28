def list_all_songs(playlist):
    print("Lista de todas as músicas:")
    for song in playlist:
        print(f"{song['title']} - {song['artist']}")

def list_songs_by_artist(playlist, artist):
    print(f"\nMúsicas do(a) cantor(a) {artist}:")
    for song in playlist:
        if song['artist'].lower() == artist.lower():
            print(f"{song['title']}")

def main():
    playlist = []

    # Leitura dos dados
    n = int(input("Quantidade de músicas: "))
    for _ in range(n):
        title = input("Digite o nome da música: ")
        artist = input("Digite o nome do cantor(a): ")
        playlist.append({'title': title, 'artist': artist})

    # Chamando as funções
    list_all_songs(playlist)

    artist_name = input("\nDigite o nome do cantor(a) para listar as músicas: ")
    list_songs_by_artist(playlist, artist_name)

if __name__ == "__main__":
    main()
