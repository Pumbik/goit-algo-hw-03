import argparse
from pathlib import Path
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Copy files recursively and sort by extension.")
    
    parser.add_argument('--source', type=str, required=True, help='Source directory to copy files from')
    parser.add_argument('--output', type=str, default="dist", help='Output directory to copy files to')
    
    return parser.parse_args()

def read_folder(path: Path, output: Path):
    try:
        for element in path.iterdir():
            if element.is_dir():
                read_folder(element, output)
            elif element.is_file():
                ext = element.suffix[1:] if element.suffix else 'others'
                target_folder = output / ext
                target_folder.mkdir(parents=True, exist_ok=True)

                target_file = target_folder / element.name
                shutil.copyfile(element, target_file)
                
                print(f"Скопійовано: {element.name} -> {target_folder}")
                
    except OSError as e:
        print(f"Помилка доступу до {path}: {e}")


def main():
    args = parse_args()
    
    source = Path(args.source)
    output = Path(args.output)

    print(f"Копіюємо з: {source}")
    print(f"Копіюємо в: {output}")

    read_folder(source, output)

if __name__ == "__main__":
    main()