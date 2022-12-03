import gtts

tts = gtts.gTTS("Specifics", lang="en")

tts.save("tmp.mp3")


audio = open('/tmp/audio.mp3', 'rb')
tb.send_audio(chat_id, audio)
tb.send_audio(chat_id, "FILEID")
