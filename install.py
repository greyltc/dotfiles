#!/usr/bin/env python3

import json
import shutil
import os.path as osp

mappings_file = "mappings.json"

with open(mappings_file, 'rb') as fp:
    mappings = json.load(fp)
    for mapping in mappings:
        shutil.copy2(mapping["name"], mapping["path"])
