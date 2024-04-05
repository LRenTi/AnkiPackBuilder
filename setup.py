from distutils.core import setup
import py2exe

# AnkiPackBuilder GUI script
gui_script = {
    "script": "main.py",
    "icon_resources": [(1, r"C:\Users\Loren\Documents\ProgProjects\APB\AnkiPackBuilder\lib\pic\APB_icon.ico")]
}

# Setup configuration
setup(
    windows=[gui_script],
    options={
        "py2exe": {
            "bundle_files": 1,
            "compressed": True
        }
    },
    zipfile=None
)
