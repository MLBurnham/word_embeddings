key_words = [
    'abortion', 'administration',

    'border',

    'conservative', 'corrupt', 'climatechange',

    'democrat', 'daca',

    'economy',

    'gun',

    'healthcare',
    
    'impeach', 'immigration', 'insurance',

    'liberal',
    
    'mcconnell',

    'oil',

    'president', 'pelosi', 'police',

    'republican', 'russia',

    'scotus',

    'tax', 'trump',

    'wall', 'wealth', 'welfare', 'whitehouse',
]

key_synonyms = {
    'realdonaldtrump': 'trump',
    'realdonald trump': 'trump',
    'donaldtrump': 'trump',
    'donald trump': 'trump',
    'presidenttrump': 'trump',
    'president trump': 'trump',
    'potus': 'trump',
    'health care': 'healthcare',
    'dems': 'democrat',
    'gop': 'republican',
    'left wing': 'liberal',
    'leftist': 'liberal',
    'progressive': 'liberal',
    'right wing': 'conservative',
    'abort': 'abortion',
    ' econ ': ' economy ',
    'economics': 'economy',
    'impeachment hearings': 'impeach',
    'impeachment hearing': 'impeach',
    'impeachment': 'impeach',
    'impeaching': 'impeach',
    'firearm': 'gun',
    'assault rifle': 'gun',
    'climate change': 'climatechange',
    'global warming': 'climatechange',
    'corruption': 'corrupt',
    'corrupted': 'corrupt',
    'nancy pelosi': 'pelosi',
    'speakerpelosi': 'pelosi',
    'speaker pelosi': 'pelosi',
    'speaker of the house pelosi': 'pelosi',
    'house speaker': 'pelosi',
    'senatemajldr': 'mcconnell',
    'senate majority leader mitch mcconnell': 'mcconnell',
    'senate majority leader mcconnell': 'mcconnell',
    'majority leader mitch mcconnell': 'mcconnell',
    'majority leader mcconnell': 'mcconnell',
    'mitch mcconnell': 'mcconnell',
    'deferred action for childhood arrivals': 'daca',
    'supreme court of the united states': 'scotus',
    'us supreme court': 'scotus',
    'united states supreme court': 'scotus',
    'supreme court': 'scotus',
    'rich': 'wealth',
    'wealthy': ' wealth',
    'billionaire': 'wealth',
    'white house': 'whitehouse',
    'fossil fuels': 'oil',
    'fossil fuel': 'oil',
    'cops': 'police',
    'law enforcement': 'police',
}

base_words = [
    'answer', 'annual', 'able',
    
    'bring', 
    
    'come', 'chance',
    
    'day',
    
    'entire',

    'far', 'find',

    'go','get',
    
    'hear', 'help', 'host', 'hold',

    'join', 

    'look', 'long', 'live',
    
    'month', 'matter', 'member', 'morning', 'meet',
    
    'night', 'near',
    
    'opportunity', 'open',
    
    'plan', 'place', 'phone',

    'read', 'receive', 'recent',
    
    'sure', 'send', 'share', 'small', 'staff', 'shut',
    
    'thank', 'think', 'take', 'today', 'talk',

    'weekend', 'week',
    
    'yesterday'
]

base_synonyms = {
    'answers': 'answer',
    'yearly': 'annual',
    'came':'come',
    'whole': 'entire',
    'distant': 'far',
    'locate':'find',
    'heard' : 'hear',
    'helped': 'help',
    'had': 'have',
    'has': 'have',
    'hosting':'host',
    'hosted':'host',
    'joint': 'join',
    'gaze' :'look',
    'glance' : 'look',
    'lengthy': 'long',
    'protracted': 'long',
    'met': 'meet',
    'greet': 'meet',
    'midnight': 'night',
    'nearly': 'near',
    'nearby': 'near',
    'ajar': 'open',
    'location': 'place',
    'telephone': 'phone',
    'cellphone': 'phone',
    'positive': 'sure',
    'sent': 'send',
    'said': 'say',
    'tiny': 'small',
    'microscopic': 'small',
    'little': 'small',
    'miniture': 'small',
    'mini': 'small',
    'grateful': 'thank',
    'thanks': 'thank',
    'gratitude': 'thank',
    'thankyou': 'thank',
    'thank you': 'thank',
    'thank-you': 'thank',
    'thought': 'think',
    'took': 'take',
    'speak': 'talk'
}

agree_words = [
    'cancer',
    
    'education',
    
    'infrastructure', 'isis',
    
    'kurd',
    
    'service',
    
    'terrorism',
    
    'usmca',
    
    'veteran',
]

agree_synonyms = {
    'cencerous': 'cancer',
    'tumor': 'cancer',
    
    'islamic state of iraq and the levant': 'isis',
    'islamic state': 'isis',
    
    'kurds': 'kurd',
    'kurdish': 'kurd',
    
    'terror attack': 'terrorism',
    'terrorist': 'terrorism',
    
    'united states mexico canada agreement': 'usmca',
    
    'vets': 'veteran',
    'vet': 'veteran'
}

#import pickle
#f = open("key_words.pkl", "wb")
#pickle.dump(key_words, f)
#f.close()

#f = open("synonym_dictionary.pkl","wb")
#pickle.dump(key_synonyms,f)
#f.close()
