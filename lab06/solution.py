def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Сколько файлов каждого расширения (в нижнем регистре, без точки)."""
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        ext = name.rsplit(".", 1)[1].lower() if "." in name else ""
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    """Путь с наибольшим числом «/»; при равенстве — первый по алфавиту."""
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))
