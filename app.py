from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
import pyaudio

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    stream.stop_stream()
    stream.close()
    audio.terminate()

app = FastAPI(lifespan=lifespan)
# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

audio = pyaudio.PyAudio()
try:
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Could not open audio stream: {e}")


def generate_audio():
    try:
        while True:
            data = stream.read(CHUNK)
            yield data
    except Exception as e:
        stream.stop_stream()
        stream.close()
        audio.terminate()
        raise HTTPException(status_code=500, detail=f"Error streaming audio: {e}")


@app.get("/audio")
def audio_stream():
    return StreamingResponse(generate_audio(), media_type="audio/wav")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
