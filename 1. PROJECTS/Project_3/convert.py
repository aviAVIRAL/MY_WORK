import base64

def convert_wav_to_base64(file_path):
    with open(file_path, 'rb') as file:
        wav_data = file.read()
        base64_data = base64.b64encode(wav_data).decode('utf-8')
    return base64_data

        

if __name__ == "__main__":
    wav_file_path = "Testingvoice1.wav"  # Replace with your .wav file path
    base64_data = convert_wav_to_base64(wav_file_path)
    print(base64_data)
