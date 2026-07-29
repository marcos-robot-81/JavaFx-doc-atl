<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="slider">Slider</a></h4>
      <p class="styleclass">Style class: slider</p>
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
              <code>-fx-orientation</code>
            </th>
            <td class="value">[ horizontal | vertical ]</td>
            <td class="default">horizontal</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-show-tick-labels</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-show-tick-marks</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-major-tick-unit</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td>25</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-minor-tick-count</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td>3</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-show-tick-labels</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-snap-to-ticks</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-block-increment</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td>10</td>
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
            <th class="propertyname" scope="row">horizontal</th>
            <td>applies if this Slider is horizontal</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">vertical</th>
            <td>applies if this Slider is vertical</td>
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
        <li>axis — NumberAxis</li>
        <li>track — Region</li>
        <li>thumb — Region</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/spinner" class="btn btn-prev"
        >❮ Spinner</router-link
      >
      <router-link to="/css/splitmenubutton" class="btn btn-next"
        >SplitMenuButton ❯</router-link
      >
    </div>
  </article>
</template>
