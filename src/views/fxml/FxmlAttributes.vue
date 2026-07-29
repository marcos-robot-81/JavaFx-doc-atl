<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="attributes">Attributes</a></h2>
      <p>An attribute in FXML may represent one of the following:</p>
      <ul>
        <li>A property of a class instance</li>
        <li>A "static" property</li>
        <li>An event handler</li>
      </ul>

      <p>Each are discussed in more detail in the following sections.</p>

      <h3><a id="instance_property_attributes">Instance Properties</a></h3>
      <p>
        Like property elements, attributes can also be used to configure the
        properties of a class instance. For example, the following markup
        creates a <span class="code">Button</span> whose text reads "Click Me!":
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.control.*?&gt;
&lt;Button text="Click Me!"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <button class="javafx-btn">Click Me!</button>
      </JavaFxPreview>

      <p>
        As with property elements, property attributes support type coercion.
        When the following markup is processed, the "x", "y", "width", and
        "height" values will be converted to doubles, and the "fill" value will
        be converted to a <span class="code">Color</span>:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;Rectangle&gt;</code>, remember to add <code>&lt;?import javafx.scene.shape.Rectangle?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Rectangle fx:id="rectangle" x="10" y="10" width="320" height="240"
    fill="#ff0000"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="width: 320px; height: 240px; background-color: #ff0000;"></div>
      </JavaFxPreview>

      <p>
        Unlike property elements, which are applied as they are processed,
        property attributes are not applied until the closing tag of their
        respective element is reached. This is done primarily to facilitate the
        case where an attribute value depends on some information that won't be
        available until after the element's content has been completely
        processed (for example, the selected index of a
        <span class="code">TabPane</span> control, which can't be set until all
        of the tabs have been added).
      </p>

      <p>
        Another key difference between property attributes and property elements
        in FXML is that attributes support a number of "resolution operators"
        that extend their functionality. The following operators are supported
        and are discussed in more detail below:
      </p>

      <ul>
        <li>Location resolution</li>
        <li>Resource resolution</li>
        <li>Variable resolution</li>
      </ul>

      <h4><a id="location_resolution">Location Resolution</a></h4>
      <p>
        As strings, XML attributes cannot natively represent typed location
        information such as a URL. However, it is often necessary to specify
        such locations in markup; for example, the source of an image resource.
        The location resolution operator (represented by an "@" prefix to the
        attribute value) is used to specify that an attribute value should be
        treated as a location relative to the current file rather than a simple
        string.
      </p>

      <p>
        For example, the following markup creates an ImageView and populates it
        with image data from <span class="filename">my_image.png</span>, which
        is assumed to be located at a path relative to the current FXML file:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;ImageView&gt;</code> and <code>&lt;Image&gt;</code>, remember to add <code>&lt;?import javafx.scene.image.ImageView?&gt;</code> and <code>&lt;?import javafx.scene.image.Image?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;ImageView&gt;
    &lt;image&gt;
        &lt;Image url="@my_image.png"/&gt;
    &lt;/image&gt;
