<script setup>
const props = defineProps({ isOpen: Boolean })
const emit = defineEmits(['close'])
</script>

<template>
  <aside class="sidebar" :class="{ 'open': isOpen }">
    <div class="sidebar-header">
      <h2>JavaFX Modern Docs</h2>
    </div>
    <nav class="sidebar-nav">
      <details class="nav-group">
        <summary><h3>FXML Tutorial</h3></summary>
      <ul class="sub-menu">
        <li><router-link to="/fxml/overview" @click="emit('close')">Overview</router-link></li>
        <li><router-link to="/fxml/elements" @click="emit('close')">Elements</router-link></li>
        <li><router-link to="/fxml/class-instance-elements" @click="emit('close')">Class Instance Elements</router-link></li>
        <li><router-link to="/fxml/instance-declarations" @click="emit('close')">Instance Declarations</router-link></li>
        <li><router-link to="/fxml/fx-include" @click="emit('close')">&lt;fx:include&gt;</router-link></li>
        <li><router-link to="/fxml/fx-constant" @click="emit('close')">&lt;fx:constant&gt;</router-link></li>
        <li><router-link to="/fxml/fx-reference" @click="emit('close')">&lt;fx:reference&gt;</router-link></li>
        <li><router-link to="/fxml/fx-copy" @click="emit('close')">&lt;fx:copy&gt;</router-link></li>
        <li><router-link to="/fxml/fx-root" @click="emit('close')">&lt;fx:root&gt;</router-link></li>
        <li><router-link to="/fxml/property-elements" @click="emit('close')">Property Elements</router-link></li>
        <li><router-link to="/fxml/property-setters" @click="emit('close')">Property Setters</router-link></li>
        <li><router-link to="/fxml/read-only-list-properties" @click="emit('close')">Read-Only List Properties</router-link></li>
        <li><router-link to="/fxml/read-only-map-properties" @click="emit('close')">Read-Only Map Properties</router-link></li>
        <li><router-link to="/fxml/default-properties" @click="emit('close')">Default Properties</router-link></li>
        <li><router-link to="/fxml/static-properties" @click="emit('close')">Static Properties</router-link></li>
        <li><router-link to="/fxml/define-blocks" @click="emit('close')">Define Blocks</router-link></li>
        <li><router-link to="/fxml/attributes" @click="emit('close')">Attributes</router-link></li>
        <li><router-link to="/fxml/instance-properties" @click="emit('close')">Instance Properties</router-link></li>
        <li><router-link to="/fxml/location-resolution" @click="emit('close')">Location Resolution</router-link></li>
        <li><router-link to="/fxml/resource-resolution" @click="emit('close')">Resource Resolution</router-link></li>
        <li><router-link to="/fxml/variable-resolution" @click="emit('close')">Variable Resolution</router-link></li>
        <li><router-link to="/fxml/escape-sequences" @click="emit('close')">Escape Sequences</router-link></li>
        <li><router-link to="/fxml/expression-binding" @click="emit('close')">Expression Binding</router-link></li>
        <li><router-link to="/fxml/event-handlers" @click="emit('close')">Event Handlers</router-link></li>
        <li><router-link to="/fxml/script-event-handlers" @click="emit('close')">Script Event Handlers</router-link></li>
        <li><router-link to="/fxml/controller-method-event-handlers" @click="emit('close')">Controller Method Event Handlers</router-link></li>
        <li><router-link to="/fxml/event-handlers-from-expressions" @click="emit('close')">Event handlers from expressions</router-link></li>
        <li><router-link to="/fxml/special-handlers-for-collections-and-properties" @click="emit('close')">Special handlers for collections and properties</router-link></li>
        <li><router-link to="/fxml/scripting" @click="emit('close')">Scripting</router-link></li>
        <li><router-link to="/fxml/controllers" @click="emit('close')">Controllers</router-link></li>
        <li><router-link to="/fxml/fxml" @click="emit('close')">@FXML</router-link></li>
        <li><router-link to="/fxml/nested-controllers" @click="emit('close')">Nested Controllers</router-link></li>
        <li><router-link to="/fxml/fxmlloader" @click="emit('close')">FXMLLoader</router-link></li>
        <li><router-link to="/fxml/custom-components" @click="emit('close')">Custom Components</router-link></li>
        <li><router-link to="/fxml/deploying-an-application-as-a-module" @click="emit('close')">Deploying an Application as a Module</router-link></li>
      </ul>
