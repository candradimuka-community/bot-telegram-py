def response(input_text):
    message = input_text['message']
    chat = message['chat']
    text = message['text']
    return {
        "user_id": chat['id'],
        "username": chat['username'],
        "text": text
    }