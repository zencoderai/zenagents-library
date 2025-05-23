# Agents Marketplace

A community-driven collection of custom coding agent configurations for AI assistants. This repository hosts JSON configuration files that define specialized AI coding agents with specific skills and toolsets.

## About This Repository

The Agents Marketplace is designed to be a central hub where developers can find and share configurations for specialized AI coding assistants. Each agent is defined by a JSON configuration file that specifies:

- The agent's name and identity
- Detailed instructions that shape the agent's behavior and expertise
- A set of tools the agent can utilize

## Available Agents

This repository includes configurations for various specialized coding agents, including:

- **Accessibility Evaluator**: Evaluates code for accessibility issues and provides guidance for creating inclusive user experiences
- **API Designer**: Creates well-structured, intuitive, and robust APIs
- **Architecture Designer**: Designs robust, scalable, and maintainable systems
- **Bug Prediction & Prevention Agent**: Predicts potential bugs and reliability issues in code
- **Code Explainer**: Analyzes code and explains its functionality, patterns, and design decisions
- **Code Migration Specialist**: Helps transition between languages, frameworks, or versions
- **Coding Tutor**: Provides personalized guidance to improve programming skills
- **Database Designer**: Creates efficient, scalable data models and access patterns
- **Debugging Assistant**: Diagnoses and fixes software issues
- **Dependency Manager**: Analyzes dependencies for vulnerabilities, conflicts, and improvement opportunities
- **Dependency Upgrade Planner**: Creates strategic upgrade plans for dependencies
- **DevOps Pipeline Builder**: Creates efficient CI/CD pipelines
- **Documentation Generator**: Creates clear, comprehensive documentation for code
- **Infrastructure as Code Specialist**: Defines cloud resources and deployments as version-controlled configuration
- **Legacy Code Modernizer**: Transforms outdated codebases into maintainable, modern implementations
- **Microservice Designer**: Designs distributed systems with proper service boundaries
- **Performance Optimizer**: Improves code efficiency, speed, and resource utilization
- **QA Engineer**: Generates comprehensive test plans and test cases for features
- **Refactoring Specialist**: Improves code quality without changing functionality
- **Security Auditor**: Identifies and addresses security vulnerabilities in code
- **Technical Debt Identifier**: Identifies, prioritizes, and addresses code quality issues
## How to Submit Your Own Agent Configuration

We welcome contributions from the community! Follow these steps to submit your own custom agent configuration:

### Submission Guidelines

1. **Follow the Standard Format**: Your JSON configuration file should follow this structure:

```json
{
  "name": "Your Agent Name",
  "description": "Clear, concise description of what your agent does",
  "instructions": "Detailed instructions that define your agent's behavior, expertise, and approach...",
  "tools": [
    "Tool 1",
    "Tool 2",
    "Tool 3"
  ]
}
```

2. **Provide Clear Description and Comprehensive Instructions**: 
   - **Description**: A concise, clear description of what your agent does (used in the README) - **REQUIRED**
   - **Instructions**: Detailed behavioral guidance including:
     - A clear identity statement (e.g., "You are SecuritySentinel, a security auditing specialist...")
     - A numbered list of steps or approaches the agent should follow
     - Guidance on how the agent should request additional information
     - Specific output format expectations
     - Any other behavioral guidance that shapes the agent's expertise

3. **Name Your File Appropriately**: Use kebab-case for your filename (e.g., `security-auditor.json`, `performance-optimizer.json`)

### Submission Process

1. Fork this repository
2. Add your agent configuration file to your forked repository
3. Ensure your file follows the required format and naming convention
4. Submit a pull request with a brief description of your agent's purpose and capabilities
5. Wait for review by the repository maintainers

### Review Criteria

Submissions will be reviewed based on:

- Adherence to the required format
- Quality and comprehensiveness of the instructions
- Uniqueness and usefulness of the agent concept
- Appropriate tool selection

## Using These Agent Configurations

These configuration files are designed to be used with AI assistant platforms that support custom instructions and tool configurations. The specific implementation details may vary depending on the platform you're using.

## Disclaimer for Contributed Custom Agents

By submitting a pull request that includes a custom agent, you agree to the following terms. This project is based on open-source work licensed under the [MIT License](https://opensource.org/license/MIT) (the full license text is included in this repository). As such:

- **License Notice**: All contributions are assumed to be made under the terms of the MIT License. By contributing, you agree that your submitted code can be used, modified, and redistributed under this license.

- **Terms of Service & Acceptable Use Policy**: By contributing or using agents through the Zencoder platform, you agree to comply with our [Zencoder's Terms of Service](https://zencoder.ai/legal/terms-of-service) and [Acceptable Use Policy](https://zencoder.ai/legal/acceptable-use-policy), which governs access to and use of the Zencoder products and services.

- **No Warranty**: In accordance with the MIT License and Zencoder Terms, all code is provided "as is," without warranty of any kind, express or implied.

- **Responsibility and Usage**: Contributors are responsible for ensuring the functionality, safety, and legality of the agents they submit. Users are equally responsible for auditing and testing any contributed agents before deployment. We disclaim all liability for any direct or indirect damages resulting from the use or misuse of submitted agents in this repository.

- **Review Limitations**: While we may review contributions for quality and safety, we do not guarantee that all issues (including bugs, security vulnerabilities, or malicious behavior) will be identified.

- **Modification Rights**: We reserve the right to accept or reject any contribution at our sole discretion, without obligation to provide feedback or justification. Additionally, we may edit, adapt, or remove contributed agents at any time for reasons including, but not limited to, technical issues, policy changes, security concerns, or project direction.

## License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thank you to all contributors who have shared their agent configurations to help build this community resource.
