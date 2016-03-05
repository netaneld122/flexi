# Flexi #

Flexi is a flexible utility that allows you to import and export any tree data structure.

### Recent Changes ###

* Version 1.0

### Usage example ###

#### Simple tree operations ####
```python
# Load the entire xml to memory
root = flexi.load('file.xml')

# Change existing values
root.some_existing_key.test = 3
root.some_existing_list[17].my_value = 3
del root.some_existing_list[17].test

# Create new sub trees
create_sub_tree(root, 'my_tree')
root.my_tree.new_value = 1.2

# Can be shortened to
create_sub_tree(root, 'a.b').value = 1
print root.a.b

# Dump all changes (can dump sub trees)
flexi.dump(root, 'file.xml')
flexi.dump(root.a, 'file.a.xml')
```

#### Adding xml serializers ####
```python
class MyDataHolder(object):
    data = None

@matches.xml_element('my_tag', attr='foobar')
@matches.python_type(MyDataHolder)
class MyTagSerializer(object):

    def tree_to_xml(self, name, my_data_holder, element):
        # ...

    def xml_to_tree(self, element, tree):
        # ...
```

### How do I get set up? ###
Make sure you have Python 2.7.

* setup.py install