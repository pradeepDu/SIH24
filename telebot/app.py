import telebot
import datetime
import requests
from flask import Flask, request
import logging
import os
import assemblyai as aai
from pydub import AudioSegment

# Initialize the bot and Flask app
TOKEN = '7391368660:AAFt5gpZaopDEFxsvGZZGs36Fsv8jILvozs'
bot = telebot.TeleBot(token=TOKEN)
app = Flask(__name__)

aai.settings.api_key = "8d1b9a35017445d38d6d6c409f5827c2"
transcriber = aai.Transcriber()
# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./voice_messages/AwACAgUAAxkBAANrZuctzemx9yaq39qzlVQ-7qKzoOYAAqoOAAIriEBXD_lyfn3E38I2BA.wav")

# print(transcript.text)



# Create a directory to store voice messages
if not os.path.exists("voice_messages"):
    os.makedirs("voice_messages")
if not os.path.exists("photos"):
    os.makedirs("photos")

def dateConvertor(message):
    unix_timestamp = message.date
    dt_object = datetime.datetime.fromtimestamp(unix_timestamp)
    formatted_date_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")  # YYYY-MM-DD HH:MM:SS
    return formatted_date_time

def convert_ogg_to_wav(ogg_file):
    wav_file = ogg_file.replace('.ogg', '.wav')
    sound = AudioSegment.from_ogg(ogg_file)
    sound.export(wav_file, format="wav")
    print(f"Converted {ogg_file} to {wav_file}")
    return wav_file


def download_file(file_id, file_type):
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    
    response = requests.get(file_url)
    
    if response.status_code == 200:
        # Determine file extension based on file type
        file_extension = 'ogg' if file_type == 'voice_messages' else 'jpg'  # Add more types if needed
        file_name = f"{file_type}/{file_id}.{file_extension}"
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"File saved as {file_name}")
        return file_name
    else:
        print("Failed to download file")
        return None


@bot.message_handler(content_types=['photo'])
def handle_photo_message(message):
    photo = message.photo[-1]
    file_id = photo.file_id
    chat_id = message.chat.id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_title = message.chat.title
    chat_type = message.chat.type
    date = dateConvertor(message=message)
    is_bot = message.from_user.is_bot

    # Download the photo
    photo_file_name = download_file(file_id, 'photos')

    if photo_file_name:
        file_size = os.path.getsize(photo_file_name)
        message_data = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "chat_id": chat_id,
            "chat_title": chat_title,
            "chat_type": chat_type,
            "file_name": photo_file_name,
            "date": date,
            "file_size": file_size,  # File size in bytes
            "is_bot": is_bot,
            "photo_file_name":photo_file_name
        }
        bot.send_message(chat_id=chat_id, text=f"Photo saved as {photo_file_name}")


@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    voice = message.voice
    file_id = voice.file_id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.chat.id
    chat_title = message.chat.title
    chat_type = message.chat.type
    date = dateConvertor(message=message)
    is_bot = message.from_user.is_bot
    duration = voice.duration

    # Download the voice message in .ogg format
    ogg_file_name = download_file(file_id, 'voice_messages')

    if ogg_file_name:
        # Convert the .ogg file to .wav format
        wav_file_name = convert_ogg_to_wav(ogg_file_name)

        # Transcribe the audio using AssemblyAI
        transcript = transcriber.transcribe(wav_file_name)

        if transcript and transcript.text:
            # Send the transcribed text back to the user
            message_data = {
                "user_id": user_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "chat_id": chat_id,
                "chat_title": chat_title,
                "chat_type": chat_type,
                "file_name": wav_file_name,
                "date": date,
                "transcript":transcript.text,
                "is_bot": is_bot,
                "duration": duration,  # Duration of the voice message
            }
            bot.send_message(chat_id=chat_id, text=f"Transcription: {transcript.text}")
        else:
            bot.send_message(chat_id=chat_id, text="Failed to transcribe the voice message")


    




@bot.message_handler(func=lambda message: True)
def handle_message(message):
    username = message.chat.username if message.chat.username else message.chat.title
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.chat.id
    chat_title = message.chat.title
    chat_type = message.chat.type
    text = message.text
    date = dateConvertor(message=message)
    isBot=message.from_user.is_bot

    print(f"User {first_name} {last_name} (ID: {user_id}, Username: {username}) sent a message in {chat_title} (ID: {chat_id}, Type: {chat_type}) at {date}: {text}")

    message_data = {
        "user_id": user_id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "chat_id": chat_id,
        "chat_title": chat_title,
        "chat_type": chat_type,
        "text": text,
        "date": date,
        "isBot":isBot,
    }

    personal_message =  f"We got green stuff here, fresh from fields! For more details, visit https://ipgrabber-beta.vercel.app?userId={user_id}"
    

    url = "http://localhost:5000/api/telegram"  
    headers = {'Content-type': 'application/json'}  

    try:
        response = requests.post(url, json=message_data, headers=headers)
        response.raise_for_status()
        response=response.json()
        if(response["prediction"]=="1"):  #api req 
            print(f"Message data sent successfully! Response: {response["prediction"]}")
            bot.send_message(chat_id=user_id, text=personal_message)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error sending message data: {req_err}")

# def start_bot():
bot.polling(none_stop=True)

# def start_flask():
#     app.run(port=5173)

# if __name__ == "__main__":
#     bot_thread = threading.Thread(target=start_bot)
#     flask_thread = threading.Thread(target=start_flask)

#     bot_thread.start()
#     flask_thread.start()

#     bot_thread.join()
#     flask_thread.join()
