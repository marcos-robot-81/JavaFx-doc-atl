<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="property_elements">Property Elements</a></h3>
<p>Elements whose tag names begin with a lowercase letter represent 
object properties. A property element may represent one of the 
following:</p>

<ul>
<li>A property setter</li>
<li>A read-only list property</li>
<li>A read-only map property</li>
</ul>

<h4><a id="property_setter_elements">Property Setters</a></h4>
<p>If an element represents a property setter, the contents of the 
element (which must be either a text node or a nested class instance 
element) are passed as the value to the setter for the property.</p>

<p>For example, the following FXML creates an instance of the <span class="code">Label</span> class and sets the value of the label's "text" property to "Hello, World!":</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.Label?&gt;
&lt;Label&gt;
    &lt;text&gt;Hello, World!&lt;/text&gt;
&lt;/Label&gt;
</code></pre></div>

<p>This produces the same result as the earlier example which used an attribute to set the "text" property:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.Label?&gt;
&lt;Label text="Hello, World!"/&gt;
</code></pre></div>

<p>Property elements are generally used when the property value is a 
complex type that can't be represented using a simple string-based 
attribute value, or when the character length of the value is so long 
that specifying it as an attribute would have a negative impact on 
readability.</p>

<h5>Type Coercion</h5>
<p>FXML uses "type coercion" to convert property values to the 
appropriate type as needed. Type coercion is required because the only 
data types supported by XML are elements, text, and attributes (whose 
values are also text). However, Java supports a number of different data
 types including built-in primitive value types as well as extensible 
reference types.</p>

<p>The FXML loader uses the <span class="code">coerce()</span> method of <span class="code">BeanAdapter</span> to perform any required type conversions. This method is capable of performing basic primitive type conversions such as <span class="code">String</span> to <span class="code">boolean</span> or <span class="code">int</span> to <span class="code">double</span>, and will also convert <span class="code">String</span> to <span class="code">Class</span> or <span class="code">String</span> to <span class="code">Enum</span>. Additional conversions can be implemented by defining a static <span class="code">valueOf()</span> method on the target type.</p>

<h4><a id="read_only_list_property_elements">Read-Only List Properties</a></h4>
<p>A read-only list property is a Bean property whose getter returns an instance of <span class="code">java.util.List</span>
 and has no corresponding setter method. The contents of a read-only 
list element are automatically added to the list as they are processed.</p>

<p>For example, the "children" property of <span class="code">javafx.scene.Group</span> is a read-only list property representing the group's child nodes:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.*?&gt;
&lt;?import javafx.scene.shape.*?&gt;
&lt;Group xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Rectangle fx:id="rectangle" x="10" y="10" width="320" height="240"
            fill="#ff0000"/&gt;
        ...
    &lt;/children&gt;
&lt;/Group&gt;
</code></pre></div>

<p>As each sub-element of the <span class="code">&lt;children&gt;</span> element is read, it is added to the list returned by <span class="code">Group#getChildren()</span>.

</p><h4><a id="read_only_map_property_elements">Read-Only Map Properties</a></h4>
<p>A read-only map property is a bean property whose getter returns an instance of <span class="code">java.util.Map</span>
 and has no corresponding setter method. The attributes of a read-only 
map element are applied to the map when the closing tag is processed.</p>

<p>The "properties" property of <span class="code">javafx.scene.Node</span> is an example of a read-only map property. The following markup sets the "foo" and "bar" properties of a <span class="code">Label</span> instance to "123" and "456", respectively:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.*?&gt;
&lt;Button&gt;
    &lt;properties foo="123" bar="456"/&gt;
&lt;/Button&gt;
</code></pre></div>

<p>Note that a read-only property whose type is neither a <span class="code">List</span> nor a <span class="code">Map</span> will be treated as if it were a read-only map. The return value of the getter method will be wrapped in a <span class="code">BeanAdapter</span> and can be used in the same way as any other read-only map.</p>

<h4><a id="default_properties">Default Properties</a></h4>
<p>A class may define a "default property" using the <span class="code">@DefaultProperty</span> annotation defined in the <span class="code">javafx.beans</span> package. If present, the sub-element representing the default property can be omitted from the markup.</p>

<p>For example, since <span class="code">javafx.scene.layout.Pane</span> (the superclass of <span class="code">javafx.scene.layout.VBox</span>) defines a default property of "children", a <span class="code">&lt;children&gt;</span> element is not required; the loader will automatically add the sub-elements of the <span class="code">VBox</span> to the container's "children" collection:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.*?&gt;
&lt;?import javafx.scene.shape.*?&gt;
&lt;VBox xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;Button text="Click Me!"/&gt;
    ...
&lt;/VBox&gt;
</code></pre></div>

<p>Note that default properties are not limited to collections. If an 
element's default property refers to a scalar value, any sub-element of 
that element will be set as the value of the property.</p>

<p>For example, since <span class="code">javafx.scene.control.ScrollPane</span> defines a default property of "content", a scroll pane containing a <span class="code">TextArea</span> as its content can be specified as follows:

</p><div class="code-block"><div class="code-header">Example</div><pre><code>&lt;ScrollPane&gt;
    &lt;TextArea text="Once upon a time..."/&gt;
&lt;/ScrollPane&gt;
</code></pre></div>

<p>Taking advantage of default properties can significantly reduce the verbosity of FXML markup.</p>
    <div class="info-alert"><strong>HTML Analogy:</strong> Property elements in FXML are similar to how HTML handles complex properties that are too large for attributes. For example, a <code>&lt;select&gt;</code> element uses nested <code>&lt;option&gt;</code> tags to define its list of options, rather than a single attribute string.</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;!-- HTML Property-like Elements --&gt;
&lt;select name="cars"&gt;
  &lt;!-- The options act as a read-only list property of select --&gt;
  &lt;option value="volvo"&gt;Volvo&lt;/option&gt;
  &lt;option value="saab"&gt;Saab&lt;/option&gt;
&lt;/select&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/fx-root" class="btn btn-prev">❮ &lt;fx:root&gt;</router-link>
      <router-link to="/fxml/property-setters" class="btn btn-next">Property Setters ❯</router-link>
    </div>
  </article>
</template>
