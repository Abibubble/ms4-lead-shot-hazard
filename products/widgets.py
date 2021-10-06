from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomImageClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/'
        'custom_image_clearable_file_input.html')


class CustomAudioClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Audio')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/'
        'custom_audio_clearable_file_input.html')
