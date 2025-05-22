![O6U Color Exchange Logo](https://raw.githubusercontent.com/abanoubnour98/o6u-color-excahnge/refs/heads/main/static/logo.png)

# 🎨 O6U Color Exchange

Welcome to **O6U Color Exchange** – a basic full-stack web application developed to detect and preview dominant colors from uploaded images. This project combines backend logic using **Flask** and image processing with **Pillow**, along with a smooth frontend experience using **HTML, CSS, and JavaScript**.

Developed by **Abanoub Abdelnour** as a showcase of web development, image manipulation, and UI integration.

---

## 🚀 Features

- 🖼️ **Image Upload**: Upload any image to extract and display its dominant color in **hexadecimal format**.
- 🎨 **Color Preview**: Input any hex code to visualize its corresponding color dynamically.
- 💾 **Local Save**: Automatically saves uploaded images locally for further processing or reference.

---

## 🛠️ Technologies Used

### 💻 Frontend
- **HTML5** – Semantic and accessible layout  
- **CSS3** – Responsive styling and layout  
- **JavaScript** – DOM manipulation and dynamic color updates (`updateColorPreview()`)

### 🧠 Backend
- **Python (Flask)** – Web framework handling server-side logic  
- **Pillow (PIL)** – Python Imaging Library used to process uploaded images  
  - `get_dominant_color(img)` – Extracts dominant hex color
  - `save_image(image)` – Saves images locally

---

## 📦 Installation

> To run the project locally:

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/o6u-color-exchange.git
   cd o6u-color-exchange
