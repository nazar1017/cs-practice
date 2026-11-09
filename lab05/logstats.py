"""Статистика журнала событий. Ввода и печати здесь нет."""

LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line: str) -> dict:
    """«время уровень сообщение» -> словарь. Негодная строка — ValueError."""
    parts = line.strip().split(None, 2)
    if len(parts) != 3:
        raise ValueError(f"ожидалось 3 части: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"неизвестный уровень {level!r}: {line!r}")
    return {"time": time, "level": level, "message": message.strip()}
