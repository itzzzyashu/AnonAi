# Run this file and wait until it download all required modules.
# Then run download "PyAudio Unofficial Library" (Google it) and Install it in your system.
# Comment the "# Requirements Install" code line [ os.system(f"""pip install -r "{req_path}" """) ] (use # to comment that line).
# After this all, run "AnonAi.py" file | Welcome to Anon Ai.
 

 
 # Your Info that Anon Ai needs for functioning.
import os



class Config():
    NAME = "Name" # Your first name that Anon can call you
    CLASS = 10 # Your class no. without section
    AGE = 16 # Your current age without(in integer).
    
    # TIME LOCATION 
    CNT = 'IST' # IST or UTC.

    # Kuki Ai Api
    AIAPI = "" # Get this from https://telegram.me/kukichatbot, for token you can ask queries at https://telegram.me/metavoidsupport.
    
    # Directories
    #    Copy paste your music directory path in music_dir.
    music_dir = r''
    #    Copy paste your photos directory path in pics_dir.
    pics_dir = r''
    #    Copy paste your videos directory path in video_dir.
    video_dir = r''
    #    Copy paste your AnonAi.py directory path in jarvis_path.
    anon_path = r''
    #    Copy paste your hidden directory path in hidden_dir.
    hidden_dir = ''
    #   Secret Codes to unlock hidden_dir.
    xsearch=[
        'tea cup',
        'tea'
        ]
        
# Copy paste your Requirements.txt path in req_path.
req_path = r"C:\Users\user\AnonAi\requirements.txt"

# Requirements Install, after this completes, comment below line by '#'
os.system(f"""pip install -r "{req_path}" """)





















