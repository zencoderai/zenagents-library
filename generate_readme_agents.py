#!/usr/bin/env python3
"""
Script to generate the "Available Agents" section for README.md
based on the actual agent JSON files in the agents folder.

Usage:
    python3 generate_readme_agents.py [--preview] [--output-only]
    
Options:
    --preview: Show what changes would be made without updating the file
    --output-only: Only output the generated section, don't update README
"""

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple


def get_agent_description(data: dict, filename: str) -> str:
    """
    Get the agent description from the JSON data.
    Requires the 'description' field to be present and non-empty.
    """
    description = data.get('description', '').strip()
    if not description:
        raise ValueError(f"Missing or empty 'description' field in {filename}")
    
    return description


def load_agent_data(agents_dir: Path) -> List[Tuple[str, str]]:
    """
    Load all agent JSON files and extract name and description.
    Returns a list of (name, description) tuples sorted by name.
    Raises an error if any agent is missing a description field.
    """
    agents = []
    errors = []
    
    for json_file in sorted(agents_dir.glob("*.json")):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            name = data.get('name', 'Unknown Agent')
            
            # Get description from the description field (will raise ValueError if missing)
            description = get_agent_description(data, json_file.name)
            
            agents.append((name, description))
            
        except ValueError as e:
            errors.append(str(e))
        except (json.JSONDecodeError, FileNotFoundError) as e:
            errors.append(f"Could not process {json_file}: {e}")
    
    # If there were any errors, report them and exit
    if errors:
        print("❌ Errors found in agent files:")
        for error in errors:
            print(f"   • {error}")
        print("\n💡 Please add a 'description' field to all agent JSON files.")
        print("   Example:")
        print('   "description": "Clear, concise description of what the agent does"')
        raise SystemExit(1)
    
    return agents


def generate_agents_section(agents: List[Tuple[str, str]]) -> str:
    """
    Generate the markdown content for the Available Agents section.
    """
    lines = ["## Available Agents", ""]
    lines.append("This repository includes configurations for various specialized coding agents, including:")
    lines.append("")
    
    for name, description in agents:
        lines.append(f"- **{name}**: {description}")
    
    return "\n".join(lines)


def update_readme(readme_path: Path, new_agents_section: str) -> None:
    """
    Update the README.md file with the new Available Agents section.
    """
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Available Agents section and replace it
    # Look for the section header and find where it ends
    pattern = r'(## Available Agents\n.*?)(?=\n## |\n### |\Z)'
    
    if re.search(pattern, content, re.DOTALL):
        # Replace existing section
        new_content = re.sub(pattern, new_agents_section, content, flags=re.DOTALL)
    else:
        # If section doesn't exist, we'll need to add it
        # For now, just print the section to stdout
        print("Available Agents section not found in README.md")
        print("Generated section:")
        print(new_agents_section)
        return
    
    # Write back to file
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully updated {readme_path}")


def main():
    """Main function to generate and update the README."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate Available Agents section for README.md")
    parser.add_argument("--preview", action="store_true", 
                       help="Show what changes would be made without updating the file")
    parser.add_argument("--output-only", action="store_true",
                       help="Only output the generated section, don't update README")
    args = parser.parse_args()
    
    # Get the script directory and project root
    script_dir = Path(__file__).parent
    agents_dir = script_dir / "agents"
    readme_path = script_dir / "README.md"
    
    # Verify paths exist
    if not agents_dir.exists():
        print(f"Error: Agents directory not found at {agents_dir}")
        return
    
    if not readme_path.exists() and not args.output_only:
        print(f"Error: README.md not found at {readme_path}")
        return
    
    # Load agent data
    print(f"Loading agents from {agents_dir}...")
    agents = load_agent_data(agents_dir)
    print(f"Found {len(agents)} agents")
    
    # Generate new section
    new_section = generate_agents_section(agents)
    
    if args.output_only:
        # Just print the section
        print("\n" + "="*50)
        print("GENERATED SECTION:")
        print("="*50)
        print(new_section)
    elif args.preview:
        # Show preview of changes
        print("\n" + "="*50)
        print("PREVIEW - New section that would be added:")
        print("="*50)
        print(new_section)
        print("\n" + "="*50)
        print("Run without --preview to apply changes")
    else:
        # Update README
        update_readme(readme_path, new_section)


if __name__ == "__main__":
    main()