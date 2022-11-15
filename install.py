#!/usr/bin/env python3

import json
import shutil
import os.path as osp
from pathlib import Path as Plp

mappings_file = "mappings.json"

with open(mappings_file, 'rb') as fp:
    mappings = json.load(fp)
    for mapping in mappings:
        shutil.copy2(mapping["name"], Plp(mapping["path"]).expanduser())
