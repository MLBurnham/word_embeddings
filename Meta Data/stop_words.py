# This is spacy's default list of stop words minus a few key terms that may
# be relevant to this particular project

from __future__ import unicode_literals

# Stop words
STOP_WORDS = set(
    """
a about after afterwards again all almost
already also although always am among amongst amount an and another any anyhow
anyone anything anyway anywhere are around as at

be became because become becomes becoming been before beforehand
being beside besides beyond both bottom but by

can cannot ca could

did do does doing done down during

each eight either eleven else elsewhere empty enough even ever every
everyone everything everywhere except

few fifteen fifty first five for former formerly forty four from front full
further

get go

had has have he hence her here hereafter hereby herein hereupon hers herself
him himself his how however hundred
stopwords
i if in indeed into is it its itself

last latter latterly least less

many may me meanwhile might mine more moreover most mostly move much
must my myself

name namely neither nevertheless next nine no nobody none noone nor not
nothing now nowhere

of off often on once one only onto or other others otherwise our ours ourselves
out over own

part per perhaps please put

quite

rather re really regarding

same say see seem seemed seeming seems serious several she should show side
since six sixty so some somehow someone something sometime sometimes somewhere
still such

take ten than that the their them themselves then thence there thereafter
thereby therefore therein thereupon these they third this those though three
through throughout thru thus to together too top toward towards twelve twenty
two

under until up unless upon used using

various very very via was we well were what whatever when whence whenever where

whereafter whereas whereby wherein whereupon wherever whether which while
whither who whoever whole whom whose why will with within without would

yet you your yours yourself yourselves
""".split()
)

contractions = ["n't", "'d", "'ll", "'m", "'re", "'s", "'ve"]
STOP_WORDS.update(contractions)

for apostrophe in ["‘", "’"]:
    for stopword in contractions:
        STOP_WORDS.add(stopword.replace("'", apostrophe))

f = open("Meta Data/stop_words.pkl","wb")
pickle.dump(STOP_WORDS,f)
f.close()
