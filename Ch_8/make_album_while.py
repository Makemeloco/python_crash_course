def make_album(artists_name, album_name, tracks=''):
    """Возвращает словарь с информацией о музыкальном альбоме."""
    person = {'artist': artists_name, 'album': album_name}
    if tracks:
        person['tracks'] = tracks
    return person

# Бесконечный цикл!
while True:
    print("\nPlease tell me about album:")
    print("(enter 'q' at any time to quit)")

    f_name = input("Artist name: ")
    if f_name == 'q':
        break

    l_name = input("Album name: ")
    if f_name == 'q':
        break

    formatted_name = make_album(f_name, l_name)
    print(formatted_name)
