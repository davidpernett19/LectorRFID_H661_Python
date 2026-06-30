from pathlib import Path

from ctypes import (
    WinDLL,
    POINTER,
    c_void_p,
    c_char_p,
    c_ushort,
    c_uint,
    c_int,
    c_byte
)

from infrastructure.rfid.structures import (
    DevicePara,
    TagInfo
)


class DLLLoader:

    def __init__(self):
        self._dll = None

    def load(self):

        dll_path = (
            Path(__file__).parent
            / "dll"
            / "UHFPrimeReader.dll"
        )

        if not dll_path.exists():
            raise FileNotFoundError(
                f"DLL no encontrada: {dll_path}"
            )

        self._dll = WinDLL(str(dll_path))

        self._configure_functions()

        return self._dll

    def _configure_functions(self):

        # ==========================================
        # OpenNetConnection
        # ==========================================

        self._dll.OpenNetConnection.argtypes = [
            POINTER(c_void_p),
            c_char_p,
            c_ushort,
            c_uint
        ]

        self._dll.OpenNetConnection.restype = c_int

        # ==========================================
        # CloseDevice
        # ==========================================

        self._dll.CloseDevice.argtypes = [
            c_void_p
        ]

        self._dll.CloseDevice.restype = c_int

        # ==========================================
        # GetDevicePara
        # ==========================================

        self._dll.GetDevicePara.argtypes = [
            c_void_p,
            POINTER(DevicePara)
        ]

        self._dll.GetDevicePara.restype = c_int

        # ==========================================
        # InventoryContinue
        # ==========================================

        self._dll.InventoryContinue.argtypes = [
            c_void_p,
            c_byte,
            c_uint
        ]

        self._dll.InventoryContinue.restype = c_int

        # ==========================================
        # InventoryStop
        # ==========================================

        self._dll.InventoryStop.argtypes = [
            c_void_p,
            c_ushort
        ]

        self._dll.InventoryStop.restype = c_int

        # ==========================================
        # GetTagUii
        # ==========================================

        self._dll.GetTagUii.argtypes = [
            c_void_p,
            POINTER(TagInfo),
            c_ushort
        ]

        self._dll.GetTagUii.restype = c_int

    @property
    def dll(self):
        return self._dll