<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="elements">Elements</a></h2>
<p>In FXML, an XML element represents one of the following:</p>
<ul>
<li>A class instance</li>
<li>A property of a class instance</li>
<li>A "static" property</li>
<li>A "define" block</li>
<li>A block of script code</li>
</ul>

<p>Class instances, instance properties, static properties, and define 
blocks are discussed in this section below. Scripting is discussed in a 
later section.</p>

<h3><a id="class_instance_elements">Class Instance Elements</a></h3>
<p>Class instances can be constructed in FXML in several ways. The most 
common is via instance declaration elements, which simply create a new 
instance of a class by name. Other ways of creating class instances 
include referencing existing values, copying existing values, and 
including external FXML files. Each is discussed in more detail below.</p>

<h4><a id="instance_declaration_elements">Instance Declarations</a></h4>
<p>If an element's tag is considered an instance declaration if the tag 
begins with uppercase letter (and the class is imported) or, as in Java,
 it denotes a fully-qualified (including the package name) name of a 
class. When the FXML loader (also introduced later) encounters such an 
element, it creates an instance of that class.</p>

<p>Importing a class is done using the "import" processing instruction (PI). For example, the following PI imports the <span class="code">javafx.scene.control.Label</span> class into the current FXML document’s namespace:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.Label?&gt;
</code></pre></div>

<p>This PI imports all classes from the javafx.scene.control package into the current namespace:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.*?&gt;
</code></pre></div>


<p>Any class that adheres to JavaBean constructor and property naming 
conventions can be readily instantiated and configured using FXML. The 
following is a simple but complete example that creates an instance of <span class="code">javafx.scene.control.Label</span> and sets its "text" property to "Hello, World!":</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.Label?&gt;
&lt;Label text="Hello, World!"/&gt;
</code></pre></div>

<p>Note that the <span class="code">Label</span>’s "text" property in 
this example is set using an XML attribute. Properties can also be set 
using nested property elements. Property elements are discussed in more 
detail later in this section. Property attributes are discussed in a 
later section.</p>

<p>Classes that don't conform to Bean conventions can also be 
constructed in FXML, using an object called a "builder". Builders are 
discussed in more detail later.</p>

<h5>Maps</h5>
<p>Internally, the FXML loader uses an instance of <span class="code">com.sun.javafx.fxml.BeanAdapter</span> to wrap an instantiated object and invoke its setter methods. This (currently) private class implements the <span class="code">java.util.Map</span> interface and allows a caller to get and set Bean property values as key/value pairs.</p>

<p>If an element represents a type that already implements <span class="code">Map</span> (such as <span class="code">java.util.HashMap</span>), it is not wrapped and its <span class="code">get()</span> and <span class="code">put()</span> methods are invoked directly. For example, the following FXML creates an instance of <span class="code">HashMap</span> and sets its "foo" and "bar" values to "123" and "456", respectively:

</p><div class="code-block"><div class="code-header">Example</div><pre><code>&lt;HashMap foo="123" bar="456"/&gt;
</code></pre></div>

<h5>fx:value</h5>
<p>The <span class="code">fx:value</span> attribute can be used to initialize an instance of a type that does not have a default constructor but provides a static <span class="code">valueOf(String)</span> method. For example, <span class="code">java.lang.String</span> as well as each of the primitive wrapper types define a <span class="code">valueOf()</span> method and can be constructed in FXML as follows:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;String fx:value="Hello, World!"/&gt;
&lt;Double fx:value="1.0"/&gt;
&lt;Boolean fx:value="false"/&gt;
</code></pre></div>

<p>Custom classes that define a static <span class="code">valueOf(String)</span> method can also be constructed this way.</p>

<h5>fx:factory</h5>
<p>The <span class="code">fx:factory</span> attribute is another means 
of creating objects whose classes do not have a default constructor. The
 value of the attribute is the name of a static, no-arg factory method 
for producing class instances. For example, the following markup creates
 an instance of an observable array list, populated with three string 
values:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;FXCollections fx:factory="observableArrayList"&gt;
    &lt;String fx:value="A"/&gt;
    &lt;String fx:value="B"/&gt;
    &lt;String fx:value="C"/&gt;
&lt;/FXCollections&gt;
</code></pre></div>

<h5>Builders</h5>
<p>A third means of creating instances of classes that do not conform to
 Bean conventions (such as those representing immutable values) is a 
"builder". The builder design pattern delegates object construction to a
 mutable helper class (called a "builder") that is responsible for 
manufacturing instances of the immutable type.</p>

<p>Builder support in FXML is provided by two interfaces. The <span class="code">javafx.util.Builder</span> interface defines a single method named <span class="code">build()</span> which is responsible for constructing the actual object:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>public interface Builder&lt;T&gt; {
    public T build();
}
</code></pre></div>

<p>A <span class="code">javafx.util.BuilderFactory</span> is responsible for producing builders that are capable of instantiating a given type:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>public interface BuilderFactory {
    public Builder&lt;?&gt; getBuilder(Class&lt;?&gt; type);
}
</code></pre></div>

