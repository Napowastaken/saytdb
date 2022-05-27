import json;
from typing import *
class create():
    def __init__(self, path):
        self.path = path
        self.load()

    def save(self) -> NoReturn:
        """ Saves the database's content to the file.

        .. note::
            
            The module already saves for you, so you won't need this unless it's a specific case."""
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
    
    def load(self) -> NoReturn:
        """ Loads the database content.
        
        .. note::
            The module already loads for you, so you won't need this unless it's a specific case. However, it might be useful if you have multiple files with the same database."""
        file = open(self.path)
        self.content = json.load(file)
        file.close()

    def set(self, key: str, value: any) -> NoReturn:
        """Set a key to a specific value in the database or create one if it doesn't exist.
        
        Parameters
        -----------
        key: :class:`str`
            The name of the key to set.

        value: :class:`any`
            The value of the key.
        -----------
        """
        if not isinstance(key, str):
            print(f'Key name type must be str, got {type(key)}')
            return
        self.load()
        self.content[key] = value
        self.save()
    
    def append(self, key: str, value: any) -> NoReturn:
        """Append an item to a list or create one if it doesn't exist or it's from a different type.

        Parameters
        -----------
        key: :class:`str`
            The name of the key to append.

        value: :class:`any`
            The item of the key.
        -----------
        """
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

    def pop(self, key: str, index: int) -> NoReturn:
        """Pop an item in a list.

        Parameters
        -----------
        key: :class:`str`
            The name of the key to pop.

        index: :class:`int`
            Index of the item to remove.
        -----------
        """
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
    
    def get(self, key: str) -> any:
        """Return the key's value or None if it doesn't exist.

        Parameters
        -----------
        key: :class:`str`
            The name of the key to get.
        -----------
        """
        self.load()
        try:
            return self.content[key]
        except:
            return None
    
    def has(self, key: str) -> bool:
        """Returns a boolean checking whether a key exists or not in the database.

        Parameters
        -----------
        key: :class:`str`
            The name of the key to check.
        -----------
        """
        return self.get(key) is not None
    
    def delete(self, key: str) -> NoReturn:
        """Delete a key from the database.

        Parameters
        -----------
        key: :class:`str`
            The name of the key to delete.
        -----------
        """
        if not isinstance(key, str):
            print(f'Key name type must be str, got {type(key)}')
            return
        try:
            self.load()
            del self.content[key]
            self.save()
        except:
            pass
    
    def clear(self) -> NoReturn:
        """Clears all the database.

        .. warning::
            This will remove everything from the database and this action is irreversible, so you must use it carefully.
        """
        self.content = {}
        self.save()