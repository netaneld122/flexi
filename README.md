# Flexi #

Flexi is a flexible utility that allows you to import and export any tree data structure.

### Recent Changes ###

* Version 1.0

### Usage example ###

#### Simple tree operations ####
```python
# Load the entire xml to memory
root = flexi.xml.load('file.xml')
# Change existing values
root.some_existing_key.test = 3

# Create new sub trees
create_sub_tree(root, 'my_tree')
root.my_tree.new_value = 1.2

# Can be shortened to
create_sub_tree(root, 'a.b').value = 1
print root.a.b

# Dump all changes 
flexi.xml.dump(root, 'file.xml')

# Can also dump a sub tree
flexi.xml.dump(root.a, 'file.xml')
```

#### Adding xml serializers ####
```python
class MyDadaHolder(object):
    data = None

@matches.xml_element('my_tag', attr='foobar')
@matches.python_type(MyDadaHolder)
class MyTagSerializer(object):

    def tree_to_xml(self, name, my_data_holder, element):
        # ...

    def xml_to_tree(self, element, tree):
        # ...
```

### How do I get set up? ###
Make sure you have Python 2.7.

* setup.py install