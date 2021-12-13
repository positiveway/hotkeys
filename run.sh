#!/bin/sh
psudo() { sudo env PATH="$PATH" "$@"; }

sudo chmod +x ./venv/bin/activate
. venv/bin/activate

psudo python ./main.py

