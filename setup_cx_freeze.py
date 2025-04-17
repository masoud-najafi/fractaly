#python setup_cx_freeze.py build
#python setup_cx_freeze.py bdist_msi

from cx_Freeze import setup, Executable
import sys
import os

# Project metadata
project_name = "fractaly"
version = "0.2.0"
description = "A fractal visualization application"
author = "Masoud NAJAFI"
author_email = "your.email@example.com"

# Determine the base for the executable (Windows vs. Mac)
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for Windows GUI apps to prevent console window

# Include files (images, data, etc.)
include_files = [
    ("src/", "src/"),  # If you have asset files
    # Add other data files as needed
]

# Packages to include (cx_Freeze sometimes misses dependencies)
packages = [
    "wx","os","ctypes","sys","math","random","numpy","pathlib"
]

# Build options
build_options = {
    "packages": packages,
    "excludes": ["tkinter","pip"],  # Exclude unnecessary packages
    "include_files": include_files,
    "optimize": 2,
    # Binary includes (for special libraries)
    #"bin_includes": [    "libfreetype.so.6",     "zlib1.dll"     ],
    #"environment_variables":[("PATH", "lib/", "PREPEND")]  # Add lib/ to PATH 
    "path": sys.path + ["src"],
}

if sys.platform == "win32":
    build_options["include_msvcr"] = True  # Include Microsoft Visual C++ runtime


# Executable configuration
executables = [
    Executable(
        "src/fractaly/algorithm/core1.py", # Adjust to your main entry point
        base=base,
        target_name="fractaly",
        icon="src/fractaly/icons/mandel.png" if sys.platform == "win32" else None,
        shortcut_name=f"{project_name} {version}",
        shortcut_dir="ProgramMenuFolder",
    )
]

setup(
    name=project_name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    options={"build_exe": build_options},
    executables=executables,
)