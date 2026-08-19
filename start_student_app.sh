#!/usr/bin/env bash
# Root shortcut to launch student evaluation app
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
exec "$SCRIPT_DIR/student_app/start_app.sh"
