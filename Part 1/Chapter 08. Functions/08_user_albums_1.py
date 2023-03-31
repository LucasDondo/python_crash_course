def make_album(artist, title, q_songs=None):
    ''' Builds a dic. w/ info. about a music album. '''
    album = {'artist': artist.title(),
             'title': title.title(),
             'q_songs': q_songs, }
    return album


print('--- This is the super-duper album tracker program! ---'
      '\nWhenever you want to exit, enter \x1B[3m"quit"\x1B[0m.')

while True:
    print('\n-- New album --')
    artist = input('Artist: ')
    if artist == 'quit':
        break

    title = input('Title: ')
    if title == 'quit':
        break

    q_songs = input('Quantity of songs: ')
    if q_songs == 'quit':
        break

    album = make_album(artist, title, q_songs)
    print(
        f"\n\t{album['artist']} made the album called "
        f"{album['title']}. It has {album['q_songs']} songs.")

print('\nThank you for using the program!')
