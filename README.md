# 🏋️ Google Workouts Tracker

A simple Python app that lets you **track workouts using plain English**.  
It integrates the [Nutritionix API](https://developer.nutritionix.com/) to calculate calories burned and the [Sheety API](https://sheety.co/) to log the results into a Google Sheet.  

You can explore the code on Replit and even fork it to run your own version with your own API keys.  

---

## 🚀 Features
- Enter workouts in **natural language** (e.g., *"ran 3 miles"*, *"30 minutes cycling"*).  
- Automatically logs:
  - Date  
  - Time  
  - Exercise name  
  - Duration  
  - Calories burned  
- Stores everything in a Google Sheet for easy tracking.  

---

## 📱 Try It on Replit
You can view and fork the project here:  
👉 [Google Workouts on Replit](https://replit.com/@tatendakasirori/Google-Workouts)

⚠️ Note:  
- If you just open the link, you can see the **code**.  
- To **run it**, you will need to **fork the project** into your own Replit account and set up your own API keys in the **Secrets Manager**.  
- Without your own API credentials, the program will not log workouts successfully.  

**Replit Fork Benefits:**  
- If you have a Replit account, you can **fork this code and run it directly** in the browser.  
- This allows **more versatile logging**, so you can track workouts even when running the app on your **mobile device**.  
- No local Python setup is needed — everything runs in the cloud.  

---

## ⚙️ Setup (Local Development)

### 1. Clone this repo
```bash
git clone https://github.com/tatendakasirori/Workout-Tracker.git
cd google-workouts
```
### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure environment variables
```ini
NU_APP_ID=your_nutritionix_app_id
NU_API_KEY=your_nutritionix_api_key
WEIGHT=70
HEIGHT=175
AGE=21
SH_URL=your_sheety_endpoint_url
AUTHORIZATION=your_sheety_auth_header
```
### 5. Run the app
```bash
python main.py
```
---
## 📊 How it works
- The app prompts:
```sql
Describe your exercise:
```
1. User enters their workout in natural language (e.g., "30 minutes cycling").
2. The app sends this info to the Nutritionix API to calculate duration and calories burned.
3. For each exercise, it sends a POST request to your Sheety endpoint, logging the workout with:
> - Date
> - Time
> - Exercise
> - Duration
> - Calories
- Status messages:
  ```bash
  Calculating values....... # when Nutritionix returns results
  Logged Successfully!!! # if Sheety logging is successful
  # HTTP status code otherwise
---
## 🛠️ Tech Stack
- Python 3
- Requests
- dotenv
- Nutritionix API
- Sheety API
- Replit (for cloud-based editing and sharing)
---
## 📌 Roadmap
- Add authentication for multiple users
- Build a front-end dashboard to visualize workout history
- Support more fitness metrics (heart rate, intensity, etc.)
---
📜 License
This project is open-source under the MIT License.
---
🙌 Acknowledgments
- Nutritionix for exercise/nutrition data
- Sheety for making Google Sheets act like a database
- Replit for easy cloud-based development
