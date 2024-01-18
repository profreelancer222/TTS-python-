import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert speech to text
def speech_to_text(audio_file_path):
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Record the audio file

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Specify the path to your audio file (replace 'your_audio_file.wav' with the actual file)

# Convert speech to text
result_text = speech_to_text('./polish_2.mp3')

# Print the result
print("Converted Text:", result_text)