import json;
class create():
    def __init__(self, path):
        self.path = path
        self.load()

    def save(self):
        readable = open(self.path)
        restorable = json.load(readable)
        file = open(self.path, 'w')
        file.seek(0)
        try:
            json.dumps(self.content)
        except BaseException as err:
            self.content = restorable
            print(err)
        file.truncate()
        file.write(json.dumps(self.content, indent=4))
        file.close()
        readable.close()
    
    def load(self):
        file = open(self.path)
        self.content = json.load(file)
        file.close()

    def set(self, key: str, value):
        if not isinstance(key, str):
            print(f'Key name type must be str, got {type(key)}')
            return
        self.load()
        self.content[key] = value
        self.save()
    
    def append(self, key: str, value):
        if not isinstance(key, str):
            print(f'Key name type must be str, got {type(key)}')
            return
        try:
            if self.has(key) and isinstance(self.get(key), list):
                self.content[key].append(value)
            else:
                self.content[key] = [value]
            self.save()
        except BaseException as err:
            print(err)

    def pop(self, key: str, index: int):
        if not isinstance(key, str):
            print(f'Key name type must be str, got {type(key)}')
            return
        if not isinstance(index, int):
            print(f'Index must be int, got {type(index)}')
            return
        if not isinstance(self.get(key), list):
            print(f'Key value must be list, got {type(self.get(key))}')
            return
        self.content[key].pop(index)
        self.save()
    
    def get(self, key):
        self.load()
        try:
            return self.content[key]
        except:
            return None
    
    def has(self, key):
        return self.get(key) is not None
    
    def delete(self, key: str):
        if not isinstance(key, str):
            print(f'Key name type must be str, got {type(key)}')
            return
        try:
            self.load()
            del self.content[key]
            self.save()
        except:
            pass
    
    def clear(self):
        self.content = {}
        self.save()