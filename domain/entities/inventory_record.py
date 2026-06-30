from dataclasses import dataclass
from datetime import datetime


@dataclass
class InventoryRecord:
    """
    Registro consolidado de inventario RFID.
    """

    epc: str
    read_count: int
    first_seen: datetime
    last_seen: datetime
    last_rssi: float