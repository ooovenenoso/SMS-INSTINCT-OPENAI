# SMS Instinct - A Discord Bot using OpenAI API

![alt text](https://github.com/ooovenenoso/SMS-INSTINCT-OPENAI/blob/main/instinct.png)

This code creates a Discord bot that uses OpenAI API to improve Spanish text for marketing purposes. When a user in Discord sends a message starting with "/instinct", the bot takes the following text and sends it to the OpenAI API to be improved. The API returns a response with the improved text, which is then sent back to the user through Discord.

The code starts by importing the openai, discord, and os libraries. Then, the environment variables are set for the OpenAI API key and the Discord bot token. The Discord intents are configured to include information about members, presences, typing, and message content. A Discord client is created using these intents.

Finally, an "on_message" event is created that is triggered when a user sends a message through Discord. If the message starts with "/instinct", the OpenAI API is used to improve the text and it is sent back to the user through Discord. The code is executed at the end, starting the Discord bot with the provided token.

## Usage

1. Clone the repository to your local machine
```git clone https://github.com/ooovenenoso/SMS-INSTINCT-OPENAI.git```

2. Navigate to the project directory
```cd SMS-Instinct```
3. Install the dependencies
```pip install -r requirements.txt```
4. Create a new bot in Discord Developer Portal and get its API token. Then create a new API key in OpenAI and add it to your environment variables as OPENAI_API_KEY.
5. Run the code using python main.py
```python main.py```
Now your bot is ready to use in your Discord server! Whenever a user starts a message with "/instinct", the bot will improve the text using OpenAI API and send it back to the user.

# Use of OpenAI to Improve Text

OpenAI uses GPT (Generative Pre-trained Transformer) models to improve text. These models are large neural networks trained with large amounts of text to develop a deep understanding of human language.

In this code, the "text-davinci-002" model is being used, a specialized version of GPT-3 for text completion tasks. The OpenAI API uses this model to generate a continuation of the provided text in a coherent and consistent format.

The influence of this model on the code is seen in the call to the "openai.Completion.create" function in the "on_message" method. This method uses the "text-davinci-002" model to complete the provided text and returns a response with the improved text. The response is then sent back to the user via Discord.

In conclusion, OpenAI's GPT-3 models allow the Discord bot to use artificial intelligence to improve text provided by users. These models are designed to understand and generate human text, making them ideal for text improvement tasks.

