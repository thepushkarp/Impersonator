"""
Cleans exported WhatsApp Chats by removing chat timestamps and unnecessary lines and
separates chats by sender names.
"""

import os
import sys
import re

# Each conversation of chat exported form WhatsApp starts with timestamp
TIMESTAMP = re.compile(
    "^([0-9][0-9]/[0-9][0-9]/[0-9][0-9], [0-9][0-9]:[0-9][0-9] - )(.*)$"
)

# Input chat file
INPUT_FILENAME = "chats.txt"

# Chat file after cleaning
CLEANED_FILENAME = "cleaned_chats.txt"

# Names of users whose chat is to be extracted
NAMESFILE = "user_names.txt"

# Lines to be removed form the chats
TO_REMOVE = ["You deleted this message", "<Media omitted>", "This message was deleted"]


def clean_chat():
    """
    Clean the conversations in the input by getting rid of the timestamps and
    joining together multiple lines of a conversation into one.
    """

    cleaned_file = open(CLEANED_FILENAME, "w")

    try:
        # Loops over each line in the chat
        for line in open(INPUT_FILENAME, "r"):
            # If the current line is the start of a conversation, add it from a new line
            if (timestamp_line := TIMESTAMP.search(line)) is not None:
                cleaned_file.write("\n")
                cleaned_file.write(timestamp_line.group(2))
            # Else, append it to the previous line
            else:
                cleaned_file.write(" ")
                cleaned_file.write(line.strip("\n"))
    except IOError:
        print("Error: Input file not accessible! Exiting...")
        sys.exit(1)
    finally:
        cleaned_file.close()


def save_user_chat(names: list):
    """
    Saves the chats of individual participants of the conversation
    """

    # Create chats folder if does not exists already
    if not os.path.exists("chats"):
        os.mkdir("chats")

    for name in names:
        # Regexp to check if the line starts with the name
        user_chat = re.compile(f"(^{name}: )(.*)$")

        # Saving the texts of each person in separate file
        out_file_name = os.path.join("chats", "_".join(name.lower().split()) + ".txt")

        # Adds all lines (except the removed lines) by a person in a separate line
        with open(out_file_name, "w") as out_file:
            for line in open(CLEANED_FILENAME, "r"):
                if (users_line := user_chat.search(line)) is not None:
                    if (chat_line := users_line.group(2)) not in TO_REMOVE:
                        out_file.write(chat_line)
                        out_file.write("\n")


def main():
    print("Clearing the chats...")
    clean_chat()

    # Getting the names of each person from the names file
    names = [line.strip("\n").strip("\r") for line in open(NAMESFILE, "r")]

    print("Creating separate file for each user...")
    save_user_chat(names)
    print("Cleaned!")


if __name__ == "__main__":
    # To run in only Python 3.8 and above
    if sys.version_info[0] < 3 or (
        sys.version_info[0] == 3 and sys.version_info[1] < 8
    ):
        raise Exception("Python 3.8 or a more recent version is required.")

    main()
