import pyaudio
import numpy as np
import keyboard
import time

# PyAudio setup
p = pyaudio.PyAudio()
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
card = True  # Set to True to enable data saving

# Recording data
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

recording = False
frames = []
header_count = 0  # Counter for the headers

def start_recording():
    global recording, header_count
    recording = True
    header_count += 1  # Increment the header count
    print(f"Recording... (Header {header_count})")

def stop_recording():
    global recording
    recording = False
    print("Finished recording.")

print("Press 'x' to start recording and 'y' to stop recording.")

try:
    while True:
        if keyboard.is_pressed('x') and not recording:
            start_recording()
            frames = []

        elif keyboard.is_pressed('y') and recording:
            stop_recording()
            # Convert frames to numpy array
            audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

            # Apply FFT
            fft_result = np.fft.fft(audio_data)
            magnitude = np.abs(fft_result)

            # Normalize magnitude to 0-255 range
            normalized_magnitude = (magnitude / np.max(magnitude) * 4095).astype(int)

            # Save data to the CSV file with the corresponding header number
            file_path = f'C:\\Users\\GTR\\Desktop\\2\\Data_Header_{header_count}.txt'
            np.savetxt(file_path, normalized_magnitude, fmt="%d", delimiter=',')
            print(f"Data appended to {file_path}")

        if recording:
            data = stream.read(CHUNK)
            frames.append(data)

        time.sleep(0.01)  # Add a small delay to reduce CPU usage

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    # Ensure to stop the stream and terminate PyAudio when done
    stream.stop_stream()
    stream.close()
    p.terminate()
