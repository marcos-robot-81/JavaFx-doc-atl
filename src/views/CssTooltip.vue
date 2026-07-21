<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="tooltip">Tooltip</a></h4>
    <p class="styleclass">Style class: tooltip</p>
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
        <th class="propertyname" scope="row">-fx-text-alignment</th>
          <td class="value">[ left | center | right | justify ]</td>
          <td>left</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-text-overrun</th>
          <td class="value">[ center-ellipsis | center-word-ellipsis | clip |
            ellipsis | leading-ellipsis | leading-word-ellipsis | word-ellipsis
            ]</td>
          <td>ellipsis</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-wrap-text</th>
          <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
          <td>false</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-graphic</th>
          <td class="value"><a href="#typeurl" class="typelink">&lt;uri&gt;</a></td>
          <td>null</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-content-display</th>
          <td class="value">[ top | right | bottom | left | center | right |
            graphic-only | text-only ]</td>
          <td>left</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-graphic-text-gap</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a></td>
          <td>4</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-font</th>
          <td class="value"><a href="#typefont" class="typelink">&lt;font&gt;</a></td>
          <td>Font.DEFAULT</td>
          <td>inherits</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-show-delay</th>
            <td class="value"><a href="#typefont" class="typelink">&lt;duration&gt;</a></td>
            <td>1000ms</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-show-duration</th>
            <td class="value"><a href="#typefont" class="typelink">&lt;duration&gt;</a></td>
            <td>5000ms</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-hide-delay</th>
            <td class="value"><a href="#typefont" class="typelink">&lt;duration&gt;</a></td>
            <td>200ms</td>
            <td>&nbsp;</td>
        </tr>

      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>label — Label</li>
      <li>page-corner — StackPane</li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/toolbar" class="btn btn-prev">❮ ToolBar</router-link>
      <router-link to="/css/treecell" class="btn btn-next">TreeCell ❯</router-link>
    </div>
  </article>
</template>
