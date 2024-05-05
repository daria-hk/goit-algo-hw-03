from pathlib import Path
import shutil
import argparse
import os

def copy_files(source_path: Path, destination_path: Path) -> None:
    try:
        if source_path.is_dir():
            for child in source_path.iterdir():
                if child.is_dir():
                    copy_files(child, destination_path)
                else:
                    subdir = os.path.join(destination_path, child.name)
                    os.makedirs(subdir, exist_ok=True)
                    shutil.copy(child, subdir)
    except FileNotFoundError:
        print("Source path doesn't exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy files')
    parser.add_argument('source', type=str, help='Source path')
    parser.add_argument('destination', type=str, default='dist', help='Destination path (default: dist)')
    args = parser.parse_args()
    print(args)
    source_path = Path(args.source)
    destination_path = Path(args.destination)

    copy_files(source_path,destination_path)