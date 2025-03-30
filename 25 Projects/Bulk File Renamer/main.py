import os

def main():
    i = 0
    path = 'D:/Gov House (Python Q3)/Python-Assignments/25 Projects/Bulk File Renamer'
    for filename in os.listdir(path):
        if filename.endswith('.jpg'):
            new_name = f'image{i}.jpg'
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
            i += 1
            print(f'Renamed {filename} to {new_name}')


if __name__ == "__main__":
    main()