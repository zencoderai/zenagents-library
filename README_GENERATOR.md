# README Generator Documentation

This directory contains scripts to automatically generate the "Available Agents" section of the README.md file based on the actual agent JSON files in the `agents/` folder.

## Files

- `generate_readme_agents.py` - Main Python script that reads agent files and generates the README section
- `update-readme.sh` - Shell script wrapper for easier usage
- `README_GENERATOR.md` - This documentation file

## Usage

### Using the Shell Script (Recommended)

The shell script provides a simple interface:

```bash
# Update the README.md file with latest agent information
./update-readme.sh

# Preview changes without updating the file
./update-readme.sh preview

# Only output the generated section (useful for debugging)
./update-readme.sh output-only

# Show help
./update-readme.sh help
```

### Using the Python Script Directly

```bash
# Update the README.md file
python3 generate_readme_agents.py

# Preview changes
python3 generate_readme_agents.py --preview

# Only output the section
python3 generate_readme_agents.py --output-only

# Show help
python3 generate_readme_agents.py --help
```

## How It Works

1. **Agent Discovery**: The script scans the `agents/` directory for all `.json` files
2. **Data Extraction**: For each agent file, it extracts:
   - Agent name from the `name` field
   - Description from the `description` field
3. **Section Generation**: Creates a markdown list with agent names and descriptions
4. **README Update**: Replaces the existing "Available Agents" section in README.md

## Agent JSON Structure

Each agent JSON file **must** follow this structure:

```json
{
  "name": "Agent Name",
  "description": "Clear, concise description of what the agent does",
  "instructions": "Detailed instructions that define the agent's behavior...",
  "tools": ["tool1", "tool2", "tool3"]
}
```

**Required Fields:**
- `name`: The agent's display name
- `description`: A clear, concise description (used in README generation)
- `instructions`: Detailed behavioral instructions for the agent
- `tools`: Array of tools the agent can use

The script will **fail** if any agent is missing the `description` field or if it's empty, ensuring all agents have proper documentation.

## Adding New Agents

When you add a new agent JSON file to the `agents/` directory:

1. Ensure it follows the standard format with **all required fields**:
   ```json
   {
     "name": "Agent Name",
     "description": "Clear, concise description of what the agent does",
     "instructions": "You are AgentName, a specialist who does X...",
     "tools": ["tool1", "tool2"]
   }
   ```
   
   ⚠️ **Important**: The `description` field is required and cannot be empty. The script will fail if it's missing.

2. Run the update script:
   ```bash
   ./update-readme.sh
   ```

The new agent will automatically be included in the README.md file using the description from the `description` field.

## Troubleshooting

### Script Not Found
If you get "command not found" errors:
```bash
# Make sure the script is executable
chmod +x update-readme.sh

# Run from the correct directory
cd /path/to/zenagents-library
./update-readme.sh
```

### Python Errors
If you get Python-related errors:
```bash
# Make sure Python 3 is installed
python3 --version

# Check if the agents directory exists
ls -la agents/

# Verify JSON files are valid
python3 -m json.tool agents/accessibility-evaluator.json
```

### README Not Updated
If the README doesn't get updated:
- Check that README.md exists in the project root
- Verify the "Available Agents" section exists in the README
- Use `--preview` to see what would be changed

### Script Fails with Description Errors
If you see errors about missing description fields:
- Add a `description` field to each agent JSON file
- Ensure the description is not empty or just whitespace
- The description should be a clear, concise summary of what the agent does
- Example error: `Missing or empty 'description' field in agent-name.json`

## Customization

### Modifying Description Handling

The script now uses the `description` field directly from each agent's JSON file. To change how descriptions are processed, edit the `get_agent_description()` function in `generate_readme_agents.py`.

### Changing Output Format

To modify the markdown format, edit the `generate_agents_section()` function.

### Adding More Information

You can extend the script to include additional information like:
- Tool lists for each agent
- Categories or tags
- Creation dates
- Author information

## Integration with CI/CD

You can integrate this script into your CI/CD pipeline to automatically update the README when agents are added or modified:

```yaml
# Example GitHub Actions workflow
name: Update README
on:
  push:
    paths:
      - 'agents/*.json'

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Update README
        run: ./update-readme.sh
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add README.md
          git commit -m "Auto-update Available Agents section" || exit 0
          git push
```

## Contributing

If you want to improve the script:

1. Test your changes with `--preview` first
2. Ensure the script works with all existing agent files
3. Add appropriate error handling
4. Update this documentation if needed

## License

These scripts are part of the zenagents-library project and follow the same MIT license.