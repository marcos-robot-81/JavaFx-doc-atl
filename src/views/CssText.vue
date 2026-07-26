<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="text">Text</a></h4>
      <p class="styleclass">Style class: empty by default</p>
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
              <code>-fx-bounds-type</code>
            </th>
            <td class="value">
              <a href="#typetextbounds" class="typelink">&lt;text-bounds&gt;</a>
            </td>
            <td>logical</td>
            <td></td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-line-spacing</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td>0</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-fill</code></th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>BLACK</td>
            <td>text color</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-font</code></th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font&gt;</a>
            </td>
            <td>Font.DEFAULT</td>
            <td>inherits</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-font-smoothing-type</code>
            </th>
            <td class="value">[ gray | lcd ]</td>
            <td>gray</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-strikethrough</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-tab-size</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td>8</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-text-alignment</code>
            </th>
            <td class="value">[ left | center | right | justify ]</td>
            <td>left</td>
            <td>inherits</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-text-origin</code>
            </th>
            <td class="value">[ baseline | top | bottom ]</td>
            <td>baseline</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-underline</code></th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has <a href="#fontprops">font properties</a> and all
              properties of <a href="#shape">Shape</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/svgpath" class="btn btn-prev"
        >❮ SVGPath</router-link
      >
      <router-link to="/css/textflow" class="btn btn-next"
        >TextFlow ❯</router-link
      >
    </div>
  </article>
</template>
