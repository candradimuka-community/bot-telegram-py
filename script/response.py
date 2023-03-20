def response(input_text) -> str:
    message = input_text['message']
    chat = message['chat']
    text = message['text']

    if text == "/all_data":
        return str(input_text)
    else:
        return str(chat)