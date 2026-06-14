# 🪐 Semantocosm

**"Type a thought, spawn a world."**

Semantocosm is a unique, never-before-seen AI product that translates abstract human thought into a tangible, procedural 3D environment. By analyzing the semantic and emotional weight of text, Semantocosm generates a unique miniature planet that reflects the "vibe" of your input.

![Semantocosm Concept](https://img.shields.io/badge/AI-NLP-blueviolet?style=for-the-badge)
![Three.js](https://img.shields.io/badge/3D-Three.js-black?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge)

## ✨ Features

- **Semantic-to-Spatial Mapping:** Uses Natural Language Processing (NLP) to map sentiment (polarity) and subjectivity to 3D procedural parameters.
- **Procedural Planet Generation:** Every world is generated on-the-fly using Simplex noise and custom vertex coloring.
- **Real-time 3D Exploration:** Rotate, zoom, and inspect your created world in a high-performance WebGL environment.
- **Dynamic Biomes:**
  - 🌿 **Lush Biomes:** Generated from positive, happy text.
  - 🌋 **Barren/Desolate Biomes:** Generated from negative or rigid text.
  - 🌏 **Temperate Biomes:** Generated from neutral or factual text.

## 🛠️ Technical Architecture

### Backend (Python/FastAPI)
- **NLP Engine:** Powered by `TextBlob`. It extracts sentiment polarity (-1 to 1) and subjectivity (0 to 1).
- **Parameter Engine:** Translates raw NLP metrics into terrain roughness, water levels, and color palettes.
- **FastAPI:** Provides a lightweight, high-speed API to serve the frontend and handle generation requests.

### Frontend (Three.js/JavaScript)
- **3D Rendering:** Uses `Three.js` for a high-fidelity WebGL experience.
- **Procedural Geometry:** Implements a sphere-deformation algorithm driven by noise to create mountains, valleys, and oceans.
- **Atmosphere & Visuals:** Includes a dynamic atmosphere glow that changes color based on the world's "mood."

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pkkarthik12/Semantocosm.git
   cd Semantocosm
   ```

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn textblob
   ```

3. **Download NLP Corpora:**
   ```bash
   python -m textblob.download_corpora lite
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

5. **Open your browser:**
   Navigate to `http://127.0.0.1:8000`

## 🎨 How to Use
Type anything in the input box—a dream, a diary entry, a technical description, or just a single word. Click **"SPAWN WORLD"** and watch the AI construct a 3D planet that represents the semantics of your text.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

