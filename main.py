from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from textblob import TextBlob
import math

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class TextRequest(BaseModel):
    text: str

@app.post("/generate")
async def generate_planet(request: TextRequest):
    text = request.text
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    blob = TextBlob(text)
    sentiment = blob.sentiment # polarity, subjectivity
    
    # Polarity: -1.0 (very negative) to 1.0 (very positive)
    # Subjectivity: 0.0 (objective) to 1.0 (subjective)
    
    # Map NLP metrics to Planet Parameters
    
    # Roughness: High subjectivity -> more jagged/rough terrain
    roughness = 0.1 + (sentiment.subjectivity * 0.8)
    
    # Water Level: Positive sentiment -> more water/blue biomes
    # We'll map polarity -1..1 to waterLevel 0..1
    water_level = (sentiment.polarity + 1) / 2
    
    # Vegetation: Positive sentiment -> more green/lush
    vegetation_density = max(0, sentiment.polarity)
    
    # Complexity: Word count / Sentence length
    words = text.split()
    avg_word_length = sum(len(w) for w in words) / len(words) if words else 5
    complexity = min(1.0, avg_word_length / 10.0)
    
    # Palette Selection
    if sentiment.polarity > 0.3:
        palette = "Lush" # Greens, Blues, Yellows
    elif sentiment.polarity < -0.3:
        palette = "Barren" # Reds, Grays, Dark Purples
    else:
        palette = "Temperate" # Earthy tones
        
    return {
        "parameters": {
            "roughness": roughness,
            "waterLevel": water_level,
            "vegetationDensity": vegetation_density,
            "complexity": complexity,
            "palette": palette,
            "sentiment": {
                "polarity": sentiment.polarity,
                "subjectivity": sentiment.subjectivity
            }
        }
    }

@app.get("/")
async def read_index():
    from fastapi.responses import FileResponse
    return FileResponse('static/index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
