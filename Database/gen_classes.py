import os



for i in range(1, 11):
    class1 = f'{i}-A'
    class2 = f'{i}-B'
    class3 = f'{i}-C'
    class4 = f'{i}-D'

    os.system(f'mkdir {class1}')
    os.system(f'chdir {class1}')
    os.system(f'mkdir Homework')
    os.system(f'chdir Homework')
    os.system('echo [] > data.json')
    os.system(f'chdir ..')
    os.system(f'mkdir Notices')
    os.system('echo [] > data.json')

    os.system(f'mkdir {class2}')
    os.system(f'chdir {class2}')
    os.system(f'mkdir Homework')
    os.system(f'chdir Homework')
    os.system('echo [] > data.json')
    os.system(f'chdir ..')
    os.system(f'mkdir Notices')
    os.system('echo [] > data.json')
    
    os.system(f'chdir ..')
    os.system(f'chdir ..')

    os.system(f'mkdir {class3}')
    os.system(f'chdir {class3}')
    os.system(f'mkdir Homework')
    os.system(f'chdir Homework')
    os.system('echo [] > data.json')
    os.system(f'chdir ..')
    os.system(f'mkdir Notices')
    os.system('echo [] > data.json')

    os.system(f'mkdir {class4}')
    os.system(f'chdir {class4}')
    os.system(f'mkdir Homework')
    os.system(f'chdir Homework')
    os.system('echo [] > data.json')
    os.system(f'chdir ..')
    os.system(f'mkdir Notices')
    os.system('echo [] > data.json')
