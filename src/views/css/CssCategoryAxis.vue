<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="categoryaxis">CategoryAxis</a></h4>
      <p class="styleclass">Style class: axis</p>
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
              <code>-fx-start-margin</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;number&gt;</a>
            </td>
            <td>5</td>
            <td>The margin between the axis start and the first tick-mark</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-end-margin</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;number&gt;</a>
            </td>
            <td>5</td>
            <td>The margin between the axis start and the first tick-mark</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-gap-start-and-end</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>
              If this is true then half the space between ticks is left at the
              start and end
            </td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Has all properties of <a href="#axis">Axis</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/bubblechart" class="btn btn-prev"
        >❮ BubbleChart</router-link
      >
      <router-link to="/css/chart" class="btn btn-next">Chart ❯</router-link>
    </div>
  </article>
</template>