<p>A default builder factory, <span class="code">JavaFXBuilderFactory</span>, is provided in the <span class="code">javafx.fxml</span>
 package. This factory is capable of creating and configuring most 
immutable JavaFX types. For example, the following markup uses the 
default builder to create an instance of the immutable <span class="code">javafx.scene.paint.Color</span> class:

</p><div class="code-block"><div class="code-header">Example</div><pre><code>&lt;Color red="1.0" green="0.0" blue="0.0"/&gt;
</code></pre></div>

<p>Note that, unlike Bean types, which are constructed when the 
element's start tag is processed, objects constructed by a builder are 
not instantiated until the element's closing tag is reached. This is 
because all of the required arguments may not be available until the 
element has been fully processed. For example, the Color object in the 
preceding example could also be written as:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;Color&gt;
    &lt;red&gt;1.0&lt;/red&gt;
    &lt;green&gt;0.0&lt;/green&gt;
    &lt;blue&gt;0.0&lt;/blue&gt;
&lt;/Color&gt;
</code></pre></div>

<p>The <span class="code">Color</span> instance cannot be fully constructed until all three of the color components are known.</p>

<p>When processing markup for an object that will be constructed by a builder, the <span class="code">Builder</span> instances are treated like value objects - if a <span class="code">Builder</span> implements the <span class="code">Map</span> interface, the <span class="code">put()</span> method is used to set the builder's attribute values. Otherwise, the builder is wrapped in a <span class="code">BeanAdapter</span> and its properties are assumed to be exposed via standard Bean setters.</p>

<h4><a id="include_elements">&lt;fx:include&gt;</a></h4>
<p>The <span class="code">&lt;fx:include&gt;</span> tag creates an object from FXML markup defined in another file. It is used as follows:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;fx:include source="<span class="variable">filename</span>"/&gt;
</code></pre></div>

<p>where <span class="variable">filename</span> is the name of the FXML 
file to include. Values that begin with a leading slash character are 
treated as relative to the classpath. Values with no leading slash are 
considered relative to the path of the current document.</p>

<p>For example, given the following markup:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.*?&gt;
&lt;?import javafx.scene.layout.*?&gt;
&lt;VBox xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;fx:include source="my_button.fxml"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre></div>

<p>If <span class="filename">my_button.fxml</span> contains the following:

</p><div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.*?&gt;
&lt;Button text="My Button"/&gt;
</code></pre></div>

<p>the resulting scene graph would contain a <span class="code">VBox</span> as a root object with a single <span class="code">Button</span> as a child node.</p>

<p>Note the use of the "fx" namespace prefix. This is a reserved prefix 
that defines a number of elements and attributes that are used for 
internal processing of an FXML source file. It is generally declared on 
the root element of a FXML document. Other features provided by the "fx"
 namespace are described in the following sections.</p>

<p><span class="code">&lt;fx:include&gt;</span> also supports attributes
 for specifying the name of the resource bundle that should be used to 
localize the included content, as well as the character set used to 
encode the source file. Resource resolution is discussed in a later 
section.</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;fx:include source="<span class="variable">filename</span>" resources="<span class="variable">resource_file</span>" charset="utf-8"/&gt;
</code></pre></div>

<h4><a id="constant_elements">&lt;fx:constant&gt;</a></h4>
<p>The <span class="code">&lt;fx:constant&gt;</span> element creates a 
reference to a class constant. For example, the following markup sets 
the value of the "minWidth" property of a<span class="code">Button</span> instance to the value of the <span class="code">NEGATIVE_INFINITY</span> constant defined by the <span class="code">java.lang.Double</span> class:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;Button&gt;
    &lt;minHeight&gt;&lt;Double fx:constant="NEGATIVE_INFINITY"/&gt;&lt;/minHeight&gt;
&lt;/Button&gt;
</code></pre></div>

<h4><a id="reference_elements">&lt;fx:reference&gt;</a></h4>
<p>The <span class="code">&lt;fx:reference&gt;</span> element creates a 
new reference to an existing element. Wherever this tag appears, it will
 effectively be replaced by the value of the named element. It is used 
in conjunction with either the <span class="code">fx:id</span> attribute
 or with a script variables, both of which are discussed in more detail 
in later sections. The "source" attribute of the <span class="code">&lt;fx:reference&gt;</span> element specifies the name of the object to which the new element will refer.</p>

<p>For example, the following markup assigns a previously-defined <span class="code">Image</span> instance named "myImage" to the "image" property of an <span class="code">ImageView</span> control:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;ImageView&gt;
    &lt;image&gt;
        &lt;fx:reference source="myImage"/&gt;
    &lt;/image&gt;
&lt;/ImageView&gt;
</code></pre></div>

<p>Note that, since it is also possible to dereference a variable using 
the attribute variable resolution operator (discussed later in the <a href="#attributes">Attributes</a> section), <span class="code">fx:reference</span>
 is generally only used when a reference value must be specified as an 
