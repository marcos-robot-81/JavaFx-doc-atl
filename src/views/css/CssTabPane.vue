<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="tabpane">TabPane</a></h4>
      <p class="styleclass">Style class: tab-pane</p>
      <p>
        Note: The styleclass is "tab-pane floating" if the TabPane is floating.
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
            <th class="propertyname" scope="row">
              <code>-fx-tab-min-width</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td>0</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tab-max-width</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td>Double.MAX_VALUE</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tab-min-height</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td>0</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tab-max-height</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td>Double.MAX_VALUE</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-open-tab-animation</code>
            </th>
            <td class="value">[ grow | none ]</td>
            <td>grow</td>
            <td>'none' disables Tab opening animation</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-close-tab-animation</code>
            </th>
            <td class="value">[ grow | none ]</td>
            <td>grow</td>
            <td>'none' disables Tab closing animation</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#control">Control</a>
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
            <th class="propertyname" scope="row">top</th>
            <td>applies if the side is top</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">right</th>
            <td>applies if the side is rght</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">bottom</th>
            <td>applies if the side is bottom</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">left</th>
            <td>applies if the side is left</td>
          </tr>
          <tr>
            <th colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of <a href="#control">Control</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>
          tab-header-area — StackPane
          <ul>
            <li>headers-region — StackPane</li>
            <li>tab-header-background — StackPane</li>
            <li>
              control-buttons-tab — StackPane
              <ul>
                <li>
                  tab-down-button — Pane
                  <ul>
                    <li>arrow — StackPane</li>
                  </ul>
                </li>
              </ul>
            </li>
            <li>
              tab — Tab
              <ul>
                <li>tab-label — Label</li>
                <li>tab-close-button — StackPane</li>
              </ul>
            </li>
          </ul>
        </li>
        <li>tab-content-area — StackPane</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/splitpane" class="btn btn-prev"
        >❮ SplitPane</router-link
      >
      <router-link to="/css/tablecolumnheader" class="btn btn-next"
        >TableColumnHeader ❯</router-link
      >
    </div>
  </article>
</template>
