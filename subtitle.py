from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence


def extract_audio(video_path, output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path)

def subtitleFun(video_path):
    audio_file = "output_audio.wav"
    extract_audio(video_path, audio_file)


    sound = AudioSegment.from_wav(audio_file)
    chunks = split_on_silence(sound, min_silence_len=150, silence_thresh=-40)


    recognizer = sr.Recognizer()

    text_output = []
    for chunk in chunks:
        
        chunk.export("temp.wav", format="wav")
        with sr.AudioFile("temp.wav") as source:
            audio = recognizer.record(source)
            try:
                # Use recognizer to convert audio to text
                text = recognizer.recognize_google(audio)
                text_output.append(text)
                print(text)
            except sr.UnknownValueError:
                text_output.append(" ")
            except sr.RequestError as e:
                text_output.append(" ")

    from pydub.silence import detect_silence

    silence_data = detect_silence(
        sound,
        min_silence_len=150,  
        silence_thresh=-40,  
        seek_step=1, 
    )

    start = 0
    end = 0
    timestamp = []

    for time in silence_data:
        end = time[0]
        timestamp.append([start,end])
        start = time[1]

    

    def convert_to_srt(timestamps, texts):
        
        srt_content = ''
        for i in range(len(timestamps)):
            start_time = timestamps[i][0]
            end_time = timestamps[i][1]
            subtitle_text = texts[i]

            # Format the timestamps in HH:MM:SS,mmm (hours:minutes:seconds,milliseconds)
            start_time_str = '{:02d}:{:02d}:{:02d},{:03d}'.format(
                int(start_time / 3600000),
                int((start_time / 60000) % 60),
                int((start_time / 1000) % 60),
                int(start_time % 1000)
            )

            end_time_str = '{:02d}:{:02d}:{:02d},{:03d}'.format(
                int(end_time / 3600000),
                int((end_time / 60000) % 60),
                int((end_time / 1000) % 60),
                int(end_time % 1000)
            )

            # Create the subtitle block in SRT format
            srt_content += f"{i + 1}\n{start_time_str} --> {end_time_str}\n{subtitle_text}\n\n"

        return srt_content


    srt_content = convert_to_srt(timestamp, text_output)


    with open('output.srt', 'w') as file:
        file.write(srt_content)

    print("Done!")
    return text_output,timestamp