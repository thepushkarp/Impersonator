import logging
import os
import json
import random
import markovify
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

NAMESFILE = "user_names.txt"
NAMES = []
NAMES_STRING = []

# JSON models
MODELS = {}

# Port to run the bot
PORT = int(os.environ.get("PORT", "8443"))


def start(update, context):
    """
    Handles the /start command
    """

    update.message.reply_text(
        f"Hi 👋, I'm Impersonator! Use /help to know more about how I can impersonate you and your friends!"
    )


def help(update, context):
    """
    Handles the /help command
    """

    update.message.reply_text(
        """Use \'/impersonate <lowercase_name>\' to make me impersonate.
        For example:
        \'/impersonate james_bond\'

        You can also use \'/impersonate2 <lowercase_name>\'
        to use the second generating algorithm."""
    )


def error(update, context):
    """
    Handles errors occurred in the dispatcher
    """

    update.message.reply_text(
        "Hmm, something doesn't seems right. I can feel the hashes colliding..."
    )


def impersonate(update, context):
    """
    Handles the /impersonate command which uses Markov Chains
    """

    try:
        if len(context.args) != 1:
            raise IndexError
        else:
            name_string = context.args[0].lower()
            if name_string in NAMES_STRING:
                # Try for a max of 20 times for generating a sentence
                count = 0
                sentence = None
                while sentence is None and count != 20:
                    curr_model = random.choice(MODELS[name_string])
                    sentence = curr_model.make_sentence()
                    count += 1
                update.message.reply_text(
                    f'{" ".join(name_string.split("_")).title()}: {sentence}'
                )
                return
            else:
                update.message.reply_text("Are you sure I know this person?")
    except (IndexError, ValueError):
        update.message.reply_text(
            "Oops! Did you use '/impersonate <persons_name>' correctly!?"
        )


def impersonate2(update, context):
    """
    Handles the /impersonate2 command which uses RNNs
    """

    try:
        if len(context.args) != 1:
            raise IndexError
        else:
            name_string = context.args[0].lower()
            if name_string in NAMES_STRING:
                user_file_name = os.path.join("rnn_texts", name_string + ".txt")
                user_texts = open(user_file_name, "r").readlines()
                texts = []
                for i in range(len(user_texts)):
                    text = user_texts[i]
                    texts.append(text)
                sentence = random.choice(texts)
                update.message.reply_text(
                    f'{" ".join(name_string.split("_")).title()}: {sentence}'
                )
                return
            else:
                update.message.reply_text("Are you sure I know this person?")
    except (IndexError, ValueError):
        update.message.reply_text(
            "Oops! Did you use '/impersonate2 <persons_name>' correctly!?"
        )


def main():

    NAMES = [line.strip("\n").strip("\r") for line in open(NAMESFILE, "r")]
    NAMES_STRING = ["_".join(name.lower().split()) for name in NAMES]

    for name_string in NAMES_STRING:

        # Loading the json file
        model_2_json_file = open(os.path.join("mkc_jsons", name_string + "_2.json"))
        model_3_json_file = open(os.path.join("mkc_jsons", name_string + "_3.json"))

        # Loading the json from that file
        model_2_json = json.dumps(json.load(model_2_json_file))
        model_3_json = json.dumps(json.load(model_3_json_file))

        # Reconstruct model from the json
        reconstituted_model_2 = markovify.Text.from_json(model_2_json)
        reconstituted_model_3 = markovify.Text.from_json(model_3_json)

        reconstituted_models = [reconstituted_model_2, reconstituted_model_3]

        # Saving it in a dictionary
        MODELS[name_string] = reconstituted_models

    """Start the bot"""

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = os.getenv("TOKEN")
    URL = os.getenv("URL")

    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for start and help commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Add an handler for errors
    dp.add_error_handler(error)

    # Add a handler for the impersonate commands
    dp.add_handler(CommandHandler("impersonate", impersonate))
    dp.add_handler(CommandHandler("impersonate2", impersonate2))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook(URL + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    # updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
