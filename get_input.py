#!/usr/bin/env python3
import requests
import sys
import os


# get session token in Chrome
# 1. Open AoC website
# 2. Open Dev Console
# 3. Switch to Application Section
# 4. See Cookies, copy Value from session row

# export the token
# copy into token.txt

# run script
# python3 get_input.py $DAY
with open("token.txt") as f:
    lines = f.read().splitlines()

sessionToken = lines[0]

year = sys.argv[1]
day = sys.argv[2]


def get_input(day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(url)
    headers = {"Cookie": "session=" + sessionToken}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")


def write_input(text, day):
    # pre-append a 0 if day is only single digit
    if len(str(day)) < 2:
        day = f"0{str(day)}"
    # create the folder if it doesn't exist
    d = f"{year}/{day}"
    if not os.path.exists(d):
        os.makedirs(d)
    # write the day input to input.txt inside the directory
    with open(f"{d}/input.txt", "w") as a:
        a.write(text)


text = get_input(day)
write_input(text, day)
