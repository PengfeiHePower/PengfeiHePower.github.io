#!/bin/bash
# Refresh _data/citations.yml from Google Scholar and push it when the numbers change.
# Scholar blocks CI runners, so this runs from a Mac via launchd (bin/install_citation_sync.sh).
# It works in its own clone so it never touches a working copy with uncommitted edits.
set -euo pipefail
export PATH="/usr/bin:/bin:/usr/sbin:/sbin"

REMOTE="https://github.com/PengfeiHePower/PengfeiHePower.github.io.git"
STATE_DIR="$HOME/.local/share/homepage-citations"
REPO="$STATE_DIR/repo"
STAMP="$STATE_DIR/last-success"

mkdir -p "$STATE_DIR"
# launchd also fires at login and on wake; one successful sync per day is enough.
if [ "${1:-}" != "--force" ] && [ -f "$STAMP" ] && [ "$(cat "$STAMP")" = "$(date +%F)" ]; then
  exit 0
fi

echo "== $(date '+%F %T') =="
if [ ! -d "$REPO/.git" ]; then
  git clone -q --depth 1 --branch master "$REMOTE" "$REPO"
fi
cd "$REPO"
git fetch -q --depth 1 origin master
git reset -q --hard origin/master

python3 bin/update_citations.py --strict

# The "updated:" date changes every run; only commit when the counts themselves moved.
if git diff -U0 -- _data/citations.yml | grep -E '^[-+] ' | grep -vqE '^[-+]updated:'; then
  git add _data/citations.yml
  git -c user.name="He Pengfei" -c user.email="billhe@yahoo.com" \
    commit -qm "Update citation counts from Google Scholar"
  git push -q origin HEAD:master
  echo "pushed: $(grep -E '^(citations|h_index):' _data/citations.yml | tr '\n' ' ')"
else
  echo "no change"
fi
date +%F > "$STAMP"
