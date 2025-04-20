from utils import *


def main():
    text_to_translate = ""
    target_lang = "EN-GB"
    
    translated_text = translator(text_to_translate, target_lang=target_lang)
    print(translated_text)

if __name__ == "__main__":
    main()