#!/bin/bash
folder_path="$1"
echo "Nazwa folderu to: $folder_path"
python3 ~/python/file-cleaner/file-cleaner.py --dir $folder_path