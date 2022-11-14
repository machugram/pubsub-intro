from pubsub import pub

def listener_alice(args):
    print("Consumer Alice receives news about: ",args["headline"])
    print("The news for Alice contains" , args["news"])
    print()


def listener_bob(args):
    print("Consumer Bob receives news on headline : ",args["headline"])
    print("The news for Bob contains" , args["news"])
    print()


#Subscribers

pub.subscribe(listener_alice, 'football')
pub.subscribe(listener_alice, 'chess')
pub.subscribe(listener_bob, 'football')


#Publishers

pub.sendMessage('football', args={'headline': 'Ronaldo','news': 'Sold for $1M'})
pub.sendMessage('chess', args={'headline': 'Chess','news': 'AlphaZero beats grandmaster Carlsen'})
pub.sendMessage('AI', args={'headline': 'AI','news': 'AlphaZero AI beats grandmaster Carlsen'})