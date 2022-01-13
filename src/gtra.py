from google.cloud.translate_v2.client import ENGLISH_ISO_639
from google.cloud import translate_v2 as translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/branimir/Projects/algolia/agpoc"

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # willq return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

if __name__ == "__main__":
    translate_text(ENGLISH_ISO_639, "Al je lep ovaj svet!")
    trc = translate.Client()
    res = trc.translate("Al je lep ovaj svet!",target_language=ENGLISH_ISO_639, source_language="sr")
    print(res["translatedText"])