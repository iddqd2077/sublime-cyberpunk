"""
Bootstrap-установщик пакетов Sublime Text.

При первом запуске просит Package Control поставить весь набор пакетов
вместе с зависимостями. Потом создаёт файл-маркер и больше не запускается.

Чтобы запустить установку заново — удали файл:
    Packages/User/.bootstrap-done
и перезапусти Sublime.
"""

import os

import sublime

WANTED_PACKAGES = [
    "A File Icon",
    "BracketHighlighter",
    "SideBarEnhancements",
    "MarkdownPreview",
    "GitSavvy",
    "SynthWave 84 - Color Scheme",
    "Dank Neon",
]

MARKER = os.path.join(sublime.packages_path(), "User", ".bootstrap-done")


def plugin_loaded():
    if os.path.exists(MARKER):
        return

    def install():
        try:
            sublime.run_command(
                "install_packages",
                {"packages": WANTED_PACKAGES, "unattended": True},
            )
        except Exception as exc:
            print("[bootstrap] install failed:", exc)
            return

        try:
            with open(MARKER, "w", encoding="utf-8") as handle:
                handle.write("ok\n")
        except OSError:
            pass

    sublime.set_timeout(install, 3000)
