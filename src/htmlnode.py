
class HTMLNode:
    def __init__(self, tag= None, value= None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def TO_HTML(self):
        raise NotImplementedError("to_html method not implemented")
    
    def PROPS_TO_HTML(self):
        if self.props is None:
            return ""
        htmlprops = ""
        for key in self.props:
            htmlprops += f' {key}="{self.props[key]}"'
        return htmlprops
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
            
    def __repr__(self):
        return f"HTMLNode('{self.tag}', '{self.value}', '{self.children}', '{self.props}')"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def TO_HTML(self):
        if self.value == None:
            raise ValueError("missing value")
        if self.tag == None:
            return self.value       
        return f"<{self.tag}{self.PROPS_TO_HTML()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
    
    def TO_HTML(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.TO_HTML()
        return f"<{self.tag}{self.PROPS_TO_HTML()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    


    
        