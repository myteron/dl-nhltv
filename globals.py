# coding=utf-8
import cookielib
from datetime import datetime
import json
import os


#Settings
USERNAME = ""
PASSWORD = ""
QUALITY = "5000"
#QUALITY = "192" # Just for testing
DOWNLOAD_FOLDER = "$HOME/Desktop/NHL/" # $HOME works since we use mkdir not python for creation
RETRY_ERRORED_DOWNLOADS=False # usually works fine if you want it perfect set to True

TEAMID = "15" # see below for team ids to pick:
# 1 NJD New Jersey Devils
# 2 NYI New York Islanders
# 3 NYR New York Rangers
# 4 PHI Philadelphia Flyers
# 7 BUF Buffalo Sabres
# 10 TOR Toronto Maple Leafs
# 12 CAR Carolina Hurricanes
# 13 FLA Florida Panthers
# 15 WHS Washington Capitals
# 17 DET Detroit Red Wings
# 18 NSH Nashville Predators
# 19 STL St. Louis Blues
# 21 COL Colorado Avalanche
# 22 EDM Edmonton Oilers
# 23 VAN Vancouver Canucks
# 24 ANA Anaheim Ducks
# 29 CBJ Columbus Blue Jackets
# 30 MIN Minnesota Wild

MASTER_FILE_TYPE = 'master_tablet60.m3u8'
SETTINGS_FILE = 'settings.json'

#User Agents
UA_GCL = 'NHL1415/5.0925 CFNetwork/711.4.6 Darwin/14.0.0'
UA_IPHONE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 iphone nhl 5.0925'
UA_IPAD = 'Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 ipad nhl 5.0925'
UA_NHL = 'NHL/2542 CFNetwork/758.2.8 Darwin/15.0.0'
UA_PC = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
UA_PS4 = 'PS4Application libhttp/1.000 (PS4) libhttp/3.15 (PlayStation 4)'

def tprint(outString):
    outString = datetime.now().strftime('%m/%d/%y %H:%M:%S - ') + outString
    print(outString) 

def find(source,start_str,end_str):    
    start = source.find(start_str)
    end = source.find(end_str,start+len(start_str))

    if start != -1:        
        return source[start+len(start_str):end]
    return ''

def getSetting(key):
    """ Read from settings file """
    if os.path.isfile(SETTINGS_FILE) is False:
        # no settings file creating empty content
        j = "{u'session_key': u'000', u'media_auth': u'mediaAuth=000', u'lastGameID': 2015030166}"
       
    # Load the settings file
    with open(SETTINGS_FILE, "r") as settingsFile:
        j = json.load(settingsFile)

    return(j[key])

def setSetting(key, value):
    """ Write to settings file """

    if os.path.isfile(SETTINGS_FILE) is False:
        # no settings file creating empty content
        j = "{u'session_key': u'000', u'media_auth': u'mediaAuth=000', u'lastGameID': 2015030166}"
    else:    
        with open(SETTINGS_FILE, "r") as settingsFile:
            j = json.load(settingsFile)
    
    j[key] = value
    
    with open(SETTINGS_FILE, "w") as settingsFile:
        json.dump(j, settingsFile, indent=4)
    
def saveCookiesAsText():
    cjT = cookielib.MozillaCookieJar('cookies.txt')

    cj = cookielib.LWPCookieJar('cookies.lwp')
    cj.load('cookies.lwp',ignore_discard=False)
    for cookie in cj: 
        cjT.set_cookie(cookie)
    cjT.save(ignore_discard=False)
