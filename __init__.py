# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

import os
import sys
from typing import Tuple
from anki import hooks
from anki.template import TemplateRenderContext, TemplateRenderOutput
from PyQt5.QtWidgets import QInputDialog

addon_name = "dynamic_gpt_card_examples"
addon_path = os.path.join(mw.pm.addonFolder(), addon_name)
sys.path.append(addon_path)
import openai

is_api_key_valid = False

def on_card_did_render(output: TemplateRenderOutput, context: TemplateRenderContext):
    if not is_api_key_valid:
        return

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "You are a medical school professor.  I will give you a sentence which has the answer included in brackets. Explain the science behind why the answer is correct.  Use relatively simple terms with bullets or if it is a pathway use numbered steps.   Include relevant medical terms.  Keep the response concise without losing information."}, 
        {"role": "user", "content": output.question_text}])
    #output.question_text = completion.choices[0].message.content
    # show a message box when complete
    showInfo("Card answer: %s" % completion.choices[0].message.content)

api_key = "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"

if api_key == "":
    try:
        api_key, ok = QInputDialog.getText(None, "Provide OpenAI api key", "OpenAI key:", text="sk-XXXXXXXXXXX")
    except:
        pass

try:
    if api_key != "":
        openai.api_key = api_key
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "Hi!"}])
        is_api_key_valid = True
except:
    pass

hooks.card_did_render.append(on_card_did_render)


def testFunction() -> None:
    return


# create a new menu item, "AI Bot"
action = QAction("AI- Answer Bot", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)