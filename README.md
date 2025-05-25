# Pdf Reverser

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

**Pdf Reverser** is a simple utility tool that takes a PDF file and generates a mirrored version of it.  
This can be useful for printing, design adjustments, or specific reading/viewing needs.

<!-- > *(Add more details here if needed—how pages are mirrored, if text is reversed, etc.)* -->

---

## Getting Started <a name = "getting_started"></a>

These instructions will help you set up **Pdf Reverser** on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python installed (recommended: Python 3.10 or higher).

Install required libraries listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
````

> *(If you're using a virtual environment, activate it before installing.)*
> *(If you remember specific required libraries like `PyPDF2` or `reportlab`, list them in `requirements.txt`.)*

---

### Installing

Clone the repository:

```bash
git clone <your-repository-url>
cd <project-directory>
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Build the project using PyInstaller:

```bash
pyinstaller --onefile ^
  --noconsole ^
  --clean ^
  --distpath "./PdfReverser_Release" ^
  main.py
```

> 📝 **Note:** Make sure `main.py` is the entry point of the app.
> *(Add any missing files, assets, or configuration if needed.)*

---

## Usage <a name = "usage"></a>

After building, the final executable will be located in the `PdfReverser_Release` folder.

Example usage:

```bash
PdfReverser_Release\main.exe
```

> *(Add instructions here: how to select the PDF, if there's a GUI, CLI arguments, etc.)*

<!-- ---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines.

```

Let me know if you want to generate all your READMEs automatically in one folder, or want help writing the `requirements.txt` for this tool.
``` -->
