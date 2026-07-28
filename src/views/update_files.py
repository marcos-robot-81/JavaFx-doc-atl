import os
import re

base_path = "/home/her/Documentos/java fx reference/v2/vue-docs/src/views/"

def process_file(fname, replacements):
    path = os.path.join(base_path, fname)
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for search, replace in replacements:
        if search in content:
            content = content.replace(search, replace)
        else:
            print(f"Warning: could not find snippet in {fname}")
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Define replacements: (search_string, replace_string)

rep_btn_vbox = (
"""    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>""",
"""    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
        </div>
      </div>"""
)

process_file("FxmlEventHandlers.vue", [rep_btn_vbox])
process_file("FxmlScriptEventHandlers.vue", [rep_btn_vbox])
process_file("FxmlEventhandlersfromexpressions.vue", [rep_btn_vbox])

rep_tf_lbl = (
"""&lt;TextField fx:id="textField"/&gt;
&lt;Label text="${textField.text}"/&gt;
</code></pre>
      </div>""",
"""&lt;TextField fx:id="textField"/&gt;
&lt;Label text="${textField.text}"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <input type="text" class="javafx-textfield" />
        <span class="javafx-label">${textField.text}</span>
      </div>"""
)
process_file("FxmlExpressionBinding.vue", [rep_tf_lbl])
process_file("FxmlInstanceProperties.vue", [rep_tf_lbl])

rep_rect = (
"""&lt;Rectangle fx:id="rectangle" x="10" y="10" width="320" height="240"
    fill="#ff0000"/&gt;
</code></pre>
      </div>""",
"""&lt;Rectangle fx:id="rectangle" x="10" y="10" width="320" height="240"
    fill="#ff0000"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-rectangle" style="width: 320px; height: 240px; background-color: #ff0000; margin: 10px;"></div>
      </div>"""
)
process_file("FxmlInstanceProperties.vue", [rect for rect in [rep_rect]]) # doing one by one

rep_img = (
"""&lt;ImageView&gt;
    &lt;image&gt;
        &lt;Image url="@my_image.png"/&gt;
    &lt;/image&gt;
&lt;/ImageView&gt;
</code></pre>
      </div>""",
"""&lt;ImageView&gt;
    &lt;image&gt;
        &lt;Image url="@my_image.png"/&gt;
    &lt;/image&gt;
&lt;/ImageView&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <img class="javafx-imageview" src="#" alt="my_image.png" />
      </div>"""
)
rep_img2 = (
"""&lt;ImageView image="@my_image.png"/&gt;
</code></pre>
      </div>""",
"""&lt;ImageView image="@my_image.png"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <img class="javafx-imageview" src="#" alt="my_image.png" />
      </div>"""
)
rep_lbl_text = (
"""&lt;Label text="%myText"/&gt;
</code></pre>
      </div>""",
"""&lt;Label text="%myText"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <span class="javafx-label">%myText</span>
      </div>"""
)
rep_radio = (
"""&lt;RadioButton text="A" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="B" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="C" toggleGroup="$myToggleGroup"/&gt;
</code></pre>
      </div>""",
"""&lt;RadioButton text="A" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="B" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="C" toggleGroup="$myToggleGroup"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-radiobutton"><input type="radio" name="myToggleGroup"> A</div>
        <div class="javafx-radiobutton"><input type="radio" name="myToggleGroup"> B</div>
        <div class="javafx-radiobutton"><input type="radio" name="myToggleGroup"> C</div>
      </div>"""
)
process_file("FxmlInstanceProperties.vue", [rep_img, rep_img2, rep_lbl_text, rep_radio])
process_file("FxmlLocationResolution.vue", [rep_img, rep_img2])
process_file("FxmlResourceResolution.vue", [rep_lbl_text])
process_file("FxmlVariableResolution.vue", [rep_radio])


rep_lbl_mytext = (
"""&lt;Label text="$myText"/&gt;
</code></pre>
      </div>""",
"""&lt;Label text="$myText"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <span class="javafx-label">$myText</span>
      </div>"""
)
process_file("FxmlScripting.vue", [rep_lbl_mytext])

