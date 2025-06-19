import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "8d1b9a35017445d38d6d6c409f5827c2"

# URL of the file to transcribe
# FILE_URL = "https://github.com/AssemblyAI-Community/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

# You can also transcribe a local file by passing in a file path
FILE_URL = './voice_messages/AwACAgUAAxkBAAN0Zuc1vrrW9rFzTKu1OTPSW-vxrYEAAroOAAIriEBXnOjDZYRbl1Y2BA.wav'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)