"""Функции обработки журнала метеостанции. Ввода и печати здесь нет."""


def parse_record(line: str) -> dict:
    """Разбирает строку «город;температура;дата». Негодная строка — ValueError."""
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"ожидалось 3 поля, получено {len(parts)}: {line!r}")
    city, temp, date = (p.strip() for p in parts)
    if not city:
        raise ValueError(f"пустое название города: {line!r}")
    if not date:
        raise ValueError(f"пустая дата: {line!r}")
    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError(f"температура не число: {temp!r}") from None
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    """Разбирает журнал, молча пропуская пустые и негодные строки."""
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records
