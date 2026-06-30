from ctypes import c_void_p, byref

from infrastructure.rfid.dll_loader import DLLLoader
from infrastructure.rfid.structures import (
    DevicePara,
    TagInfo
)


class UHFPrimeReaderAdapter:
    """
    Adaptador encargado de encapsular todas las llamadas
    al SDK RFID UHF Prime Reader.

    La aplicación nunca debe interactuar directamente
    con la DLL. Todas las operaciones RFID deben pasar
    por esta clase.
    """

    def __init__(self):

        self._loader = DLLLoader()

        self._dll = self._loader.load()

        self._handler = c_void_p()

        self._connected = False

    @property
    def is_connected(self):
        return self._connected

    @property
    def handler(self):
        return self._handler

    def connect(
        self,
        ip: str,
        port: int,
        timeout_ms: int = 5000
    ) -> bool:
        """
        Establece una conexión TCP/IP con el lector RFID.
        """

        result = self._dll.OpenNetConnection(
            byref(self._handler),
            ip.encode(),
            port,
            timeout_ms
        )

        print("Resultado OpenNetConnection:", result)
        print("Handler:", self._handler.value)

        self._connected = result == 0

        return self._connected

    def disconnect(self) -> bool:
        """
        Cierra la conexión con el lector RFID.
        """

        if not self._connected:
            return True

        result = self._dll.CloseDevice(
            self._handler
        )

        if result == 0:
            self._connected = False

        return result == 0

    def get_device_parameters(self):
        """
        Obtiene la configuración actual del lector RFID.
        """

        if not self._connected:
            raise RuntimeError(
                "El lector no está conectado"
            )

        info = DevicePara()

        result = self._dll.GetDevicePara(
            self._handler,
            byref(info)
        )

        return result, info

    def start_inventory(
        self,
        inv_count: int = 0,
        inv_param: int = 0
    ) -> bool:
        """
        Inicia el proceso de inventario RFID.
        """

        if not self._connected:
            raise RuntimeError(
                "El lector no está conectado"
            )

        result = self._dll.InventoryContinue(
            self._handler,
            inv_count,
            inv_param
        )

        print("InventoryContinue:", result)

        return result == 0

    def stop_inventory(
        self,
        timeout_ms: int = 1000
    ) -> bool:
        """
        Detiene el proceso de inventario RFID.
        """

        if not self._connected:
            return False

        result = self._dll.InventoryStop(
            self._handler,
            timeout_ms
        )

        print("InventoryStop:", result)

        return result == 0

    def get_tag(
        self,
        timeout_ms: int = 1000
    ):
        """
        Obtiene un tag leído por el lector RFID.

        Returns:
            tuple[int, TagInfo]
        """

        if not self._connected:
            raise RuntimeError(
                "El lector no está conectado"
            )

        tag = TagInfo()

        result = self._dll.GetTagUii(
            self._handler,
            byref(tag),
            timeout_ms
        )

        return result, tag