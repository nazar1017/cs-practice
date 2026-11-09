def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Сколько файлов каждого расширения (в нижнем регистре, без точки)."""
    result = {}
    for path in paths:
        name = path.split("/")[-1].lstrip(".")  # скрытый файл .gitignore без расширения
        ext = name.rsplit(".", 1)[1].lower() if "." in name else ""
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    """Путь с наибольшим числом «/»; при равенстве — первый по алфавиту."""
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    """1536 -> «1.5 КБ»; байты — целым числом."""
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = float(n_bytes)
    units = ["КБ", "МБ", "ГБ", "ТБ"]
    unit = units[0]
    size /= 1024
    for unit in units:
        if size < 1024 or unit == units[-1]:
            break
        size /= 1024
    return f"{size:.1f} {unit}"
