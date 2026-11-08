"""Package the working copies of the two Python runtime packages."""

from pathlib import Path
import subprocess
import sys
import tarfile

project_dir = Path(sys.argv[1]).resolve()
app_dir = Path(__file__).resolve().parent / "esphome_mgm240"
metadata = {"LICENSE", "MANIFEST.in", "README.md", "pyproject.toml"}

with tarfile.open(app_dir / "sources.tar.gz", "w:gz", compresslevel=6) as archive:
    for repo, package, extra in (
        ("esphome", "esphome", {"requirements.txt", "requirements_dev.txt", "requirements_test.txt"}),
        ("device-builder", "esphome_device_builder", set()),
    ):
        checkout = project_dir / repo
        tracked = subprocess.check_output(["git", "-C", str(checkout), "ls-files", "-z"])
        new = subprocess.check_output(
            [
                "git", "-C", str(checkout), "ls-files", "-z", "--others",
                "--exclude-standard", "--", "esphome/components/efr32",
                "esphome/components/zephyr/build.py",
            ]
        ) if repo == "esphome" else b""
        for name in sorted(set((tracked + new).decode().split("\0")) - {""}):
            if name not in metadata | extra and not name.startswith(package + "/"):
                continue
            source = checkout / name
            if source.is_symlink():
                raise ValueError(f"Unexpected symlink: {source}")
            if source.is_file():
                archive.add(source, arcname=f"{repo}/{name}", recursive=False)
