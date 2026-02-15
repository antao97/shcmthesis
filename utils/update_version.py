#!/usr/bin/env python3

import pathlib
import re
import sys
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
)

def get_latest_version_from_changelog():
    """从CHANGELOG.md中读取最新版本号"""
    changelog_path = pathlib.Path("CHANGELOG.md")
    if not changelog_path.exists():
        logger.error("CHANGELOG.md not found")
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
        logger.error("No version found in CHANGELOG.md")
        return None

def update_file_version(file_path, version):
    """更新文件中的 \def\version{...} 定义"""
    # 移除版本号前的 'v' 前缀，因为 \version 定义中不使用 v 前缀
    version_num = version.lstrip('v')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 \def\version{1.0}（可能有空格）
    # 使用 re.escape 确保特殊字符被正确转义
    pattern = r'\\def\s*\\version\s*\{[^}]*\}'

    if re.search(pattern, content):
        new_content = re.sub(pattern, f'\\\\def\\\\version{{{version_num}}}', content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        logger.info(f"Updated version in {file_path} to {version_num}")
        return True
    else:
        logger.error(f"\\def\\version{{...}} not found in {file_path}")
        return False

def main():
    version = get_latest_version_from_changelog()
    if not version:
        logger.error("Failed to get version from CHANGELOG.md")
        sys.exit(1)

    # 需要更新的文件
    files_to_update = [
        pathlib.Path("shcmthesis.dtx"),
        pathlib.Path("shcmthesis.cls"),
    ]

    success = True
    for file_path in files_to_update:
        if not file_path.exists():
            logger.warning(f"File {file_path} does not exist, skipping")
            continue
        if not update_file_version(file_path, version):
            success = False

    if success:
        logger.info("Version updated successfully")
        # 重新生成 .cls 文件从 .dtx
        logger.info("Note: You may need to run 'make cls' to regenerate .cls from .dtx")
    else:
        logger.error("Failed to update version in some files")
        sys.exit(1)

if __name__ == "__main__":
    main()