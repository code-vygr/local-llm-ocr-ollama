# 📘 **Local LLM OCR using Ollama (Free & Offline Image-to-Text Extraction)**

This project demonstrates **OCR (Optical Character Recognition)** using **locally running LLMs** via **Ollama** — completely **free**, **private**, and **offline**.
No API keys, no external calls, no cloud costs.

It works with any vision-enabled Ollama model such as:

* `qwen2.5vl:3b`
* `llava` models
* `moondream`
* any future Ollama models supporting image input

---

## 🚀 **Features**

* **100% free, offline OCR**
* Works with any **vision-enabled LLM in Ollama**
* Supports:

  * 🖼️ Local images
  * 🌐 Online image URLs (download → base64 → LLM)
* Preserves text order and completeness
* Easy to modify for structured JSON output
* Privacy-friendly: image never leaves your machine

---

## 🛠️ **Requirements**

* Python 3.8+
* Ollama installed locally
  👉 [https://ollama.com/download](https://ollama.com/download)
* A vision-capable model pulled in Ollama:

```bash
ollama pull qwen2.5vl:3b
# or any other vision-enabled model
```

Install Python dependencies:

```bash
pip install requests
```

(Ollama's Python client comes built into the package when Ollama is installed.)

---

## 📦 **Project Structure**

### ✔️ `image_to_base64(image_path)`

Converts any local image to a Base64 string.

### ✔️ `image_to_text_from_url(image_url)`

Downloads the image → converts to Base64 → sends to local LLM.

### ✔️ `image_to_text_from_base64(image_base64)`

Sends Base64 image directly to the LLM for OCR.

---

## 🧠 **Why Local LLM OCR?**

Traditional OCR tools struggle with:

* Small text
* Handwritten notes
* Blurry/low-quality images
* Mixed text layouts

LLM-based OCR:

* Understands context
* Reconstructs partial text
* Keeps reading order
* Works even on messy images

And with **Ollama**, you get all that **fully offline**.

---

## 🧪 **Usage Example**

### **Extract text from a local image**

```python
local_image_path = "image.jpg"
image_base64 = image_to_base64(local_image_path)

text = image_to_text_from_base64(image_base64)
print(text)
```

### **Extract text from an online image**

```python
image_url = "https://example.com/sample.jpg"
text = image_to_text_from_url(image_url)
print(text)
```

### **Save output to a text file**

```python
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
```

---

## 🔁 **Replace the Model Easily**

Change this:

```python
model="qwen2.5vl:3b"
```

To any Ollama vision model:

```python
model="llava:13b"
model="moondream:latest"
model="bakllava"
model="llama3.2-vision"
```

No other changes needed.

---

## 🧩 **Full Script Included**

This repository contains:

* Local image → OCR
* URL image → OCR
* Base64 utilities
* Text saving to `.txt`

Everything ready to use out of the box.

---

## 🎯 **Use Cases**

* Extract text from scanned documents
* Read PDFs (after converting PDF → image)
* OCR for receipts & invoices
* Handwritten note transcription
* Desktop automation
* Data extraction & cleanup

---

## 🤝 Contributing

Pull requests are welcome!
You can extend this to:

* OCR → JSON structuring
* Multi-image batch processing
* CLI tool
* GUI for drag-and-drop OCR

---

## 📄 License

MIT License — free for personal & commercial use.
