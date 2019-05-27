def make_album(artists_name, album_name, tracks=''):
    """Возвращает словарь с информацией о музыкальном альбоме."""
    person = {'artist': artists_name, 'album': album_name}
    if tracks:
        person['tracks'] = tracks
    return person

album_info = make_album('bjork', 'utopia', 10)
print(album_info)

album_info = make_album('jimi hendrix', 'woodstock')
print(album_info)

album_info = make_album('aurora', 'running with the wolves')
print(album_info)
