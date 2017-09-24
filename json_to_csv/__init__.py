#!/usr/bin/env python
"""
"""

import csv
import copy
import json
import uuid

ROW_TEMPLATE = {
    "id": None,
    "parentId": None,
    "type": None,
    "key": None,
    "value": None
}

def structureToRelationalDicts(data, parentId=None, parentKey=None):

    row = copy.copy(ROW_TEMPLATE)

    row.update({
        "id": uuid.uuid4().hex,
        "parentId": parentId,
        "key": parentKey,
    })

    if isinstance(data, dict):
        row.update({
            "type": "dict"
        })
        for k, v in data.items():
            yield from structureToRelationalDicts(v, parentId=row["id"], parentKey=str(k))
    elif isinstance(data, list):
        row.update({
            "type": "list"
        })
        for n, v in enumerate(data):
            yield from structureToRelationalDicts(v, parentId=row["id"], parentKey=str(n))
    elif isinstance(data, bool):
        row.update({
            "type": "bool",
            "value": str(data).upper()
        })
    elif data is None:
        row.update({
            "type": "null",
            "value": "NULL"
        })
    else:
        row.update({
            "type": "str",
            "value": str(data)
        })

    yield row

def jsonToCsv(jsonFilepath, csvFilepath):
    with open(jsonFilepath, "r") as fh:
        data = json.load(fh)
    
    with open(csvFilepath, "w") as fh:
        writer = csv.DictWriter(fh, fieldnames=sorted(ROW_TEMPLATE.keys()))
        writer.writeheader()

        for row in structureToRelationalDicts(data):
            writer.writerow(row)
