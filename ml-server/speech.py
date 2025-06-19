import speech_recognition as sr
from pydub import AudioSegment
from datetime import datetime
import os

def convert_ogg_to_wav(ogg_file_path):
    """Convert an OGG file to WAV format."""
    wav_file_path = ogg_file_path.rsplit('.', 1)[0] + '.wav'  # Change the file extension to .wav
    audio = AudioSegment.from_ogg(ogg_file_path)
    audio.export(wav_file_path, format="wav")
    return wav_file_path

def record_text_from_file(audio_file_path):
    """Transcribe text from a WAV audio file."""
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            print("Processing audio file...")
            audio = r.record(source)
            print("Recognizing...")
            MyText = r.recognize_google(audio)
            print(f"Recognized Text: {MyText}")  # Ensure the text is captured
            return MyText
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except ValueError as e:
        print(f"ValueError: {e}")
    return None

def output_text(text):
    """Write the transcribed text to a file with date and time."""
    if text:  # Ensure text is not None or empty
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        formatted_text = f"[{date_time}] {text}"
        print(f"Writing to file: {formatted_text}")  # Print to confirm the text being written
        with open("output.txt", "a") as f:
            f.write(formatted_text + '\n')  # Write the recognized text with date and time to the file with a newline
    else:
        print("No text to write.")

# Path to your OGG file
ogg_file_path = r"bruh.ogg"  # Update this to the path of your OGG file

# Convert OGG to WAV
wav_file_path = convert_ogg_to_wav(ogg_file_path)

# Process the WAV file
text = record_text_from_file(wav_file_path)  # Capture text from audio file
output_text(text)  # Write the recognized text with date and time to the file

# Optionally, delete the temporary WAV file after processing
os.remove(wav_file_path)

print('Processing complete.\n')
