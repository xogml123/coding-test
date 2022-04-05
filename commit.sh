#!/bin/sh

suffix=".py"

find . -name "$2$suffix" -exec git add '{}' \;
git commit -m "$1/$2$suffix - $3"
git push
