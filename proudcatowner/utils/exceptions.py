class UnsupportedService(Exception):
    """
    - **API Code** : 100
    - **API Message** : Unsupported service. Your client may be out of date. Please update it to the latest version.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class FileTooLarge(Exception):
    """
    - **API Code** : 102
    - **API Message** : ``Unknown Message``
    - **API String** : API_STD_ERR_ENTITY_TOO_LARGE_RAW
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidRequest(Exception):
    """
    - **API Code** : 103, 104
    - **API Message** : Invalid Request. Please update to the latest version. If the problem continues, please contact us.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidSession(Exception):
    """
    - **API Code** : 105
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AccessDenied(Exception):
    """
    - **API Code** : 106
    - **API Message** : Access denied.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UnexistentData(Exception):
    """
    - **API Code** : 107
    - **API Message** : The requested data does not exist.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ActionNotAllowed(Exception):
    """
    - **API Code** : 110
    - **API Message** : Action not allowed.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ServiceUnderMaintenance(Exception):
    """
    - **API Code** : 111
    - **API Message** : Sorry, this service is under maintenance. Please check back later.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class MessageNeeded(Exception):
    """
    - **API Code** : 113
    - **API Message** : Be more specific, please.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidAccountOrPassword(Exception):
    """
    - **API Code** : 200
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AccountDisabled(Exception):
    """
    - **API Code** : 210
    - **API Message** : This account is disabled.
    - **API String** : AUTH_DISABLED_ACCOUNT
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidEmail(Exception):
    """
    - **API Code** : 213
    - **API Message** : Invalid email address.
    - **API String** : API_ERR_EMAIL
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidPassword(Exception):
    """
    - **API Code** : 214
    - **API Message** : Invalid password. Password must be 6 characters or more and contain no spaces.
    - **API String** : API_ERR_PASSWORD
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class EmailAlreadyTaken(Exception):
    """
    - **API Code** : 215
    - **API Message** : Hey this email ``X`` has been registered already. You can try to log in with the email or edit the email.
    - **API String** : API_ERR_EMAIL_TAKEN
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UnsupportedEmail(Exception):
    """
    - **API Code** : 215
    - **API Message** : This email address is not supported.
    - **API String** : API_ERR_EMAIL_TAKEN
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AccountDoesntExist(Exception):
    """
    - **API Code** : 216
    - **API Message** : ``Unknown Message``
    - **API String** : AUTH_ACCOUNT_NOT_EXISTS
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidDevice(Exception):
    """
    - **API Code** : 218
    - **API Message** : Error! Your device is currently not supported, or the app is out of date. Please update to the latest version.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AccountLimitReached(Exception):
    """
    - **API Code** : 219
    - **API Message** : A maximum of 3 accounts can be created from this device. If you forget your password, please reset it.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class TooManyRequests(Exception):
    """
    - **API Code** : 219
    - **API Message** : Too many requests. Try again later.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CantFollowYourself(Exception):
    """
    - **API Code** : 221
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UserUnavailable(Exception):
    """
    - **API Code** : 225
    - **API Message** : This user is unavailable.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class YouAreBanned(Exception):
    """
    - **API Code** : 229
    - **API Message** : You are banned.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UserNotMemberOfCommunity(Exception):
    """
    - **API Code** : 230
    - **API Message** : You have to join this Community first.
    - **API String** : API_ERR_USER_NOT_IN_COMMUNITY
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class RequestRejected(Exception):
    """
    - **API Code** : 235
    - **API Message** : Request rejected. You have been temporarily muted (read only mode) because you have received a strike. To learn more, please check the Help Center.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ActivateAccount(Exception):
    """
    - **API Code** : 238
    - **API Message** : Please activate your account first. Check your email, including your spam folder.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CantLeaveCommunity(Exception):
    """
    - **API Code** : 239
    - **API Message** : Sorry, you can not do this before transferring your Agent status to another member.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ReachedTitleLength(Exception):
    """
    - **API Code** : 240
    - **API Message** : Sorry, the max length of member's title is limited to 20.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AccountDeleted(Exception):
    """
    - **API Code** : 246
    - **API Message** : ``Unknown Message``
    - **API String** : AUTH_RECOVERABLE_DELETED_ACCOUNT
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_EMAIL_NO_PASSWORD(Exception):
    """
    - **API Code** : 251
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_EMAIL_NO_PASSWORD
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_COMMUNITY_USER_CREATED_COMMUNITIES_VERIFY(Exception):
    """
    - **API Code** : 257
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_COMMUNITY_USER_CREATED_COMMUNITIES_VERIFY
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ReachedMaxTitles(Exception):
    """
    - **API Code** : 262
    - **API Message** : You can only add up to 20 Titles. Please choose the most relevant ones.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class VerificationRequired(Exception):
    """
    - **API Code** : 270
    - **API Message** : Verification Required.
    - **API String** : API_ERR_NEED_TWO_FACTOR_AUTHENTICATION
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_INVALID_AUTH_NEW_DEVICE_LINK(Exception):
    """
    - **API Code** : 271
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_INVALID_AUTH_NEW_DEVICE_LINK
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommandCooldown(Exception):
    """
    - **API Code** : 291
    - **API Message** : Whoa there! You've done too much too quickly. Take a break and try again later.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UserBannedByTeamAmino(Exception):
    """
    - **API Code** : 293
    - **API Message** : Sorry, this user has been banned by Team Amino.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class BadImage(Exception):
    """
    - **API Code** : 300
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidThemepack(Exception):
    """
    - **API Code** : 313
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidVoiceNote(Exception):
    """
    - **API Code** : 314
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class RequestedNoLongerExists(Exception):
    """
    - **API Code** : 500, 700, 1600
    - **API Message** : Sorry, the requested data no longer exists. Try refreshing the view.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class PageRepostedTooRecently(Exception):
    """
    - **API Code** : 503
    - **API Message** : Sorry, you have reported this page too recently.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InsufficientLevel(Exception):
    """
    - **API Code** : 551
    - **API Message** : This post type is restricted to members with a level ``X`` ranking and above.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class WallCommentingDisabled(Exception):
    """
    - **API Code** : 702
    - **API Message** : This member has disabled commenting on their wall.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommunityNoLongerExists(Exception):
    """
    - **API Code** : 801
    - **API Message** : This Community no longer exists.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidCodeOrLink(Exception):
    """
    - **API Code** : 802
    - **API Message** : Sorry, this code or link is invalid.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommunityNameAlreadyTaken(Exception):
    """
    - **API Code** : 805
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommunityCreateLimitReached(Exception):
    """
    - **API Code** : 806
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_COMMUNITY_USER_CREATED_COMMUNITIES_EXCEED_QUOTA
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommunityDisabled(Exception):
    """
    - **API Code** : 814
    - **API Message** : This Community is disabled.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommunityDeleted(Exception):
    """
    - **API Code** : 833
    - **API Message** : This Community has been deleted.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class DuplicatePollOption(Exception):
    """
    - **API Code** : 1501
    - **API Message** : Sorry, you have duplicate poll options.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ReachedMaxPollOptions(Exception):
    """
    - **API Code** : 1507
    - **API Message** : Sorry, you can only join or add up to 5 of your items per poll.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class TooManyChats(Exception):
    """
    - **API Code** : 1602
    - **API Message** : Sorry, you can only have up to 1000 chat sessions.
    - **API String** : ``Unknown String``
    """

    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ChatFull(Exception):
    """
    - **API Code** : 1605
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class TooManyInviteUsers(Exception):
    """
    - **API Code** : 1606
    - **API Message** : Sorry, you can only invite up to 999 people.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ChatInvitesDisabled(Exception):
    """
    - **API Code** : 1611
    - **API Message** : This user has disabled chat invite requests.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class RemovedFromChat(Exception):
    """
    - **API Code** : 1612
    - **API Message** : You've been removed from this chatroom.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UserNotJoined(Exception):
    """
    - **API Code** : 1613
    - **API Message** : Sorry, this user has not joined.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_CHAT_VVCHAT_NO_MORE_REPUTATIONS(Exception):
    """
    - **API Code** : 1627
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_CHAT_VVCHAT_NO_MORE_REPUTATIONS
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class MemberKickedByOrganizer(Exception):
    """
    - **API Code** : 1637
    - **API Message** : This member was previously kicked by the organizer and cannot be reinvited.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class LevelFiveRequiredToEnableProps(Exception):
    """
    - **API Code** : 1661
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ChatViewOnly(Exception):
    """
    - **API Code** : 1663
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ChatMessageTooBig(Exception):
    """
    - **API Code** : 1664
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_CHAT_MESSAGE_CONTENT_TOO_LONG
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InviteCodeNotFound(Exception):
    """
    - **API Code** : 1900
    - **API Message** : Sorry, the requested data no longer exists. Try refreshing the view.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AlreadyRequestedJoinCommunity(Exception):
    """
    - **API Code** : 2001
    - **API Message** : Sorry, you have already submitted a membership request.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_PUSH_SERVER_LIMITATION_APART(Exception):
    """
    - **API Code** : 2501
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_PUSH_SERVER_LIMITATION_APART
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_PUSH_SERVER_LIMITATION_COUNT(Exception):
    """
    - **API Code** : 2502
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_PUSH_SERVER_LIMITATION_COUNT
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_PUSH_SERVER_LINK_NOT_IN_COMMUNITY(Exception):
    """
    - **API Code** : 2503
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_PUSH_SERVER_LINK_NOT_IN_COMMUNITY
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class API_ERR_PUSH_SERVER_LIMITATION_TIME(Exception):
    """
    - **API Code** : 2504
    - **API Message** : ``Unknown Message``
    - **API String** : API_ERR_PUSH_SERVER_LIMITATION_TIME
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AlreadyCheckedIn(Exception):
    """
    - **API Code** : 2601
    - **API Message** : Sorry, you can't check in any more.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AlreadyUsedMonthlyRepair(Exception):
    """
    - **API Code** : 2611
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AccountAlreadyRestored(Exception):
    """
    - **API Code** : 2800
    - **API Message** : Account already restored.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class IncorrectVerificationCode(Exception):
    """
    - **API Code** : 3102
    - **API Message** : Incorrect verification code.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NotOwnerOfChatBubble(Exception):
    """
    - **API Code** : 3905
    - **API Message** : You are not the owner of this chat bubble.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NotEnoughCoins(Exception):
    """
    - **API Code** : 4300
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AlreadyPlayedLottery(Exception):
    """
    - **API Code** : 4400
    - **API Message** : You have played the maximum number of lucky draws.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CannotSendCoins(Exception):
    """
    - **API Code** : 4500, 4501
    - **API Message** : ``Unknown Message``
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AminoIDAlreadyChanged(Exception):
    """
    - **API Code** : 6001
    - **API Message** : Amino ID cannot be changed after you set it.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidAminoID(Exception):
    """
    - **API Code** : 6002
    - **API Message** : Invalid Amino ID
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class InvalidName(Exception):
    """
    - **API Code** : 99001
    - **API Message** : Sorry, the name is invalid.
    - **API String** : ``Unknown String``
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class SpecifyType(Exception):
    """
    Raised when you need to specify the output of the command.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class WrongType(Exception):
    """
    Raised when you attribute the function the wrong type.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UnknownResponse(Exception):
    """
    Raised when an error occurs but the reason is unknown.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NotLoggedIn(Exception):
    """
    Raised when you try to make an action but you aren't logged in.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NoCommunity(Exception):
    """
    Raised when you try to make an action but no community was selected.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommunityNotFound(Exception):
    """
    Raised when you search for a community but nothing is found.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NoChatThread(Exception):
    """
    Raised when you try to make an action but no chat was selected.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ChatRequestsBlocked(Exception):
    """
    Raised when you try to make an action but the end user has chat requests blocked.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NoImageSource(Exception):
    """
    Raised when you try to make an action but no image source was selected.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CannotFetchImage(Exception):
    """
    Raised when an image cannot be fetched.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class FailedLogin(Exception):
    """
    Raised when you try to login but it fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AgeTooLow(Exception):
    """
    Raised when you try to configure an account but the age is too low. Minimum is 13.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UnsupportedLanguage(Exception):
    """
    Raised when you try to use a language that isn't supported or exists.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CommunityNeeded(Exception):
    """
    Raised when you try to execute an command but a Community needs to be specified.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class FlagTypeNeeded(Exception):
    """
    Raised when you try to flag a community, blog or user but a Flag Type needs to be specified.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ReasonNeeded(Exception):
    """
    Raised when you try to execute an command but a Reason needs to be specified.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


class TransferRequestNeeded(Exception):
    """
    Raised when you need to transfer host to complete the action.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class LibraryUpdateAvailable(Exception):
    """
    Raised when a new library update is available.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


def CheckException(data):
    api_code = data["api:statuscode"]
    from colored import attr, back, bg, fg, fore, style
    BP = fore.WHITE + back.RED_1 + style.BLINK
    reset = attr('reset')
    if api_code == 100: print (f'{BP}({data}){reset}')
    elif api_code == 102: print (f'{BP}({data}){reset}')
    elif api_code == 103 or api_code == 104: print (f'{BP}({data}){reset}')
    elif api_code == 105: print (f'{BP}({data}){reset}')
    elif api_code == 106: print (f'{BP}({data}){reset}')
    elif api_code == 107: print (f'{BP}({data}){reset}')
    elif api_code == 110: print (f'{BP}({data}){reset}')
    elif api_code == 111: print (f'{BP}({data}){reset}')
    elif api_code == 113: print (f'{BP}({data}){reset}')
    elif api_code == 200: print (f'{BP}({data}){reset}')
    elif api_code == 201: print (f'{BP}({data}){reset}')
    elif api_code == 213: print (f'{BP}({data}){reset}')
    elif api_code == 214: print (f'{BP}({data}){reset}')
    elif api_code == 215: print (f'{BP}({data}){reset}')
    elif api_code == 216: print (f'{BP}({data}){reset}')
    elif api_code == 218: print (f'{BP}({data}){reset}')
    elif api_code == 219: print (f'{BP}({data}){reset}')
    elif api_code == 221: print (f'{BP}({data}){reset}')
    elif api_code == 225: print (f'{BP}({data}){reset}')
    elif api_code == 229: print (f'{BP}({data}){reset}')
    elif api_code == 230: print (f'{BP}({data}){reset}')
    elif api_code == 235: print (f'{BP}({data}){reset}')
    elif api_code == 238: print (f'{BP}({data}){reset}')
    elif api_code == 239: print (f'{BP}({data}){reset}')
    elif api_code == 240: print (f'{BP}({data}){reset}')
    elif api_code == 246: print (f'{BP}({data}){reset}')
    elif api_code == 251: print (f'{BP}({data}){reset}')
    elif api_code == 257: print (f'{BP}({data}){reset}')
    elif api_code == 262: print (f'{BP}({data}){reset}')
    elif api_code == 270: print (f'{BP}({data}){reset}')
    elif api_code == 271: print (f'{BP}({data}){reset}')
    elif api_code == 291: print (f'{BP}({data}){reset}')
    elif api_code == 293: print (f'{BP}({data}){reset}')
    elif api_code == 300: print (f'{BP}({data}){reset}')
    elif api_code == 313: print (f'{BP}({data}){reset}')
    elif api_code == 314: print (f'{BP}({data}){reset}')
    elif api_code == 500 or api_code == 700 or api_code == 1600: print (f'{BP}({data}){reset}')
    elif api_code == 503: print (f'{BP}({data}){reset}')
    elif api_code == 551: print (f'{BP}({data}){reset}')
    elif api_code == 702: print (f'{BP}({data}){reset}')
    elif api_code == 801: print (f'{BP}({data}){reset}')
    elif api_code == 802: print (f'{BP}({data}){reset}')
    elif api_code == 805: print (f'{BP}({data}){reset}')
    elif api_code == 806: print (f'{BP}({data}){reset}')
    elif api_code == 814: print (f'{BP}({data}){reset}')
    elif api_code == 833: print (f'{BP}({data}){reset}')
    elif api_code == 1501: print (f'{BP}({data}){reset}')
    elif api_code == 1507: print (f'{BP}({data}){reset}')
    elif api_code == 1602: print (f'{BP}({data}){reset}')
    elif api_code == 1605: print (f'{BP}({data}){reset}')
    elif api_code == 1606: print (f'{BP}({data}){reset}')
    elif api_code == 1611: print (f'{BP}({data}){reset}')
    elif api_code == 1612: print (f'{BP}({data}){reset}')
    elif api_code == 1613: print (f'{BP}({data}){reset}')
    elif api_code == 1627: print (f'{BP}({data}){reset}')
    elif api_code == 1637: print (f'{BP}({data}){reset}')
    elif api_code == 1661: print (f'{BP}({data}){reset}')
    elif api_code == 1663: print (f'{BP}({data}){reset}')
    elif api_code == 1664: print (f'{BP}({data}){reset}')
    elif api_code == 1900: print (f'{BP}({data}){reset}')
    elif api_code == 2001: print (f'{BP}({data}){reset}')
    elif api_code == 2501: print (f'{BP}({data}){reset}')
    elif api_code == 2502: print (f'{BP}({data}){reset}')
    elif api_code == 2503: print (f'{BP}({data}){reset}')
    elif api_code == 2504: print (f'{BP}({data}){reset}')
    elif api_code == 2601: print (f'{BP}({data}){reset}')
    elif api_code == 2611: print (f'{BP}({data}){reset}')
    elif api_code == 2800: print (f'{BP}({data}){reset}')
    elif api_code == 3102: print (f'{BP}({data}){reset}')
    elif api_code == 3905: print (f'{BP}({data}){reset}')
    elif api_code == 4300: print (f'{BP}({data}){reset}')
    elif api_code == 4400: print (f'{BP}({data}){reset}')
    elif api_code == 4500 or api_code == 4501: print (f'{BP}({data}){reset}')
    elif api_code == 6001: print (f'{BP}({data}){reset}')
    elif api_code == 6002: print (f'{BP}({data}){reset}')
    elif api_code == 9901: print (f'{BP}({data}){reset}')
    else: raise Exception(data)