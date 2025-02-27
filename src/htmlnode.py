class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()
  
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