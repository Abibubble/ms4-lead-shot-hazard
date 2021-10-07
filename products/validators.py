import os
import magic
from django.core.exceptions import ValidationError


# Code used from
# https://stackoverflow.com/questions/3648421/only-accept-a-certain-file-type-in-filefield-server-side
def validate_is_audio(file):
    """
    Validate that the file being uploaded is genuinely an accepted audio file
    """

    valid_mime_types = ['audio/mpeg', 'audio/ogg', 'audio/vnd.wav']
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')
    valid_file_extensions = ['.mp3', '.ogg', '.wav']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')
