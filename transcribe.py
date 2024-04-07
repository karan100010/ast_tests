import os
import fnmatch
import nemo.collections.asr as nemo_asr
#import telebot
#bot = telebot.TeleBot("7144846540:AAGMzRZRmlV8NtQQfQ67vD5butARXFL4tCM")
def find_new_wave_files(repo_path, known_files):
    """
    Find new wave files in a repository.

    Parameters:
        repo_path (str): The path to the repository.
        known_files (list): List of known file names.

    Returns:
        list: List of new wave file names found in the repository.
    """
    new_wave_files = []

    # Walk through the directory tree
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if fnmatch.fnmatch(file, '*.wav'):
                # Check if the file is new
                if file not in known_files:
                    new_wave_files.append(os.path.join(root, file))

    return new_wave_files

# Example usage:
asr_model_hi = nemo_asr.models.EncDecCTCModelBPE.from_pretrained(model_name="stt_hi_conformer_ctc_medium")
while True:
    repo_path="recording"
    known_files = os.listdir("recording")
    new_wave_files = find_new_wave_files(repo_path, known_files)
    print("New wave files found:")
    if new_wave_files:
        
        x=asr_model_hi.transcribe(new_wave_files)
        print("transcibing files")
        
        with open('example.txt', 'w') as file:
            for i in x:
                file.write(i)
                file.write("\n")
                print("written transcript  "+i)
                


        


    
        

