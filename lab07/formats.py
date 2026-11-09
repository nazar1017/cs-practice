import json


def csv_to_records(text: str) -> list[dict]:
    """CSV с заголовком -> список словарей; значения остаются строками."""
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = lines[0].split(",")
    return [dict(zip(header, line.split(","))) for line in lines[1:]]


def records_to_json(records: list[dict]) -> str:
    """Список словарей -> JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
