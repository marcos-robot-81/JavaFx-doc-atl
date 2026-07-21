<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="pagination">Pagination</a></h4>
    <p class="styleclass">Style class: pagination</p>
	<p>Pagination has all the pseudo‑class states of <a href="#control">Control</a></p>
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
        <th class="propertyname" scope="row">-fx-max-page-indicator-count</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;number&gt;</a></td>
          <td>10</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-arrows-visible</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;boolean&gt;</a></td>
          <td>true</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-tooltip-visible</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;boolean&gt;</a></td>
          <td>false</td>
          <td>When set to true, a tooltip which shows the page number is set on the page indicators.
              This property controls whether or not the tooltip is visible on the page indicators and <em>does
              not</em> affect the visibility of the tooltip set or installed on the Pagination control itself.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-page-information-visible</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;boolean&gt;</a></td>
          <td>true</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-page-information-alignment</th>
          <td class="value">[ top | bottom | left | right ]</td>
          <td>bottom</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th colspan="4" class="parents" scope="row">Also has all properties of <a href="#control">Control</a></th>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
	  <li>page — StackPane</li>
      <li>pagination-control — StackPane
        <ul>
          <li>leftArrowButton — Button
	        <ul>
		      <li>leftArrow — StackPane</li>
	        </ul>
          </li>
	      <li>rightArrowButton — Button
     	    <ul>
	    	  <li>rightArrow — StackPane</li>
	        </ul>
          </li>
	      <li>bullet-button — ToggleButton</li>
	      <li>number-button — ToogleButton</li>
	      <li>page-information — Label</li>
	  </ul>
      </li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/menuitem" class="btn btn-prev">❮ MenuItem</router-link>
      <router-link to="/css/passwordfield" class="btn btn-next">PasswordField ❯</router-link>
    </div>
  </article>
</template>