</details>
    <h3>CSS Reference Guide</h3>
      <details class="nav-group">
  <summary><h4>Introduction</h4></summary>
      <ul class="sub-menu">
        <li><router-link to="/css/introduction" @click="emit('close')">Introduction</router-link></li>
        <li><router-link to="/css/css-and-the-javafx-scene-graph" @click="emit('close')">CSS and the JavaFX Scene Graph</router-link></li>
        <li><router-link to="/css/scene-parent-and-subscene-stylesheets" @click="emit('close')">Scene, Parent and SubScene Stylesheets</router-link></li>
        <li><router-link to="/css/naming-conventions" @click="emit('close')">Naming Conventions</router-link></li>
        <li><router-link to="/css/css-public-api" @click="emit('close')">CSS Public API</router-link></li>
        <li><router-link to="/css/inheritance" @click="emit('close')">Inheritance</router-link></li>
        <li><router-link to="/css/transitions" @click="emit('close')">Transitions</router-link></li>
        <li><router-link to="/css/example" @click="emit('close')">Example</router-link></li>
        <li><router-link to="/css/-rules" @click="emit('close')">@ Rules</router-link></li>
        <li><router-link to="/css/import" @click="emit('close')">@import</router-link></li>
        <li><router-link to="/css/font-face" @click="emit('close')">@font-face</router-link></li>
        <li><router-link to="/css/media" @click="emit('close')">@media</router-link></li>
        <li><router-link to="/css/examples" @click="emit('close')">Examples</router-link></li>
        <li><router-link to="/css/understanding-----parser-warnings" @click="emit('close')">Understanding         Parser Warnings</router-link></li>
        <li><router-link to="/css/limitations" @click="emit('close')">Limitations</router-link></li>
      </ul>
</details>
      <details class="nav-group">
  <summary><h4>Types</h4></summary>
      <ul class="sub-menu">
        <li><router-link to="/css/types" @click="emit('close')">Types</router-link></li>
        <li><router-link to="/css/inherit" @click="emit('close')">inherit</router-link></li>
        <li><router-link to="/css/boolean" @click="emit('close')">&lt;boolean&gt;</router-link></li>
        <li><router-link to="/css/string" @click="emit('close')">&lt;string&gt;</router-link></li>
        <li><router-link to="/css/number-----integer" @click="emit('close')">&lt;number&gt; &amp;         &lt;integer&gt;</router-link></li>
        <li><router-link to="/css/size" @click="emit('close')">&lt;size&gt;</router-link></li>
        <li><router-link to="/css/length" @click="emit('close')">&lt;length&gt;</router-link></li>
        <li><router-link to="/css/percentage" @click="emit('close')">&lt;percentage&gt;</router-link></li>
        <li><router-link to="/css/angle" @click="emit('close')">&lt;angle&gt;</router-link></li>
        <li><router-link to="/css/duration" @click="emit('close')">&lt;duration&gt;</router-link></li>
        <li><router-link to="/css/point" @click="emit('close')">&lt;point&gt;</router-link></li>
        <li><router-link to="/css/color-stop" @click="emit('close')">&lt;color-stop&gt;</router-link></li>
        <li><router-link to="/css/uri" @click="emit('close')">&lt;uri&gt;</router-link></li>
        <li><router-link to="/css/effect" @click="emit('close')">&lt;effect&gt;</router-link></li>
        <li><router-link to="/css/drop-shadow" @click="emit('close')">Drop Shadow</router-link></li>
        <li><router-link to="/css/inner-shadow" @click="emit('close')">Inner Shadow</router-link></li>
        <li><router-link to="/css/font" @click="emit('close')">&lt;font&gt;</router-link></li>
        <li><router-link to="/css/font-properties" @click="emit('close')">Font Properties</router-link></li>
        <li><router-link to="/css/paint" @click="emit('close')">&lt;paint&gt;</router-link></li>
        <li><router-link to="/css/linear-gradients-------linear-gradient" @click="emit('close')">Linear Gradients             &lt;linear-gradient&gt;</router-link></li>
        <li><router-link to="/css/radial-gradients-------radial-gradient" @click="emit('close')">Radial Gradients              &lt;radial-gradient&gt;</router-link></li>
        <li><router-link to="/css/image-paint-------image-pattern" @click="emit('close')">Image Paint              &lt;image-pattern&gt;</router-link></li>
        <li><router-link to="/css/color" @click="emit('close')">&lt;color&gt;</router-link></li>
        <li><router-link to="/css/named-colors-named-color" @click="emit('close')">Named Colors &lt;named-color&gt;</router-link></li>
        <li><router-link to="/css/looked-up-colors-looked-up-color" @click="emit('close')">Looked-up Colors &lt;looked-up-color&gt;</router-link></li>
        <li><router-link to="/css/rgb-colors-rgb-color" @click="emit('close')">RGB Colors &lt;rgb-color&gt;</router-link></li>
        <li><router-link to="/css/hsb-colors-hsb-color" @click="emit('close')">HSB Colors &lt;hsb-color&gt;</router-link></li>
        <li><router-link to="/css/color-functions-color-function" @click="emit('close')">Color Functions &lt;color-function&gt;</router-link></li>
        <li><router-link to="/css/easing-function" @click="emit('close')">&lt;easing-function&gt;</router-link></li>
        <li><router-link to="/css/text-bounds" @click="emit('close')">&lt;text-bounds&gt;</router-link></li>
      </ul>
