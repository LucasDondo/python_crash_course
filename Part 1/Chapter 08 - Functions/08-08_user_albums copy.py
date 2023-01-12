def make_album(artist, title, songs=None):
    ''' Build a dic. w/ info. about a music album. '''
    album_dic = {'artist': artist, 'title': title, 'songs': songs}
    return album_dic


print('--- Welcome to the super-duper album logger! ---')
print('Insert "quit" at any time to stop the program.')
while True:
    print('\n-- Insert new album: --')

    artist = input('Artist: ')
    if artist == 'quit':
        break

    title = input('Title: ')
    if title == 'quit':
        break

    songs = input('Quantity of songs (optional): ')
    if songs == 'quit':
        break
    print(type(songs))

    album = make_album(artist, title)
    print(f"{album['artist']} made the album called {album['title']}.")

# if album['songs'] == 0:
#     print(f"{album['artist']} made the album called {album['title']}.")
# elif album['songs'] == 1:
#     print(f"{album['artist']} made the album called {album['title']} "
#           f"with {album['songs']} song.")
# elif album['songs'] >= 2:
#     print(f"{album['artist']} made the album called {album['title']} "
#           f"with {album['songs']} songs.")
