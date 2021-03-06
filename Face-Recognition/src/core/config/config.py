DATA_DIR = "./data"

ALL_METHODS = ["scale", "hist", "grad", "dft", "dct"]

METHODS_PARAM = {
    "scale": {"name": "l", "default": "2", "range": (2, 10)},
    "hist": {"name": "BIN", "default": "32", "range": (8, 65)},
    "grad": {"name": "W", "default": "10", "range": (4, 21)},
    "dft": {"name": "P", "default": "20", "range": (6, 31)},
    "dct": {"name": "P", "default": "20", "range": (6, 31)},
}

ALL_DATABASES = ["ORL"]

DATABASE_CONF = {
    "ORL": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "./data/ORL/s{g}/{im}.png",
    },
    "ORL_mask": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "./data/ORL_mask/s{g}/{im}-with-mask-cropped.jpg",
    },
    "ORL_fawkes": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "./data/ORL_fawkes/s{g}/{im}_cloaked_cropped.jpg",
    }
}

RESEARCHES = ["1/N-1", "L/N-L"]

RESULT = "./data/results/{im}.jpg"
DATA_PATH = "./data/"
