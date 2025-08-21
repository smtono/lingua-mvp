"""
e
"""

import os
import json

from pathlib import Path
import langcodes

# Grammar properties
with open(Path(os.getcwd(), 'data', 'language_grammar.json'),
          'r',
          encoding='UTF-8') as f:
    LANGUAGE_GRAMMAR = json.load(f)


def get_language_metadata(lang_code):
    """
    Returns a dict of metadata for the given language code,
        combining langcodes info and custom grammar mapping.
    """
    lang_info = langcodes.get(lang_code)
    grammar = LANGUAGE_GRAMMAR.get(lang_code, {})

    metadata = {
        'display_name': lang_info.display_name(),  # e.g., "French"
        'root': grammar.get('root', 'Unknown'),
        'word_order': grammar.get('word_order', 'Unknown'),
        'gendered_nouns': grammar.get('gendered_nouns', None),
        'script': grammar.get('script', lang_info.script),
        'iso_code': lang_info.language,
    }
    return metadata
