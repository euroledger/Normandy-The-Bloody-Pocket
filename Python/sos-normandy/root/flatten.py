import os

def flatten_codebase(root_dir, output_file):
    # Folders to skip
    exclude_dirs = {'.git', '__pycache__', 'venv', 'node_modules', '.vscode', 'dist', 'build'}
    # File extensions to skip
    exclude_exts = {'.pyc', '.exe', '.bin', '.pdf', '.jpg', '.png', '.zip', '.lock'}

    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(root_dir):
            # Modifying dirs in-place to skip excluded folders
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if any(file.endswith(ext) for ext in exclude_exts):
                    continue
                
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, root_dir)
                
                # Add a clear header for each file
                f.write(f"\n{'='*60}\n")
                f.write(f"PATH: {rel_path}\n")
                f.write(f"{'='*60}\n\n")
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as code_file:
                        f.write(code_file.read())
                    f.write("\n")
                except Exception as e:
                    f.write(f"[Error reading file: {e}]\n")

if __name__ == "__main__":
    # Change '.' to your project folder path if running from elsewhere
    flatten_codebase('.', 'full_codebase_dump.txt')
    print("Done! Upload 'full_codebase_dump.txt' to ChatGPT.")
