# iithlp

**iithlp** is a Python package that converts text from various Indic scripts (Devanagari, Tamil, Telugu, Malayalam) into the **iithlp** Romanized format. This tool is designed for linguistic research, transliteration tasks, and script processing workflows.

## Features

- Supports **Devanagari**, **Tamil**, **Telugu**, and **Malayalam** scripts.
- Converts characters based on a predefined mapping to **iithlp** format.
- Provides both **Python API** and **Command-Line Interface (CLI)** for easy usage.
- Handles unmapped characters gracefully by passing them through unchanged.

---

## Installation

You can install **iithlp** directly from PyPI:

```bash
pip install iithlp
```

Alternatively, if you are developing or testing locally:

```bash
git clone https://github.com/yourusername/iithlp.git
cd iithlp
pip install .
```

---

## Usage

### 1. Using as a Python Library

You can import and use **iithlp** in your Python scripts.

```python
from iithlp.converter import convert_to_iithlp

# Example for Tamil text
tamil_text = "அஆஇஈ"
converted_text = convert_to_iithlp(tamil_text, 'tamil')
print(converted_text)  # Output: aAiI
```

### 2. Using from the Command Line

After installation, you can use the `iithlp` command from your terminal:

```bash
iithlp "அஆஇஈ" tamil
```

**Expected Output:**
```
aAiI
```

#### CLI Arguments:
- `text`: The input text you want to convert.
- `script`: The script of the input text. Supported values are: `devanagari`, `tamil`, `telugu`, `malayalam`.

---

## Supported Scripts & Examples

| Script      | Example Input | iithlp Output |
|-------------|---------------|---------------|
| Devanagari  | अआइई (अआइई)   | aAiI          |
| Tamil       | அஆஇஈ (அஆஇஈ) | aAiI          |
| Telugu      | అఆఇఈ (అఆఇఈ) | aAiI          |
| Malayalam   | അആഇഈ (അആഇഈ) | aAiI          |

---

## Development

If you'd like to contribute or modify the package:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/iithlp.git
    cd iithlp
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run tests:
    ```bash
    pytest
    ```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgements

This tool was developed to support transliteration and linguistic research efforts, making it easier to work with Indic scripts in a standardized Romanized format.

Special thanks to the **Department of Heritage Science and Technology (HST)** at **IIT Hyderabad (IITH)** for their support and guidance.

---

## Team

This project was created and maintained by the **IITH HST Department** team in collaboration with contributors from the open-source community.

---

## Contact

For questions, issues, or contributions, feel free to open an issue on [GitHub](https://github.com/theAutoBiography/iithlp) or contact **Ramanan Sivasubramanian** at **ramanan93@gmail.com**, **ht23mtech15007@iith.ac.in**.

