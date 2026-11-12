import os
import urllib.request
import re
import rich as rprint

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print(raw_text)
