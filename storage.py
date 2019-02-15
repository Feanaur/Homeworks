import tempfile
import os
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

key_value_store = {args.key:args.value}

if args.value:
    try:
        with open(storage_path, "r") as f:
            storage = json.load(f)
            storage.update(key_value_store)
            if args.key not in storage.keys():
                storage.update(key_value_store)
            elif args.key in storage.keys():
                values_list = list(storage[args.key])
                values_list.append(key_value_store[args.key])
                storage[args.key] = values_list
        with open(storage_path, 'w') as f:
            json.dump(storage, f)
            print(args.key, args.value)
    except:
        with open(storage_path, 'w') as f:
            json.dump(key_value_store, f)
            print(args.key,args.value)
else:
    try:
        with open(storage_path, 'r') as f:
            storage = json.load(f)
            value = str(storage.get(args.key, None))
            value = value.translate({ord(c):None for c in "''[]"})
            print(value)
    except IOError:
        print(None)