import jigglypuff
import logzero
from logzero import logger

from pathlib import Path

# GLOBALS
BASE_DIR = Path(__file__).resolve()


# SETTING UP LOGGER
log_file = BASE_DIR / "jigglypuff.log"
logzero.logfile(str(log_file))


try:

    # LOAD AUDIO
    input_file = Path("lol.wav")
    audio = jigglypuff.load_audio(input_file)

    # EDITING


    # EXPORT AUDIO
    output_file = Path("cool.wav")
    jigglypuff.export_audio(audio, output_file, "mp3")

except Exception as e:
    logger.error(e)
