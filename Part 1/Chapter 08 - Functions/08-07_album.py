def make_album(artist, title, q_songs=None):
    ''' Builds a dic. w/ info. about a music album. '''
    album = {'artist': artist, 'title': title, 'q_songs': q_songs}
    return album


afterglow = make_album('ed sheeran', 'afterglow')
print(afterglow)

_12_historias = make_album('tommy torres', '12 historias')
print(_12_historias)

la_la_land = make_album(
    'justin hurwitz, justin paul & benj pasek', 'la la land')
print(la_la_land)

clouds = make_album('zach sobiech', 'clouds', 1)
print(clouds)