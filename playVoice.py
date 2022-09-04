import pyaudio
import wave
import time
import threading
import sys
import os
from pynput import keyboard


filePath = ""
device = 0
playing = ""
importedVoices = {}


def initDevice():
    global device

    p = pyaudio.PyAudio()
    # choose VoiceMeeter Input device
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    if len(sys.argv) == 2:
        if sys.argv[1] == "-c":
            print("请输入输出设备：")
            for i in range(0, numdevices):
                if p.get_device_info_by_index(i)["maxOutputChannels"] > 0:
                    print(str(p.get_device_info_by_index(i)["index"]) +
                          "\t" + p.get_device_info_by_index(i)["name"])

            del p
            device = int(input())
        else:
            print("参数错误")
            sys.exit(0)
    else:
        for i in range(0, numdevices):
            if p.get_device_info_by_index(i)["maxOutputChannels"] > 0 and "VoiceMeeter Input" in p.get_device_info_by_index(i)["name"]:
                del p
                device = i
                break


def readConfig():
    # read config file
    with open("config.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            tkey = line[0:line.index(" ")]
            tname = line[line.index(" ")+1:]
            if tname[-1:] == "\n":
                tname = tname[:-1]
            importedVoices[tkey] = tname

    # print config
    for k, v in importedVoices.items():
        print(k + "\t" + v)


def playAudio():
    global playing

    p = pyaudio.PyAudio()
    wf = wave.open(filePath, "rb")

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    output_device_index=device,
                    stream_callback=callback)
    stream.start_stream()

    while stream.is_active():
        if playing == "":
            break
        else:
            time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()
    p.terminate()
    playing = ""


def cb(key):
    tkey = ""
    if(hasattr(key, "name")):
        tkey = key.name
    if(hasattr(key, "char")):
        tkey = key.char

    if tkey == "r":
        os.system("cls")
        importedVoices.clear()
        initDevice()
        readConfig()
        return

    def cPlay():
        thread = threading.Thread(target=playAudio)
        thread.start()

    def cStop():
        global playing
        playing = ""

    if tkey in importedVoices:
        global playing
        global filePath

        if playing == "":
            filePath = "./voice/" + importedVoices[tkey]
            playing = tkey
            cPlay()
        else:
            if playing == tkey:
                cStop()
            else:
                cStop()
                filePath = "./voice/" + importedVoices[tkey]
                time.sleep(0.5)
                playing = tkey
                cPlay()


initDevice()
readConfig()

with keyboard.Listener(on_release=cb) as listener:
    listener.join()
