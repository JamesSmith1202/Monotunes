import requests, os, sqlite3, json, urllib2

if not os.path.isfile("creds.json"):
    print("Missing credentials file.")
    exit(1)

source = open("creds.json")
data = source.read()
data = json.loads(data)
api_base = "http://api.musixmatch.com/ws/1.1/{0}?{1}&apikey=" + data["musix_match"]["key"]#formatting strings for the command and parameters
data.close()

def get_song_id(track, artist):
    url = api_base.format("track.search", "q_track={0}&q_artist={1}&page_size=5&page=1&s_track_rating=desc".format(track.replace(" ", "%20"), artist.replace(" ", "%20")))
    u = urllib2.urlopen(url)
    msg = u.read()
    search_dict = json.loads(msg)
    if search_dict["message"]["body"]["track_list"] == []:
        return 0
    return search_dict["message"]["body"]["track_list"][0]["track"]["track_id"]

def get_lyrics(track_id):
    url = api_base.format("track.lyrics.get","track_id={}".format(track_id))
    u = urllib2.urlopen(url)
    msg = u.read()
    lyrics_dict = json.loads(msg)
    return lyrics_dict["message"]["body"]["lyrics"]["lyrics_body"]

def get_img(track_id):
    url = api_base.format("track.get","track_id={}".format(track_id))
    u = urllib2.urlopen(url)
    msg = u.read()
    track_dict = json.loads(msg)
    print track_dict
    return track_dict["message"]["body"]["track"]["album_coverart_500x500"]

def get_artistid(artist):
    url = api_base.format("artist.search","q_artist={}".format(artist))
    u = urllib2.urlopen(url)
    msg = u.read()
    search_dict = json.loads(msg)
    if search_dict["message"]["body"]["artist_list"] == []:
        return 0
    return search_dict["message"]["body"]["artist_list"][0]["artist"]["artist_id"]

def get_albums(artistid):
    url = api_base.format("artist.albums.get","artist_id={}".format(artistid))
    u = urllib2.urlopen(url)
    msg = u.read()
    search_dict = json.loads(msg)
    return search_dict["message"]["body"]["album_list"]

def get_album_tracks(albumid):
    url = api_base.format("albums.tracks.get","album_id={}".format(albumid))
    u = urllib2.urlopen(url)
    msg = u.read()
    search_dict = json.loads(msg)
    return search_dict["message"]["body"]["track_list"]

def get_top_songs():
    url = api_base.format("chart.tracks.get","page=1&page_size=10&country=us&f_has_lyrics=1")
    u = urllib2.urlopen(url)
    msg = u.read()
    search_dict = json.loads(msg)
    return search_dict["message"]["body"]["track_list"]

def get_wav(text, filename, voice = "en-US_AllisonVoice"):
  if not os.path.isfile("creds.json"):
    print("Missing credentials file.")
    exit(1)
  if not os.path.isfile(filename):
    apiurl = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
    headers = {"content-type": "application/json", "Accept": "audio/wav", "Content-Disposition": "attachment;filename=audio.wav"}
    dictionary = {"text": text, "voice": voice}
    source = open("creds.json")
    data = source.read()
    data = json.loads(data)
    user = data['text_to_speech']['username']
    pwd = data['text_to_speech']['password']
    try:
      r = requests.get(apiurl, auth=(user, pwd), stream=True, params=dictionary)
    except Exception as e:
      print e
      return False
    with open(filename, 'wb') as f:
      f.write(r.content)
  return True

if __name__ == "__main__":
  get_wav("Testing text to speech API", "../static/test.wav")
