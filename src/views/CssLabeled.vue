<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="labeled">Labeled</a></h4>
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
            <th class="propertyname" scope="row"><code>-fx-alignment</code></th>
            <td class="value">
              [ top-left | top-center | top-right | center-left | center |
              center-right bottom-left | bottom-center | bottom-right |
              baseline-left | baseline-center | baseline-right ]
            </td>
            <td class="default">center-left</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-text-alignment</code>
            </th>
            <td class="value">[ left | center | right | justify ]</td>
            <td>left</td>
            <td>text-align from CSS spec maps to textAlignment in JavaFX</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-text-overrun</code>
            </th>
            <td class="value">
              [ center-ellipsis | center-word-ellipsis | clip | ellipsis |
              leading-ellipsis | leading-word-ellipsis | word-ellipsis ]
            </td>
            <td>ellipsis</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-wrap-text</code></th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-font</code></th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font&gt;</a>
            </td>
            <td>platform dependent</td>
            <td>
              inherits<br />The initial value is that of Font.getDefault()
            </td>
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
            <th class="propertyname" scope="row"><code>-fx-graphic</code></th>
            <td class="value">
              <a href="#typeurl" class="typelink">&lt;uri&gt;</a>
            </td>
            <td>null</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-content-display</code>
            </th>
            <td class="value">
              [ top | right | bottom | left | center | right | graphic-only |
              text-only ]
            </td>
            <td>left</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-graphic-text-gap</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>4</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-label-padding</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>[0,0,0,0]</td>
            <td>&nbsp;</td>
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
              <code>-fx-ellipsis-string</code>
            </th>
            <td class="value">
              <a href="#typestring" class="typelink">&lt;string&gt;</a>
            </td>
            <td>...</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has properties of <a href="#control">Control</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/label" class="btn btn-prev">❮ Label</router-link>
      <router-link to="/css/listcell" class="btn btn-next"
        >ListCell ❯</router-link
      >
    </div>
  </article>
</template>
