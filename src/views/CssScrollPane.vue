<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="scrollpane">ScrollPane</a></h4>
      <p class="styleclass">Style class: scroll-pane</p>
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
              <code>-fx-fit-to-width</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-fit-to-height</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-pannable</code></th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-hbar-policy</code>
            </th>
            <td class="value">[ never | always | as-needed ]</td>
            <td>as-needed</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-vbar-policy</code>
            </th>
            <td class="value">[ never | always | as-needed ]</td>
            <td>as-needed</td>
            <td>&nbsp;</td>
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
            <th class="propertyname" scope="row">pannable</th>
            <td>applies if this ScrollPane is pannable</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">fitToWidth</th>
            <td>applies if this ScrollPane is fitToWidth</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">fitToHeight</th>
            <td>applies if this ScrollPane is fitToHeight</td>
          </tr>
          <tr>
            <td colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of <a href="#control">Control</a>
            </td>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>
          viewport — StackPane
          <ul>
            <li>* — StackPane</li>
            <li>
              <ul>
                <li>The ScrollPane's content</li>
              </ul>
            </li>
          </ul>
        </li>
        <li>scroll-bar:vertical — ScrollBar</li>
        <li>scroll-bar:horizontal — ScrollBar</li>
        <li>corner — StackPane</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/scrollbar" class="btn btn-prev"
        >❮ ScrollBar</router-link
      >
      <router-link to="/css/separator" class="btn btn-next"
        >Separator ❯</router-link
      >
    </div>
  </article>
</template>