&lt;/ImageView&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="width: 100px; height: 100px; background: #ddd; display: flex; align-items: center; justify-content: center; border: 1px solid #aaa;">my_image.png</div>
      </JavaFxPreview>

      <p>
        Since <span class="code">Image</span> is an immutable object, a builder
        is required to construct it. Alternatively, if
        <span class="code">Image</span> were to define a
        <span class="code">valueOf(URL)</span> factory method, the image view
        could be populated as follows:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;ImageView&gt;</code>, remember to add <code>&lt;?import javafx.scene.image.ImageView?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;ImageView image="@my_image.png"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="width: 100px; height: 100px; background: #ddd; display: flex; align-items: center; justify-content: center; border: 1px solid #aaa;">my_image.png</div>
      </JavaFxPreview>

      <p>
        The value of the "image" attribute would be converted to a URL by the
        FXML loader, then coerced to an <span class="code">Image</span> using
        the <span class="code">valueOf()</span> method.
      </p>

      <p>
        Note that whitespace values in the URL must be encoded; for example, to
        refer to a file named "My Image.png", the FXML document should contain
        the following:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;Image&gt;</code>, remember to add <code>&lt;?import javafx.scene.image.Image?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Image url="@My%20Image.png"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="width: 100px; height: 100px; background: #ddd; display: flex; align-items: center; justify-content: center; border: 1px solid #aaa;">My Image.png</div>
      </JavaFxPreview>

      <p>rather than:</p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;Image&gt;</code>, remember to add <code>&lt;?import javafx.scene.image.Image?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Image url="@My Image.png"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="width: 100px; height: 100px; background: #f8d7da; color: #721c24; display: flex; align-items: center; justify-content: center; border: 1px solid #f5c6cb;">Error: unencoded space</div>
      </JavaFxPreview>

      <h4><a id="resource_resolution">Resource Resolution</a></h4>

      <p>
        In FXML, resource substitution can be performed at load time for
        localization purposes. When provided with an instance of
        <span class="code">java.util.ResourceBundle</span>, the FXML loader will
        replace instances of resource names with their locale-specific values.
        Resource names are identified by a "%" prefix, as shown below:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;Label&gt;</code>, remember to add <code>&lt;?import javafx.scene.control.Label?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Label text="%myText"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <span class="javafx-label">%myText</span>
      </JavaFxPreview>

      <p>If the loader is given a resource bundle defined as follows:</p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>myText = This is the text!
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 5px; background: #eee; font-family: monospace;">myText = This is the text!</div>
      </JavaFxPreview>

      <p>
        the output of the FXML loader would be a
        <span class="code">Label</span> instance containing the text "This is
        the text!".
      </p>

      <h4><a id="variable_resolution">Variable Resolution</a></h4>
      <p>
        An FXML document defines a variable namespace in which named elements
        and script variables may be uniquely identified. The variable resolution
        operator allows a caller to replace an attribute value with an instance
        of a named object before the corresponding setter method is invoked.
        Variable references are identified by a "$" prefix, as shown below:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;ToggleGroup&gt;</code> and <code>&lt;RadioButton&gt;</code>, remember to add <code>&lt;?import javafx.scene.control.ToggleGroup?&gt;</code> and <code>&lt;?import javafx.scene.control.RadioButton?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;fx:define&gt;
    &lt;ToggleGroup fx:id="myToggleGroup"/&gt;
