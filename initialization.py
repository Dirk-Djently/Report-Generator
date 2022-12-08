import sys
import subprocess

reqs = subprocess.check_output([sys.executable, '-m', 'pip',
                                'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

if 'pynput' in installed_packages and 'PyAutoGUI' in installed_packages and 'barnum' in installed_packages and 'keyboard' in installed_packages:
    print('required packages already in place \n')

else:
    print('downloading necessary packages')
    subprocess.check_call([sys.executable, '-m', 'pip',
                           'install', 'pynput'])

    subprocess.check_call([sys.executable, '-m', 'pip',
                           'install', 'pyautogui'])

    subprocess.check_call([sys.executable, '-m', 'pip',
                           'install', 'barnum'])

    reqs = subprocess.check_output([sys.executable, '-m', 'pip',
                                    'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    if 'pynput' in installed_packages and 'PyAutoGUI' in installed_packages and 'barnum' in installed_packages:
        print("installation successful")
    else:
        print('error during module installation. exit program and try again')
