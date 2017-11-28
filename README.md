# Monotunes
## Kevin Li, Adeebur Rahman, James Smith, Michael Cheng

### Overview:
Monotunes is a website which uses the Watson Text to Speech API and Musixmatch API. Our program is a lyrics library where you can search up a song by its name and artist or just search through an artist's albums to find a song. Once a song is selected, it brings you to a page displaying its lyrics and an audio file can be played through the page that reads you the lyrics. You may also have an account if you want to save your favorite songs somewhere.
 
### Instructions on Running Monotunes:

#### How to obtain source code
To get started, you first need to clone our repository.  
To clone with https:  
`$ git clone https://github.com/Kli16/Monotunes.git`  
To clone with ssh:  
`$ git clone git@github.com:Kli16/Monotunes.git`  

#### How to procure API Keys

First make a copy of 'sample_creds.json' called 'creds.json' in the monotunes directory.
```bash
$ cd Monotunes/monotunes
$ cp sample_creds.json creds.json
```
Then procure the API keys with the following instructions.

* ##### Watson Text to Speech

    1. Go to [Watson Text to Speech](https://www.ibm.com/watson/services/text-to-speech/).
    2. Click 'Get started free'.
    3. Fill out the form to create an account.
    4. Open the link in the email sent by The Bluemix Team to activate your account.
    5. Sign into your new account.
    6. You should now be at [https://console.bluemix.net/catalog/services/text-to-speech/](https://console.bluemix.net/catalog/services/text-to-speech/).
        If not, click on that link.
    7. Click 'Create'.
    8. Click on 'Service Credentials'.
    9. Click on 'New credential' and then 'Add' in the pop-up to create your credentials.
    10. Click 'View credentials' in the new credential that just appeared.
    11. Copy the username and password into the fields under 'text_to_speech' in 'creds.json'.

* ##### Musixmatch

    1. Go to [developer.musixmatch.com](https://developer.musixmatch.com/).
    2. Sign up for a developer account.
    3. Confirm your account through email and click 'Plans'.
    4. Click 'Get Started' under the 'Free' option.
    5. Fill out the required information to get your API key.
    6. The key should now be listed under 'Applications' within your account overview, accessible by clicking your username at the top right.
    7.  Copy the key into the 'musix_match' field in 'creds.json'

### Dependencies and how to install them
There are a couple of python module dependencies to run Monotunes:

* flask
* requests

We suggest using python virtual environment to install them.
```bash
$ virtualenv venv
$ . venv/bin/activate
$ pip install flask
$ pip install requests
```

### How to start the website

After installing the dependencies, run:

`$ python main.py`

Then, in a browser, go to the website at [http://localhost:5000/](http://localhost:5000/) to use the site.
