import os
import re


#Get top level directories in order
def sortKey(x):
    try:
        return int((x.name).split('.')[0])
    except:
        return 0
home = os.getcwd()
grok = list(os.scandir(home+ '/GrokkCode'))
grok.sort(key = sortKey)

langCode = {
    '1.1': 'Java',
    '1.2': 'Python',
    '1.3': 'C++',
    '1.4': 'Javascript'
}

# Handle double nested sections
def processExtra(f, section):
    subsections = list(os.scandir(section))
    subsections.sort(key = sortKey)
    for i, subsect in enumerate(subsections):
        sectName = " ".join(subsect.name.split("_")[1:])
        if not sectName:
            sectName = 'Introduction'
        f.write(f'\t{i+1}. {sectName} \n\n')
        files = list(os.scandir(subsect))
        files.sort(key = sortKey)
        for file in files: 
            fileName = 'Java'
            if file.name[0:3] in langCode:
                fileName = langCode[file.name[0:3]]
            f.write(f'\t\t | [{fileName}]({os.path.relpath(file)})')
        f.write(' |\n\n')

# Handle general section
def processSection(f, section):
    subsections = list(os.scandir(section))
    subsections.sort(key = sortKey)
    for i, subsect in enumerate(subsections):
        sectName = " ".join(subsect.name.split("_")[1:])
        if not sectName:
            sectName = 'Introduction'
        f.write(f'{i+1}. {sectName} \n\n')
        if all(x.is_dir() for x in os.scandir(subsect)):
            processExtra(f, subsect)
            continue
        else:
            files = list(os.scandir(subsect))
            files.sort(key = sortKey)
            for file in files: 
                fileName = 'Java'
                if file.name[0:3] in langCode:
                    fileName = langCode[file.name[0:3]]
                f.write(f' \t| [{fileName}]({os.path.relpath(file)})')
            f.write(' |\n\n')


# Driver code
with open('GrokkCode.md', 'w+') as f:
    f.write('# Grokking the Coding Interview\n\n')

    ## Handle Intro
    f.write(f'## ' + " ".join(grok[0].name.split("_")[1:]) + '\n')
    for i, file in enumerate(list(os.scandir(grok[0]))):
        f.write(f'{i+1}. [{" ".join(file.name.split("_")[1:])}]({os.path.relpath(file)})\n\n')

    ## Handle Main Sections
    for section in grok[1:-1]:
        f.write('## ' + " ".join(section.name.split("_")[1:])+ '\n')
        processSection(f, section)

    ## Handle Conlusion
    f.write(f'## ' + " ".join(grok[-1].name.split("_")[1:]) + '\n')
    for i, file in enumerate(list(os.scandir(grok[-1]))):
        f.write(f'{i+1}. [{" ".join(file.name.split("_")[:5])}]({os.path.relpath(file)})\n\n')
