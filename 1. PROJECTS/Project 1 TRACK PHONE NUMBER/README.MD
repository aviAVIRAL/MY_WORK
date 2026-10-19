# Phone Number Location Tracker 📍

A Python-based project that extracts geographic and telecom information from an international phone number and visualizes its approximate location on an interactive map.

## 📌 Project Overview

The **Phone Number Location Tracker** uses Python libraries and geocoding services to identify the region associated with a phone number, retrieve carrier information when available, and display the resulting geographic coordinates on an interactive map.

The project generates an HTML map that can be opened in a web browser.

## ✨ Features

- **Phone Number Parsing:** Parses international phone numbers using the `phonenumbers` library.
- **Location Identification:** Retrieves the country or region associated with the phone number.
- **Carrier Detection:** Identifies the mobile carrier when the information is available.
- **Geocoding:** Converts the identified region into approximate latitude and longitude coordinates using the OpenCage Geocoding API.
- **Interactive Map:** Creates a map using Folium and OpenStreetMap.
- **Location Marker:** Displays a marker with a popup showing the identified region.
- **HTML Export:** Saves the generated map as `GoogleMap.html` for viewing in a web browser.

## 🛠️ Technologies Used

| Technology             | Purpose                                           |
| ---------------------- | ------------------------------------------------- |
| Python                 | Core programming language                         |
| phonenumbers           | Phone number parsing and regional information     |
| OpenCage Geocoding API | Converts geographic descriptions into coordinates |
| Folium                 | Generates interactive maps                        |
| OpenStreetMap          | Provides map tiles and geographic visualization   |

## ⚙️ How It Works

1. The user enters an international phone number, including its country code.
2. The `phonenumbers` library parses the number.
3. The program identifies the associated geographic region.
4. The carrier name is retrieved when available.
5. OpenCage Geocoding converts the region name into latitude and longitude.
6. Folium creates an interactive map centered on the returned coordinates.
7. A marker is added to the map, and the output is saved as `GoogleMap.html`.

## 📂 Project Structure

```text
Phone-Number-Location-Tracker/
│
├── main.py
├── GoogleMap.html
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

**File descriptions:**

- `main.py` — Contains the Python application logic.
- `GoogleMap.html` — Generated interactive map.
- `requirements.txt` — Lists the Python dependencies.
- `.env` — Stores the OpenCage API key locally.
- `.gitignore` — Prevents sensitive and unnecessary files from being committed.
- `README.md` — Project documentation.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Phone-Number-Location-Tracker
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install phonenumbers folium opencage
```

Alternatively, create a `requirements.txt` file containing:

```text
phonenumbers
folium
opencage
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure the OpenCage API Key

Obtain an API key from [OpenCage Geocoding](https://opencagedata.com/).

Store the key in an environment variable named `OPENCAGE_API_KEY` rather than hardcoding it in your Python source code.

For Windows PowerShell:

```powershell
$env:OPENCAGE_API_KEY="_api_key_"
```

For macOS or Linux:

```bash
export OPENCAGE_API_KEY="_api_key_"
```

Update the Python code to read the environment variable:

```python
import os

Key = os.environ["api_key"]
```

Replace the existing hardcoded API key assignment with this code.

### 4. Run the Application

```bash
python main.py
```

Enter a phone number with its international country code when prompted.

Example input:

```text
+1417752671
```

The application will display the available regional and carrier information, retrieve coordinates, and generate the map.

### 5. View the Map

After successful execution, open `GoogleMap.html` in a web browser to view the interactive map.

An active internet connection is required to retrieve OpenStreetMap tiles.

## 🗺️ Sample Output

The generated map includes:

- An interactive geographic map.
- A marker at the approximate coordinates returned by the geocoding service.
- A popup displaying the identified region.
- Zoom and pan controls for exploring the map.

**Output file:** `GoogleMap.html`

## ⚠️ Limitations

- The application identifies an approximate geographic region associated with a phone number, not the phone's current physical location.
- It cannot track a person's real-time movements or access GPS coordinates.
- Carrier information may be unavailable or inaccurate, particularly for ported numbers or unsupported number types.
- Geocoding accuracy depends on the geographic description returned by the phone number library and the results provided by OpenCage.
- The OpenCage API is subject to its applicable usage limits, pricing, and service availability.
- The phone number must be provided in an appropriate international format.

## 🔒 Security and Privacy

- Never publish API keys, passwords, or other credentials in a public repository.
- Keep local environment files such as `.env` out of version control.
- Use phone number information responsibly and respect individual privacy.
- Do not use this project to attempt unauthorized tracking or identification.

Recommended `.gitignore` entries:

```gitignore
.env
__pycache__/
*.pyc
.venv/
venv/
```

## 🔮 Future Enhancements

- Add phone number validity and formatting checks.
- Improve error handling for invalid numbers and failed API requests.
- Add support for displaying additional geographic information.
- Build a simple web interface for entering phone numbers.
- Add configurable map zoom levels and map styles.
- Improve logging and API request handling.
