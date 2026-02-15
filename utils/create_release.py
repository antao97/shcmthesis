#!/usr/bin/env python3

import pathlib
import zipfile
import os
import argparse
import subprocess
import glob
import logging
import re

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
)

FILE_GLOB_LIST = [
    # template files
    "LICENSE",
    "README.md",
    "README.pdf",
    "CHANGELOG.md",
    "shcmthesis.dtx",
    "shcmthesis.ins",
    "Makefile",
    "latexmkrc",
    "shcmthesis.cls",
    # example files
    "shcmthesis-example.tex",
    "shcmthesis-example.pdf",
    "shcmsetup.tex",
    "data/*.tex",
    "figures/*",
    # others
]


def generate_file_list():
    for g in FILE_GLOB_LIST:
        files = glob.glob(g)
        if len(files) == 0:
            raise FileNotFoundError(
                f"No file found for pattern '{g}', did you run `make all-dev` first?"
            )
        for f in files:
            yield f


def create_release_zip(version: str):
    dist_dir = pathlib.Path("dist")
    dist_dir.mkdir(exist_ok=True)
    release_zip = dist_dir / f"shcmthesis-{version}.zip"
    if release_zip.exists():
        logger.info(f"Release {release_zip} already exists, will overwrite")
    with zipfile.ZipFile(release_zip, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for f in generate_file_list():
            logger.debug(f"Adding to release zip: {f}")
            z.write(f)
    s = os.stat(release_zip)
    logger.info(f"Release {release_zip} created with size {s.st_size} bytes")


def get_latest_version_from_changelog():
    """从CHANGELOG.md中读取最新版本号"""
    changelog_path = pathlib.Path("CHANGELOG.md")
    if not changelog_path.exists():
        logger.warning("CHANGELOG.md not found, falling back to git tag")
        return None

    with open(changelog_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配格式：## [v1.2] - 2026-02-15，支持 v1.2、v1.2.3 等格式
    pattern = r'^\s*##\s*\[(v\d+(?:\.\d+)*)\]\s*-\s*\d{4}-\d{2}-\d{2}'
    match = re.search(pattern, content, re.MULTILINE)

    if match:
        latest_version = match.group(1)
        logger.info(f"Found latest version in CHANGELOG.md: {latest_version}")
        return latest_version
    else:
        logger.warning("No version found in CHANGELOG.md, falling back to git tag")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create release zip for shcmthesis")
    parser.add_argument("--version", required=False)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="只打印版本信息，不创建zip文件")
    args = parser.parse_args()

    if not args.version:
        # 优先从CHANGELOG.md读取最新版本号
        changelog_version = get_latest_version_from_changelog()
        if changelog_version:
            version = changelog_version
        else:
            # 回退到git tag
            version = (
                subprocess.check_output(["git", "describe", "--tags", "--always"])
                .strip()
                .decode("utf-8")
            )
    else:
        version = args.version

    if args.debug:
        logger.setLevel(logging.DEBUG)
    logger.info(f"Creating release zip for version {version}")
    if args.dry_run:
        logger.info("Dry run mode enabled, skipping zip creation")
    else:
        create_release_zip(version)
