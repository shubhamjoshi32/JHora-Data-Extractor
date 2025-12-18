# 🪔 JHora Data Extractor

A simple Python utility that extracts birth data from multiple **`.jhd` (JHora)** files and exports them into a clean **CSV** file for further analysis.  
This tool provides a minimal **GUI interface** to select a folder, validates the files, and shows friendly messages using **Tkinter**.

---

## ✨ Features

- 🗂️ Select folder via GUI (no need to type paths)
- ✅ Automatically validates `.jhd` files only
- 📄 Extracts structured birth data and saves to a single CSV
- ⚡ Instantly extract details from *all* JHora files in one go — no need to open each `.jhd` manually!
- ⚠️ Displays warnings for invalid or missing folders/files
- 💾 CSV automatically saved to the selected folder
- 🔒 Graceful exit after completion
- ✅ **`JhoraDataExtractor.exe`** included for plug and play use.

---

## 🧠 How It Works

1. You select a folder that contains your `.jhd` files.  
2. The script checks and filters only valid `.jhd` files.  
3. Each file is read and parsed — data is cleaned and stored.  
4. A file named**`1Extracted_details.csv`** and **`1Extracted_details.Excel`** is created in the same folder.  
5. A popup confirms successful extraction with summary details.
6. You can directly use **`JhoraDataExtractor.exe`** `.exe` file directly on your system instead of setting up python and other libraries 

---

## 🛠️ Requirements
- No specific requiremnets to run **`JhoraDataExtractor.exe`** `.exe`
- **Python 3.8+**
- Modules:
  ```bash
  pip install tk
  ```

*(Note: `tkinter`, `os`, `csv`, and `sys` are part of the Python Standard Library — no extra installs usually required.)*

---

## 🚀 Usage

1. Save the script as `JhoraExtractor.py` or directly run **`JhoraDataExtractor.exe`**
2. Run it using: ( skip this step for **`JhoraDataExtractor.exe`** )
   ```bash
   python JhoraExtractor.py
   ```
3. Choose the folder containing your `.jhd` files when prompted.
4. Wait for the extraction to finish.
5. Check your selected folder for `1Extracted_details.csv`.

---

## 💡 Notes

- Non-`.jhd` files are automatically skipped.
- The script will warn and exit gracefully if no valid files are found.
- Works best on **Windows** (**`JhoraDataExtractor.exe`** included ), but compatible with **macOS** and **Linux** (minor GUI differences possible).

---

## 🧾 License

This project is released under the **MIT License** — free to use, modify, and distribute.

---

## 🙌 Credits

Developed with curiosity and precision by **Shubham Joshi** 🪷  
Made to make **JHora data extraction** faster, cleaner, and automated.

Special thanks to **P. V. R. Narasimha Rao**, the author of **[Jagannatha Hora](https://www.vedicastrologer.org/jh/)** —  
for creating this incredible and free software that empowers astrology enthusiasts and researchers worldwide.
