<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="border">BorderPane</a></h4>
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
            <th colspan="4" scope="row">
              BorderPane extends Pane and does not add any additional CSS
              properties.
            </th>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#pane">Pane</a>
            </th>
          </tr>
        </tbody>
      </table>
      <br />
    </section>
    <div class="pagination">
      <router-link to="/css/anchorpane" class="btn btn-prev"
        >❮ AnchorPane</router-link
      >
      <router-link to="/css/dialogpane" class="btn btn-next"
        >DialogPane ❯</router-link
      >
    </div>
  </article>
</template>
