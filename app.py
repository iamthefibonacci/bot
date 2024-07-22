
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template
import requests

app = Flask(__name__)

headers = {
    'x-api-key': 'sec_6JMNi9x0nWy7P9BPjwyVpyuDgM4EXG6a',
    'Content-Type': 'application/json'
}

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'


# Route to render the HTML form
@app.route('/')
def show_form():
    return render_template('form.html')


@app.route('/bot', methods=['POST'])
def whatsapp_webhook():

    incoming_msg = request.values.get('Body', '').lower()

    ebook = {'url': 'fervent.pdf'}

    url = "https://api.chatpdf.com/v1/chats/message"

    response = requests.post('https://api.chatpdf.com/v1/sources/add-url',
                             headers=headers, json=ebook)

    data = {
        "stream": True,
        "sourceId": response.json()['sourceId'],
        "messages": [

            {"role": "user",
             "content": incoming_msg,
             },
        ],
    }

    response = requests.post(url, json=data, headers=headers, stream=True)
    print(response)


    return f'Received message: {incoming_msg}'


def chat_pdf_api(user_message):
    ebook = {'url': 'https://itbank.co.zw/WiseSureCustomerService.pdf'}

    url = "https://api.chatpdf.com/v1/chats/message"

    response = requests.post('https://api.chatpdf.com/v1/sources/add-url',
                             headers=headers, json=ebook)

    data = {
        "stream": True,
        "sourceId": response.json()['sourceId'],
        "messages": [

            {"role": "user",
             "content": user_message,
             },
        ],
    }

    response = requests.post(url, json=data, headers=headers, stream=True)

    return response.text
