# 🔐 Python Message Encryption & Decryption System

A **Python-based encryption tool** that allows users to send and receive messages securely using **two different custom encryption methods**.

---

## 📌 Overview

This program provides a **sender** and **receiver** mode, enabling users to:

- Encrypt a message using one of two available keys.
- Decrypt messages that were encrypted using the same system.
- Protect sensitive communication with custom symbol and number-based transformations.

---

## ✨ Features

### **Two Encryption Methods**

1. **Key1 Encryption**

   - Maps each character to a predefined numeric code.
   - Swaps every two adjacent numbers.
   - Adds a progressive numeric offset.
   - Wraps the message with start and end markers (`1` at both ends).

2. **Key2 Encryption**
   - Maps characters to numbers, then converts numbers into symbol pairs.
   - Reverses the entire encrypted symbol string.
   - Wraps the message with `<<` at the start and `>>` at the end.

### **Decryption**

- **Key1 Decryption**

  - Removes markers.
  - Reverses the numeric offset and swaps.
  - Converts numbers back to characters.

- **Key2 Decryption**
  - Removes boundary markers.
  - Reverses the string and converts symbol pairs to numbers.
  - Converts numbers back to original characters.

### **General Features**

- Handles unknown characters with `"?"`.
- Ensures encrypted messages are identifiable.
- Fully interactive CLI.

---

## 📥 Installation

No installation is required. Just download the `.py` file and run it.

---

## ▶ How to Run

1. Save the script as `encryption_system.py`
2. Open a terminal in the script’s directory.
3. Run:
   ```bash
   python MessageEncryption.py
   ```
