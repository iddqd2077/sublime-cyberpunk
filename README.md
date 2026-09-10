# Моя сборка Sublime Text

Это моя личная сборка Sublime Text 4. Сохранена тут на всякий случай —
чтобы в любой момент восстановить всё (тема, пакеты, хоткеи, сборки) на любой машине.

Ниже — инструкция: как восстановить и как всем этим пользоваться.

---

## Как восстановить на новой машине

1. Установи Sublime Text 4.
2. Установи **Package Control**: https://packagecontrol.io/installation
3. Склонируй репозиторий в папку `Packages\User`:
   ```powershell
   git clone https://github.com/iddqd2077/sublime-cyberpunk "$env:APPDATA\Sublime Text\Packages\User"
   ```
   (если папка не пустая — сначала сохрани из неё свои файлы)
4. Перезапусти Sublime → плагин `sublime_bootstrap.py` сам поставит все пакеты и патч грамматики.
5. Перезапусти ещё раз → патч грамматики C++ подхватится.

### Бинарники, которые нужно поставить отдельно

| Инструмент | Зачем | Команда установки |
|---|---|---|
| MinGW (g++) | компилятор C++ | установщик MinGW-w64 |
| clangd (LLVM) | C++ сервер автодополнения | `winget install LLVM.LLVM` |
| pyright | Python сервер | `npm i -g pyright` |
| flake8 | Python линтер | `pip install flake8` |

---

## Как писать и запускать код

### C++

1. Файл `main.cpp`:
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```
2. **`Ctrl+B`** — собрать и запустить. **`Ctrl+Shift+B`** — варианты (`Build Only` / `Run Only`).

### Python

1. Файл `main.py` → **`Ctrl+B`** — запуск. `Ctrl+Shift+B` → `Check Syntax`.

### Терминал

**`Ctrl+Alt+T`** — панель снизу, `Ctrl+Alt+Shift+T` — вкладка. Жёлтый текст на тёмном фоне.

---

## Языковые серверы (LSP) — автодополнение и ошибки на лету

Открой `.cpp` или `.py` — внизу справа появится имя сервера (`clangd` / `pyright`).
Если нет: `Ctrl+Shift+P` → `LSP: Enable Language Server In Project`.

| Клавиша | Действие |
|---|---|
| `F12` | перейти к определению |
| `F2` | переименовать |
| `Shift+F12` | найти использования |
| `Ctrl+Alt+M` | панель ошибок |
| `Ctrl+Alt+Space` | подсказка параметров функции |

Остальное — `Ctrl+Shift+P` → набери `LSP:`.

---

## Пакеты: что делает каждый

### Линтеры (подчёркивают ошибки)
- **SublimeLinter** + **cppcheck** — ошибки в C++ на лету.
- **Python Flake8 Lint** — стиль и ошибки в Python.

### Git
- **GitGutter** — полоски слева: что изменено/добавлено/удалено.
- **GitSavvy** — git-интерфейс: `Ctrl+Shift+P` → `GitSavvy: Status`.

### Сборка
- **CMake** — подсветка `CMakeLists.txt`.
- **CMakeBuilder** — сборка многофайловых CMake-проектов (`Ctrl+B` в папке проекта).

### Удобства
- **Terminus** — терминал.
- **A File Icon** — иконки файлов (циан), папки (розовый).
- **BracketHighlighter** — подсветка парных скобок.
- **SideBarEnhancements** — ПКМ по файлу: rename, delete, copy path.
- **MarkdownPreview** — предпросмотр `.md`.
- **All Autocomplete** / **C++ Snippets** — базовое автодополнение и сниппеты.
- **auto-save** — автосохранение.

---

## Цветовая схема

Основная — **sublime-cyberpunk** (палитра из темы Cyberpunk 2077 для VS Code):
фон `#030d22`, строки циан, числа жёлтые, ключевые слова магента, функции синие.

Сменить: `Ctrl+Shift+P` → `UI: Select Color Scheme` (есть SynthWave 84, Dank Neon и др.).

---

## GitHub

| Команда | Что делает |
|---|---|
| `git status` | что изменилось |
| `git add -A` | добавить всё |
| `git commit -m "текст"` | зафиксировать |
| `git push` | отправить |
| `git pull --rebase` | забрать правки |

Правило: не правь один файл в двух местах (Sublime + сайт GitHub) — будет конфликт.
