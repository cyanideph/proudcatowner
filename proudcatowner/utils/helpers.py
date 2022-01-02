
import json
from functools import reduce
from base64 import b64decode
from typing import Union
import requests
def generate_device_info() -> dict:
    return {
        "device_id": device.deviceGenerator(),
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/star2ltexx-user 7.1.; com.narvii.amino.master/3.4.33592)"
    }

def signature(data: Union[str, dict]) -> str:
    if isinstance(data, dict): data = json.dumps(data)
    return requests.get(f"http://forevercynical.com/generate/signature?data={str(data)}").json()['signature']

def decode_sid(sid: str) -> dict:
    return json.loads(b64decode(reduce(lambda a, e: a.replace(*e), ("-+", "_/"), sid + "=" * (-len(sid) % 4)).encode())[1:-20].decode())

def sid_to_uid(SID: str) -> str: return decode_sid(SID)["2"]

def sid_to_ip_address(SID: str) -> str: return decode_sid(SID)["4"]
