
# Audio Streaming API

This is a FastAPI-based application that streams live audio using the PyAudio library. The API provides a single endpoint to access the audio stream.

## Enhancements Made

1. **Error Handling:** Added error handling for audio stream.
2. **Graceful Shutdown:** Ensured that the audio stream closes gracefully when the application stops.
3. **Configuration:** Added configurable parameters for audio settings.
4. **Documentation:** Enhanced documentation with detailed descriptions and instructions.

## Features

- **Live Audio Streaming:** Stream live audio data in real-time.
- **Configurable Audio Settings:** Adjust the audio format, channels, rate, and chunk size through configuration.
- **Graceful Shutdown:** Ensure resources are cleaned up when the application stops.

## Requirements

   ```bash
  sudo apt-get install portaudio19-dev
   ```
- Python 3.7+
- FastAPI
- PyAudio
- Uvicorn

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:sirajjunior540/audio-streaming-api.git
   cd audio-streaming-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. Access the audio stream at `http://localhost:8000/audio`.

## Configuration

You can adjust the audio settings by modifying the following variables in the `main.py` file:

- `FORMAT`: Audio format (default: `pyaudio.paInt16`)
- `CHANNELS`: Number of audio channels (default: `2`)
- `RATE`: Sampling rate (default: `44100`)
- `CHUNK`: Buffer size (default: `1024`)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)

---

This README provides a comprehensive guide to setting up and running the audio streaming application, including details on installation, configuration, and usage.