import os
import library.modules.return_random_string as return_random_string
import library.modules.config as config

config.main()


def main(condition):
    if condition == 'system_initiated':
        if os.path.isfile(os.path.join(os.getcwd(), 'resources', 'PyIris.cred')):
            print(config.pos + 'PyIris.cred key file located - OK')
            pass
        else:
            print(config.neg + 'PyIris.cred key file not found/generated - ERROR, AUTO-GENERATING KEY')
            prompt = input(config.pro + 'Listener key [Enter to generate a random 50 length key] : ')
            if not prompt:
                prompt = return_random_string.main(50)
            with open('resources/PyIris.cred', 'w') as f:
                f.write(prompt)
            print(config.pos + 'Generated PyIris.cred key file with key as : ' + prompt)
    elif condition == 'user_initiated':
        continue_on = input(config.war + 'This will overwrite existing key, continue? [y|n] : ')
        if continue_on == 'y':
            prompt = input(config.pro + 'Listener key [Enter to generate a random 50 length key] : ')
            if not prompt:
                prompt = return_random_string.main(50)
            with open('resources/PyIris.cred', 'w') as f:
                f.write(prompt)
            print(config.pos + 'Generated PyIris.cred key file with key as : ' + prompt)
            config.key = prompt
