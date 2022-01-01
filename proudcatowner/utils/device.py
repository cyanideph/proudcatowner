import requests

def deviceGenerator():
    deviceId = requests.get("http://forevercynical.com/generate/deviceid").text
    return deviceId

def user_agent():
    user_agent = "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/star2ltexx-user 7.1.; com.narvii.amino.master/3.4.33592)"
    return user_agent