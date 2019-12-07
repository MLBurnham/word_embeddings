key_words = [
    'trump',
    'president',
    'healthcare',
    'border',
    'wall',
    'democrat',
    'republican',
    'liberal',
    'conservative',
    'abortion',
    'clinton',
    'sanders',
    'socialist',
    'economy',
    'jobs',
    'impeach',
    'obama',
    'russia',
    'mueller',
    'collusion',
    'military',
    'budget',
    'market',
    'trade',
    'vote',
    'democracy',
    'gun',
    'agriculture',
    'women',
    'business',
    'tax',
    'medicare',
    'police',
    'immigration',
    'insurance',
    'climatechange',
    'corrupt',
    'electoralcollege',
    'judge',
    'court',
    'gerrymander',
    'pelosi',
    'mcconnell',
    'mikepence',
    'citizensunited',
    'daca',
    'dreamers',
    'lgbtq',
    'ACA',
    'scotus',
    'partisan',
    'patriot',
    'welfare',
    'privilege',
    'minority',
    'islam',
    'muslim',
    'christian',
    'god',
    'religion',
    'administration',
    'politics',
    'fair',
    'witchhunt',
    'warren',
    'biden',
    'security',
    'terrorism',
    'defense',
    'pentagon',
    'homelandsecurity',
    'senate',
    'wealth',
    'american',
    'church',
    'science',
    'stockmarket',
    'congress',
    'whitehouse',
    'constitution',
    'federal',
    'syria',
    'northkorea',
    'saudiarabia',
    'mexico',
    'debt',
    'fiscal',
    'oil',
    'media',
    'cnn',
    'fox',
    'news',
    'racist',
    'refugee',
    'education',
    'maga',
    'campaign',
    'party',
    'poll'
]

key_words_small = [
    'abortion', 'administration',

    'border', 'biden',

    'conservative', 'collusion', 'clinton', 'campaignfinance', 'corrupt', 'court', 'climatechange', 'cnn',

    'democrat', 'daca',

    'economy', 'electoralcollege', 'education',
    
    'fox',

    'gun', 'god', 'gerrymander',

    'healthcare',
    
    'impeach', 'immigration', 'insurance',

    'liberal',
    
    'mueller', 'mikepence', 'mcconnell', 'mexico', 'media'
    
    'news',

    'obama', 'oil',

    'president', 'pelosi', 'police'

    'republican', 'russia', 'religion', 'racist', 'refugee',

    'sanders', 'socialist', 'scotus',

    'tax', 'trump',

    'usmca',

    'wall', 'wealth',
    
    'welfare', 'warren', 'whitehouse',
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
    'bernie sanders': 'sanders',
    'bernie': 'sanders',
    ' econ ': ' economy ',
    'economics': 'economy',
    'impeachment hearings': 'impeach',
    'impeachment hearing': 'impeach',
    'impeachment': 'impeach',
    'president obama': 'obama',
    'prsident barack obama': 'obama',
    'barack obama': 'obama',
    'robert mueller': 'mueller',
    'armed forces': 'military',
    'armed services': 'military',
    'firearm': 'gun',
    'assault rifle': 'gun',
    'climate change': 'climatechange',
    'global warming': 'climatechange',
    'corruption': 'corrupt',
    'corrupted': 'corrupt',
    'electoral college': 'electoralcollege',
    'court justice': 'judge',
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
    'vice president mike pence': 'mikepence',
    'vice president pence': 'mikepence',
    'mike pence': 'mikepence',
    ' pence ': ' mikepence ',
    'citizens united': 'campaignfinance',
    'campaign finance': 'campaignfinance',
    'deferred action for childhood arrivals': 'daca',
    'lgbt': 'lgbtq',
    'affordable care act': 'aca',
    'obamacare': 'aca',
    'obama care': 'aca',
    'supreme court of the united states': 'scotus',
    'us supreme court': 'scotus',
    'united states supreme court': 'scotus',
    'supreme court': 'scotus',
    'islamic': 'islam',
    'christianity': ' christian',
    'political': 'politics',
    'witch hunt': 'witchhunt',
    'senator elizabeth warren': 'warren',
    'senator warren': 'warren',
    'elizabeth warren': 'warren',
    'ewarren': 'warren',
    'counterterrorism': 'terrorism',
    'counter-terrorism': 'terrorism',
    'homeland security': 'homelandsecurity',
    'us senate': 'senate',
    'united states senate': 'senate',
    'senatorial': 'senate',
    'rich': 'wealthy',
    'wealthy': ' wealth',
    'billionaire': 'wealthy',
    'temple': 'church',
    'stock market': 'stockmarket',
    'stocks': 'stockmarket',
    'congressional': 'congress',
    'white house': 'whitehouse',
    'north korean': 'northkorea',
    'north korea': 'northkorea',
    'saudi arabian': 'saudiarabia',
    'saudi arabia': 'saudiarabia',
    ' saudi ': ' saudiarabia ',
    'mexican': 'mexico',
    'fox news': 'fox',
    'cable news network': 'cnn',
    'make america great again': 'maga',
    'fossil fuels': 'oil',
    'fossil fuel': 'oil',
    'united states mexicocanada agreement': 'usmca'
}

base_words = [
    'answer', 'annual', 'able',
    
    'bring', 

    'cancer', 'come', 'chance'
    
    ' day ',
    
    'entire',

    'far', 'find',

    'go','get',
    
    'hear', 'help', 'host', 'hold',

    ' join ', 

    'look', 'long', 'like', 'live',
    
    'month', 'matter', 'member', 'morning', 'meet',
    
    'night', 'near',
    
    'opportunity', 'open',
    
    'plan', 'place', 'phone',

    'read', 'receive', 'recent',
    
    'sure', 'send', 'share', 'small', 'staff', 'shut'

    'thanksgiving', ' thank ', 'think', 'take', 'today', 'talk',

    'weekend', ' week ',
    
    'yesterday'
]

base_synonyms = {
    'answers': 'answer',
    'yearly': 'annual',
    'cancerous':'cancer',
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
    'thanks giving': 'thanksgiving',
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

#import pickle
#f = open("key_words.pkl", "wb")
#pickle.dump(key_words, f)
#f.close()

#f = open("synonym_dictionary.pkl","wb")
#pickle.dump(key_synonyms,f)
#f.close()
