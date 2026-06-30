from infrastructure.rfid.structures import TagInfo


def bytes_to_hex(data, length) -> str:
    """
    Convierte un arreglo de bytes en una cadena
    hexadecimal continua.
    """

    return "".join(
        f"{data[i]:02X}"
        for i in range(length)
    )


def tag_to_epc(tag: TagInfo) -> str:
    """
    Convierte un TagInfo recibido desde la DLL
    en una cadena EPC hexadecimal.
    """

    return bytes_to_hex(
        tag.m_code,
        tag.m_len
    )