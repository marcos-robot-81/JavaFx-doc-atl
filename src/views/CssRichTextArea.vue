<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="richtextarea">RichTextArea</a></h4>
    <p class="styleclass">Style class: rich-text-area</p>
      <table class="table table-dark table-striped table-hover table-bordered" >
        <caption>Available CSS Properties</caption>
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
            <th class="propertyname" scope="row">-fx-caret-blink-period</th>
            <td class="value"><a href="#typeduration" class="typelink">&lt;duration&gt;</a></td>
            <td>1000 ms</td>
            <td>Determines the caret blink period.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">-fx-content-padding</th>
			<td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a>
			  | <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
			  <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
			</td>
            <td>0 0 0 0</td>
            <td>Amount of padding in the content area.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">-fx-display-caret</th>
            <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
            <td>true</td>
            <td>Determines whether the caret is displayed.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">-fx-highlight-current-paragraph</th>
            <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
            <td>false</td>
            <td>Determines whether the current paragraph is highlighted.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">-fx-use-content-height</th>
            <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
            <td>false</td>
            <td>Determines whether the preferred height is the same as the content height.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">-fx-use-content-width</th>
            <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
            <td>false</td>
            <td>Determines whether the preferred width is the same as the content width.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">-fx-wrap-text</th>
            <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
            <td>false</td>
            <td>Determines whether text should be wrapped.</td>
          </tr>
          <tr>
           <th colspan="4" class="parents" scope="row">Also has all properties of <a href="#control">Control</a></th>
          </tr>
        </tbody>
      </table>
    <h4>Pseudo-classes</h4>
    <table class="table table-dark table-striped table-hover table-bordered" >
      <caption>Available CSS Pseudo-classes</caption>
      <thead>
        <tr>
        <th class="propertyname" scope="col">CSS Pseudo-class</th>
        <th scope="col">Comments</th>
      </tr>
      </thead>
      <tbody>
        <!--
        <tr>
        <th class="propertyname" scope="row">horizontal</th>
            <td>applies if this Slider is horizontal</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">vertical</th>
            <td>applies if this Slider is vertical</td>
        </tr>
        -->
        <tr>
          <th colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#control">Control</a></th>
        </tr>
        </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>main-pane — Pane
        <ul>
          <li>vflow — Pane
          <ul>
            <li>content — Pane
            <ul>
              <li>caret-line — Path</li>
              <li>selection-highlight — Path</li>
              <li>flow — Pane</li>
              <li>caret — Path</li>
            </ul></li>
            <li>left-side — Pane</li>
            <li>right-side — Pane</li>
          </ul></li>
          <li>scroll-bar:vertical — ScrollBar</li>
          <li>scroll-bar:horizontal — ScrollBar</li>
        </ul></li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/incubator-modules" class="btn btn-prev">❮ Incubator Modules</router-link>
      <router-link to="/css/codearea" class="btn btn-next">CodeArea ❯</router-link>
    </div>
  </article>
</template>
