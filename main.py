from gui import AnkiPackBuilderGUI
from utils import check_for_update

if __name__ == "__main__":
    check_for_update()
    anki_pack_builder = AnkiPackBuilderGUI()
    anki_pack_builder.start()
