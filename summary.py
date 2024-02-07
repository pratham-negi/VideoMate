import re

import requests


def clean(filename):
  with open(filename, "r") as f:
    lines = f.readlines()

  # Regular expression to match timestamps and sentence-ending punctuation
  timestamp_regex = re.compile(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$")
  punctuation_regex = re.compile(r"[.?!]$")

  # Filter and clean lines
  filtered_lines = ""
  for line in lines:
    if not timestamp_regex.match(line) and len(line.strip()) >= 3:
      cleaned_line = line.strip()
      if not punctuation_regex.search(cleaned_line):
        cleaned_line += ". "
      filtered_lines += cleaned_line

  # Print the final lines
  return filtered_lines



def summarizationTextFun(filename):
    url = "https://api.meaningcloud.com/summarization-1.0"

    payload={
        'key': 'e084a0f7894d09163ac03e0cff3a9c03',
        'txt': clean(filename),
        'sentences': 15
    }

    response = requests.post(url, data=payload)
    sumData = response.json()
    return sumData["summary"]