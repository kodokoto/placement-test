import requests
import json

def main():
    URL = 'https://api.ampifymusic.com/packs'
    response: dict = requests.get(URL).json()
    parsed: dict = parseGenres(response)
    genres = list(parsed.keys())
    # for genre in genres: print(genre)
    # for pack in parsed['hip-hop']: print(json.dumps(pack, indent=4, sort_keys=True))
    print(parsed)

# parses response json and sorts by genres
def parseGenres(response: dict) -> dict:
    parsed = {}
    for pack in response['packs']:
        genres = pack.pop('genres', None)    # returns None if 'genres' key does not exist
        for genre in genres:
            if genre not in parsed:
                parsed[genre] = []
            parsed[genre].append(pack)
    return parsed


if __name__ == '__main__':
    main()
