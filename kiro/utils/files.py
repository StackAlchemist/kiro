#for every file read file replace placeholders write file
from pathlib import Path

def replace_placeholders(project_path, state):
    placeholders = {
        "{{project_name}}": state.project_name,
        "{{runtime}}": state.runtime,
        "{{framework}}": state.framework,
        "{{language}}": state.language or "",
    }

    for file in Path(project_path).rglob("*"):
        if file.is_file():
            try:
                content = file.read_text(encoding="utf-8")

                for placeholder, value in placeholders.items():
                    content = content.replace(placeholder, value)

                file.write_text(content, encoding = "utf-8")

            except UnicodeDecodeError:

                continue