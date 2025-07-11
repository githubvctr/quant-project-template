# tools/summarize_project.py

from pathlib import Path
import ast

def main():
    project_root = Path(__file__).resolve().parent.parent
    include_dirs = ["src", "app", "notebooks", "tests", "streamlit_app"]
    output_lines = []

    def summarize_file(file_path: Path):
        try:
            tree = ast.parse(file_path.read_text())
        except Exception as e:
            return [f"# Failed to parse {file_path.name}: {e}"]

        lines = [f"## File: {file_path.relative_to(project_root)}"]
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                args = ", ".join(arg.arg for arg in node.args.args)
                lines.append(f"- def {node.name}({args}):")
            elif isinstance(node, ast.ClassDef):
                lines.append(f"- class {node.name}:")
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_args = ", ".join(arg.arg for arg in item.args.args)
                        lines.append(f"  - def {item.name}({method_args}):")
        return lines

    for dir_name in include_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists():
            for py_file in dir_path.rglob("*.py"):
                output_lines.extend(summarize_file(py_file))
                output_lines.append("")

    summary_path = project_root / "project_summary.md"
    summary_path.write_text("\n".join(output_lines))
    print(f"✅ Project summary written to {summary_path}")