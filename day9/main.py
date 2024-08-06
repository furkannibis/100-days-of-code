programming_dictionary = {
    'Bug': 'A bug is an unexpected problem with software or hardware. Typical problems are often the result of external interference with the program\'s performance that was not anticipated by the developer. Minor bugs can cause small problems like frozen screens or unexplained error messages that do not significantly affect usage.',
    'Function': 'Functions are blocks of reusable and organised code that usually perform a single, related action. They are a crucial part of programming because they save you a lot of time and make your code cleaner.',
    'Loop': 'In computer programming, a loop is a sequence of instruction s that is continually repeated until a certain condition is reached. Typically, a certain process is done, such as getting an item of data and changing it, and then some condition is checked such as whether a counter has reached a prescribed number.'
}
print(programming_dictionary['Loop'])

programming_dictionary['Loop'] = 'The action of doing something over and over again.'
print(programming_dictionary['Loop'])

programming_dictionary = {}
print(programming_dictionary)

programming_dictionary['Bug'] = 'A bug is an unexpected problem with software or hardware. Typical problems are often the result of external interference with the program\'s performance that was not anticipated by the developer. Minor bugs can cause small problems like frozen screens or unexplained error messages that do not significantly affect usage.'
print(programming_dictionary['Bug'])

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Stuttgart', 'Berlin']
}
print(travel_log['France'][1])

nesned_list = ['A', 'B', ['C', 'D']]
print(nesned_list[2][1])

travel_log = {
    'France': {
        'total_visits': 12,
        'cities_visited': ['Paris', 'Lille', 'Dijon']
    },
    'Germany': {
        'total_visits': 5,
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart']
    }
}
print(travel_log['Germany']['cities_visited'][0])