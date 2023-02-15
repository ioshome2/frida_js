"""
uuid  ->  base64
"""
import ctypes
import json

from loguru import logger

# uuid   aid  openudid    1f9eedbeeb19fdfg    CWY5ZWVuYwVvYtO5ZwHwZm==
uuid = [49, 102, 57, 101, 101, 100, 98, 101, 101, 98, 49, 57, 102, 55, 102, 101]

# area   1_72_2799_0   CV83Cv8yDzu5XzK=
area = [49, 95, 55, 50, 95, 50, 55, 57, 57, 95, 48]

# d_model   M2010J19SC   JJSmCJLACJvJGm==
d_model = [77, 50, 48, 49, 48, 74, 49, 57, 83, 67]

# wifiBssid  unknown  dW5hbw93bq==
wifiBssid = [117, 110, 107, 110, 111, 119, 110]

# osVersion     11   CJO=
osVersion = [49, 49]

# d_brand    Xiaomi     WQvrb21f
d_brand = [88, 105, 97, 111, 109, 105]

# screen    2218*1080      CtSnEMenCNqm
screen = [50, 50, 49, 56, 42, 49, 48, 56, 48]
base = ""

# 请求参数
"""
{
    "abTest800": true,
    "acceptPrivacy": true,
    "avoidLive": false,
    "brand": "Redmi",
    "cityCode": 72,
    "cityId": 0,
    "cpsNoTuan": null,
    "darkModelEnum": 3,
    "debug": "",
    "districtId": 0,
    "eventId": "Startup_OpenAppParam_Status",
    "fromType": 0,
    "isDesCbc": true,
    "latitude": "0.0",
    "lego": true,
    "longitude": "0.0",
    "model": "M2010J19SC",
    "ocrFlag": false,
    "oneboxChannel": false,
    "oneboxKeyword": "",
    "oneboxSource": "",
    "overseas": 0,
    "personas": null,
    "pluginVersion": 101050,
    "plusClickCount": 0,
    "plusLandedFatigue": 0,
    "productJdv": "0|appmarket|t_2018512525_appmarket|tuiguang|42111_0_xiaomi001_0_0|1666678967000|1667798922",
    "provinceId": "0",
    "prstate": "0",
    "searchWareflag": "",
    "selfDelivery": "0",
    "skuId": "10058104029613",
    "source_type": "m_destination_page",
    "source_value": "",
    "townId": 0,
    "uAddrId": "0",
    "utmMedium": null,
    "wareInnerSource": "extra.inner.source.init"
}
"""
dd = 123,34,97,98,84,101,115,116,56,48,48,34,58,116,114,117,101,44,34,97,99,99,101,112,116,80,114,105,118,97,99,121,34,58,116,114,117,101,44,34,97,118,111,105,100,76,105,118,101,34,58,102,97,108,115,101,44,34,98,114,97,110,100,34,58,34,82,101,100,109,105,34,44,34,99,105,116,121,67,111,100,101,34,58,55,50,44,34,99,105,116,121,73,100,34,58,48,44,34,99,112,115,78,111,84,117,97,110,34,58,110,117,108,108,44,34,100,97,114,107,77,111,100,101,108,69,110,117,109,34,58,51,44,34,100,105,115,116,114,105,99,116,73,100,34,58,48,44,34,101,118,101,110,116,73,100,34,58,34,83,116,97,114,116,117,112,95,79,112,101,110,65,112,112,80,97,114,97,109,95,83,116,97,116,117,115,34,44,34,102,114,111,109,84,121,112,101,34,58,48,44,34,105,115,68,101,115,67,98,99,34,58,116,114,117,101,44,34,108,97,116,105,116,117,100,101,34,58,34,48,46,48,34,44,34,108,101,103,111,34,58,116,114,117,101,44,34,108,111,110,103,105,116,117,100,101,34,58,34,48,46,48,34,44,34,109,111,100,101,108,34,58,34,77,50,48,49,48,74,49,57,83,67,34,44,34,111,99,114,70,108,97,103,34,58,102,97,108,115,101,44,34,111,110,101,98,111,120,67,104,97,110,110,101,108,34,58,102,97,108,115,101,44,34,111,110,101,98,111,120,75,101,121,119,111,114,100,34,58,34,34,44,34,111,110,101,98,111,120,83,111,117,114,99,101,34,58,34,34,44,34,111,118,101,114,115,101,97,115,34,58,48,44,34,112,100,86,101,114,115,105,111,110,34,58,34,49,34,44,34,112,101,114,115,111,110,97,115,34,58,110,117,108,108,44,34,112,108,117,103,105,110,86,101,114,115,105,111,110,34,58,49,48,49,48,53,48,44,34,112,108,117,115,67,108,105,99,107,67,111,117,110,116,34,58,48,44,34,112,108,117,115,76,97,110,100,101,100,70,97,116,105,103,117,101,34,58,48,44,34,112,114,111,100,117,99,116,74,100,118,34,58,34,48,124,97,112,112,109,97,114,107,101,116,124,116,95,50,48,49,56,53,49,50,53,50,53,95,97,112,112,109,97,114,107,101,116,124,116,117,105,103,117,97,110,103,124,53,48,57,54,54,95,48,95,116,101,110,99,101,110,116,95,48,95,48,124,49,54,55,54,50,55,55,49,57,50,34,44,34,112,114,111,118,105,110,99,101,73,100,34,58,34,48,34,44,34,112,114,115,116,97,116,101,34,58,34,48,34,44,34,115,101,97,114,99,104,87,97,114,101,102,108,97,103,34,58,34,34,44,34,115,101,108,102,68,101,108,105,118,101,114,121,34,58,34,48,34,44,34,115,107,117,73,100,34,58,34,49,48,48,53,52,55,54,56,49,50,55,54,53,51,34,44,34,115,111,117,114,99,101,95,116,121,112,101,34,58,34,109,105,110,105,95,119,97,114,101,34,44,34,115,111,117,114,99,101,95,118,97,108,117,101,34,58,34,34,44,34,116,111,119,110,73,100,34,58,48,44,34,117,65,100,100,114,73,100,34,58,34,48,34,44,34,117,116,109,77,101,100,105,117,109,34,58,110,117,108,108,44,34,119,97,114,101,73,110,110,101,114,83,111,117,114,99,101,34,58,34,101,120,116,114,97,46,105,110,110,101,114,46,115,111,117,114,99,101,46,105,110,105,116,34,44,34,121,114,113,78,101,119,34,58,34,49,34,125
for one in dd:
    base += chr(one)
