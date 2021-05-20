def greet(lastName, formOfAddress, language = 'English', timeOfDay = 'morning'):

      greetings = { 'English': { 'morning': 'Good morning', 'afternoon': 'Good afternoon' },

                    'Spanish': { 'morning': 'Buenos dias', 'afternoon': 'Buenas tardes' } }

      return '{0}, {1} {2}!'.format(greetings[language][timeOfDay], formOfAddress, lastName)


print(greet('Smith', 'Mrs.'))

print(greet('Rodriguez', 'Sr.', language = 'Spanish', timeOfDay = 'afternoon')) 
