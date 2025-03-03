class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    props = self.props
    if props is None:
      return ""
    html_prop_value_list = []
    for prop_name, prop_value in sorted(props.items()):
      html_prop_value_list.append(f'{prop_name}="{prop_value}"')
    return " ".join(html_prop_value_list)
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

  def __eq__(self, other):
    if not isinstance(other, HTMLNode):
      return False
    return (
      self.tag == other.tag and
      self.value == other.value and
      self.children == other.children and
      self.props == other.props
    )

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None,  props)

  def to_html(self):
    if self.value is None:
      raise ValueError("invalid HTML: no value")
    if self.tag is None:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)
  
  def to_html(self):
    if self.tag == None:
      raise ValueError("invalid: no tag")
    if self.children == None:
      raise ValueError("invalid: no children")
    children_html = ""
    for child in self.children:
      children_html += child.to_html()
    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
  
  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
