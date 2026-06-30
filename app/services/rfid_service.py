from infrastructure.rfid.adapter import (
    UHFPrimeReaderAdapter
)

from app.services.rfid_tag_factory import (
    RFIDTagFactory
)
from database.repositories.tag_repository import (
    TagRepository
)
from domain.entities.rfid_tag import RFIDTag

class RFIDService:
    """
    Servicio principal RFID.

    Encapsula toda la lógica relacionada
    con conexión, inventario y lectura
    de tags RFID.

    La UI debe interactuar únicamente
    con esta clase.
    """

    def __init__(self):

        self._reader = UHFPrimeReaderAdapter()

        self._repository = TagRepository()

    @property
    def is_connected(self) -> bool:

        return self._reader.is_connected

    def connect(
        self,
        ip: str,
        port: int
    ) -> bool:
        """
        Conecta con el lector RFID.
        """

        return self._reader.connect(
            ip,
            port
        )

    def disconnect(self) -> bool:
        """
        Desconecta el lector RFID.
        """

        return self._reader.disconnect()

    def start_inventory(self) -> bool:
        """
        Inicia inventario RFID.
        """

        return self._reader.start_inventory()

    def stop_inventory(self) -> bool:
        """
        Detiene inventario RFID.
        """

        return self._reader.stop_inventory()

    def read_tag(self) -> RFIDTag | None:
        """
        Lee un tag RFID y lo convierte
        a entidad de dominio RFIDTag.

        Returns:
            RFIDTag | None
        """

        result, tag = self._reader.get_tag()

        if result != 0:
            return None

        rfid_tag = RFIDTagFactory.create(tag)

        self._repository.add(rfid_tag)

        return rfid_tag

    def get_all_tags(self) -> list[RFIDTag]:

        """
        Retorna todas las lecturas almacenadas.
        """

        return self._repository.get_all()


    def get_total_reads(self) -> int:

        """
        Retorna el número total de lecturas.
        """

        return self._repository.count()


    def clear_reads(self) -> None:

        """
        Limpia todas las lecturas almacenadas.
        """

        self._repository.clear()