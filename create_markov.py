import os
import markovify
import json

# Names of users whose chat is to be extracted
NAMESFILE = "user_names.txt"


def compile(names: list):
    """
    Compiles markov models of each chat and saves them locally
    """
    for name in names:
        print(f"Compiling model for {name}...")

        # Lowercase and join names with a '_'
        name_string = "_".join(name.lower().split())

        # Reading the chat file
        chat_file = os.path.join("chats", name_string + ".txt")
        with open(chat_file) as f:
            text = f.read()

        # Building the markov model
        text_model_2 = markovify.NewlineText(text, state_size=2)
        text_model_3 = markovify.NewlineText(text, state_size=3)

        # Compiling the model
        text_model_2.compile(inplace=True)
        text_model_3.compile(inplace=True)

        # Exporting the model to json
        model_2_json = text_model_2.to_json()
        model_3_json = text_model_3.to_json()
        model_jsons = [model_2_json, model_3_json]

        if not os.path.exists("mkc_jsons"):
            os.mkdir("mkc_jsons")

        # Saving both the models in a single json file
        for idx, model_json in enumerate(model_jsons):
            json_file_name = os.path.join("mkc_jsons", f"{name_string}_{idx+2}.json")
            with open(json_file_name, "w+") as j:
                j.write(model_json)


def main():
    print("Compiling Markov Models...")

    # Getting the names of each person from the names file
    names = [line.strip("\n").strip("\r") for line in open(NAMESFILE, "r")]
    compile(names)

    print("Markovified!")


if __name__ == "__main__":
    main()
