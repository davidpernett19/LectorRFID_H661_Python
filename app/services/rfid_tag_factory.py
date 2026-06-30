from datetime import datetime

from domain.entities.rfid_tag import RFIDTag
from infrastructure.rfid.structures import TagInfo
from infrastructure.rfid.tag_utils import tag_to_epc


class RFIDTagFactory:
    """
    Convierte estructuras nativas del SDK RFID
    en entidades de dominio RFIDTag.

    Esta clase desacopla completamente el SDK
    del resto de la aplicación.
    """

    @staticmethod
    def create(tag: TagInfo) -> RFIDTag:
        """
        Convierte un TagInfo en una entidad RFIDTag.
        """

        return RFIDTag(
            epc=tag_to_epc(tag),
            rssi=tag.m_rssi / 10,
            antenna=tag.m_ant,
            channel=tag.m_channel,
            timestamp=datetime.now()
        )