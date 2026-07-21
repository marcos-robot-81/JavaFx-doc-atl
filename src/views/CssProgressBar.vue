<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="progressbar">ProgressBar</a></h4>
    <p class="styleclass">Style class: progress-bar</p>
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
        <th class="propertyname" scope="row">-fx-indeterminate-bar-length</th>
          <td class="value"><a href="#typenumber" class="typelink">&lt;number&gt;</a></td>
          <td>60</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-indeterminate-bar-escape</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;boolean&gt;</a></td>
          <td>true</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-indeterminate-bar-flip</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;boolean&gt;</a></td>
          <td>true</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-indeterminate-bar-animation-time</th>
          <td class="value"><a href="#typenumber" class="typelink">&lt;number&gt;</a></td>
          <td>2.0</td>
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
        <th class="propertyname" scope="row">CSS Pseudo-class</th>
            <th scope="col">Comments</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <th class="propertyname" scope="row">determinate</th>
            <td>applies if the <strong>indeterminate</strong> variable is false</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">indeterminate</th>
            <td>applies if the <strong>indeterminate</strong> variable is true</td>
        </tr>
        <tr>
        <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#control">Control</a></td>
        </tr>
        </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>track — StackPane
      <ul>
        <li>bar — Region</li>
      </ul>
      </li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/popupcontrol" class="btn btn-prev">❮ PopupControl</router-link>
      <router-link to="/css/progressindicator" class="btn btn-next">ProgressIndicator ❯</router-link>
    </div>
  </article>
</template>
