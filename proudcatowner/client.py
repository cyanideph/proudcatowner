# coding = utf-8
# credits to slimakoi for amino.py base
import base64, json, random, time, colorama, requests, secmail, threading
from .utils import entities, exceptions, headers, helpers, signature
from locale import getdefaultlocale as locale
from .websocket import Callbacks, SocketHandler
from colored import attr, back, fore, style
from torpy.http.requests import TorRequests
from .utils.device import user_agent, deviceGenerator
from time import time as timestamp
from typing import BinaryIO, Union
from time import timezone, sleep
from bs4 import BeautifulSoup
from binascii import hexlify
from os import urandom
from uuid import UUID
MB = fore.MAGENTA_3A + back.BLACK + style.BLINK
OB = fore.ORANGE_1 + back.BLACK + style.BLINK
BO = fore.BLACK + back.ORANGE_1 + style.BLINK
OM = fore.ORANGE_1 + back.MAGENTA_3A + style.BLINK
WB = fore.BLACK + back.WHITE + style.BLINK
xxx="┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄"
reset = attr('reset')
bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_charx = [random.choice(colors) + char for char in xxx]
rb = ''.join(colored_charx)
device = deviceGenerator()

class Client(Callbacks, SocketHandler):
    def __init__(self, deviceId: str = None, proxies: dict = None, certificatePath = None, socket_trace = False, socketDebugging = False):
        self.api = "https://service.narvii.com/api/v1"
        self.authenticated = False
        self.configured = False
        self.user_agent = user_agent
        if deviceId is not None: self.device_id = deviceId
        else: self.device_id = device

        SocketHandler.__init__(self, self, socket_trace=socket_trace, debug=socketDebugging)
        Callbacks.__init__(self, self)
        self.proxies = proxies
        self.certificatePath = certificatePath

        self.json = None
        self.sid = None
        self.userId = None
        self.account: entities.UserProfile = entities.UserProfile(None)
        self.profile: entities.UserProfile = entities.UserProfile(None)

    def parse_headers(self, data: str = None):
        if not data:
            return headers.ApisHeaders(deviceId=self.device_id).headers
        else:
            return headers.ApisHeaders(deviceId=self.device_id, data=data).headers
        
    def join_voice_chat(self, comId: str, chatId: str, joinType: int = 1):
        """
        Joins a Voice Chat

        **Parameters**
            - **comId** : ID of the Community
            - **chatId** : ID of the Chat
        """

        # Made by Light, Ley and Phoenix

        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = json.dumps(data)
        self.send(data)

    def join_video_chat(self, comId: str, chatId: str, joinType: int = 1):
        """
        Joins a Video Chat

        **Parameters**
            - **comId** : ID of the Community
            - **chatId** : ID of the Chat
        """

        # Made by Light, Ley and Phoenix

        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "joinRole": joinType,
                "channelType": 5,
                "id": "2154531"  # Need to change?
            },
            "t": 108
        }
        data = json.dumps(data)
        self.send(data)

    def join_video_chat_as_viewer(self, comId: str, chatId: str):
        data = {
            "o":
                {
                    "ndcId": int(comId),
                    "threadId": chatId,
                    "joinRole": 2,
                    "id": "72446"
                },
            "t": 112
        }
        data = json.dumps(data)
        self.send(data)

    def run_vid(self, comId: str, chatId: str):
        self.send(json.dumps({"o":{"ndcId":comId,"threadId":chatId,"joinRole":1,"id":"168112677"},"t":112}))
        self.send(json.dumps({"t":102,"o":{"threadId":chatId,"userList":[{"userProfile":{"isGuest":False,"uid":self.userId,"status":0,"icon":self.profile.icon,"reputation":self.profile.reputation,"role":0,"nickname":self.profile.nickname,"level":self.profile.level,"accountMembershipStatus":self.profile.accountMembershipStatus,"isNicknameVerified":False},"channelUid":22077774,"joinRole":1,"isHost":False,"hostStatus":0,"joinedTime":"2021-10-19T14:54:01Z"}],"ndcId":comId}}))
        self.send(json.dumps({"t":113,"o":{"id":"168112677","threadId":chatId,"ndcId":comId,"user":{"userProfile":{"isGuest":False,"uid":self.userId,"status":0,"icon":self.profile.icon,"reputation":self.profile.reputation,"role":0,"nickname":self.profile.nickname,"level":self.profile.level,"accountMembershipStatus":self.profile.accountMembershipStatus,"isNicknameVerified":False},"channelUid":22077774,"joinRole":1,"isHost":False,"hostStatus":0,"joinedTime":"2021-10-19T14:54:01Z"}}}))
        self.send(json.dumps({"o":{"ndcId":comId,"threadId":chatId,"channelType":5,"id":"168112999"},"t":108}))

    def run_vc(self, comId: str, chatId: str, joinType: str):
        while self.active:
            data = {
                "o": {
                    "ndcId": comId,
                    "threadId": chatId,
                    "joinRole": joinType,
                    "id": "2154531"  # Need to change?
                },
                "t": 112
            }
            data = json.dumps(data)
            self.send(data)
            sleep(1)

    def start_vc(self, comId: str, chatId: str, joinType: int = 1):
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = json.dumps(data)
        self.send(data)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "channelType": 1,
                "id": "2154531"  # Need to change?
            },
            "t": 108
        }
        data = json.dumps(data)
        self.send(data)
        self.active = True
        threading.Thread(target=self.run_vc, args=[comId, chatId, joinType])

    def end_vc(self, comId: str, chatId: str, joinType: int = 2):
        self.active = False
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = json.dumps(data)
        self.send(data)

    def login_sid(self, SID: str):
        """
        Login into an account with an SID

        **Parameters**
            - **SID** : SID of the account
        """
        uId = helpers.sid_to_uid(SID)
        self.authenticated = True
        self.sid = SID
        self.userId = uId
        self.account: entities.UserProfile = self.get_user_info(uId)
        self.profile: entities.UserProfile = self.get_user_info(uId)
        headers.sid = self.sid
        self.start()
        self.run_socket()

    def login(self, email: str, password: str):
        """
        Login into an account.

        **Parameters**
            - **email** : Email of the account.
            - **password** : Password of the account.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = json.dumps({
            "email": email,
            "v": 2,
            "secret": f"0 {password}",
            "deviceID": self.device_id,
            "clientType": 100,
            "action": "normal",
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/auth/login", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        self.run_socket()
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))

        else:
            self.authenticated = True
            self.json = json.loads(response.text)
            self.sid = self.json["sid"]
            self.userId = self.json["account"]["uid"]
            self.account: entities.UserProfile = entities.UserProfile(self.json["account"]).UserProfile
            self.profile: entities.UserProfile = entities.UserProfile(self.json["userProfile"]).UserProfile
            headers.sid = self.sid
            self.start()
            return response.status_code
    def generate_nickname(self):
        import names
        from fancy_text import fancy
        xx = [fancy.light, fancy.bold, fancy.box]
        xy = random.choice(xx)
        nm=''
        for i in names.get_first_name():
            nm=nm+i
            x = (f'{nm}⁷⁷⁷⁷')
        nickname = (xy(x))
        return nickname

    def logout(self):
        """
        Logout from an account.

        **Parameters**
            - No parameters required.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = json.dumps({
            "deviceID": self.device_id,
            "clientType": 100,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/auth/logout", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else:
            self.authenticated = False
            self.json = None
            self.sid = None
            self.userId = None
            self.account: None
            self.profile: None
            headers.sid = None
            self.close()
            return response.status_code

    def check_device(self, deviceId: str):
        """
        Check if the Device ID is valid.

        **Parameters**
            - **deviceId** : ID of the Device.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = json.dumps({
            "deviceID": deviceId,
            "bundleID": "com.narvii.amino.master",
            "clientType": 100,
            "timezone": -timezone // 1000,
            "systemPushEnabled": True,
            "locale": locale()[0],
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/device", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: self.configured = True; return response.status_code

    def get_account_info(self):
        response = requests.get(f"{self.api}/g/s/account", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.UserProfile(json.loads(response.text)["account"]).UserProfile

    def upload_media(self, file: BinaryIO, fileType: str):
        """
        Upload file to the amino servers.

        **Parameters**
            - **file** : File to be uploaded.

        **Returns**
            - **Success** : Url of the file uploaded to the server.

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        if fileType == "audio":
            t = "audio/aac"
        elif fileType == "image":
            t = "image/jpg"
        else: raise exceptions.SpecifyType(fileType)

        data = file.read()

        response = requests.post(f"{self.api}/g/s/media/upload", data=data, headers=headers.Headers(type=t, data=data, deviceId=self.device_id, sig=sig).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return json.loads(response.text)["mediaValue"]

    def handle_socket_message(self, data):
        return self.resolve(data)

    def get_eventlog(self):
        response = requests.get(f"{self.api}/g/s/eventlog/profile?language=en", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return json.loads(response.text)

    def get_communities(self, start: int = 0, size: int = 25):
        """
        List of Communities the account is in.

        **Parameters**
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Community List <amino.lib.util.entities.CommunityList>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        if not self.authenticated: raise exceptions.NotLoggedIn()
        response = requests.get(f"{self.api}/g/s/community/joined?v=1&start={start}&size={size}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.CommunityList(json.loads(response.text)["communityList"]).CommunityList

    def sub_clients_profile(self, start: int = 0, size: int = 25):
        if not self.authenticated: raise exceptions.NotLoggedIn()
        response = requests.get(f"{self.api}/g/s/community/joined?v=1&start={start}&size={size}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return json.loads(response.text)["userInfoInCommunities"]

    def get_user_info(self, userId: str):
        """
        Information of an User.

        **Parameters**
            - **userId** : ID of the User.

        **Returns**
            - **Success** : :meth:`User Object <amino.lib.util.entities.UserProfile>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.UserProfile(json.loads(response.text)["userProfile"]).UserProfile

    def watch_ad(self, userId: str = None):
        data = json.dumps(headers.Tapjoy(userId if userId else self.userId).data) 
        response = requests.post("https://ads.tapdaq.com/v4/analytics/reward", data=data, headers=headers.Tapjoy().headers)
        if response.status_code != 204: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def get_chat_threads(self, start: int = 0, size: int = 25):
        """
        List of Chats the account is in.

        **Parameters**
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Chat List <amino.lib.util.entities.ThreadList>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/chat/thread?type=joined-me&start={start}&size={size}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.ThreadList(json.loads(response.text)["threadList"]).ThreadList

    def get_chat_thread(self, chatId: str):
        """
        Get the Chat Object from an Chat ID.

        **Parameters**
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : :meth:`Chat Object <amino.lib.util.entities.Thread>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.Thread(json.loads(response.text)["thread"]).Thread

    def get_chat_users(self, chatId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}/member?start={start}&size={size}&type=default&cv=1.2", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.UserProfileList(json.loads(response.text)["memberList"]).UserProfileList

    def join_chat(self, chatId: str):
        """
        Join an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.userId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def leave_chat(self, chatId: str):
        """
        Leave an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.delete(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.userId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def start_chat(self, userId: Union[str, list], message: str, title: str = None, content: str = None, isGlobal: bool = False, publishToGlobal: bool = False):
        """
        Start an Chat with an User or List of Users.

        **Parameters**
            - **userId** : ID of the User or List of User IDs.
            - **message** : Starting Message.
            - **title** : Title of Group Chat.
            - **content** : Content of Group Chat.
            - **isGlobal** : If Group Chat is Global.
            - **publishToGlobal** : If Group Chat should show in Global.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        if isinstance(userId, str): userIds = [userId]
        elif isinstance(userId, list): userIds = userId
        else: raise exceptions.WrongType()

        data = {
            "title": title,
            "inviteeUids": userIds,
            "initialMessageContent": message,
            "content": content,
            "timestamp": int(timestamp() * 1000)
        }

        if isGlobal is True: data["type"] = 2; data["eventSource"] = "GlobalComposeMenu"
        else: data["type"] = 0

        if publishToGlobal is True: data["publishToGlobal"] = 1
        else: data["publishToGlobal"] = 0

        data = json.dumps(data)


        response = requests.post(f"{self.api}/g/s/chat/thread", data=data, headers=self.parse_headers(data=data), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def invite_to_chat(self, userId: Union[str, list], chatId: str):
        """
        Invite a User or List of Users to a Chat.

        **Parameters**
            - **userId** : ID of the User or List of User IDs.
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        if isinstance(userId, str): userIds = [userId]
        elif isinstance(userId, list): userIds = userId
        else: raise exceptions.WrongType

        data = json.dumps({
            "uids": userIds,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/invite", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def kick(self, userId: str, chatId: str, allowRejoin: bool = True):
        if allowRejoin: allowRejoin = 1
        if not allowRejoin: allowRejoin = 0
        response = requests.delete(f"{self.api}/g/s/chat/thread/{chatId}/member/{userId}?allowRejoin={allowRejoin}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def get_chat_messages(self, chatId: str, size: int = 25, pageToken: str = None):
        """
        List of Messages from an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.
            - *size* : Size of the list.
            - *size* : Size of the list.
            - *pageToken* : Next Page Token.

        **Returns**
            - **Success** : :meth:`Message List <amino.lib.util.entities.MessageList>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        if pageToken is not None: url = f"{self.api}/g/s/chat/thread/{chatId}/message?v=2&pagingType=t&pageToken={pageToken}&size={size}"
        else: url = f"{self.api}/g/s/chat/thread/{chatId}/message?v=2&pagingType=t&size={size}"

        response = requests.get(url, headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.GetMessages(json.loads(response.text)).GetMessages

    def get_message_info(self, chatId: str, messageId: str):
        """
        Information of an Message from an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.
            - **messageId** : ID of the Message.

        **Returns**
            - **Success** : :meth:`Message Object <amino.lib.util.entities.Message>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.Message(json.loads(response.text)["message"]).Message

    def get_community_info(self, comId: str):
        """
        Information of an Community.

        **Parameters**
            - **comId** : ID of the Community.

        **Returns**
            - **Success** : :meth:`Community Object <amino.lib.util.entities.Community>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s-x{comId}/community/info?withInfluencerList=1&withTopicList=true&influencerListOrderStrategy=fansCount", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.Community(json.loads(response.text)["community"]).Community

    def search_community(self, aminoId: str):
        """
        Search a Community byt its Amino ID.

        **Parameters**
            - **aminoId** : Amino ID of the Community.

        **Returns**
            - **Success** : :meth:`Community List <amino.lib.util.entities.CommunityList>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/search/amino-id-and-link?q={aminoId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else:
            response = json.loads(response.text)["resultList"]
            if len(response) == 0: raise exceptions.CommunityNotFound(aminoId)
            else: return entities.CommunityList([com["refObject"] for com in response]).CommunityList
    def request_verify_code(self, email: str):
        deviceId = deviceGenerator()
        data = {
        "identity": email,
        "type": 1,
        "deviceID": deviceId
        }
        data = json.dumps(data)
        request = requests.post(f"{self.api}/g/s/auth/request-security-validation", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        return request.json()

    def request_generate_code(self, nickname: str, email: str, password: str):
        try:
            deviceId = deviceGenerator()
            data = {
            "identity": email,
            "type": 1,
            "deviceID": deviceId
            }
            data = json.dumps(data)
            with TorRequests() as client:
                with client.get_session() as session:
                    session.post(f"{self.api}/g/s/auth/request-security-validation", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
            print(f"Generating account with {email}..")
            self.check_mail_00(nickname, email = email, deviceId = deviceId, password = password)
        except Exception as e:
            print(e)
        
    def generate_device(self):
        device = requests.get("http://forevercynical.com/generate/deviceid").text
        return (OB + device + reset)

    def update_password(self, email: str, new_password: str, deviceId: str, code: str):
        data = json.dumps({
            "updateSecret": f"0 {new_password}",
            "emailValidationContext": {
                "data": {
                    "code": code
                },
                "type": 1,
                "identity": email,
                "level": 2,
                "deviceID": deviceId
            },
            "phoneNumberValidationContext": None,
            "deviceID": deviceId
        })
        request = requests.post(f"{self.api}/g/s/auth/reset-password", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        print(f"""\nSuccessfully changed password for {email}
        & Written to updatedpass.json""")
        with open('updatedpass.json', 'a') as x:
            passw = f'\n{{\n"email": "{email}",\n"password":"{new_password}",\n"device": "{deviceId}"\n}},'
            x.write(passw)
        return request.json()

    def check_mail(self, email: str, new_password: str, deviceId: str):
        try:
            time.sleep(10)
            mail = secmail.SecMail()
            mails = mail.get_messages(email = email).id
            print(f"\nChecking inbox: {email}")
            themail1 = mails[0]
            inbox = mail.read_message(email, themail1).htmlBody
            self.solve_captcha(email, new_password = new_password, deviceId = deviceId, inbox = inbox)
        except IndexError:
            self.check_mail(email, new_password = new_password, deviceId = deviceId, inbox = inbox)

    def check_mail_00(self, nickname: str, email: str, password: str, deviceId: str):
        try:
            time.sleep(10)
            mail = secmail.SecMail()
            mails = mail.get_messages(email = email).id
            print(f"\nChecking inbox: {email}")
            themail1 = mails[0]
            inbox = mail.read_message(email, themail1).htmlBody
            self.solve_captcha_00(nickname, email = email, password = password, deviceId = deviceId, inbox = inbox)
        except IndexError or inbox:
            self.check_mail_00(nickname, email = email, password = password, deviceId = deviceId, inbox = inbox)

    def solve_captcha_00(self, nickname, email: str, password: str, deviceId: str, inbox):
        soup = BeautifulSoup(inbox, "lxml")
        url = soup.find_all("a")
        url = url[0].get("href")
        print(f'\n{url}')
        code = input("\nEnter code here >> ")
        self.register(nickname, email = email, password = password, deviceId = deviceId, code = code)

    def solve_captcha(self, email: str, new_password: str, deviceId: str, inbox):
        soup = BeautifulSoup(inbox, "lxml")
        url = soup.find_all("a")
        url = url[0].get("href")
        print(f'\n{url}')
        code = input("\nEnter code here >> ")
        self.update_password(email = email, new_password = new_password, deviceId = deviceId, code = code)

    def request_pass_code(self, email: str, new_password: str):
        try:
            deviceId = deviceGenerator()
            print(deviceId)
            data = {
            "identity": email,
            "type": 1,
            "deviceID": deviceId,
            "level": 2,
            "purpose":  "reset-password"
            }
            data = json.dumps(data)
            requests.post(f"{self.api}/g/s/auth/request-security-validation", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
            print('\nPassword Request Sent..')
            self.check_mail(email = email, deviceId = deviceId, new_password = new_password)
        except Exception as e:
            print (e) 

    def get_user_following(self, userId: str, start: int = 0, size: int = 25):
        """
        List of Users that the User is Following.

        **Parameters**
            - **userId** : ID of the User.
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`User List <amino.lib.util.entities.UserProfileList>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/joined?start={start}&size={size}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.UserProfileList(json.loads(response.text)["userProfileList"]).UserProfileList

    def get_user_followers(self, userId: str, start: int = 0, size: int = 25):
        """
        List of Users that are Following the User.

        **Parameters**
            - **userId** : ID of the User.
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`User List <amino.lib.util.entities.UserProfileList>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/member?start={start}&size={size}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.UserProfileList(json.loads(response.text)["userProfileList"]).UserProfileList


    def send_message(self, chatId: str, message: str = None, messageType: int = 0, file: BinaryIO = None, fileType: str = None, replyTo: str = None, mentionUserIds: list = None, stickerId: str = None, embedId: str = None, embedType: int = None, embedLink: str = None, embedTitle: str = None, embedContent: str = None, embedImage: BinaryIO = None):
        """
        Send a Message to a Chat.

        **Parameters**
            - **message** : Message to be sent
            - **chatId** : ID of the Chat.
            - **file** : File to be sent.
            - **fileType** : Type of the file.
                - ``audio``, ``image``, ``gif``
            - **messageType** : Type of the Message.
            - **mentionUserIds** : List of User IDS to mention. '@' needed in the Message.
            - **replyTo** : Message ID to reply to.
            - **stickerId** : Sticker ID to be sent.
            - **embedTitle** : Title of the Embed.
            - **embedContent** : Content of the Embed.
            - **embedLink** : Link of the Embed.
            - **embedImage** : Image of the Embed.
            - **embedId** : ID of the Embed.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """

        if message is not None and file is None:
            message = message.replace("<$", "‎‏").replace("$>", "‬‭")

        mentions = []
        if mentionUserIds:
            for mention_uid in mentionUserIds:
                mentions.append({"uid": mention_uid})

        if embedImage:
            embedImage = [[100, self.upload_media(embedImage, "image"), None]]

        data = {
            "type": messageType,
            "content": message,
            "clientRefId": int(timestamp() / 10 % 1000000000),
            "attachedObject": {
                "objectId": embedId,
                "objectType": embedType,
                "link": embedLink,
                "title": embedTitle,
                "content": embedContent,
                "mediaList": embedImage
            },
            "extensions": {"mentionedArray": mentions},
            "timestamp": int(timestamp() * 1000)
        }

        if replyTo: data["replyMessageId"] = replyTo

        if stickerId:
            data["content"] = None
            data["stickerId"] = stickerId
            data["type"] = 3

        if file:
            data["content"] = None
            if fileType == "audio":
                data["type"] = 2
                data["mediaType"] = 110

            elif fileType == "image":
                data["mediaType"] = 100
                data["mediaUploadValueContentType"] = "image/jpg"
                data["mediaUhqEnabled"] = True

            elif fileType == "gif":
                data["mediaType"] = 100
                data["mediaUploadValueContentType"] = "image/gif"
                data["mediaUhqEnabled"] = True

            else: raise exceptions.SpecifyType

            data["mediaUploadValue"] = base64.b64encode(file.read()).decode()

        data = json.dumps(data)

        

        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/message", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code


    def register(self, nickname: str, email: str, password: str, deviceId: str, code: str):
        try:
            data = json.dumps({
            "secret": f"0 {password}",
            "deviceID": deviceId,
            "email": email,
            "clientType": 100,
            "nickname": nickname,
            "latitude": 0,
            "longitude": 0,
            "address": None,
            "clientCallbackURL": "narviiapp://relogin",
            "validationContext": {
                "data": {
                    "code": code
                },
                "type": 1,
                "identity": email
            },
            "type": 1,
            "identity": email,
            "timestamp": int(time.time() * 1000)
            })  
            requests.post(f"{self.api}/g/s/auth/register", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
            short_device = f"{deviceId[:5]}...{deviceId[-5:]}"
            print(f"""{rb}
        {OB}Successfully Generated Account! 
        Username: {nickname}
        Email: {email}
        Password: {password}
        Device: {short_device}{reset}!
{rb}{reset}""")
            with open('accounts.json', 'a') as x:
                acc = f'\n{{\n"email": "{email}",\n"password":"{password}",\n"device": "{deviceId}"\n}},'
                x.write(acc)
        except Exception as e:
            print(e)
    def change_password(self, email: str = None, new_password: str = None):
        """
        Change password to your account.

        **Parameters**
            - **Email** : Email of the account.
            - **New password** : New password for the account.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        self.request_pass_code(email, new_password)

    def generate_account(self, password: str = None):
        """
        Generate Accounts.

        **Parameters**
            - **password** : input password for the accounts.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        mail = secmail.SecMail()
        email = mail.generate_email()
        nickname = self.generate_nickname()
        self.request_generate_code(nickname, email, password)

        
    def delete_message(self, chatId: str, messageId: str, asStaff: bool = False, reason: str = None):
        """
        Delete a Message from a Chat.

        **Parameters**
            - **messageId** : ID of the Message.
            - **chatId** : ID of the Chat.
            - **asStaff** : If execute as a Staff member (Leader or Curator).
            - **reason** : Reason of the action to show on the Moderation History.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = {
            "adminOpName": 102,
            "adminOpNote": {"content": reason},
            "timestamp": int(timestamp() * 1000)
        }

        data = json.dumps(data)
        
        if not asStaff: response = requests.delete(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        else: response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}/admin", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def send_coins(self, coins: int, blogId: str = None, chatId: str = None, objectId: str = None, transactionId: str = None):
        url = None
        if transactionId is None: transactionId = str(UUID(hexlify(urandom(16)).decode('ascii')))

        data = {
            "coins": coins,
            "tippingContext": {"transactionId": transactionId},
            "timestamp": int(timestamp() * 1000)
        }

        if blogId is not None: url = f"{self.api}/g/s/blog/{blogId}/tipping"
        if chatId is not None: url = f"{self.api}/g/s/chat/thread/{chatId}/tipping"
        if objectId is not None:
            data["objectId"] = objectId
            data["objectType"] = 2
            url = f"{self.api}/g/s/tipping"

        if url is None: raise exceptions.SpecifyType()

        data = json.dumps(data)
        
        response = requests.post(url, headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def follow(self, userId: Union[str, list]):
        """
        Follow an User or Multiple Users.

        **Parameters**
            - **userId** : ID of the User or List of IDs of the Users.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        if isinstance(userId, str):
            response = requests.post(f"{self.api}/g/s/user-profile/{userId}/member", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)

        elif isinstance(userId, list):
            data = json.dumps({"targetUidList": userId, "timestamp": int(timestamp() * 1000)})
            
            response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}/joined", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)

        else: raise exceptions.WrongType

        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def unfollow(self, userId: str):
        """
        Unfollow an User.

        **Parameters**
            - **userId** : ID of the User.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.delete(f"{self.api}/g/s/user-profile/{userId}/member/{self.userId}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def join_community(self, comId: str, invitationId: str = None):
        """
        Join a Community.

        **Parameters**
            - **comId** : ID of the Community.
            - **invitationId** : ID of the Invitation Code.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = {"timestamp": int(timestamp() * 1000)}
        if invitationId: data["invitationId"] = invitationId

        data = json.dumps(data)
        
        response = requests.post(f"{self.api}/x{comId}/s/community/join", data=data, headers=self.parse_headers(data=data), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code


    def edit_profile(self, nickname: str = None, content: str = None, icon: BinaryIO = None, backgroundColor: str = None, backgroundImage: str = None, defaultBubbleId: str = None):
        """
        Edit account's Profile.

        **Parameters**
            - **nickname** : Nickname of the Profile.
            - **content** : Biography of the Profile.
            - **icon** : Icon of the Profile.
            - **backgroundImage** : Url of the Background Picture of the Profile.
            - **backgroundColor** : Hexadecimal Background Color of the Profile.
            - **defaultBubbleId** : Chat bubble ID.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = {
            "address": None,
            "latitude": 0,
            "longitude": 0,
            "mediaList": None,
            "eventSource": "UserProfileView",
            "timestamp": int(timestamp() * 1000)
        }

        if nickname: data["nickname"] = nickname
        if icon: data["icon"] = self.upload_media(icon, "image")
        if content: data["content"] = content
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        if backgroundImage: data["extensions"] = {"style": {"backgroundMediaList": [[100, backgroundImage, None, None, None]]}}
        if defaultBubbleId: data["extensions"] = {"defaultBubbleId": defaultBubbleId}

        data = json.dumps(data)
        
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def like_blog(self, blogId: Union[str, list] = None, wikiId: str = None):
        """
        Like a Blog, Multiple Blogs or a Wiki.

        **Parameters**
            - **blogId** : ID of the Blog or List of IDs of the Blogs. (for Blogs)
            - **wikiId** : ID of the Wiki. (for Wikis)

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = {
            "value": 4,
            "timestamp": int(timestamp() * 1000)
        }

        if blogId:
            if isinstance(blogId, str):
                data["eventSource"] = "UserProfileView"
                data = json.dumps(data)
                
                response = requests.post(f"{self.api}/g/s/blog/{blogId}/g-vote?cv=1.2", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)

            elif isinstance(blogId, list):
                data["targetIdList"] = blogId
                data = json.dumps(data)
                
                response = requests.post(f"{self.api}/g/s/feed/g-vote", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)

            else: raise exceptions.WrongType(type(blogId))

        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            
            response = requests.post(f"{self.api}/g/s/item/{wikiId}/g-vote?cv=1.2", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)

        else: raise exceptions.SpecifyType()

        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return response.status_code

    def get_wallet_info(self):
        """
        Get Information about the account's Wallet.

        **Parameters**
            - No parameters required.

        **Returns**
            - **Success** : :meth:`Wallet Object <amino.lib.util.entities.WalletInfo>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/wallet", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.WalletInfo(json.loads(response.text)["wallet"]).WalletInfo

    def get_wallet_history(self, start: int = 0, size: int = 25):
        """
        Get the Wallet's History Information.

        **Parameters**
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Wallet Object <amino.lib.util.entities.WalletInfo>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/wallet/coin/history?start={start}&size={size}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.WalletHistory(json.loads(response.text)["coinHistoryList"]).WalletHistory

    def get_from_deviceid(self, deviceId: str):
        """
        Get the User ID from an Device ID.

        **Parameters**
            - **deviceID** : ID of the Device.

        **Returns**
            - **Success** : :meth:`User ID <amino.lib.util.entities.UserProfile.userId>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/auid?deviceId={deviceId}")
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return json.loads(response.text)["auid"]

    def get_from_link(self, code: str):
        """
        Get the Object Information from the Amino URL Code.

        **Parameters**
            - **code** : Code from the Amino URL.
                - ``http://aminoapps.com/p/EXAMPLE``, the ``code`` is 'EXAMPLE'.

        **Returns**
            - **Success** : :meth:`From Code Object <amino.lib.util.entities.FromLink>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        response = requests.get(f"{self.api}/g/s/link-resolution?q={code}", headers=self.parse_headers(), proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.FromLink(json.loads(response.text)["linkInfoV2"]).FromLink

    def get_from_id(self, objectId: str, objectType: int, comId: str = None):
        """
        Get the Object Information from the Object ID and Type.

        **Parameters**
            - **objectID** : ID of the Object. User ID, Blog ID, etc.
            - **objectType** : Type of the Object.
            - *comId* : ID of the Community. Use if the Object is in a Community.

        **Returns**
            - **Success** : :meth:`From Code Object <amino.lib.util.entities.FromLink>`

            - **Fail** : :meth:`Exceptions <proudcatowner.lib.util.exceptions>`
        """
        data = json.dumps({
            "objectId": objectId,
            "targetCode": 1,
            "objectType": objectType,
            "timestamp": int(timestamp() * 1000)
        })
        
        if comId: response = requests.post(f"{self.api}/g/s-x{comId}/link-resolution", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        else: response = requests.post(f"{self.api}/g/s/link-resolution", headers=self.parse_headers(data=data), data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
        else: return entities.FromLink(json.loads(response.text)["linkInfoV2"]).FromLink

