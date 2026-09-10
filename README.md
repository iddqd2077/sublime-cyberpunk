# Sublime Text — мои настройки

Личный репозиторий настроек Sublime Text 4: пакеты, горячие клавиши, системы сборки
для C++ и Python, цветовая схема и интерфейс.

## Что внутри

| Файл / папка | Что это |
|---|---|
| `Preferences.sublime-settings` | Основные настройки: тема, шрифт, автосохранение |
| `sublime-cyberpunk.sublime-color-scheme` | Кастомная схема по палитре темы Cyberpunk 2077 из VS Code |
| `Cyberpunk.sublime-theme` | Тема-оверрайд Adaptive: фон сайдбара = фон кода, цветные папки |
| `A File Icon.sublime-settings` | Иконки файлов в один цвет (акцент темы) |
| `Default (Windows).sublime-keymap` | Горячие клавиши (Terminus: `Ctrl+Alt+T`) |
| `C++ (MinGW).sublime-build` | Сборка C++ через `g++ -std=c++17` + запуск в Terminus |
| `Python.sublime-build` | Запуск Python + вариант `Check Syntax` |
| `Package Control.sublime-settings` | Список установленных пакетов |
| `sublime_bootstrap.py` | Плагин: при первом запуске доставляет все пакеты |

## Установленные пакеты

- **Terminus** — терминал прямо в Sublime (`Ctrl+Alt+T`)
- **SublimeLinter** + **SublimeLinter-cppcheck** — подсветка ошибок в C++
- **C++ Snippets**, **All Autocomplete** — автодополнение
- **GitGutter** — метки изменений напротив строк
- **auto-save** — автосохранение
- **A File Icon** — иконки файлов в боковой панели
- **BracketHighlighter** — подсветка парных скобок
- **SideBarEnhancements** — операции с файлами через ПКМ
- **MarkdownPreview** — просмотр `.md` в браузере
- **GitSavvy** — Git из редактора
- **SynthWave 84**, **Dank Neon** — дополнительные неоновые схемы (на выбор)
- **1337 / 3024 Color Scheme** — старые схемы

## Как восстановить на новой машине

1. Установи Sublime Text 4.
2. Установи **Package Control** (https://packagecontrol.io/installation).
3. Склонируй этот репозиторий в папку `Packages\User` Windows: `%APPDATA%\Sublime Text\Packages\User`
   ```powershell
   git clone https://github.com/iddqd2077/sublime-cyberpunk "$env:APPDATA\Sublime Text\Packages\User"
   ```
   Если папка не пустая — сначала сохрани оттуда свои файлы.
5. Перезапусти Sublime. Плагин `sublime_bootstrap.py` сам поставит все пакеты
   из списка `WANTED_PACKAGES` вместе с зависимостями.
6. Готово.

## Сборка кода

- **C++:** `Ctrl+B` — собрать и запустить. `Ctrl+Shift+B` — варианты `Build Only` / `Run Only`.
  Нужен `g++` в `PATH` (MinGW).
- **Python:** `Ctrl+B` — запуск. `Ctrl+Shift+B` → `Check Syntax`.
- **Терминал:** `Ctrl+Alt+T` — панель снизу, `Ctrl+Alt+Shift+T` — новая вкладка.

## Цветовая схема Sublime Cyberpunk

Палитра взята из темы `endormi/vscode-2077-theme` (VS Code) и перенесена в формат
Sublime `.sublime-color-scheme`. Основные цвета:

- фон `#030d22`, строки `#0ef3ff`, числа `#ffd400`
- ключевые слова `#ff2cf1`, константы `#ff2e97`, функции `#39c0ff`
- комментарии `#0098df` (курсив), курсор `#ff2cf1`

Тема интерфейса — `Cyberpunk.sublime-theme` (надстройка над `Adaptive`): фон
сайдбара совпадает с фоном кода, иконки папок — в цвет акцента.

## Патч грамматики C++ (std::cout)

Sublime по умолчанию не красит квалифицированные имена (`std::cout`, `std::endl`)
— это ограничение его грамматики C++. Патч находится **вне этого репозитория**:

    %APPDATA%\Sublime Text\Packages\C++\C++.sublime-syntax

Он добавляет scope для `std` (`entity.name.namespace`) и `cout` (`variable.other`).
Чтобы применить заново — скопируй `C++.sublime-syntax` из установленного пакета
`C++.sublime-package` и замени контекст `identifiers` (как в коммите).