</details>
      <details class="nav-group">
  <summary><h4>Stage</h4></summary>
      <ul class="sub-menu">
        <li><router-link to="/css/stage" @click="emit('close')">Stage</router-link></li>
        <li><router-link to="/css/popupwindow" @click="emit('close')">PopupWindow</router-link></li>
      </ul>
</details>
      <details class="nav-group">
  <summary><h4>Nodes</h4></summary>
      <ul class="sub-menu">
        <li><router-link to="/css/nodes" @click="emit('close')">Nodes</router-link></li>
        <li><router-link to="/css/group" @click="emit('close')">Group</router-link></li>
        <li><router-link to="/css/node" @click="emit('close')">Node</router-link></li>
        <li><router-link to="/css/parent" @click="emit('close')">Parent</router-link></li>
        <li><router-link to="/css/scene" @click="emit('close')">Scene</router-link></li>
        <li><router-link to="/css/imageview" @click="emit('close')">ImageView</router-link></li>
        <li><router-link to="/css/anchorpane" @click="emit('close')">AnchorPane</router-link></li>
        <li><router-link to="/css/borderpane" @click="emit('close')">BorderPane</router-link></li>
        <li><router-link to="/css/dialogpane" @click="emit('close')">DialogPane</router-link></li>
        <li><router-link to="/css/flowpane" @click="emit('close')">FlowPane</router-link></li>
        <li><router-link to="/css/gridpane" @click="emit('close')">GridPane</router-link></li>
        <li><router-link to="/css/hbox" @click="emit('close')">HBox</router-link></li>
        <li><router-link to="/css/pane" @click="emit('close')">Pane</router-link></li>
        <li><router-link to="/css/region" @click="emit('close')">Region</router-link></li>
        <li><router-link to="/css/stackpane" @click="emit('close')">StackPane</router-link></li>
        <li><router-link to="/css/tilepane" @click="emit('close')">TilePane</router-link></li>
        <li><router-link to="/css/vbox" @click="emit('close')">VBox</router-link></li>
        <li><router-link to="/css/mediaview" @click="emit('close')">MediaView</router-link></li>
        <li><router-link to="/css/shape" @click="emit('close')">Shape</router-link></li>
        <li><router-link to="/css/arc" @click="emit('close')">Arc</router-link></li>
        <li><router-link to="/css/circle" @click="emit('close')">Circle</router-link></li>
        <li><router-link to="/css/cubiccurve" @click="emit('close')">CubicCurve</router-link></li>
        <li><router-link to="/css/ellipse" @click="emit('close')">Ellipse</router-link></li>
        <li><router-link to="/css/line" @click="emit('close')">Line</router-link></li>
        <li><router-link to="/css/path" @click="emit('close')">Path</router-link></li>
        <li><router-link to="/css/polygon" @click="emit('close')">Polygon</router-link></li>
        <li><router-link to="/css/quadcurve" @click="emit('close')">QuadCurve</router-link></li>
        <li><router-link to="/css/rectangle" @click="emit('close')">Rectangle</router-link></li>
        <li><router-link to="/css/svgpath" @click="emit('close')">SVGPath</router-link></li>
        <li><router-link to="/css/text" @click="emit('close')">Text</router-link></li>
        <li><router-link to="/css/textflow" @click="emit('close')">TextFlow</router-link></li>
        <li><router-link to="/css/webview" @click="emit('close')">WebView</router-link></li>
      </ul>
