def convert(number):

    sound = {3:'Pling', 5:'Plang', 7:'Plong'}
    rain = [item for key, item in sound.items() if not number % key]

    return ''.join(rain) if rain else str(number)