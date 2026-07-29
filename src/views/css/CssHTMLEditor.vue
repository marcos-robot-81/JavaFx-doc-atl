<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="htmleditor">HTMLEditor</a></h4>
      <p class="styleclass">Style class: html-editor</p>
      <p>
        The Hyperlink control has all the properties of
        <a href="#control">Control</a>.
      </p>
      <h4>Substructure</h4>
      <ul>
        <li>
          grid — GridPane (contains WebView)
          <ul>
            <li>
              top-toolbar — ToolBar
              <ul>
                <li>
                  html-editor-cut — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-copy — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-paste — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-align-left —
                  <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-align-right —
                  <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-align-center —
                  <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-align-justify —
                  <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-outdent — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-indent — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-bullets — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-numbers — <a href="#togglebutton">ToggleButton</a>
                </li>
              </ul>
            </li>
            <li>web-view — <a href="#webview">WebView</a></li>
            <li>
              bottom-toolbar — ToolBar
              <ul>
                <li>format-menu-button — ComboBox</li>
                <li>
                  font-family-menu-button — <a href="#combobox">ComboBox</a>
                </li>
                <li>
                  font-size-menu-button — <a href="#combobox">ComboBox</a>
                </li>
                <li>
                  html-editor-bold — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-italic — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-underline —
                  <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-strike — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-hr — <a href="#togglebutton">ToggleButton</a>
                </li>
                <li>
                  html-editor-foreground —
                  <a href="#colorpicker">ColorPicker</a>
                </li>
                <li>
                  html-editor-background —
                  <a href="#colorpicker">ColorPicker</a>
                </li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/datepicker" class="btn btn-prev"
        >❮ DatePicker</router-link
      >
      <router-link to="/css/hyperlink" class="btn btn-next"
        >Hyperlink ❯</router-link
      >
    </div>
  </article>
</template>
