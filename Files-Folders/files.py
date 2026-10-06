import shutil
from pathlib import Path


def organize(source_dir):
    source_dir = Path(source_dir).expanduser().resolve()

    if not source_dir.exists():
        print(f"{source_dir} does not exist")
        return

    for file in source_dir.iterdir():
        if not file.is_file():
            continue

        extension = file.suffix.lower().lstrip(".") or "no extension"
        target_folder = source_dir / extension
        target_folder.mkdir(exist_ok=True)

        destination = target_folder / file.name
        if destination.exists():
            base_name = file.stem
            counter = 1
            while destination.exists():
                destination = target_folder / f"{base_name}_{counter}{file.suffix}"
                counter += 1

        shutil.move(str(file), str(destination))
        print(f"{file} moved to {destination}.")


if __name__ == "__main__":
    automate_dir = Path(__file__).resolve().parent / "raw data"
    organize(automate_dir)