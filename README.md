# Jarvis
# Voice-Activated Assistant

A voice-activated assistant script that listens for an activation word ("computer") and responds to various commands. The assistant can execute shell scripts, open files, and interact with the terminal based on voice commands.

## Prerequisites

- Python 3.x
- SpeechRecognition library (`pip install SpeechRecognition`)
- Pyttsx3 library (`pip install pyttsx3`)

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/voice-activated-assistant.git
    cd voice-activated-assistant
    ```

2. Install dependencies:
    ```bash
    pip install SpeechRecognition pyttsx3
    sudo apt install portaudio19-dev
    sudo apt install python3-dev
    pip install pyaudio
    pip install espaek
    ```

3. Run the assistant:
    ```bash
    python assistant.py
    ```

4. The assistant will listen for the activation word ("computer") and respond to your voice commands.

## Features

- **Script Execution:** Run predefined shell scripts by voicing commands.
- **File Opening:** Open text files using voice commands.
- **Terminal Interaction:** Interact with the terminal and execute commands.
- **User Feedback:** The assistant provides verbal and printed feedback based on user commands.

## Customization

- **Adding Scripts:** Add your shell scripts to the `scripts` folder and extend the assistant to recognize additional script keywords.

## Troubleshooting

- If you encounter any issues with speech recognition, ensure that your microphone is working correctly and check for external noise.

## Contributors

- [Kevin Dunkley](https://github.com/RAuthentic)

## License

This project is licensed under the.