rep_gridpane = (
"""&lt;GridPane&gt;
    &lt;children&gt;
        &lt;Label text="My Label"&gt;
            &lt;GridPane.rowIndex&gt;0&lt;/GridPane.rowIndex&gt;
       &lt;GridPane.columnIndex&gt;0&lt;/GridPane.columnIndex&gt;
        &lt;/Label&gt;
    &lt;/children&gt;
&lt;/TabPane&gt;
</code></pre>
      </div>""",
"""&lt;GridPane&gt;
    &lt;children&gt;
        &lt;Label text="My Label"&gt;
            &lt;GridPane.rowIndex&gt;0&lt;/GridPane.rowIndex&gt;
       &lt;GridPane.columnIndex&gt;0&lt;/GridPane.columnIndex&gt;
        &lt;/Label&gt;
    &lt;/children&gt;
&lt;/GridPane&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-gridpane" style="display: grid;">
          <span class="javafx-label" style="grid-row: 1; grid-column: 1;">My Label</span>
        </div>
      </div>"""
)
# Fixed TabPane typo in the original XML snippet for GridPane just in case
rep_gridpane_actual = (
"""&lt;GridPane&gt;
    &lt;children&gt;
        &lt;Label text="My Label"&gt;
            &lt;GridPane.rowIndex&gt;0&lt;/GridPane.rowIndex&gt;
       &lt;GridPane.columnIndex&gt;0&lt;/GridPane.columnIndex&gt;
        &lt;/Label&gt;
    &lt;/children&gt;
&lt;/TabPane&gt;
</code></pre>
      </div>""",
"""&lt;GridPane&gt;
    &lt;children&gt;
        &lt;Label text="My Label"&gt;
            &lt;GridPane.rowIndex&gt;0&lt;/GridPane.rowIndex&gt;
       &lt;GridPane.columnIndex&gt;0&lt;/GridPane.columnIndex&gt;
        &lt;/Label&gt;
    &lt;/children&gt;
&lt;/GridPane&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-gridpane" style="display: grid;">
          <span class="javafx-label" style="grid-row: 1; grid-column: 1;">My Label</span>
        </div>
      </div>"""
)
process_file("FxmlStaticProperties.vue", [rep_gridpane_actual])

rep_const_btn = (
"""&lt;Button&gt;
    &lt;minHeight&gt;&lt;Double fx:constant="NEGATIVE_INFINITY"/&gt;&lt;/minHeight&gt;
&lt;/Button&gt;
</code></pre>
      </div>""",
"""&lt;Button&gt;
    &lt;minHeight&gt;&lt;Double fx:constant="NEGATIVE_INFINITY"/&gt;&lt;/minHeight&gt;
&lt;/Button&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <button class="javafx-btn">Button</button>
      </div>"""
)
process_file("Fxmlfxconstant.vue", [rep_const_btn])

rep_custom_hbox = (
"""&lt;HBox&gt;
    &lt;CustomControl text="Hello World!"/&gt;
&lt;/HBox&gt;
</code></pre>
      </div>""",
"""&lt;HBox&gt;
    &lt;CustomControl text="Hello World!"/&gt;
&lt;/HBox&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-hbox">
          <div class="javafx-customcontrol">Hello World!</div>
        </div>
      </div>"""
)
process_file("FxmlFXMLLoader.vue", [rep_custom_hbox])

rep_nested = (
"""&lt;VBox fx:controller="com.foo.MainController"&gt;
   &lt;fx:define&gt;
      &lt;fx:include fx:id="dialog" source="dialog.fxml"/&gt;
   &lt;/fx:define&gt;
   ...
&lt;/VBox&gt;
</code></pre>
      </div>""",
"""&lt;VBox fx:controller="com.foo.MainController"&gt;
   &lt;fx:define&gt;
      &lt;fx:include fx:id="dialog" source="dialog.fxml"/&gt;
   &lt;/fx:define&gt;
   ...
&lt;/VBox&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox">...</div>
      </div>"""
)
process_file("FxmlNestedControllers.vue", [rep_nested])

rep_empty_vbox = (
"""&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children onChange="#handleChildrenChange"/&gt;
&lt;/VBox&gt;
</code></pre>
      </div>""",
"""&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children onChange="#handleChildrenChange"/&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox"></div>
      </div>"""
)
rep_empty_vbox2 = (
"""&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml" onParentChange="#handleParentChange"/&gt;
</code></pre>
      </div>""",
"""&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml" onParentChange="#handleParentChange"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox"></div>
      </div>"""
)
process_file("FxmlEventHandlers.vue", [rep_empty_vbox, rep_empty_vbox2])
process_file("FxmlSpecialhandlersforcollectionsandproperties.vue", [rep_empty_vbox, rep_empty_vbox2])