&lt;/fx:define&gt;
...
&lt;RadioButton text="A" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="B" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="C" toggleGroup="$myToggleGroup"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <label class="javafx-radiobutton"><input type="radio" name="myToggleGroup" /> A</label>
          <label class="javafx-radiobutton"><input type="radio" name="myToggleGroup" /> B</label>
          <label class="javafx-radiobutton"><input type="radio" name="myToggleGroup" /> C</label>
        </div>
      </JavaFxPreview>

      <p>
        Assigning an <span class="code">fx:id</span> value to an element creates
        a variable in the document's namespace that can later be referred to by
        variable dereference attributes, such as the "toggleGroup" attribute
        shown above, or in script code, discussed in a later section.
        Additionally, if the object's type defines an "id" property, this value
        will also be passed to the objects
        <span class="code">setId()</span> method.
      </p>

      <h4><a id="escape_sequences">Escape Sequences</a></h4>

      <p>
        If the value of an attribute begins with one of the resource resolution
        prefixes, the character can be escaped by prepending it with a leading
        backslash ("\") character. For example, the following markup creates a
        <span class="code">Label</span> instance whose text reads "$10.00":
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;Label&gt;</code>, remember to add <code>&lt;?import javafx.scene.control.Label?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Label text="\$10.00"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <span class="javafx-label">$10.00</span>
      </JavaFxPreview>

      <h4><a id="expression_binding">Expression Binding</a></h4>
      <p>
        Attribute variables as shown above are resolved once at load time. Later
        updates to the variables value are not automatically reflected in any
        properties to which the value was assigned. In many cases, this is
        sufficient; however, it is often convenient to "bind" a property value
        to a variable or expression such that changes to the variable are
        automatically propagated to the target property. Expression bindings can
        be used for this purpose.
      </p>

      <p>
        An expression binding also begins with the variable resolution operator,
        but is followed by a set of curly braces which wrap the expression
        value. For example, the following markup binds the value of a text
        input's "text" property to the "text" property of a
        <span class="code">Label</span> instance:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;TextField&gt;</code> and <code>&lt;Label&gt;</code>, remember to add <code>&lt;?import javafx.scene.control.TextField?&gt;</code> and <code>&lt;?import javafx.scene.control.Label?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;TextField fx:id="textField"/&gt;
&lt;Label text="${textField.text}"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-hbox">
          <input type="text" class="javafx-textfield" value="Type here..." />
          <span class="javafx-label">Type here...</span>
        </div>
      </JavaFxPreview>

      <p>
        As the user types in the text input, the label's text content will be
        automatically updated.
      </p>

      <p>
        More complex expression are also supported. A list of supported
        constants and operators follows:
      </p>

      <table>
        <caption>
          Constants and Operators Table
        </caption>
        <tbody>
          <tr>
            <th scope="col">Constant / Operator</th>
            <th scope="col">Description</th>
          </tr>
          <tr>
            <th scope="row">"string"<br />'string'</th>
            <td>A string constant</td>
          </tr>
          <tr>
            <th scope="row">true<br />false</th>
            <td>A boolean constant</td>
          </tr>
          <tr>
            <th scope="row">null</th>
            <td>A constant representing the null value</td>
          </tr>
          <tr>
            <th scope="row">50.0<br />3e5<br />42</th>
            <td>A numerical constant</td>
          </tr>
          <tr>
            <th scope="row">- <br />(unary operator)</th>
            <td>Unary minus operator, applied on a number</td>
          </tr>
          <tr>
            <th scope="row">! <br />(unary operator)</th>
            <td>Unary negation of a boolean</td>
          </tr>
          <tr>
            <th scope="row">
              + - <br />
              * / %
            </th>
            <td>Numerical binary operators</td>
          </tr>
          <tr>
            <th scope="row">&amp;&amp; ||</th>
            <td>Boolean binary operators</td>
          </tr>
          <tr>
            <th scope="row">
              &gt; &gt;= <br />
              &lt; &lt;= <br />
              == !=
            </th>
            <td>
              Binary operators of comparison.<br />
              Both arguments must be of type Comparable
            </td>
          </tr>
        </tbody>
      </table>

      <h3><a id="static_property_attributes">Static Properties</a></h3>
      <p>
        Attributes representing static properties are handled similarly to
        static property elements and use a similar syntax. For example, the
        earlier <span class="code">GridPane</span> markup shown earlier to
        demonstrate static property elements could be rewritten as follows:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;GridPane&gt;</code>, <code>&lt;Label&gt;</code> and <code>&lt;TabPane&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.GridPane?&gt;</code>, <code>&lt;?import javafx.scene.control.Label?&gt;</code> and <code>&lt;?import javafx.scene.control.TabPane?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;GridPane&gt;
    &lt;children&gt;
        &lt;Label text="My Label" GridPane.rowIndex="0" GridPane.columnIndex="0"/&gt;
    &lt;/children&gt;
&lt;/TabPane&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-gridpane">
          <span class="javafx-label">My Label</span>
        </div>
      </JavaFxPreview>

      <p>
        In addition to being more concise, static property attributes, like
        instance property attributes, support location, resource, and variable
        resolution operators, the only limitation being that it is not possible
        to create an expression binding to a static property.
      </p>

      <h3><a id="event_handler_attributes">Event Handlers</a></h3>
      <p>
        Event handler attributes are a convenient means of attaching behaviors
        to document elements. Any class that defines a
        <span class="code">setOn<span class="variable">Event</span>()</span>
        method can be assigned an event handler in markup.
      </p>

      <p>
        FXML supports three types of event handler attributes: script event
        handlers, controller method event handlers and expressions. Each are
        discussed below.
      </p>

      <h4><a id="script_event_handlers">Script Event Handlers</a></h4>
      <p>
        A script event handler is an event handler that executes script code
        when the event is fired, similar to event handlers in HTML. For example,
        the following script-based handler for the button's "onAction" event
        uses JavaScript to write the text "You clicked me!" to the console when
        the user presses the button:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code> and <code>&lt;Button&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> and <code>&lt;?import javafx.scene.control.Button?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?language javascript?&gt;
...

&lt;VBox&gt;
    &lt;children&gt;
        &lt;Button text="Click Me!"
            onAction="java.lang.System.out.println('You clicked me!');"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>

      <p>
        Note the use of the language processing instruction at the beginning of
        the code snippet. This PI tells the FXML loader which scripting language
        should be used to execute the event handler. A page language must be
        specified whenever inline script is used in an FXML document, and can
        only be specified once per document. However, this does not apply to
        external scripts, which may be implemented using any number of supported
        scripting languages. Scripting is discussed in more detail in the next
        section.
      </p>

      <p>
        Note: to turn off automatic compilation of script code place the
        processing instruction
        <span class="code">&lt;?compile false?&gt;</span> before the element
        that contains the script. To turn on compilation of script code again
        use the processing instruction
        <span class="code">&lt;?compile true?&gt;</span> (or short:
        <span class="code">&lt;?compile?&gt;</span>). The compile processing
        instruction can be used repeatedly to turn compilation of script code
        off and on.
      </p>

      <p>
        <strong>Note:</strong> The JavaScript script engine is disabled by
        default. If the JDK has a JavaScript script engine, it can be enabled
        using a system property <span class="code">javafx.allowjs=true.</span>
      </p>

      <h4>
        <a id="controller_method_event_handlers"
          >Controller Method Event Handlers</a
        >
      </h4>
      <p>
        A controller method event handler is a method defined by a document's
        "controller". A controller is an object that is associated with the
        deserialized contents of an FXML document and is responsible for
        coordinating the behaviors of the objects (often user interface
        elements) defined by the document.
      </p>

      <p>
        A controller method event handler is specified by a leading hash symbol
        followed by the name of the handler method. For example:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code> and <code>&lt;Button&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> and <code>&lt;?import javafx.scene.control.Button?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Button text="Click Me!" onAction="#handleButtonAction"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>

      <p>
        Note the use of the <span class="code">fx:controller</span> attribute on
        the root element. This attribute is used to associate a controller class
        with the document. If <span class="code">MyController</span> is defined
        as follows:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

public class MyController {
    public void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
    }
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Controller Method: handleButtonAction(ActionEvent)</div>
      </JavaFxPreview>

      <p>
        the <span class="code">handleButtonAction()</span> will be called when
        the user presses the button, and the text "You clicked me!" will be
        written to the console.
      </p>

      <p>
        In general, a handler method should conform to the signature of a
        standard event handler; that is, it should take a single argument of a
        type that extends <span class="code">javafx.event.Event</span> and
        should return void (similar to an event delegate in C#). The event
        argument often carries important and useful information about the nature
        of the event; however, it is optional and may be omitted if desired. So
        this is also a valid handler:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

public class MyController {
    public void handleButtonAction() {
        System.out.println("You clicked me!");
    }
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Controller Method: handleButtonAction() [No args]</div>
      </JavaFxPreview>

      <p>Controllers are discussed in more detail in a later section.</p>

      <h4><a id="expression_handlers">Event handlers from expressions</a></h4>
      <p>
        Any expression that point to a
        <a href="#variable_resolution">variable</a> of javafx.event.EventHandler
        type can be used as an expression handler.
      </p>
      <p>Previous example using an expression handler:</p>
      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code> and <code>&lt;Button&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> and <code>&lt;?import javafx.scene.control.Button?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Button text="Click Me!" onAction="$controller.onActionHandler"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>

      <p>With the controller that contains a field like this</p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public class MyController {

    @FXML
    public EventHandler&lt;ActionEvent&gt; onActionHandler = new EventHandler&lt;&gt;() { ... }

    ...
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Field: onActionHandler = new EventHandler&lt;&gt;() {...}</div>
      </JavaFxPreview>

      <p>
        Note that other kinds of expressions, like
        <a href="#expression_binding">binding expressions</a> are not supported
        in this context.
      </p>

      <h4>
        <a id="collections_and_property_handlers"
          >Special handlers for collections and properties</a
        >
      </h4>
      <p>
        Collections and object properties cannot be listen to using
        <span class="code">setOn<span class="variable">Event</span>()</span>
        methods. For these reason, special handler methods need to be used.
        <span class="code">ObservableList</span>,
        <span class="code">ObservableMap</span> or
        <span class="code">ObservableSet</span> uses a special
        <span class="code">onChange</span> attribute that points to a handler
        method with a <span class="code">ListChangeListener.Change</span>,
        <span class="code">MapChangeListener.Change</span> or
        <span class="code">SetChangeListener.Change</span> parameter,
        respectively.
      </p>
      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children onChange="#handleChildrenChange"/&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #eee; border: 1px dashed #ccc; font-size: 12px; color: #666;">VBox (Listening to children changes)</div>
      </JavaFxPreview>

      where the handler method looks like this:

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

import javafx.collections.ListChangeListener.Change;

public class MyController {
    public void handleChildrenChange(ListChangeListener.Change c) {
        System.out.println("Children changed!");
    }
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Method: handleChildrenChange(ListChangeListener.Change)</div>
      </JavaFxPreview>

      <p>
        Similarly, the property handlers are methods that have the same
        parameters as changed method of ChangeListener :
      </p>
      <p>
        <span class="code"
          >changed(ObservableValue&lt;? extends T&gt; observable, T oldValue, T
          newValue)</span
        >
      </p>

      <p>A handler for parent property would look like this</p>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public class MyController {
    public void handleParentChange(ObservableValue value, Parent oldValue, Parent newValue) {
        System.out.println("Parent changed!");
    }
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Method: handleParentChange(...)</div>
      </JavaFxPreview>

      <p>
        For convenience, the first parameter can be a subclass of
        <span class="code">ObservableValue</span>, e.g.
        <span class="code">Property</span>
      </p>

      <p>
        For registering to a property, a special
        <span class="code">on&lt;propertyName&gt;Change</span> attribute must be
        used.
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml" onParentChange="#handleParentChange"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #eee; border: 1px dashed #ccc; font-size: 12px; color: #666;">VBox (Listening to parent changes)</div>
      </JavaFxPreview>

      <p>
        Note that collections and properties do not currently support scripting
        handlers.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, elements use attributes for
        configuring layout, linking resources, assigning IDs/classes, and
        hooking up event handlers (e.g., <code>onclick="handleClick()"</code>).
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code class="language-html">&lt;!-- HTML Analogy for Attributes in General --&gt;
&lt;button id="myBtn" class="primary" onclick="alert('Clicked!')" data-custom="value"&gt;
  Click Me!
&lt;/button&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <button id="myBtn" class="javafx-btn" onclick="alert('Clicked!')" data-custom="value">Click Me!</button>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link to="/fxml/define-blocks" class="btn btn-prev"
        >❮ Define Blocks</router-link
      >
      <router-link to="/fxml/instance-properties" class="btn btn-next"
        >Instance Properties ❯</router-link
      >
    </div>
  </article>
</template>
