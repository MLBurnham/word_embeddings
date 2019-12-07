# This is spacy's default list of stop words minus a few key terms that may
# be relevant to this particular project

from __future__ import unicode_literals

# Stop words
stop_words = set(
    """
a about after afterwards again all almost
already also although always am among amongst amount an and another any anyhow
anyone anything anyway anywhere are around as at

b be became because become becomes becoming been before beforehand
being beside besides beyond both bottom but by

c can cannot ca could

d did do does doing done down during

e each eight either eleven else elsewhere empty enough even ever every
everyone everything everywhere except

f few fifteen fifty first five for former formerly forty four from front full
further

g

h had has have he hence her here hereafter hereby herein hereupon hers herself
him himself his how however hundred

i if in indeed into is it its itself

j

k

l last latter latterly least less

m many may me meanwhile might mine more moreover most mostly move much
must my myself

n name namely neither nevertheless next nine no nobody none noone nor not
nothing now nowhere

o of off often on once one only onto or other others otherwise our ours ourselves
out over own

p part per perhaps please put

q quite

r rather re really regarding

s same say see seem seemed seeming seems serious several she should show side
since six sixty so some somehow someone something sometime sometimes somewhere
still such

t take ten than that the their them themselves then thence there thereafter
thereby therefore therein thereupon these they third this those though three
through throughout thru thus to together too top toward towards twelve twenty
two

u under until up unless upon used using

v various very very via was we well were what whatever when whence whenever where

w whereafter whereas whereby wherein whereupon wherever whether which while
whither who whoever whole whom whose why will with within without would

x

y yet you your yours yourself yourselves

z
""".split()
)

contractions = ["n't", "'d", "'ll", "'m", "'re", "'s", "'ve"]
stop_words.update(contractions)

for apostrophe in ["‘", "’"]:
    for stopword in contractions:
        stop_words.add(stopword.replace("'", apostrophe))

#import pickle
#f = open("stop_words.pkl","wb")
#pickle.dump(stop_words,f)
#f.close()
