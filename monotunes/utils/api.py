import requests, os, sqlite3, json

def get_wav(text, filename, voice = "en-US_AllisonVoice"):
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
  get_wav("Testing text to speech API", "test.wav")
