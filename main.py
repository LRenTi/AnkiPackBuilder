from gui import AnkiPackBuilderGUI
from utils import check_for_updates

if __name__ == "__main__":
    check_for_updates()
    anki_pack_builder = AnkiPackBuilderGUI()
    anki_pack_builder.start()
