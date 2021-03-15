class transCookie:
    def __init__(self, cookie) -> None:
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = 'U_TRS1=0000005a.f45f9f1f.5e6db9b1.c35f5d94; UOR=www.baidu.com,finance.sina.com.cn,; SCF=Aio_yCEK7PdXaT1IvaJv25O3vhX3Z74Jw4M2BCsQAGy7JbN95RNg4K2932XCOHpk1wovN1xhY7nxqVcX_3CEHfs.; sso_info=v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLWOk5i2jbOUuI2DlLKJp5WpmYO0tY6TmLaNs5S4jYOUsg==; UM_distinctid=1755a65b8cc424-037a578ef99b7e-b7a1334-144000-1755a65b8cd881; SINAGLOBAL=121.238.243.149_1604154938.825564; Apache=58.211.250.146_1606807392.586098; name=sinaAds; post=massage; page=23333; ULV=1606807394112:4:1:1:58.211.250.146_1606807392.586098:1604661121074; SGUID=1606807395625_69824467; CNZZDATA5832809=cnzz_eid%3D306119988-1606802834-%26ntime%3D1606802834; lxlrttp=1578733570; NowDate=Tue Dec 01 2020 15:30:24 GMT+0800 (中国标准时间); CNZZDATA1271237680=1351611256-1606807474-%7C1606807474; CNZZDATA1271230489=958668403-1606802084-%7C1606806825; directAd=true; __gads=ID=d7cef9d445bd558c-222a2647f8c400c3:T=1606808993:RT=1606808993:S=ALNI_MY2VuV7ExvemUy-gPhSFzBPId_vNA; ULOGIN_IMG=tc-1cb286a6099ff7df970facfabe9c29a85684'
    trans = transCookie(cookie)
    print(trans.stringToDict())

