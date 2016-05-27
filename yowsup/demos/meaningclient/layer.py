from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.common.tools import Jid
import requests

class MeaningLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        #self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))

        if messageProtocolEntity.getType() == 'text' and 'meaning' in messageProtocolEntity.getBody():
            phone = messageProtocolEntity.getFrom()
            word = messageProtocolEntity.getBody().lower().replace("meaning", "").strip()
            url = 'https://wordsapiv1.p.mashape.com/words/' + word
            headers = {"X-Mashape-Key": "mUFkRnNzzkmshprtCzJabFXeypDgp1tI7vZjsnPFdzXVL7buZx",
                       "Accept": "application/json"}
            response = requests.get(url, headers=headers)
            print (response.text)
            meaning = response.text
            messageToBeSent = meaning
            messageEntity = TextMessageProtocolEntity(messageToBeSent, to = Jid.normalize(phone))
            self.toLower(messageEntity)


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
