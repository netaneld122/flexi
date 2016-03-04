import lxml.objectify


def remove_objectify_garbage(element):
    lxml.etree.strip_attributes(element, '{http://www.w3.org/2001/XMLSchema-instance}nil')
    lxml.etree.cleanup_namespaces(element)
    return element


def make(tag, text=None, **attributes):
    maker = lxml.objectify.ElementMaker(annotate=False)
    element = getattr(maker, tag)(text, **attributes)
    return remove_objectify_garbage(element)
