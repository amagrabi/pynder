from enum import Enum

API_BASE = "https://api.gotinder.com"
CONTENT_BASE = "https://content.gotinder.com"

USER_AGENT = "Tinder/6.8.0 (iPhone; iOS 9.0.2; Scale/2.00)"

HEADERS = {
    "x-client-version":	"68023",
    "app-version": "1824",
    "Accept-Encoding": "gzip, deflate",
    "platform": "ios",
    "Accept-Language": "it;q=1, en-US;q=0.9",
    "Accept": "*/*",
    "Connection": "keep-alive",
    "os_version": "90000000002",
    "Content-type": "application/json; charset=utf-8"
}

GENDER_MAP = ("male", "female")

GENDER_MAP_REVERSE = {"male": 0, "female": 1}

UPDATABLE_FIELDS = [
    'gender', 'age_filter_min', 'age_filter_max',
    'distance_filter', 'bio', 'interested_in',
    'discoverable'
]

SIMPLE_FIELDS = {"name", "bio", "birth_date", "ping_time", "content_hash", "s_number"}

VALID_PHOTO_SIZES = {84, 172, 320, 640}


class ReportCause(Enum):
    Other = 0
    Spam = 1
    Inappropriate_Photos = 4
    Bad_Offline_Behavior = 5
    Inappropriate_Messages = 6
