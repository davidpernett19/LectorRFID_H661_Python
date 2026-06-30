from domain.entities.inventory_record import (
    InventoryRecord
)

from domain.entities.rfid_tag import (
    RFIDTag
)


class InventoryService:
    """
    Servicio encargado de consolidar
    lecturas RFID por EPC.
    """

    def __init__(self):

        self._records: dict[
            str,
            InventoryRecord
        ] = {}

    def process_tag(
        self,
        tag: RFIDTag
    ) -> None:
        """
        Procesa una lectura RFID y
        actualiza el inventario consolidado.
        """

        if tag.epc not in self._records:

            self._records[tag.epc] = InventoryRecord(
                epc=tag.epc,
                read_count=1,
                first_seen=tag.timestamp,
                last_seen=tag.timestamp,
                last_rssi=tag.rssi
            )

            return

        record = self._records[tag.epc]

        record.read_count += 1
        record.last_seen = tag.timestamp
        record.last_rssi = tag.rssi

    def get_all_records(
        self
    ) -> list[InventoryRecord]:
        """
        Retorna todos los EPCs consolidados.
        """

        return list(
            self._records.values()
        )

    def clear(self) -> None:
        """
        Limpia el inventario consolidado.
        """

        self._records.clear()