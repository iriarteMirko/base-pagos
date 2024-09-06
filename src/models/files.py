import os

def get_file_name() -> list[str]:
    file_list = []
    for file in os.listdir('bases/pagos/'):
        if file.endswith('.xlsx') and 'Base Pagos' in file:
            file_list.append(file)
    return file_list