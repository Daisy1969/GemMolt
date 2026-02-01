import os

class ProjectManager:
    def __init__(self, root_path):
        self.root_path = root_path
    
    def list_projects(self):
        """Scans the root path for directories that look like projects."""
        if not os.path.exists(self.root_path):
            return f"Error: Path {self.root_path} does not exist."
        
        projects = []
        try:
            for item in os.listdir(self.root_path):
                item_path = os.path.join(self.root_path, item)
                if os.path.isdir(item_path):
                    # Check for indicators of a project
                    repo_indicator = os.path.exists(os.path.join(item_path, ".git"))
                    config_indicator = os.path.exists(os.path.join(item_path, "package.json")) or \
                                       os.path.exists(os.path.join(item_path, "requirements.txt")) or \
                                       os.path.exists(os.path.join(item_path, "pyproject.toml"))
                    
                    if repo_indicator or config_indicator:
                        projects.append(item)
        except Exception as e:
            return f"Error scanning projects: {e}"
        
        return projects

    def get_project_summary(self, project_name):
        """Reads the README.md of a specific project."""
        project_path = os.path.join(self.root_path, project_name)
        readme_path = os.path.join(project_path, "README.md")
        
        if os.path.exists(readme_path):
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read(500) # Read first 500 chars
                return content + "..."
            except Exception as e:
                return f"Error reading README: {e}"
        return "No README.md found."
