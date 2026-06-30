from domain.entities.rfid_tag import RFIDTag


class TagRepository:
    """
    Repositorio de lecturas RFID.

    Actualmente almacena las lecturas en memoria.
    En futuras versiones podrá persistir en SQLite
    o SQL Server sin afectar al resto de la aplicación.
    """

    def __init__(self):

        self._tags: list[RFIDTag] = []

    def add(self, tag: RFIDTag) -> None:
        """
        Agrega una lectura RFID.
        """

        self._tags.append(tag)

    def get_all(self) -> list[RFIDTag]:
        """
        Retorna todas las lecturas.
        """

        return self._tags.copy()

    def count(self) -> int:
        """
        Retorna la cantidad total de lecturas.
        """

        return len(self._tags)

    def clear(self) -> None:
        """
        Elimina todas las lecturas.
        """

        self._tags.clear()