print(base)


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


#  该方法后面为负数时  不对  不推荐
def unsigned_right_shift(n, i):
    # 如果js右移为0, 且数字小于0
    if i == 0 and n < 0:
        return n + 2 ** 32
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)


# 推荐使用这个
def unsinged_right_shift(x, y):
    x, y = ctypes.c_uint32(x).value, y % 32
    return ctypes.c_uint32(x >> y).value


def get_cipher_uuid(uuid: str):
    end_str = ""
    base_byte = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9', '+', '/']
    b_arr = [ord(i) for i in uuid]
    logger.info(f"dd:{b_arr}")
    i2 = 0
    while i2 <= len(b_arr)-1:
        b_arr2 = [0, 0, 0, 0]
        b2 = 0

        i3 = 0
        while i3 <= 2:
            i4 = i2 + i3
            if i4 <= len(b_arr) - 1:
                b_arr2[i3] = int_overflow(b2 | unsinged_right_shift(int_overflow(b_arr[i4] & 255), (i3 * 2) + 2))
                b2 = unsinged_right_shift(int_overflow(int_overflow((b_arr[i4] & 255) << (((2-i3) * 2) + 2)) & 255), 2)
            else:
                b_arr2[i3] = b2
                b2 = 64
            i3 += 1
        b_arr2[3] = b2

        i5 = 0
        while i5 <= 3:
            if b_arr2[i5] <= 63:
                end_str += base_byte[b_arr2[i5]]
            else:
                end_str += "="
            i5 += 1

        i2 += 3
    logger.info(f"最终结果为:{end_str}")


