<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
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
        <div class="javafx-rectangle" style="width: 320px; height: 240px; background-color: #ff0000; margin: 10px;"></div>
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
        <img class="javafx-imageview" src="#" alt="my_image.png" />
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
        <img class="javafx-imageview" src="#" alt="my_image.png" />
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
        <div class="javafx-rect" style="padding: 10px; background: #eee; border: 1px dashed #ccc; font-size: 12px; color: #666;">URL: My%20Image.png</div>
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
        <div class="javafx-rect" style="padding: 10px; background: #ffebee; border: 1px dashed red; font-size: 12px; color: #c62828;">Error: Unescaped space in URL</div>
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
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Resource Bundle entry: myText</div>
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
        <div class="javafx-radiobutton"><input type="radio" name="myToggleGroup"> A</div>
        <div class="javafx-radiobutton"><input type="radio" name="myToggleGroup"> B</div>
        <div class="javafx-radiobutton"><input type="radio" name="myToggleGroup"> C</div>
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
        <input type="text" class="javafx-textfield" />
        <span class="javafx-label">${textField.text}</span>
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
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, elements have attributes like
        <code>class</code>, <code>id</code>, <code>src</code>, or
        <code>href</code> which configure the DOM element's properties.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code class="language-html">&lt;!-- HTML Analogy for Instance Properties --&gt;
&lt;img src="/logo.png" width="320" height="240" alt="Logo" /&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc;">
            <img src="#" alt="Logo" style="width: 160px; height: 120px; background: #ddd; display: block;" />
        </div>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link to="/fxml/attributes" class="btn btn-prev"
        >❮ Attributes</router-link
      >
      <router-link to="/fxml/location-resolution" class="btn btn-next"
        >Location Resolution ❯</router-link
      >
    </div>
  </article>
</template>
