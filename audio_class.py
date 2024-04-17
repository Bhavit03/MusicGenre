# !pip install transformers
from transformers import pipeline
import torchaudio
import numpy as np
pipe = pipeline("audio-classification", model="dima806/music_genres_classification")
def find_class(audio):

    RATE_HZ = 16000
    audio,rate = torchaudio.load(audio)
    transform = torchaudio.transforms.Resample(rate,RATE_HZ)
    audio = transform(audio).numpy().reshape(-1)
    classes = pipe(audio)
    return classes[0]['label']
classifier = pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")
# def find_emotions(audio):
#     RATE_HZ = 16000
#     transform = torchaudio.transforms.Resample(rate,RATE_HZ)
#     audio = transform(audio).numpy().reshape(-1)
#     labels = classifier(audio, top_k=5)
#     return labels[0]['label']
