# Indian Kids Screen Time - EDA Project

This project explores patterns in screen time behavior among Indian children using a public dataset.

## 📊 Dataset
The dataset `Indian_Kids_Screen_Time.csv` contains columns like:
- Age
- Avg_Daily_Screen_Time_hr
- Primary_Device
- Urban_or_Rural
- Exceeded_Recommended_Limit
- Educational_to_Recreational_Ratio
- Health_Impacts

## 🛠️ Features
- Data preprocessing and handling of multi-label columns.
- Seaborn visualizations to explore relationships between device use, age, education vs recreation ratio, and health impacts.
- Output of all plots saved to `outputs/plots`.

## 🔧 Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/indian-kids-screen-time-eda.git
cd indian-kids-screen-time-eda

# Create environment
pip install -r requirements.txt

# Run the EDA script
python scripts/eda_screen_time.py
