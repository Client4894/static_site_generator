
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # An HTMLNode without a tag will just render as raw text
        self.value = value # An HTMLNode without a value will be assumed to have children
        self.children = children # An HTMLNode without children will be assumed to have a value
        self.props = props # An HTMLNode without props simply won't have any attributes

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'        
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
