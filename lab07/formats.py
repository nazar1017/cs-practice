import json


def csv_to_records(text: str) -> list[dict]:
    """CSV с заголовком -> список словарей; значения остаются строками."""
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    return [dict(zip(header, (v.strip() for v in line.split(",")))) for line in lines[1:]]


def _convert(value: str):
    value = value.strip()
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return value


def parse_settings(lines: list[str]) -> dict:
    """Учебный YAML: «ключ: значение», списки через «- », комментарии после #."""
    result = {}
    current_list = None
    for raw in lines:
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("- ") or stripped == "-":
            if current_list is not None:
                current_list.append(stripped[1:].strip())
            continue
        key, _, value = stripped.partition(":")
        key = key.strip()
        if value.strip() == "":
            current_list = []
            result[key] = current_list
        else:
            current_list = None
            result[key] = _convert(value)
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из справочника; поля записи важнее."""
    merged = []
    for row in rows:
        merged.append({**extra.get(row.get(key), {}), **row})
    return merged


def records_to_json(records: list[dict]) -> str:
    """Список словарей -> JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