if __name__ == '__main__':
    """
    oyTrYvHvc3G4CNKsExHydWUiSwPtY2VmdPLyaXZrY3usExHydWUiSwP2b2vuJQv2ZIS6ZwPic2UiSwTyYW5uStesUwVubWusBMTtaXH5G29uZIS6DzSiSwDfdRvTZMS6CMmsY3LzJw9UdWPkStfkdWniBMTuYXThJW9uZWnPbxVjStezBMTuaXD0cwvtdOvuStemBMTvdwVkd
OvuStesU3HrcxH1cP9FcQVkGXLmUQPyYW1pU3HrdRVzSsmsZxTlbVH5cQUsEtKiSwvzHQVzG2TtStf0cxVvBMTiYXHfdRVuZIS6StKkCMSiSwnvZ28sExHydWUiSwnlbwdfdRVuZIS6StKkCMSiSw1lZQViStesJJSmCJLACJvJGySiSw9tcuZiYWcsEwZrbRDvBMTlbwVsb3
rNaQPkbwViStfwYWnzZImsb25vYw94I2V5d29yZMS6SsSiSw9kZWTloPDldXTtZIS6SsSiSw92ZXTzZWPzStemBMTmZPZvcxDfb24sEsSnSsmscQVyc29kYXCsEw51bQmiSxLidWdfbvZvcxDfb24sEtOmCJK1CMmscQn1c0DiaWDhG291bxGsEtKiSxLidXDCYW5uZWHQYXH
fZ3VvStemBMTmcw9udWD0IwH2StesCRnrcRLjYXThZXH8dP8yCNO4DJOyDJS1X2PmcQ1rcwjvdRn0dWvxdWPkZ3m1CNu2Dv8mX3HvbwDvbxHpCP8mpNO2DzYyDzcnEJSsBMTmcw92aW5tZUvuStesCMSiSxLyc3HrdQUsEsSmSsmsc2VrcwDeV2PyZWZiYWcsEsSsBMTzZWnw
HQViaXZvcxusEsSmSsmsc2j1IWGsEsSnCNK1DNc2ENOyDzY1CySiSxDldXTtZV90oXLvStesbWvkaV93YXTvSsmsc291cwDvX3ZrbRVvStesSsmsdQ93buvuStemBMT1GWHucuvuStesCMSiSxV0bU1vZQv1bIS6bxVibMmsd2PyZUvkbwVyU291cwDvStesZXr0cwOkaW5kZ
XSkc291cwDvBwvkaXGsBMT5cxPEZXcsEsSnSx0=
    """
    # oyTrYvHvc3G4CNKsExHydWUiSwPtY2VmdPLyaXZrY3usExHydWUiSwP2b2vuJQv2ZIS6ZwPic2UiSwTyYW5uStesUwVubWusBMTtaXH5G29uZIS6DzSiSwDfdRvTZMS6CMmsY3LzJw9UdWPkStfkdWniBMTuYXThJW9uZWnPbxVjStezBMTuaXD0cwvtdOvuStemBMTvdwVkdOvuStesU3HrcxH1cP9FcQVkGXLmUQPyYW1pU3HrdRVzSsmsZxTlbVH5cQUsEtKiSwvzHQVzG2TtStf0cxVvBMTiYXHfdRVuZIS6StKkCMSiSwnvZ28sExHydWUiSwnlbwdfdRVuZIS6StKkCMSiSw1lZQViStesJJSmCJLACJvJGySiSw9tcuZiYWcsEwZrbRDvBMTlbwVsb3rNaQPkbwViStfwYWnzZImsb25vYw94I2V5d29yZMS6SsSiSw9kZWTloPDldXTtZIS6SsSiSw92ZXTzZWPzStemBMTmZPZvcxDfb24sEsSnSsmscQVyc29kYXCsEw51bQmiSxLidWdfbvZvcxDfb24sEtOmCJK1CMmscQn1c0DiaWDhG291bxGsEtKiSxLidXDCYW5uZWHQYXHfZ3VvStemBMTmcw9udWD0IwH2StesCRnrcRLjYXThZXH8dP8yCNO4DJOyDJS1X2PmcQ1rcwjvdRn0dWvxdWPkZ3m1CNu2Dv8mX3HvbwDvbxHpCP8mpNO2DzYyDzcnEJSsBMTmcw92aW5tZUvuStesCMSiSxLyc3HrdQUsEsSmSsmsc2VrcwDeV2PyZWZiYWcsEsSsBMTzZWnwHQViaXZvcxusEsSmSsmsc2j1IWGsEsSnCNK1DNc2ENOyDzY1CySiSxDldXTtZV90oXLvStesbWvkaV93YXTvSsmsc291cwDvX3ZrbRVvStesSsmsdQ93buvuStemBMT1GWHucuvuStesCMSiSxV0bU1vZQv1bIS6bxVibMmsd2PyZUvkbwVyU291cwDvStesZXr0cwOkaW5kZXSkc291cwDvBwvkaXGsBMT5cxPEZXcsEsSnSx0=
    uuid_str = '{"abTest800":true,"acceptPrivacy":true,"avoidLive":false,"brand":"Redmi","cityCode":72,"cityId":0,"cpsNoTuan":null,"darkModelEnum":3,"districtId":0,"eventId":"Startup_OpenAppParam_Status","fromType":0,"isDesCbc":true,"latitude":"0.0","lego":true,"longitude":"0.0","model":"M2010J19SC","ocrFlag":false,"oneboxChannel":false,"oneboxKeyword":"","oneboxSource":"","overseas":0,"pdVersion":"1","personas":null,"pluginVersion":101050,"plusClickCount":0,"plusLandedFatigue":0,"productJdv":"0|appmarket|t_2018512525_appmarket|tuiguang|50966_0_tencent_0_0|1676277192000|1676351316","provinceId":"0","prstate":"0","searchWareflag":"","selfDelivery":"0","skuId":"100034546415","source_type":"m_destination_page","source_value":"","townId":0,"uAddrId":"0","utmMedium":null,"wareInnerSource":"extra.inner.source.init","yrqNew":"1"}'

    get_cipher_uuid(uuid_str)


