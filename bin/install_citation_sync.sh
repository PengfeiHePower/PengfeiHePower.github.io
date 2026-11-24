#!/bin/bash
# Install (or reinstall) the launchd job that runs bin/sync_citations.sh several times a day.
# Uninstall: launchctl bootout gui/$(id -u)/com.pengfeihe.homepage-citations && rm ~/Library/LaunchAgents/com.pengfeihe.homepage-citations.plist
set -euo pipefail

LABEL="com.pengfeihe.homepage-citations"
STATE_DIR="$HOME/.local/share/homepage-citations"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG="$HOME/Library/Logs/homepage-citations.log"

mkdir -p "$STATE_DIR" "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
# Run a copy: the job hard-resets its own clone, which would rewrite a script that is executing.
cp "$(dirname "$0")/sync_citations.sh" "$STATE_DIR/sync_citations.sh"
chmod +x "$STATE_DIR/sync_citations.sh"

slots=""
for hour in 9 13 18 22; do
  slots+="<dict><key>Hour</key><integer>$hour</integer><key>Minute</key><integer>0</integer></dict>"
done

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array><string>/bin/bash</string><string>$STATE_DIR/sync_citations.sh</string></array>
  <key>StartCalendarInterval</key><array>$slots</array>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>$LOG</string>
  <key>StandardErrorPath</key><string>$LOG</string>
</dict>
</plist>
EOF

launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "Installed $LABEL; log: $LOG"
