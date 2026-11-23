"""读取项目使用的合成器材资料。"""
import json
from pathlib import Path


def load_records(path: Path) -> dict:
    source = Path(path)
    with source.open(encoding="utf-8") as stream:
        data = json.load(stream)
    if not isinstance(data, dict) or not isinstance(data.get("format_version"), int):
        raise ValueError("资料必须是带格式版本的对象")
    return data