element, such as when adding the reference to a collection:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;ArrayList&gt;
    &lt;fx:reference source="element1"/&gt;
    &lt;fx:reference source="element2"/&gt;
    &lt;fx:reference source="element3"/&gt;
&lt;/ArrayList&gt;
</code></pre></div>

<p>For most other cases, using an attribute is simpler and more concise.</p>

<h4><a id="copy_elements">&lt;fx:copy&gt;</a></h4>
<p>The <span class="code">&lt;fx:copy&gt;</span> element creates a copy of an existing element. Like <span class="code">&lt;fx:reference&gt;</span>,
 it is used with the fx:id attribute or a script variable. The element's
 "source" attribute specifies the name of the object that will be 
copied. The source type must define a copy constructor that will be used
 to construct the copy from the source value.</p>

<p>At the moment, no JavaFX platform classes provide such a copy 
constructor, so this element is provided primarily for use by 
application developers. This may change in a future release.</p>

<h4><a id="root_elements">&lt;fx:root&gt;</a></h4>
<p>The <span class="code">&lt;fx:root&gt;</span> element creates a reference to a previously defined root element. It is only valid as the root node of an FXML document. <span class="code">&lt;fx:root&gt;</span> is used primarily when creating custom controls that are backed by FXML markup. This is discussed in more detail in the <a href="#fxmlloader">FXMLLoader</a> section.</p>

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

<h3><a id="static_property_elements">Static Properties</a></h3>
<p>An element may also represent a "static" property (sometimes called 
an "attached property"). Static properties are properties that only make
 sense in a particular context. They are not intrinsic to the class to 
which they are applied, but are defined by another class (often, the 
parent container of a control).</p>

<p>Static properties are prefixed with the name of class that defines 
them. For example, The following FXML invokes the static setter for <span class="code">GridPane</span>'s "rowIndex" and "columnIndex" properties:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;GridPane&gt;
    &lt;children&gt;
        &lt;Label text="My Label"&gt;
            &lt;GridPane.rowIndex&gt;0&lt;/GridPane.rowIndex&gt;
       &lt;GridPane.columnIndex&gt;0&lt;/GridPane.columnIndex&gt;
        &lt;/Label&gt;
    &lt;/children&gt;
&lt;/TabPane&gt;
</code></pre></div>

<p>This translates roughly to the following in Java:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>GridPane gridPane = new GridPane();

Label label = new Label();
label.setText("My Label");

GridPane.setRowIndex(label, 0);
GridPane.setColumnIndex(label, 0);

gridPane.getChildren().add(label);
</code></pre></div>

<p>
The calls to <span class="code">GridPane#setRowIndex()</span> and <span class="code">GridPane#setColumnIndex()</span> "attach" the index data to the <span class="code">Label</span> instance. <span class="code">GridPane</span> then uses these during layout to arrange its children appropriately. Other containers, including <span class="code">AnchorPane</span>, <span class="code">BorderPane</span>, and <span class="code">StackPane</span>, define similar properties.</p>

<p>As with instance properties, static property elements are generally 
used when the property value cannot be efficiently represented by an 
attribute value. Otherwise, static property attributes (discussed in a 
later section) will generally produce more concise and readable markup.</p>

<h3><a id="define_elements">Define Blocks</a></h3>
<p>The <span class="code">&lt;fx:define&gt;</span> element is used to create objects that exist outside of the object hierarchy but may need to be referred to elsewhere.</p>

<p>For example, when working with radio buttons, it is common to define a <span class="code">ToggleGroup</span>
 that will manage the buttons' selection state. This group is not part 
of the scene graph itself, so should not be added to the buttons' 
parent. A define block can be used to create the button group without 
interferering with the overall structure of the document:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;VBox&gt;
    &lt;fx:define&gt;
        &lt;ToggleGroup fx:id="myToggleGroup"/&gt;
    &lt;/fx:define&gt;
    &lt;children&gt;
        &lt;RadioButton text="A" toggleGroup="$myToggleGroup"/&gt;
        &lt;RadioButton text="B" toggleGroup="$myToggleGroup"/&gt;
        &lt;RadioButton text="C" toggleGroup="$myToggleGroup"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre></div>

<p>Elements in define blocks are usually assigned an ID that can be used
 to refer to the element's value later. IDs are discussed in more detail
 in later sections.</p>
    <div class="info-alert"><strong>HTML Analogy:</strong> Like HTML tags that instantiate DOM nodes (e.g. <code>&lt;div&gt;</code>, <code>&lt;input&gt;</code>), FXML elements define class instances. FXML also allows elements to define properties, similar to how some HTML elements act as configuration for their parents (e.g. <code>&lt;source&gt;</code> inside <code>&lt;video&gt;</code>).</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;!-- HTML Elements --&gt;
&lt;form action="/submit"&gt;
  &lt;!-- Instance declaration --&gt;
  &lt;input type="text" name="username" /&gt;
  &lt;button type="submit"&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/overview" class="btn btn-prev">❮ Overview</router-link>
      <router-link to="/fxml/class-instance-elements" class="btn btn-next">Class Instance Elements ❯</router-link>
    </div>
  </article>
</template>
