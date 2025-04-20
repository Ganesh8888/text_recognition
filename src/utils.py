
import deepl

def translator(text_to_translate, target_lang):
    '''
    Translates the given text to the specified target language using DeepL API.
    Parameters:
    text_to_translate (str): The text to be translated.
    target_lang (str): The target language code (e.g., "EN-GB" for British English).
    Returns:
    str: The translated text.
    '''
    
    # Your API key (replace with your own key)
    api_key = "e10f2c5f-9ae4-4516-badf-e713f2e77998:fx"

    # Create a DeepL Translator object
    translator = deepl.Translator(api_key)

    # Perform the translation
    result = translator.translate_text(text_to_translate, target_lang=target_lang)

    return result.text
