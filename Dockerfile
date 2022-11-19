FROM python:3.10.7-slim

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt
ENV Twitch_Client_ID [Replace with Client ID]
ENV Twitch_Token [Replace with Token, not Secret]

CMD [ "python", "main.py"]