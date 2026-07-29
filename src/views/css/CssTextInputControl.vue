<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="textinputcontrol">TextInputControl</a></h4>
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
            <td>null</td>
            <td>inherits</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-text-fill</code></th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>black</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-prompt-text-fill</code>
            </th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>gray</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-highlight-fill</code>
            </th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>dodgerblue</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-highlight-text-fill</code>
            </th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>white</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-display-caret</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has <a href="#fontprops">Font Properties</a> and all
              properties of <a href="#control">Control</a>
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
            <th class="propertyname" scope="row">readonly</th>
            <td>applies if this TextInputControl is not editable</td>
          </tr>
          <tr>
            <th colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of <a href="#control">Control</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/textarea" class="btn btn-prev"
        >❮ TextArea</router-link
      >
      <router-link to="/css/textfield" class="btn btn-next"
        >TextField ❯</router-link
      >
    </div>
  </article>
</template>
