# ROT47 Challenge Decoder

A lightweight Python command-line utility for encoding and decoding text using the **ROT47 substitution cipher**.

Designed for CTFs, cybersecurity labs, cryptography exercises, and quick challenge-solving workflows.

---

## 🚀 Features

* 🔐 ROT47 encoding/decoding
* 💻 Interactive terminal mode
* ⚡ Command-line argument support
* 🔄 Piped input support
* 🧹 Quiet mode for clean output
* 🐍 Pure Python — no external dependencies
* 📦 Python 3 compatible
* 🔁 Same function can encode and decode

---

## 📋 Requirements

* Python 3.x

No third-party Python packages are required.

Check your Python installation:

```bash
python3 --version
```

---

## 📥 Installation

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
cd rot47
```

Make the script executable on Linux/macOS:

```bash
chmod +x rot47.py
```

---

## 💻 Usage

### 1. Interactive Mode

Run:

```bash
python3 rot47.py
```

You'll see:

```text
========================================================
                 ROT47 DECODER
========================================================
Enter a ROT47 string, then press Enter.
Press Ctrl+C to exit.

ROT47 >
```

Enter a ROT47 string:

```text
7=28Lx{@G6~776?D:G6$64FC:EJPN
```

Output:

```text
Decoded:
--------------------------------------------------------
flag{ILoveOffensiveSecurity!}
```

---

### 2. Command-Line Mode

Pass the encoded string directly:

```bash
python3 rot47.py "7=28Lx{@G6~776?D:G6$64FC:EJPN"
```

Output:

```text
Decoded:
--------------------------------------------------------
flag{ILoveOffensiveSecurity!}
```

> **Tip:** Quoting the input is recommended because characters such as `$`, `!`, `*`, and `&` can have special meanings in different shells.

---

### 3. Quiet Mode

Use `-q` or `--quiet` when you want only the decoded result:

```bash
python3 rot47.py --quiet "7=28Lx{@G6~776?D:G6$64FC:EJPN"
```

Output:

```text
flag{ILoveOffensiveSecurity!}
```

This is useful when piping the result into another command or script.

---

### 4. Pipe Input

The utility also accepts input through standard input:

```bash
echo '7=28Lx{@G6~776?D:G6$64FC:EJPN' | python3 rot47.py
```

For clean output:

```bash
echo '7=28Lx{@G6~776?D:G6$64FC:EJPN' | python3 rot47.py --quiet
```

---

## 🔐 How ROT47 Works

ROT47 operates on the **94 printable ASCII characters** ranging from:

```text
!   ASCII 33
```

to:

```text
~   ASCII 126
```

Each character is shifted by **47 positions**.

For example:

```text
7 → f
= → l
2 → a
8 → g
L → {
```

Therefore:

```text
7=28L
```

becomes:

```text
flag{
```

ROT47 works with:

* Numbers
* Uppercase letters
* Lowercase letters
* Symbols

---

## 🔄 ROT47 Is Reversible

ROT47 is symmetric.

Applying ROT47 twice returns the original text:

```text
ROT47(ROT47(text)) = text
```

This means the same `rot47()` function can be used for both encoding and decoding.

---

## 🧪 Example

### Encoded

```text
7=28Lx{@G6~776?D:G6$64FC:EJPN
```

### Decoded

```text
flag{ILoveOffensiveSecurity!}
```

---

## 📖 Command Reference

| Command                           | Description            |
| --------------------------------- | ---------------------- |
| `python3 rot47.py`                | Start interactive mode |
| `python3 rot47.py "TEXT"`         | Process supplied text  |
| `python3 rot47.py -q "TEXT"`      | Output result only     |
| `python3 rot47.py --quiet "TEXT"` | Output result only     |
| `echo "TEXT" \| python3 rot47.py` | Process piped input    |

---

## 📁 Project Structure

```text
rot47/
│
├── rot47.py
└── README.md
```

---

## 🛡️ Security & CTF Use

This tool is intended for legitimate educational and security-testing purposes, including:

* Capture The Flag (CTF) challenges
* Cybersecurity training
* Cryptography exercises
* Reverse-engineering practice
* Encoding/decoding exercises
* Security research labs

> **Note:** ROT47 is a substitution/encoding technique and is **not cryptographically secure**. It should never be used to protect passwords, credentials, keys, or other sensitive information.

---

## 📜 License

MIT License

---

## 👤 Author

**DMN SECURITY**

Cybersecurity | Offensive Security | Security Engineering

**GitHub:** `<https://github.com/DMN-Security>`

