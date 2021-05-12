#!/bin/bash
for cmd in ipython3 ipython python3 python; do
  if [[ "$VIRTUAL_ENV" != "" ]] && [[ $cmd == ipython* ]]; then
    # Don't use ipython in virtual environments
    continue
  fi
  if command -v $cmd > /dev/null; then
    $cmd $@
    exit 0
  fi
done
echo "Couldn't find any python executable"
exit 1