</details>
      <details class="nav-group">
  <summary><h4>Controls</h4></summary>
      <ul class="sub-menu">
        <li><router-link to="/css/controls" @click="emit('close')">Controls</router-link></li>
        <li><router-link to="/css/accordion" @click="emit('close')">Accordion</router-link></li>
        <li><router-link to="/css/button" @click="emit('close')">Button</router-link></li>
        <li><router-link to="/css/buttonbase" @click="emit('close')">ButtonBase</router-link></li>
        <li><router-link to="/css/cell" @click="emit('close')">Cell</router-link></li>
        <li><router-link to="/css/checkbox" @click="emit('close')">CheckBox</router-link></li>
        <li><router-link to="/css/checkmenuitem" @click="emit('close')">CheckMenuItem</router-link></li>
        <li><router-link to="/css/choicebox" @click="emit('close')">ChoiceBox</router-link></li>
        <li><router-link to="/css/colorpicker" @click="emit('close')">ColorPicker</router-link></li>
        <li><router-link to="/css/combobox" @click="emit('close')">ComboBox</router-link></li>
        <li><router-link to="/css/comboboxbase" @click="emit('close')">ComboBoxBase</router-link></li>
        <li><router-link to="/css/contextmenu" @click="emit('close')">ContextMenu</router-link></li>
        <li><router-link to="/css/control" @click="emit('close')">Control</router-link></li>
        <li><router-link to="/css/datepicker" @click="emit('close')">DatePicker</router-link></li>
        <li><router-link to="/css/htmleditor" @click="emit('close')">HTMLEditor</router-link></li>
        <li><router-link to="/css/hyperlink" @click="emit('close')">Hyperlink</router-link></li>
        <li><router-link to="/css/indexedcell" @click="emit('close')">IndexedCell</router-link></li>
        <li><router-link to="/css/label" @click="emit('close')">Label</router-link></li>
        <li><router-link to="/css/labeled" @click="emit('close')">Labeled</router-link></li>
        <li><router-link to="/css/listcell" @click="emit('close')">ListCell</router-link></li>
        <li><router-link to="/css/listview" @click="emit('close')">ListView</router-link></li>
        <li><router-link to="/css/menu" @click="emit('close')">Menu</router-link></li>
        <li><router-link to="/css/menubar" @click="emit('close')">MenuBar</router-link></li>
        <li><router-link to="/css/menubutton" @click="emit('close')">MenuButton</router-link></li>
        <li><router-link to="/css/menuitem" @click="emit('close')">MenuItem</router-link></li>
        <li><router-link to="/css/pagination" @click="emit('close')">Pagination</router-link></li>
        <li><router-link to="/css/passwordfield" @click="emit('close')">PasswordField</router-link></li>
        <li><router-link to="/css/popupcontrol" @click="emit('close')">PopupControl</router-link></li>
        <li><router-link to="/css/progressbar" @click="emit('close')">ProgressBar</router-link></li>
        <li><router-link to="/css/progressindicator" @click="emit('close')">ProgressIndicator</router-link></li>
        <li><router-link to="/css/radiobutton" @click="emit('close')">RadioButton</router-link></li>
        <li><router-link to="/css/radiomenuitem" @click="emit('close')">RadioMenuItem</router-link></li>
        <li><router-link to="/css/scrollbar" @click="emit('close')">ScrollBar</router-link></li>
        <li><router-link to="/css/scrollpane" @click="emit('close')">ScrollPane</router-link></li>
        <li><router-link to="/css/separator" @click="emit('close')">Separator</router-link></li>
        <li><router-link to="/css/spinner" @click="emit('close')">Spinner</router-link></li>
        <li><router-link to="/css/slider" @click="emit('close')">Slider</router-link></li>
        <li><router-link to="/css/splitmenubutton" @click="emit('close')">SplitMenuButton</router-link></li>
        <li><router-link to="/css/splitpane" @click="emit('close')">SplitPane</router-link></li>
        <li><router-link to="/css/tabpane" @click="emit('close')">TabPane</router-link></li>
        <li><router-link to="/css/tablecolumnheader" @click="emit('close')">TableColumnHeader</router-link></li>
        <li><router-link to="/css/tableview" @click="emit('close')">TableView</router-link></li>
        <li><router-link to="/css/textarea" @click="emit('close')">TextArea</router-link></li>
        <li><router-link to="/css/textinputcontrol" @click="emit('close')">TextInputControl</router-link></li>
        <li><router-link to="/css/textfield" @click="emit('close')">TextField</router-link></li>
        <li><router-link to="/css/titledpane" @click="emit('close')">TitledPane</router-link></li>
        <li><router-link to="/css/togglebutton" @click="emit('close')">ToggleButton</router-link></li>
        <li><router-link to="/css/toolbar" @click="emit('close')">ToolBar</router-link></li>
        <li><router-link to="/css/tooltip" @click="emit('close')">Tooltip</router-link></li>
        <li><router-link to="/css/treecell" @click="emit('close')">TreeCell</router-link></li>
        <li><router-link to="/css/treetablecell" @click="emit('close')">TreeTableCell</router-link></li>
        <li><router-link to="/css/treeview" @click="emit('close')">TreeView</router-link></li>
        <li><router-link to="/css/treeview-1" @click="emit('close')">TreeView 1</router-link></li>
      </ul>
