# Flexi #

Flexi is a flexible utility that allows you to import and export any tree data structure.

### Recent Changes ###

* Version 1.0

### Usage example ###

```python
# Load the entire json to memory
root = flexi.json.load('file.json')
# Change existing values
root.some_existing_key.test = 3

# Add new sub trees
root.new('my_tree')
root.my_tree.new_value = [1, 2, 3]

# Can be shortened to
root.new('a.b').value = 1
print root.a.b

# Dump all changes 
flexi.xml.dump(root, 'file.xml')

# Can also dump a sub tree
flexi.xml.dump(root.a, 'file.xml')
```

### How do I get set up? ###
Make sure you have Python 2.7.

* setup.py install