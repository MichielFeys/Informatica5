def vlag(richting, kleuren):
    antw = ''
    for i in range(0, len(kleuren)):
        antw += kleuren[i]
        if richting == 'verticaal' and kleuren[i] != kleuren[-1]:
            antw += ' | '

        elif richting == 'horizontaal' and kleuren[i] != kleuren[-1]:
            antw += '\n' + '-' + '\n'

    return antw