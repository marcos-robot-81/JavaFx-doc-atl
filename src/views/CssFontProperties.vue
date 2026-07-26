<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="fontprops">Font Properties</a></h4>
      <p>
        Most classes that use text will support the following font properties.
        In some cases a similar set of properties will be supported but with a
        different prefix instead of "<code>-fx-font</code>".
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
            <th class="propertyname" scope="row"><code>-fx-font</code></th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font&gt;</a>
            </td>
            <td>inherit</td>
            <td>
              shorthand property for font-size, font-family, font-weight and
              font-style
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-font-family</code>
            </th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font-family&gt;</a>
            </td>
            <td>inherit</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-font-size</code></th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font-size&gt;</a>
            </td>
            <td>inherit</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-font-style</code>
            </th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font-style&gt;</a>
            </td>
            <td>inherit</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-font-weight</code>
            </th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font-weight&gt;</a>
            </td>
            <td>inherit</td>
            <td>&nbsp;</td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/font" class="btn btn-prev"
        >❮ &lt;font&gt;</router-link
      >
      <router-link to="/css/paint" class="btn btn-next"
        >&lt;paint&gt; ❯</router-link
      >
    </div>
  </article>
</template>
