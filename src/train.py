from util.song import Song

def read_input(filename):
    songs = list()

    input_file = file(filename)
    for line in input_file:
        songs.append(Song(line))

    return songs

def main():
    currentNN = NN("yeni",3,1)

    songs = read_input('beatles.txt')

    for song in songs:
        currentNN.addSong(song)
    currentNN.train()

    currentNN.saveNetworkToFile()

if __name__ == '__main__':
    main()
