<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="spinner">Spinner</a></h4>
    <p class="styleclass">Style class: spinner</p>
    <p>Note that the default style class, "spinner", puts arrows on right, stacked vertically. The following
        style classes can also be used in combination with the default style class in order to control the
        layout of the Spinner.
    </p>
<table class="table table-dark table-striped table-hover table-bordered" >
    <caption>Available Style Classes</caption>
        <thead>
        <tr>
        <th class="propertyname" scope="col">Style Class</th>
        <th scope="col">Comment</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <th scope="row" class="propertyname">arrows-on-right-horizontal</th>
            <td>The arrows are placed on the right of the Spinner, pointing horizontally (i.e. left and right)</td>
        </tr>
        <tr>
        <th scope="row" class="propertyname">arrows-on-left-vertical</th>
            <td>The arrows are placed on the left of the Spinner, pointing vertically (i.e. up and down)</td>
        </tr>
        <tr>
        <th scope="row" class="propertyname">arrows-on-left-horizontal</th>
            <td>The arrows are placed on the left of the Spinner, pointing horizontally (i.e. left and right)</td>
        </tr>
        <tr>
        <th scope="row" class="propertyname">split-arrows-vertical</th>
            <td>The arrows are placed above and beneath the spinner, stretching to take the entire width</td>
        </tr>
        <tr>
        <th scope="row" class="propertyname">split-arrows-horizontal</th>
            <td>The decrement arrow is placed on the left of the Spinner, and the increment on the right</td>
        </tr>
        </tbody>
    </table>

    <p>&nbsp;</p>
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
        <th scope="row" class="propertyname">-fx-initial-delay</th>
            <td class="value"><a href="#typeduration" class="typelink">&lt;duration&gt;</a></td>
            <td>300ms</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
        <th scope="row" class="propertyname">-fx-repeat-delay</th>
            <td class="value"><a href="#typeduration" class="typelink">&lt;duration&gt;</a></td>
            <td>60ms</td>
            <td>&nbsp;</td>
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
        <tr>
        <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#control">Control</a></td>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>text-field — TextField</li>
      <li>increment-arrow-button — StackPane
      <ul>
          <li>increment-arrow — Region</li>
      </ul>
      </li>
        <li>decrement-arrow-button — StackPane
            <ul>
                <li>decrement-arrow — Region</li>
            </ul>
        </li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/separator" class="btn btn-prev">❮ Separator</router-link>
      <router-link to="/css/slider" class="btn btn-next">Slider ❯</router-link>
    </div>
  </article>
</template>
