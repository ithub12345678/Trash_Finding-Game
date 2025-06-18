# Trash_Finding-Game 🕹️	

**Find Trash in Indian Cities** is an interactive game where players explore random street view locations from top Indian cities and identify whether they see trash. It aims to raise awareness about urban cleanliness and the importance of keeping cities clean.

Cities included in this game:
- Delhi
- Mumbai
- Chandigarh
- Kolkata
- Chennai
- Pune
- Bangalore
- Patna

---

## **Table of Contents**
1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Setup Instructions](#setup-instructions)
4. [Environment Variables](#environment-variables)
5. [Google Maps Integration](#google-maps-integration)
6. [How It Works](#how-it-works)
7. [Future Enhancements](#future-enhancements)
8. [License](#license)

---

## **Features**
- 🌐 Explore random street views from India's top 8 cities.
- 🎯 Identify trash with simple "Yes" and "No" buttons.
- 🖥️ Rank the cities from 1-5 based on the trash found.
- 📝 Score points as you progress through 8 rounds.
- 🕹️ Retro game-inspired design with responsive UI.
- 🎥 End screen with a play again responsive button to restart the game.

---

## **Tech Stack**
- **Frontend**:
  - HTML, CSS (Retro Design)
  - JavaScript
  - Google Maps JavaScript API
- **Backend**:
  - Python
  - Flask
  - Google Street View API
- **Deployment**:
  - Heroku
  - GitHub for version control

---

## **Setup Instructions**

### Prerequisites
```
1. A Google Cloud Project with Maps API enabled.
```

### Clone the Repository
```bash
git clone https://github.com/your-username/trash-detection-game.git
cd trash-detection-game
```
### Create and Activate a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
### Install Dependencies
```
flask 
render_template
threading
request
Check for more in the 'requirements.txt' file.
```
### Notes
```
Ensure you have an active internet connection if you're using the Google Maps API for Street View.

You can add your API key inside the JS file or via Flask's environment variables if needed.

For deployment, consider using Render, Heroku, or Replit.
```
> Note: Update the localhost proxy address (http://127.0.0.1:5000) for running the proxy server locally.

Visit `(http://127.0.0.1:5000)` in your browser to access the game.

---

## **Environment Variables**

This project uses a `.env` file to securely store API keys. Create a `.env` file in the proxy server directory with the following keys:

```env
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
SIGNING_SECRET=your-google-digital-signature-key
```

> Note: The `GOOGLE_MAPS_API_KEY` should have HTTP referrer restrictions to secure it.

---

## Google Maps Integration
This project uses the Google Maps JavaScript API to display street views and allow users to find trash in real-world environments.

### API Setup
```
To use Google Maps in your local version of the game:

Go to the Google Cloud Console.

Create a new project and enable:

Maps JavaScript API

Street View Static API

Generate an API key.
```

In your game.html or JavaScript file, add your API key:

html
Copy
Edit
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initializeMap" async defer></script>
```
Never commit your API key to GitHub. You can use environment variables or a config.js file excluded in .gitignore.
```
### Live Features
```
Interactive street view.

Real map-based trash locating.

Zoom, drag, and explore via Google Street View.
```
---

## **How It Works**

1. The game fetches 8 random valid Street View locations using Google Maps and Street View APIs.
2. Players view the locations and decide if trash is visible by clicking **Yes** or **No**.
3. The player ranks the cities based on the trash found there.
4. This score is tracked across 8 rounds.
5. At the end, the game displays the player’s score along
6. This game is created to raise awareness of the demand for Cleaner Cities.

---

## **Future Enhancements**
- 📱 Make it more user-friendly by adding more user input in the game itself.
- 🔊 Enhance animations and add sound effects for an immersive experience.
- 🎮 Make an entirely new game inspired by the browser game called GeoGuessr from this template

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.
