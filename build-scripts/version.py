#!/usr/bin/env python3
import re
import subprocess
import sys
from pathlib import Path
import configparser
import tomli
import tomli_w

def get_current_branch():
    """Получает имя текущей ветки Git."""
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

def check_version_changed(file_path):
    """Проверяет, была ли версия изменена вручную."""
    result = subprocess.run(
        ["git", "diff", "--cached", file_path],
        capture_output=True,
        text=True,
        check=True
    )
    diff = result.stdout

    # Ищем строки с version в дифе
    version_lines = re.findall(r'[-+]version\s*=\s*["\'].*?["\']', diff)
    return len(version_lines) > 0

def update_version(file_path):
    """Обновляет версию в pyproject.toml согласно правилам."""
    # Читаем файл pyproject.toml
    with open(file_path, "rb") as f:
        data = tomli.load(f)

    current_version = data.get("project", {}).get("version", "0.0.0")
    print(f"Текущая версия: {current_version}")

    # Определяем новую версию на основе текущей
    if re.search(r'dev(\d+)$', current_version):
        # Если версия заканчивается на dev<число>, инкрементируем номер
        new_version = re.sub(r'dev(\d+)$', lambda m: f"dev{int(m.group(1)) + 1}", current_version)
    elif re.search(r'post(\d+)$', current_version):
        # Если версия заканчивается на post<число>, инкрементируем номер
        new_version = re.sub(r'post(\d+)$', lambda m: f"post{int(m.group(1)) + 1}", current_version)
    else:
        # Если версия имеет вид x.x.x
        version_parts = current_version.split('.')
        if len(version_parts) >= 3:
            try:
                version_parts[-1] = str(int(version_parts[-1]) + 1)
                new_version = '.'.join(version_parts) + "-dev1"
            except ValueError:
                # Если последняя часть версии не числовая
                new_version = current_version + "-dev1"
        else:
            # Если версия не соответствует шаблону x.x.x
            new_version = current_version + "-dev1"

    print(f"Новая версия: {new_version}")

    # Обновляем версию в данных
    if "project" in data:
        data["project"]["version"] = new_version

    # Записываем обновленные данные обратно в файл
    with open(file_path, "wb") as f:
        tomli_w.dump(data, f)

    # Добавляем измененный файл в индекс Git
    subprocess.run(["git", "add", file_path], check=True)

    return True

def main():
    # Проверяем, что мы в ветке v2
    branch = get_current_branch()
    if branch != "v2":
        print(f"Текущая ветка: {branch}, не v2. Пропускаем обновление версии.")
        return 0

    # Путь к pyproject.toml
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("Файл pyproject.toml не найден.")
        return 1

    # Проверяем, не изменена ли версия вручную
    if check_version_changed(pyproject_path):
        print("Версия уже изменена вручную. Пропускаем автоматическое обновление.")
        return 0

    # Обновляем версию
    success = update_version(pyproject_path)
    if success:
        print("Версия успешно обновлена.")
        return 0
    else:
        print("Не удалось обновить версию.")
        return 1

if __name__ == "__main__":
    sys.exit(main())