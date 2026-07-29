<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="listview">ListView</a></h4>
      <p class="styleclass">Style class: list-view</p>
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
            <td class="default">vertical</td>
            <td>&nbsp;</td>
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
            <td>applies if this ListView is horizontal</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">vertical</th>
            <td>applies if this ListView is vertical</td>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>
          .list-view — the ListView&lt;T&gt;
          <ul>
            <li>
              .virtual-flow — VirtualFlow
              <ul>
                <li>
                  .clipped-container — <a href="#region">Region</a>
                  <ul>
                    <li>
                      .sheet — Group
                      <ul>
                        <li>
                          .cell.indexed-cell.list-cell —
                          <a href="#listcell">ListCell&lt;T&gt;</a>
                        </li>
                      </ul>
                    </li>
                    <li>.scroll-bar — <a href="#scrollbar">ScrollBar</a></li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/listcell" class="btn btn-prev"
        >❮ ListCell</router-link
      >
      <router-link to="/css/menu" class="btn btn-next">Menu ❯</router-link>
    </div>
  </article>
</template>
