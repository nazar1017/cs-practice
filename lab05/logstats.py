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


def _events(lines):
    """Перебирает строки, пропуская пустые; негодные отдаёт как None."""
    for line in lines:
        if not line.strip():
            continue
        try:
            yield parse_event(line)
        except ValueError:
            yield None


def count_levels(lines) -> dict:
    """Сколько строк каждого уровня; негодные — под ключом BROKEN."""
    counts = {}
    for event in _events(lines):
        key = "BROKEN" if event is None else event["level"]
        counts[key] = counts.get(key, 0) + 1
    return counts


def top_errors(lines, n: int) -> list:
    """n самых частых сообщений ERROR: [сообщение, число]; при равенстве — по алфавиту."""
    freq = {}
    for event in _events(lines):
        if event is not None and event["level"] == "ERROR":
            freq[event["message"]] = freq.get(event["message"], 0) + 1
    ordered = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return [[message, count] for message, count in ordered[:n]]
