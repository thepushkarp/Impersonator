# Impersonator

A Telegram bot that takes in an exported WhatsApp chat and uses it to send you text in your and your friend's writing style 😎.

Internally, Impersonator can generate texts in two ways:

-   The `/impersonate` command uses Markov Chains
-   The `/impersonate2` command uses Character Level RNNs

NOTE: Currently only tested for WhatsApp CHats exported from Android, but I think it should work for iOS as well.

## How to run?

-   Run `pip install -r requirements.txt`
-   Place the exported chat in the root folder as `chats.txt`.
-   Add the names of people who you want to personate using the bot in a new line in `user_names.txt`, as they appear in your exported chat.
    Ex: If you have someone's number saved as 'Birdy Bro 2', add this full name in the file.
-   Run `python clean.py` to clean the file.
-   To impersonate suing Markov Chains, run `create_markov.py`.
-   To impersonate using RNN, follow [this Colab link](https://colab.research.google.com/drive/1lRsuBCVRzl8zu8lxuGyron9tqt3h5heM?usp=sharing) to generate the text files and then save them offline.
-   In the `.env` file, add the Telegram Bot token you get from [BotFather](https://core.telegram.org/bots#6-botfather) and your your Heroku WebHook URL for deploying this.
-   Deploy to [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).
-   Have Fun 🖖

## TODO

-   [x] Add the initial implementation.
-   [ ] Add details on how Markov Chains and RNNs work here to generate text in the style of the person.
-   [ ] Elaborate instructions in the README.
-   [ ] Tweak the hyperparameters in the RNN to improve text generation and use weights to generate text on-the fly.
-   [ ] Refactor the codebase

## Thanks

-   Thanks to [Filip Hracek](https://github.com/filiph) for creating the [Automatic Donald Trump](https://filiph.github.io/markov/) which was the inspiration for this project.
-   Thanks to [Max Woolf](https://github.com/minimaxir) for developing [textgenrnn](https://github.com/minimaxir/textgenrnn) that uses Character-level RNNs. Check [here](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) to read more about Karapathy's blog on char-rnn.
-   Thanks to [Jeremy Singer-Vine](https://github.com/jsvine) for developing [markovify](https://github.com/jsvine/markovify) that made developing the Markov Chain Models a lot easier.
-   Thanks to my friends to extensively testing the initial versions of this and suggesting various improvements.
