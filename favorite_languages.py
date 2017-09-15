favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python',
                      }

names = ['zhua','keane','jen']

for name in names:
    if name in favorite_languages.keys():
        print(name.title() + ", Thank you for your feedback!")
    else:
        print(name.title() + ", Please help me!")
