## saytdb
saytdb is a JSON database I made, with very little python knowledge. It's pretty basic right now, but I will try to get better.

### Getting started
First of all, you will need to append the folder of the database to `sys.path` in order to be able to import it. There are many other ways, but I think it's the easiest. You can learn more about sys.path [here.](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)
```py
import sys
import os
sys.path.append(os.path.abspath('FOLDER of database.py'))
```

If you don't have a folder for it, just write a dot.

```py
sys.path.append(os.path.abspath('.'))
```

Now we are ready to start!

## Creating a database
This will be our setup for the database. You can of course, change it as you want.

![Setup](https://i.imgur.com/8x1RjSo.png)

database.py file will be this module. test.json will be an empty json file with just `{}` as content. main.py will be our main file.

To create a database, you can use this:
```py
import database

# "database/test.json" is the location of the json file, but you can just type the route of the actual json. If it doesn't exist, it will throw an error.
test = database.create('database/test.json')
```
**Good job!** You have now created your database.
Now, let's take use of it!
```py
# In this case we will set some data.
import database
test = database.create('database/test.json')
test.set('hello', 'world')
print(test.get('hello'))
```

In test.json file, you will see something like this:
```json
{
    "hello": "world"
}
``` 
And in the console, you will see this:

```world```

Very easy, right? There are more methods and properties you can use.

## Note
All the properties and methods correspond to `database.create` class, not `database` itself.

## Properties
### content
Return all the content from the database.

### path
Return the path to the database.

## Methods
### append
Append an item to a list in the specified key. It will create one if it doesn't exist or the value isn't a list.

__Usage:__
```py
append('key_name', 'value')
```

### clear
Clear the database and its content completely. This cannot be undone, use it carefully!

__Usage:__
```py
clear()
```

### delete
Delete a key from the database.

__Usage:__
```py
delete('key')
```

### get
Get a key from the database. Returns the key's value or None is not found. 

__Usage:__
```py
get('key')
```

### has
Returns a boolean indicating whether the key exists or not in database.

__Usage:__
```py
has('key')
```

### load
Load the content from database file. Useful if you have multiple files using the same database.

__Usage:__
```py
load()
```

### pop
Remove the specified index from a list with the specified key.

__Usage:__
```py
index = 0 # index of item to remove
pop('key', index)
```

### save
Save the current content to the database file. You won't need this one unless it's a very specific case, since it already saves for you.

__Usage:__
```py
save()
```

### set
Create a key with the specified value or replace it if it already exists.

__Usage:__
```py
set('key', 'value')
```