import os
import glob

# Get a list of all files in the folder
folder = os.getcwd()
files = glob.glob(folder + "/*")

# Count the number of MP3 and MP4 files in the list
mp3_files = [f for f in files if f.endswith(".mp3")]
mp4_files = [f for f in files if f.endswith(".mp4")]

if(len(mp3_files)>0):
    folder=os.getcwd()
    for file in glob.glob(os.path.join(folder, '*.mp3')):
        os.remove(file)
    
if(len(mp4_files)>0):
    folder=os.getcwd()
    for file in glob.glob(os.path.join(folder, '*.mp4')):
        os.remove(file)



flag=0
end=0
import streamlit as st
import os
st.title('Mashup:musical_note::musical_note::musical_note:')
st.write('Made by Nipun Garg')
name=st.text_input("Singer Name")
n=int(st.number_input("No. of videos",step=1))
duration=int(st.number_input("Duration",step=1))

Email=st.text_input("Email id")
if st.button('Submit'):
    
        from youtube_search import YoutubeSearch
        results = YoutubeSearch(name, max_results=n).to_dict()
        link=['https://www.youtube.com/'+results[i]['url_suffix'] for i in range(n)]
        print(link)
        from pytube import YouTube
        def Download(link):
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_lowest_resolution()
            try:
                youtubeObject.download()
            except:
                print("An error has occurred")
            print("Download is completed successfully")

        for i in range(0,n):    
            Download(link[i])


        directory = os.getcwd()


        files = os.listdir(directory)


        mp4_files = [file for file in files if file.endswith('.mp4')]

        for file in mp4_files:
            print(file)

        print(mp4_files)

        from moviepy.editor import VideoFileClip,AudioFileClip

        for i in range(0,len(mp4_files)):
            video = VideoFileClip(mp4_files[i])
            audio = video.audio
            audio.write_audiofile("audio_file"+str(i)+".mp3")

        #from pydub import AudioSegment

        import os

        directory = os.getcwd()

        files = os.listdir(directory)

        mp3_files = [file for file in files if file.endswith('.mp3')]

        for file in mp3_files:
            print(file)

        from moviepy.editor import *
        audio = AudioFileClip(mp3_files[0])

# Trim the audio file
        merged_audio = audio.subclip(0,0)
        

        for i in range(0,len(mp3_files)):
            audio = AudioFileClip(mp3_files[i])
            trimmed=audio.subclip(0,duration)
            merged_audio = concatenate_audioclips([merged_audio, trimmed])
#name1=sys.argv[4]
        merged_audio.write_audiofile("merged.mp3")
#merger.export( name1, format="mp3")
        import zipfile 
        def compress_mp3_to_zip(mp3_file_path, zip_file_path):
            with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                zip_file.write(mp3_file_path)

        compress_mp3_to_zip('merged.mp3', 'music.zip')
        flag=1
        folder=os.getcwd()
#         for file in glob.glob(os.path.join(folder, '*.mp4')):
#             os.remove(file)



if(flag==1):
        with open("music.zip", "rb") as fp:
    
            btn = st.download_button(
            label="Download ZIP",
            data=fp,
            file_name="merged.zip",
            mime="application/zip"
            )
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email.mime.text import MIMEText
        from email import encoders

        
# Email credentials
        from_email = "ngarg2k2testing@gmail.com"
        to_email = Email
        password = "cfhmoxuzbzlpexii"

# Email settings
        subject = "Zip file attached"
        zip_file_path = 'music.zip'

# Create message
        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject

# Attach zip file
        with open(zip_file_path, "rb") as f:
             part = MIMEBase("application", "octet-stream")
             part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition",
                f"attachment; filename={zip_file_path}")
        message.attach(part)

# Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(from_email, password)
            smtp.sendmail(from_email, to_email, message.as_string())
            st.write('File sent to', Email)
            end=1
# import glob

# folder = os.getcwd()
# if(end==1):
#     folder=os.getcwd()
#     for file in glob.glob(os.path.join(folder, '*.mp3')):
#         os.remove(file)
