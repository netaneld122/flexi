from flexi.xml import element_maker
from flexi.xml import matches


class ParamSerializer(object):

    def tree_to_xml(self, name, value, element):
        param_type = self.xml_element.get('type')
        sub_element = element_maker.make('param', value, type=param_type, name=name)
        element.append(sub_element)
        return element

    def xml_to_tree(self, element, tree):
        tree[element.get('name')] = self.python_type(element.pyval)
        return tree


@matches.xml_element('param', type='long')
@matches.python_type(int)
class LongParamSerializer(ParamSerializer):
    pass


@matches.xml_element('param', type='double')
@matches.python_type(float)
class DoubleParamSerializer(ParamSerializer):
    pass


@matches.xml_element('param', type='string')
@matches.python_type(str)
class StringParamSerializer(ParamSerializer):
    pass


@matches.xml_element('param', type='bool')
@matches.python_type(bool)
class BoolParamSerializer(ParamSerializer):
    pass
