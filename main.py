import os

# Configurar para usar modelos menores e offload para CPU
os.environ["SUNO_USE_SMALL_MODELS"] = "True"
os.environ["SUNO_OFFLOAD_CPU"] = "True"

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# Carrega todos os modelos na memória (deverá usar menos VRAM com as configurações acima)
preload_models()

# Gera áudio a partir do texto
text_prompt = """
      Olá, meu nome é Cronos. E, ah - eu gosto de pizza. [rir]
     Mas eu também tenho outros interesses, como jogar jogo da velha.
"""
audio_array = generate_audio(text_prompt, history_prompt="v2/pt_speaker_8")

# Salva o áudio em disco
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

# Reproduz o texto no notebook
Audio(audio_array, rate=SAMPLE_RATE)