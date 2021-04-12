#!/bin/bash
for cmd in ipython3 ipython python3 python; do
  if command -v $cmd > /dev/null; then
    $cmd $@
    exit 0
  fi
done
echo "Couldn't find any python executable"
exit 1
