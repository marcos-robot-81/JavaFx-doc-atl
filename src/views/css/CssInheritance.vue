<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="introinheritance">Inheritance</a></h3>
      <p>
        CSS also provides for certain properties to be inherited by default, or
        to be inherited if the property value is 'inherit'. If a value is
        inherited, it is inherited from the computed value of the element's
        parent in the document tree. In JavaFX, inheritance is similar, except
        that instead of elements in the document tree, inheritance occurs from
        parent nodes in the scene‑graph.
      </p>
      <p>
        The following properties inherit by default. Any property can be made to
        inherit by giving it the value
        <a href="#typeinherit" class="typelink">"inherit"</a>.
      </p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Properties that inherit by default
        </caption>
        <thead>
          <tr>
            <th scope="col">Class</th>
            <th scope="col">Property</th>
            <th scope="col">CSS Property</th>
            <th scope="col">Initial Value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">javafx.scene.Node</th>
            <td>cursor</td>
            <td><code>-fx-cursor</code></td>
            <td>javafx.scene.Cursor.DEFAULT</td>
          </tr>
          <tr>
            <th scope="row">javafx.scene.text.Text</th>
            <td>textAlignment</td>
            <td><code>-fx-text-alignment</code></td>
            <td>javafx.scene.text.TextAlignment.LEFT</td>
          </tr>
          <tr>
            <th scope="row">javafx.scene.text.Font</th>
            <td>font</td>
            <td>
              <code>-fx-font</code>, <code>-fx-font-family</code>,
              <code>-fx-font-size</code>, <code>-fx-font-weight</code>,
              <code>-fx-font-style</code>
            </td>
            <td>Font.DEFAULT (12px system)</td>
          </tr>
        </tbody>
      </table>
      <p>
        Within the hierarchy of JavaFX classes (for example, Rectangle is a
        subclass of Shape, which in turn is a subclass of Node), the CSS
        properties of an ancestor are also CSS properties of the descendant.
        This means that a subclass will respond to the same set of properties as
        its ancestor classes, and to additional properties it defines itself.
        So, a Shape supports all the properties of Node plus several more, and
        Rectangle supports all the properties of Shape plus a couple more.
        However, because using a JavaFX class name as a type selector is an
        exact match, providing style declarations for a Shape will not cause a
        Rectangle to use those values (unless the .css value for the Rectangle's
        property is "inherit").
      </p>
      <p>
        For font inheritance, the CSS engine looks
        <span style="font-style: italic">only</span> for the styles in the table
        above. When looking for a font to inherit, the search terminates at any
        node that has a Font property that was set by the user. The user-set
        font is inherited provided there is not an author or an inline-style
        that applies specifically to that node. In this case, the inherited font
        is created from the user-set font and any parts of the applicable author
        or in-line style.
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/css-public-api" class="btn btn-prev"
        >❮ CSS Public API</router-link
      >
      <router-link to="/css/transitions" class="btn btn-next"
        >Transitions ❯</router-link
      >
    </div>
  </article>
</template>
