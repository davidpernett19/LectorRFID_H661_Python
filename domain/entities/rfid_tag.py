from dataclasses import dataclass
from datetime import datetime


@dataclass
class RFIDTag:
    """
    Representa una lectura RFID dentro del dominio
    de la aplicación.

    Esta entidad no conoce nada de la DLL,
    ctypes ni estructuras nativas.
    """

    epc: str
    rssi: float
    antenna: int
    channel: int
    timestamp: datetime