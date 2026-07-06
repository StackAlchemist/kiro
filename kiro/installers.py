 # Runs npm/pip commands for deps installation

import subprocess
import shutil

def install_dependencies(state):
    project = state.project_name
    npm = shutil.which("npm") or shutil.which("npm.cmd")

    try:
        subprocess.run([npm, "install"], cwd=project, check=True)
        print("✅ Dependencies installed successfully")

    except FileNotFoundError:
        print("❌ npm was not found. Please install Node.js first.")