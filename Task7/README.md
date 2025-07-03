# 🖼️ Task 07 – Image Resizer Tool

## 📌 Objective
Resize and convert images in bulk using Python and Pillow. This tool helps you reduce image sizes by a scale factor (1–10) and optionally convert formats.

---

## 🚀 Features
- Resize all images in a folder using a divisor (e.g., 2 → half size, 3 → one-third size)
- Converts images to a chosen format (e.g., PNG by default)
- Automatically creates output folder if not present
- Works with JPG, PNG, and other formats
- Lightweight and beginner-friendly script

---

## 🛠 Tech Stack
- Python 3.x
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- OS module

---

## 📁 Folder Structure
```
task-07-image-resizer/
├── images/           # Input images (put your original files here)
├── output/           # Output resized images (auto-generated)
├── resizer.py        # Python script to resize images
└── README.md         # This file
```

---

## ⚙️ How to Run

### 1. 📦 Install Dependencies
```bash
pip install pillow
```

### 2. 🖼️ Add images
Place your images in the `images/` folder. Supported formats: `.jpg`, `.png`, `.webp`, etc.

### 3. ▶️ Run the Script
```bash
python resizer.py
```

You will be prompted:
```
Enter reduction factor (1–10):
```

For example:
- `2` → reduces image size by half
- `4` → reduces to one-fourth
- `10` → reduces to 1/10th

---

---

## 🧠 Interview Prep – Key Concepts

1. What is PIL/Pillow?
2. How do you open and save images?
3. How does the `resize()` method work?
4. How to list all files in a directory using `os.listdir()`?
5. How to convert image formats?
6. What is a pixel?
7. Why use `try-except` while opening images?
8. Can this be extended to a GUI or web app?

---

## ✅ Deliverables
- `resizer.py` script
- Input images (in `/images`)
- Output images (auto-created in `/output`)
- Screenshots (if required)
- `README.md`

---



