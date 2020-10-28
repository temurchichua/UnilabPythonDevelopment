from flask_restful import Resource, reqparse
from database import MessageModel
import json
from flask_login import current_user

class OldMessageFetcher(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("room",type=str,required=True,help="Porvide room")

    def get(self):
        data = OldMessageFetcher.parser.parse_args()
        messages = MessageModel.getMessages(data["room"])
        messageList = []
        for message in messages:
            messageList.append({"text":message.message,"received":message.username != current_user.username})
        return messageList