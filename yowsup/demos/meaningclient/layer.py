from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.common.tools import Jid
from meaning import getmeaningfromapi
from tweet import gettweetsfromapi
from wishsender import sendwish

class MeaningLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        try:
            if messageProtocolEntity.getType() == 'text':
                self.onTextMessage(messageProtocolEntity)
            elif messageProtocolEntity.getType() == 'media':
                self.onMediaMessage(messageProtocolEntity)
            
            #self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
            self.toLower(messageProtocolEntity.ack())
            self.toLower(messageProtocolEntity.ack(True))
            
            phone = messageProtocolEntity.getFrom()
            messageBody = messageProtocolEntity.getBody()
            messageToBeSent = ""
            if messageProtocolEntity.getType() == 'text':
                if 'happy' in messageBody.lower() or 'congrats' in messageBody.lower():
                    sendmessage = sendwish(messageBody)
                    if sendmessage == True:
                        self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))

                if 'meaning?' in messageBody.lower():
                    messageToBeSent = getmeaningfromapi(messageBody)
                    messageEntity = TextMessageProtocolEntity(messageToBeSent, to = Jid.normalize(phone))
                    self.toLower(messageEntity)

                if '#' in messageBody.lower():
                    messageToBeSent = gettweetsfromapi(messageBody)
                    messageEntity = TextMessageProtocolEntity(messageToBeSent, to = Jid.normalize(phone))
                    self.toLower(messageEntity)

                if 'book ecg' in messageBody.lower():
                    messageToBeSent = queueThisPerson(phone)
                    messageEntity = TextMessageProtocolEntity(messageToBeSent, to = Jid.normalize(phone))
                    self.toLower(messageEntity)

                if 'ecg done' in messageBody.lower():
                    phone = dequeueEcg()
                    messageToBeSent = "Please report for ecg..";
                    messageEntity = TextMessageProtocolEntity(messageToBeSent, to = Jid.normalize(phone))
                    self.toLower(messageEntity)

                print (messageToBeSent)
        except Exception, e:
            print (e)

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
