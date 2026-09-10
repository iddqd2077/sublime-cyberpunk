"""
Bootstrap-установщик Sublime Text.

При каждом запуске:
  1. Копирует патч грамматики C++ (чтобы красился std::cout).
  2. Ставит все недостающие пакеты через Package Control.

Требует установленного Package Control.
"""

import os
import shutil

import sublime

WANTED_PACKAGES = [
    "1337 Color Scheme",
    "3024 Color Scheme",
    "A File Icon",
    "All Autocomplete",
    "auto-save",
    "BracketHighlighter",
    "C++ Snippets",
    "Dank Neon",
    "GitGutter",
    "GitSavvy",
    "MarkdownPreview",
    "SideBarEnhancements",
    "SublimeLinter",
    "SublimeLinter-cppcheck",
    "SynthWave 84 - Color Scheme",
    "Terminus",
]


def _is_installed(name):
    packages = sublime.packages_path()
    installed_packages = os.path.join(os.path.dirname(packages), "Installed Packages")
    packed = os.path.join(installed_packages, name + ".sublime-package")
    unpacked = os.path.join(packages, name)
    return os.path.exists(packed) or os.path.isdir(unpacked)


def _missing_packages():
    return [name for name in WANTED_PACKAGES if not _is_installed(name)]


def _copy_grammar_patch():
    src = os.path.join(
        sublime.packages_path(), "User", "grammar-patch", "C++.sublime-syntax"
    )
    dst_dir = os.path.join(sublime.packages_path(), "C++")
    dst = os.path.join(dst_dir, "C++.sublime-syntax")
    if not os.path.exists(src) or os.path.exists(dst):
        return
    try:
        os.makedirs(dst_dir, exist_ok=True)
        shutil.copyfile(src, dst)
        print("[bootstrap] C++ grammar patch applied")
    except OSError as exc:
        print("[bootstrap] grammar patch failed:", exc)


def plugin_loaded():
    _copy_grammar_patch()

    missing = _missing_packages()
    if not missing:
        return

    def install():
        try:
            sublime.run_command(
                "install_packages",
                {"packages": missing, "unattended": True},
            )
        except Exception as exc:
            print("[bootstrap] install failed:", exc)

    sublime.set_timeout(install, 3000)
