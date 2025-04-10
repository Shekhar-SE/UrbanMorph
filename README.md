UrbanMorph: AI-based Urban Growth Visualizer
UrbanMorph is a lightweight AI-driven project that detects and predicts urbanization patterns using satellite images of your city over the last 15 years (2010–2024).
It visualizes changes and forecasts future growth to assist in thoughtful city planning — all on a modest laptop (no GPU required!).

How It Works :
Accepts yearly satellite images (e.g., from Google Earth).

Computes change maps using image difference techniques.

Plots urban growth trends.

Predicts future changes using linear regression.

Project Structure :

UrbanMorph_Project/
├── data/
│   ├── raw_images/           # Year-wise folders (2010, 2011, ..., 2024)
│   └── processed_images/     # (optional for future enhancements)
├── notebooks/
│   └── urban_morph.py        # Main analysis script
├── outputs/
│   ├── visualizations/       # Yearly change maps
│   └── predictions/          # Growth trend plots
├── models/                   # (Reserved for future ML models)
├── utils/                    # (For helper functions)
└── README.md

 Requirements :
 Install Python dependencies: pip install -r requirements.txt

 Run the Script :
 cd notebooks
 python urban_morph.py

 Sample Output :
 change_map_2010_2011.png (visual diff between years)
 urban_change_trend.png (line graph of yearly changes)
 Terminal output with predicted urbanization for 2025, 2030, and 2035.

 Why UrbanMorph? :
 Works with low-end hardware
 No deep learning, just innovative engineering
 Encourages data-driven urban planning
 Ideal for Tier-3 cities aiming for 2047 vision 

 To-Do (Future Scope) :
 Add better vegetation detection to reduce false positives (e.g., due to crop harvesting)
 Improve prediction using more advanced models (Random Forest, LSTM, etc.)
 Support different regions and map overlays

 Acknowledgments :
 Created by Satyam Shekhar (@Shekhar-SE) — inspired by the dream of transforming his hometown into a model smart city.
 
 Thank you.
