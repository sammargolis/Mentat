# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

# from google.cloud import aiplatform

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

# import vertexai
# from vertexai.preview.language_models import ChatModel, InputOutputTextPair

# vertexai.init(project="mygcpmlprojectspace", location="us-central1")
# chat_model = ChatModel.from_pretrained("chat-bison-32k")
parameters = {
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    currentCardID = mw.reviewer.card.id
    currentCard = mw.col.get_card(currentCardID)
    currentQuestion = currentCard.question()

    # chat = chat_model.start_chat(
    #     context="""What class of helper T cell promotes humoral immunity?""",
    # )
    # response = chat.send_message("""Explain the science behind why in simple terms with numbered steps""", **parameters)

    # show a message box
    showInfo("Card answer: %s" % currentQuestion)

# create a new menu item, "test"
action = QAction("AI- Answer Bot", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)