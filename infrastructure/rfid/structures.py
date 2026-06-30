from ctypes import (
    Structure,
    c_ushort,
    c_short,
    c_byte,
    c_ubyte
)


class TagInfo(Structure):
    _fields_ = [
        ("m_no", c_ushort),
        ("m_rssi", c_short),
        ("m_ant", c_byte),
        ("m_channel", c_byte),
        ("m_crc", c_ubyte * 2),
        ("m_pc", c_ubyte * 2),
        ("m_len", c_ubyte),
        ("m_code", c_ubyte * 255),
    ]


class DevicePara(Structure):
    _fields_ = [
        ("DEVICEARRD", c_byte),
        ("RFIDPRO", c_byte),
        ("WORKMODE", c_byte),
        ("INTERFACE", c_byte),
        ("BAUDRATE", c_byte),
        ("WGSET", c_byte),
        ("ANT", c_byte),
        ("REGION", c_byte),
        ("STRATFREI", c_ushort),
        ("STRATFRED", c_ushort),
        ("STEPFRE", c_ushort),
        ("CN", c_byte),
        ("RFIDPOWER", c_byte),
        ("INVENTORYAREA", c_byte),
        ("QVALUE", c_byte),
        ("SESSION", c_byte),
        ("ACSADDR", c_byte),
        ("ACSDATALEN", c_byte),
        ("FILTERTIME", c_byte),
        ("TRIGGLETIME", c_byte),
        ("BUZZERTIME", c_byte),
        ("INTERNELTIME", c_byte),
    ]