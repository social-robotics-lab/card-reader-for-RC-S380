import nfc
import re
from typing import cast


def on_connect(tag):
    sys_code = 0xFE00
    service_code = 0x1A8B
    idm, pmm = tag.polling(system_code=sys_code)
    tag.idm, tag.pmm, tag.sys = idm, pmm, sys_code
    sc = nfc.tag.tt3.ServiceCode(service_code >> 6, service_code & 0x3F)

    # student_num
    bc = nfc.tag.tt3.BlockCode(0, service=0)
    student_num = cast(bytearray, tag.read_without_encryption([sc], [bc]))
    student_num = student_num.decode("shift_jis")
    #re.findall()　：　マッチした部分をリストとして返す
    #r'.{2}(.{10}).{2}'　：　.は任意の1文字を示し、{}内の数値の回数繰り返したものにマッチさせる
    #(.{10}) 　：　（）内の要素をグループ化しキャプチャ（今回は任意の一文字10個分）
    Dgakuseki_num = re.findall(r'.{2}(.{10}).{2}', student_num)
    #リストで返されるため、最初の要素を返す
    print("student number : " + str(Dgakuseki_num[0]))

    # name
    bc = nfc.tag.tt3.BlockCode(1, service=0)
    name = cast(bytearray, tag.read_without_encryption([sc], [bc]))
    name = name.decode("shift_jis")
    print("name : " + str(name))


with nfc.ContactlessFrontend("usb") as clf:
    clf.connect(rdwr={"on-connect": on_connect})
