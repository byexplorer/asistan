# This Python file uses the following encoding: utf-8
import os, sys
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import smtplib
import pyaudio
r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("anlayamadım")
        except sr.UnknownValueError:
            speak("sistem çalışmadı")
        return voice
def mailgönder(voice):
    if "e-posta gönder" in voice:
        mesaj = record("mesaj nedir")
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        speak("kullanıcı adını ve şifreni gir")
        a = str(input("kullanıcı adınız :"))
        b = str(input("şifreniz"))
        mail.login(a,b)
        c = input("gönderilecek adres :")
        mail.sendmail(a,c,mesaj)
        speak("gönderiliyorr")

def response(voice):
    if "nasılsın" in voice:
        speak("iyiyim sen nasılsın")
    if "arama yap" in voice:
        search = record("ne aramak istiyorsun")
        url = "www.youtube.com"+search
        webbrowser.get().open(url)
        speak(search+"Buyrun Efendim")


    if "ne haber" in voice:
        speak("iyiyim senden naber")
    if "teşekkür ederim" in voice:
        speak("İyi Günler Dilerim Efendim")
        
    if "saat kaç" in voice:

        speak(datetime.now().strftime("%H:%M"))

    if "Kendini kapat" in voice:
        speak("İyi Günler Dilerim Efendim")
        exit()

    if "Merhaba" in voice:
        speak("Merhaba efendim")
    if "terminal" in voice:
        search = record("açılıyor")
        url = "https://www.instagram.com"+search
        webbrowser.get().open(url)
        speak(search+"açılıyor")

    if "günaydın" in voice:
        speak("Günaydın efendim")
    if "Bugün Nasılsın" in voice:
        speak("İyiyim Efendim Siz Nasılsınız")
    if "Instagram" in voice:
        speak("hemen efendim")
        search = record("açılıyor")
        url = "https://www.instagram.com/"+search
        webbrowser.get().open(url)
        


    if "Selam" in voice:
        speak("Merhaba efendim")
    if "yemek yap" in voice:
        search = record("Error 404")
        url = "https://yemek.com/tarif/"+search
        webbrowser.get().open(url)
        speak(search+"Üzgünüm Efendim Ben Bir Yapay Zekayım Ama Sizin İçin Tarifler Önerebilirim")

    if "iltifat et" in voice:
        speak("tabiki")
    
        speak("Sen benim mucizemsin, mucizelere inanma sebebimsin Seni Seviyorum Saçlarının 1 teli olmak isterdim hep yanında kalmak için.")

    if "küfür et" in voice:
        speak("tabiki")
    
        speak("siktir git")


def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("Hoşgeldiniz ByExplorer ")
while 1:
   voice = record()
   print(voice)
   response(voice)
   mailgönder(voice)

   #ByExplorer
