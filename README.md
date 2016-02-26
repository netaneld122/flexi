# Flexi #

Flexi is a flexible utility that allows you to import and export any tree data structure.

### Recent Changes ###

* Version 1.0

### Usage example ###

**Standard serialization routines**
```python
root = flexi.json.load('file.json')
root.some_existing_key.test = 3
root.new('my_tree').new_value = [1, 2, 3]
flexi.xml.dump(root, 'file.xml')
```

### How do I get set up? ###
Make sure you have Python 2.7.

* setup.py install