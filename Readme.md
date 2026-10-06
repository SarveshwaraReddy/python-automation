# Python Automation

This project will grow through the following topics, in order:

1. [completed] **Files** — Organize files and folders with Python.
2. [ ] **APIs** — Request data from web APIs.
3. [ ] **JSON and data processing** — Read, transform, and save structured data.
4. [ ] **SQL** — Store and query data in a database.
5. [ ] **Scheduling** — Run automation on a schedule.
6. [ ] **Logging** — Record actions, progress, and errors.
7. [ ] **Testing** — Verify behavior with automated tests.
8. [ ] **Celery** — Run background tasks asynchronously.
9. [ ] **Docker** — Package and run the application in containers.
10. [ ] **CI/CD** — Automate checks and delivery.

## Sections

### Files
Describe the file-organizing automation, how to run it, and its behavior.

### APIs
Document the API used, request details, and how responses are handled.

### JSON and data processing
Explain the input and output data formats and any transformations.

### SQL
Describe the database, schema, and queries used.

### Scheduling
Explain how and when scheduled automation runs.

### Logging
Document where logs are written and what they record.

### Testing
List how to run the tests and what behavior they cover.

### Celery
Describe the background tasks and how to start the worker.

### Docker
Document how to build and run the container.

### CI/CD
Explain the automated checks and deployment workflow.



## File organizer

The script is [files.py](./Files-Folders/files.py). By default, it organizes files in the `Files-Folders/raw data` directory, relative to the script's location.

For example, files such as `notes.txt`, `photo.jpg`, and `report.pdf` are moved into:

```text
Files-Folders/
└── raw data/
    ├── txt/
    │   └── notes.txt
    ├── jpg/
    │   └── photo.jpg
    └── pdf/
        └── report.pdf
```

Files without an extension are placed in a folder named `no extension`.

## Requirements

- Python 3

## Run

From the project root, run:

```powershell
python .\Files-Folders\files.py
```

The script can also be run directly from the `Files-Folders` directory:

```powershell
python .\files.py
```

## Behavior and notes

- Only files directly inside `raw data` are organized; subdirectories are skipped.
- Extension names are converted to lowercase.
- Existing files are moved into their extension folders. If a destination filename already exists, the moved file is given a numbered name rather than overwriting that file.
- The operation moves files, so make a backup before running it on important data.
- To organize a different directory, call `organize()` with that directory path in `files.py`.