</details>
      <details class="nav-group">
  <summary><h4>Charts</h4></summary>
      <ul class="sub-menu">
        <li><router-link to="/css/charts" @click="emit('close')">Charts</router-link></li>
        <li><router-link to="/css/areachart" @click="emit('close')">AreaChart</router-link></li>
        <li><router-link to="/css/axis" @click="emit('close')">Axis</router-link></li>
        <li><router-link to="/css/barchart" @click="emit('close')">BarChart</router-link></li>
        <li><router-link to="/css/bubblechart" @click="emit('close')">BubbleChart</router-link></li>
        <li><router-link to="/css/categoryaxis" @click="emit('close')">CategoryAxis</router-link></li>
        <li><router-link to="/css/chart" @click="emit('close')">Chart</router-link></li>
        <li><router-link to="/css/legend" @click="emit('close')">Legend</router-link></li>
        <li><router-link to="/css/linechart" @click="emit('close')">LineChart</router-link></li>
        <li><router-link to="/css/numberaxis" @click="emit('close')">NumberAxis</router-link></li>
        <li><router-link to="/css/piechart" @click="emit('close')">PieChart</router-link></li>
        <li><router-link to="/css/scatterchart" @click="emit('close')">ScatterChart</router-link></li>
        <li><router-link to="/css/valueaxis" @click="emit('close')">ValueAxis</router-link></li>
        <li><router-link to="/css/xychart" @click="emit('close')">XYChart</router-link></li>
      </ul>
</details>
      <details class="nav-group">
  <summary><h4>Incubator Modules</h4></summary>
      <ul class="sub-menu">
        <li><router-link to="/css/incubator-modules" @click="emit('close')">Incubator Modules</router-link></li>
        <li><router-link to="/css/richtextarea" @click="emit('close')">RichTextArea</router-link></li>
        <li><router-link to="/css/codearea" @click="emit('close')">CodeArea</router-link></li>
      </ul>
</details>
    </nav>
  </aside>
</template>

<style scoped>
.sidebar { width: 280px; background-color: var(--bg-sidebar); border-right: 1px solid var(--glass-border); position: fixed; height: 100vh; overflow-y: auto; transition: transform 0.3s ease; z-index: 100; }
.sidebar-header { padding: 24px; border-bottom: 1px solid var(--glass-border); }
.sidebar-header h2 { font-size: 1.2rem; font-weight: 700; color: var(--accent); letter-spacing: 0.5px; background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.sidebar-nav { padding: 24px 0; }
.sidebar-nav h3 { font-size: 0.85rem; text-transform: uppercase; color: var(--text-muted); padding: 0 24px; margin-top: 16px; margin-bottom: 8px; letter-spacing: 1px; }
.sidebar-nav ul { list-style: none; margin-bottom: 12px; }
.sidebar-nav a { display: block; padding: 6px 24px; color: var(--text-main); text-decoration: none; font-size: 0.85rem; transition: all 0.2s; border-left: 3px solid transparent; }
.sidebar-nav a:hover { background-color: rgba(255, 255, 255, 0.05); color: var(--accent); }
.sidebar-nav a.router-link-active { border-left-color: var(--accent); background-color: rgba(56, 189, 248, 0.1); color: var(--accent); font-weight: 600; }
</style>
