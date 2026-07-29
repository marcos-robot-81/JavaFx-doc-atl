<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="control">Control</a></h4>
      <p>
        The Control class has all the properties of <a href="#region">Region</a>
      </p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Properties
        </caption>
        <thead>
          <tr>
            <th class="propertyname" scope="col">CSS Property</th>
            <th class="value" scope="col">Values</th>
            <th scope="col">Default</th>
            <th scope="col">Comments</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-skin</code></th>
            <td class="value">
              <a href="#typestring" class="typelink">&lt;string&gt;</a>
            </td>
            <td>null</td>
            <td>The class name of the Control's Skin.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-focus-traversable</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">true</td>
            <td>
              Control sets the default value of the focusTraversable property to
              true. The default value of the focusTraversable property for the
              following controls is false: Accordion, Cell, Label, MenuBar,
              ProgressBar, ProgressIndicator, ScrollBar, ScrollPane, Separator,
              SplitPane, ToolBar.
            </td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/contextmenu" class="btn btn-prev"
        >❮ ContextMenu</router-link
      >
      <router-link to="/css/datepicker" class="btn btn-next"
        >DatePicker ❯</router-link
      >
    </div>
  </article>
</template>
