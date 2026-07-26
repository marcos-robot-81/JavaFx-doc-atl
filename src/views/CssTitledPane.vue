<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="titledpane">TitledPane</a></h4>
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
            <th class="propertyname" scope="row"><code>-fx-animated</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-collapsible</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has <a href="#fontprops">Font Properties</a> and all
              properties of <a href="#labeled">Labeled</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Pseudo-classes</h4>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Pseudo-classes
        </caption>
        <thead>
          <tr>
            <th class="propertyname" scope="col">CSS Pseudo-class</th>
            <th scope="col">Comments</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th class="propertyname" scope="row">expanded</th>
            <td>applies if this TitledPane is expanded</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">collapsed</th>
            <td>applies if this TitledPane is collapsed</td>
          </tr>
          <tr>
            <th colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of <a href="#labeled">Labeled</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>
          title — HBox
          <ul>
            <li>text — Label/li&gt;</li>
            <li>
              arrow-button — StackPane/li&gt;
              <ul>
                <li>arrow — StackPane</li>
              </ul>
            </li>
          </ul>
        </li>
        <li>content — StackPane/li&gt;</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/textfield" class="btn btn-prev"
        >❮ TextField</router-link
      >
      <router-link to="/css/togglebutton" class="btn btn-next"
        >ToggleButton ❯</router-link
      >
    </div>
  </article>
</template>
