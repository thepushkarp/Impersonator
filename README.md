<h1 align="center">Impersonator</h1>

<p align="center">
  <a href="https://lgtm.com/projects/g/thepushkarp/Impersonator"><img alt="LGTM Grade" src="https://img.shields.io/lgtm/grade/python/github/thepushkarp/Impersonator?style=for-the-badge"></a>
  <a href="https://github.com/thepushkarp/Impersonator/issues"><img alt="GitHub Issues" src="https://img.shields.io/github/issues/thepushkarp/Impersonator?style=for-the-badge"></a>
  <a href="https://lgtm.com/projects/g/thepushkarp/Impersonator"><img alt="LGTM Alerts" src="https://img.shields.io/lgtm/alerts/github/thepushkarp/Impersonator?style=for-the-badge"></a>
  <a href="https://github.com/thepushkarp/Impersonator/stargazers"><img alt="Stargazers" src="https://img.shields.io/github/stars/thepushkarp/Impersonator?style=for-the-badge"></a>
  <a href="https://github.com/thepushkarp/Impersonator/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/github/license/thepushkarp/Impersonator?style=for-the-badge"></a>
</p>

<p align="center">A Telegram bot that takes in an exported WhatsApp chat and uses it to send you text in your and your friend's writing style 😎</p>

---

Internally, Impersonator can generate texts in two ways:

-   The `/impersonate` command uses Markov Chains
-   The `/impersonate2` command uses Character Level RNNs

NOTE: Currently only tested for WhatsApp Chats exported from Android, but I think it should work for iOS as well.

## How to run?

-   Run `pip install -r requirements.txt`
-   Place the exported chat in the root folder as `chats.txt`.
-   Add the names of people who you want to personate using the bot in a new line in `user_names.txt`, as they appear in your exported chat.
    Ex: If you have someone's number saved as 'Birdy Bro 2', add this full name in the file.
-   Run `python clean.py` to clean the file.
-   To impersonate using Markov Chains, run `create_markov.py`.
-   To impersonate using RNN, follow [this Colab link](https://colab.research.google.com/drive/1lRsuBCVRzl8zu8lxuGyron9tqt3h5heM?usp=sharing) to generate the text files and then save them offline.
-   In the `.env` file, add the Telegram Bot token you get from [BotFather](https://core.telegram.org/bots#6-botfather) and your your Heroku WebHook URL for deploying this.
-   Deploy to [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).
-   Have Fun impersonating 🖖.

## TODO

-   [x] Add the initial implementation
-   [ ] Use custom models for RNN
-   [ ] Refactor the codebase
-   [ ] Elaborate instructions in the README

## Thanks

-   [Filip Hracek](https://github.com/filiph) who created the [Automatic Donald Trump](https://filiph.github.io/markov/) which was the inspiration for this project.
-   [Max Woolf](https://github.com/minimaxir) who developed [textgenrnn](https://github.com/minimaxir/textgenrnn) that uses Character-level RNNs. Check [here](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) to read more about Karapathy's blog on char-rnn.
-   [Jeremy Singer-Vine](https://github.com/jsvine) who developed [markovify](https://github.com/jsvine/markovify) that made developing the Markov Chain Models a lot easier.
-   My friends who extensively tested the initial versions of this and suggesting further improvements.
