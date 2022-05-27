# %%
from pybtex.database.input import bibtex
import os
import datetime
import re
parser = bibtex.Parser()
bib = parser.parse_file('./files/myPubs/myPubs.bib')

# %%
def IEEE(e):
    f = str()
    for a in e.persons['author']:
        if len(a.first_names):
            f+= a.first_names[0][0] + '.'
        if len(a.middle_names):
            f += a.middle_names[0][0] + '.'

        f+= ' ' + a.last_names[0] + ', '

    title = re.sub('[^A-Za-z0-9 /]+', '', e.fields['title']).title()
    journal =  re.sub('[^A-Za-z0-9 /]+','', e.fields['journal'])

    f = f[0:-2] + '. "' + title + '", <i>' + journal  + '</i>, ' + e.fields['year']

    return(f) 


# %%
for key in bib.entries.keys():
    print(key)
    mdFile = os.path.join('_publications/',key+'.md')
    if not False: #os.path.isfile(mdFile):
        e = bib.entries[key]
        f = open(mdFile,'w+')

        f.write('---\n')
        title =  re.sub('[^A-Za-z0-9 /]+', '', e.fields['title']).title()
        f.write(r"title: '" + title + r"'" + '\n')

        f.write('collection: publications' + '\n')
        #f.write('permalink: ' + '/' + key + '\n')
        f.write('Venue: NA \n')

        # % Dates are hard
        if 'abstract' in e.fields.keys():
            ab = re.sub('[^A-Za-z0-9 /]+', '', e.fields['abstract'])
            f.write(r"abstract: '" + ab + r"'" + '\n')

        # %% make up dates if needed
        year = e.fields['year']
        if 'month' in e.fields.keys():
            month = str(datetime.datetime.strptime(e.fields['month'], "%B").month)
        else:
            month = '1'

        if 'day' in e.fields.keys():
            day = str(datetime.datetime.strptime(e.fields['day'], "%B").day)
        else:
            day = '1'

        f.write('date: ' + year + '-' + month + '-' + day + '\n')

        # %
        f.write('paperurl: /files/myPubs/' + bib.entries[key].fields['file'].split(':')[1] + '\n')

        f.write(r"citation: '")
        f.write(IEEE(e))
        f.write(r".'" '\n')
        f.write('---\n')

        f.close()