# VtubeStudio_Connector

A Python connector for controlling VTube Studio parameters (like mouth movement) in sync with text-to-speech audio.  
This project demonstrates how to animate a VTube Studio model's mouth while speaking using `pyttsx3` for TTS and `pyvts` for VTube Studio API communication.

---

## Features

- Connects to VTube Studio via WebSocket API
- Registers custom parameters (e.g., mouth open, eye blink)
- Animates mouth movement while speaking
- Uses `pyttsx3` for offline text-to-speech
- Asynchronous, non-blocking animation and speech

---

## Requirements

- Python 3.8+
- VTube Studio (running and API enabled)
- [pyvts](https://github.com/DenchiSoft/VTubeStudioAPI)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- numpy

Install dependencies:
```sh
pip install pyvts pyttsx3 numpy
```

---

## Usage

1. **Start VTube Studio** and enable the API.
2. **Clone this repository** and navigate to the folder.
3. **Run the script:**
    ```sh
    python main.py
    ```
4. The script will connect to VTube Studio, register parameters, and animate the mouth while speaking the test message.

---

## Customization

- **Change the spoken message:**  
  Edit the string in `await connector.speak("...")` in `main.py`.
- **Add more parameters:**  
  Modify the `params` dictionary in `main.py` to register more custom parameters.

---

## File Overview

- `main.py` — Main script for connecting, registering parameters, and running the mouth animation with TTS.
- `token.txt` — (Optional) Stores the VTube Studio API authentication token.

---

## Credits

- [VTube Studio API](https://github.com/DenchiSoft/VTubeStudioAPI)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
-