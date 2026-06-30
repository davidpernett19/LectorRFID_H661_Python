#Proyecto MAIN

from app.services.rfid_service import RFIDService
from app.services.inventory_service import (
    InventoryService
)
from database.sqlite_manager import (
    SQLiteManager
)

db = SQLiteManager()

print("SQLite conectado")

db.close()

print("SQLite cerrado")


def main():

    rfid = RFIDService()

    inventory = InventoryService()

    connected = rfid.connect(
        "192.168.1.200",
        2022
    )

    print("Conectado:", connected)

    if not connected:
        return

    try:

        started = rfid.start_inventory()

        print("Inventario iniciado:", started)

        for i in range(5):

            tag = rfid.read_tag()

            if tag:

                inventory.process_tag(tag)

                print()
                print(f"Lectura #{i + 1}")
                print(tag)

        print()
        print("=" * 50)
        print("INVENTARIO CONSOLIDADO")
        print("=" * 50)

        for record in inventory.get_all_records():

            print(record)

        print()
        print(
            "Total lecturas:",
            rfid.get_total_reads()
        )

    finally:

        print()
        print("Deteniendo inventario...")

        rfid.stop_inventory()

        print("Desconectando lector...")

        rfid.disconnect()


if __name__ == "__main__":
    main()