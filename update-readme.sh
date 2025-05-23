#!/bin/bash

# Script to update the README.md with the latest agent information
# Usage: ./update-readme.sh [preview|output-only]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/generate_readme_agents.py"

# Check if Python script exists
if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    echo "Error: Python script not found at $PYTHON_SCRIPT"
    exit 1
fi

# Parse arguments
case "${1:-}" in
    "preview")
        echo "🔍 Previewing changes..."
        python3 "$PYTHON_SCRIPT" --preview
        ;;
    "output-only")
        echo "📄 Generating section only..."
        python3 "$PYTHON_SCRIPT" --output-only
        ;;
    "help"|"-h"|"--help")
        echo "Usage: $0 [preview|output-only]"
        echo ""
        echo "Options:"
        echo "  preview     - Show what changes would be made without updating the file"
        echo "  output-only - Only output the generated section, don't update README"
        echo "  (no args)   - Update the README.md file with latest agent information"
        echo ""
        exit 0
        ;;
    "")
        echo "🚀 Updating README.md with latest agent information..."
        python3 "$PYTHON_SCRIPT"
        echo "✅ README.md has been updated successfully!"
        ;;
    *)
        echo "Error: Unknown option '$1'"
        echo "Use '$0 help' for usage information"
        exit 1
        ;;
esac