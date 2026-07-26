<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="imageview">ImageView</a></h4>
      <p class="styleclass">Style class: image-view</p>
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
              <code>-fx-fit-height</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">0</td>
            <td>
              The height of the bounding box within which the source image is
              resized as necessary to fit.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-fit-width</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">0</td>
            <td>
              The width of the bounding box within which the source image is
              resized as necessary to fit.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-image</code></th>
            <td class="value">
              <a href="#typeurl" class="typelink">&lt;uri&gt;</a>
            </td>
            <td class="default">null</td>
            <td>
              Relative URLs are resolved against the URL of the stylesheet.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-preserve-ratio</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">false</td>
            <td>
              Indicates whether to preserve the aspect ratio of the source image
              when scaling to fit the image within the fitting bounding box.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-smooth</code></th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">Platform-specific</td>
            <td>
              Indicates whether to use a better quality filtering algorithm or a
              faster one when transforming or scaling the source image to fit.
            </td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#node">Node</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h3 class="package">javafx.scene.layout</h3>
      <br />
    </section>
    <div class="pagination">
      <router-link to="/css/scene" class="btn btn-prev">❮ Scene</router-link>
      <router-link to="/css/anchorpane" class="btn btn-next"
        >AnchorPane ❯</router-link
      >
    </div>
  </article>
</template>
