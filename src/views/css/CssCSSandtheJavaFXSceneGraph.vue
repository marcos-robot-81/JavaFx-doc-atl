<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="introscenegraph">CSS and the JavaFX Scene Graph</a></h3>
      <p>
        JavaFX Cascading Style Sheets (CSS) is based on the W3C CSS version 2.1
        <a href="#references">[1]</a> with some additions from current work on
        version 3 <a href="#references">[2]</a>. JavaFX CSS also has some
        extensions to CSS in support of specific JavaFX features. The goal for
        JavaFX CSS is to allow web developers already familiar with CSS for HTML
        to use CSS to customize and develop themes for JavaFX controls and
        scene‑graph objects in a natural way.
      </p>
      <p>
        JavaFX has a rich set of extensions to CSS in support of features such
        as color derivation, property lookup, and multiple background colors and
        borders for a single node. These features add significant new power for
        developers and designers and are described in detail in this document.
      </p>

      <p>
        To the extent possible, JavaFX CSS follows the W3C standards; however,
        with few exceptions, JavaFX property names have been prefixed with a
        vendor extension of "<code>-fx-</code>". Even if these properties seem
        to be compatible with standard HTML CSS, JavaFX CSS processing assumes
        that the property values make use of JavaFX CSS extensions.
      </p>

      <p>
        CSS styles are applied to nodes in the JavaFX scene‑graph in a way
        similar to the way CSS styles are applied to elements in the HTML DOM.
        Styles are first applied to the parent, then to its children. The code
        is written such that only those branches of the scene‑graph that might
        need CSS reapplied are visited. A node is styled after it is added to
        the scene graph. Styles are reapplied when there is a change to the
        node's pseudo‑class state, style‑class, id, inline style, or parent, or
        stylesheets are added to or removed from the scene. Note that the Node
        must be in the scene‑graph for CSS to be applied. The Node does not have
        to be shown, but must have a non‑null value for its sceneProperty. See
        <a
          href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Node.html#applyCss--"
          >applyCss</a
        >
        for more details.
      </p>

      <p>
        During a normal scene‑graph pulse, CSS styles are applied before the
        scene‑graph is laid out and painted. Styles for events that trigger a
        pseudo‑class state change, such as MouseEvent.MOUSE_ENTERED which
        triggers the "hover" state, are applied on the next pulse following the
        event.
      </p>
      <p>
        <a href="http://www.w3.org/TR/css3-selectors/">CSS selectors</a> are
        used to match styles to scene‑graph nodes. The relationship of a Node to
        a CSS selector is as follows:
      </p>
      <ul>
        <li>
          Node's
          <a
            href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Node.html#getTypeSelector--"
            >getTypeSelector</a
          >
          method returns a String which is analogous to a CSS
          <a href="http://www.w3.org/TR/css3-selectors/#type-selectors"
            >Type Selector</a
          >. By default, this method returns the simple name of the class. Note
          that the simple name of an inner class or of an anonymous class may
          not be usable as a type selector. In such a case, this method should
          be overridden to return a meaningful value.
        </li>
        <li>
          Each node in the scene‑graph has a
          <a
            href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Node.html#getStyleClass--"
            >styleClass property</a
          >. Note that a node may have more than one style‑class. A Node's
          styleClass is analogous to the class="..." attribute that can appear
          on HTML elements. See
          <a href="http://www.w3.org/TR/css3-selectors/#class-html"
            >Class Selectors</a
          >.
        </li>
        <li>
          Each node in the scene‑graph has an <strong>id</strong> variable, a
          string. This is analogous to the id="..." attribute that can appear
          HTML elements. See
          <a href="http://www.w3.org/TR/css3-selectors/#id-selectors"
            >ID Selectors</a
          >.
        </li>
      </ul>
      <p>
        JavaFX CSS also supports pseudo‑classes, but does not implement the full
        range of pseudo‑classes as specified in
        <a href="http://www.w3.org/TR/css3-selectors/#pseudo-classes"
          >Pseudo‑classes</a
        >. The pseudo‑classes supported by each Node type are given in the
        tables within this reference.
      </p>
      <p>
        Each node honors a set of properties that depends on the node's JavaFX
        class (as distinct from its styleClass). The properties honored by each
        node class are shown in detail in tables later in this document. The
        property value that is actually applied depends on the precedence of the
        origin of the rule, as described above, as well as the specificity of
        the rule's selector as described in CSS 2
        <a
          href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/doc-files/cssref.html#references"
          >[1]</a
        >
        . Ultimately, a property value string is converted into a JavaFX value
        of the appropriate type and is then assigned to an instance variable of
        the JavaFX object.
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/introduction" class="btn btn-prev"
        >❮ Introduction</router-link
      >
      <router-link
        to="/css/scene-parent-and-subscene-stylesheets"
        class="btn btn-next"
        >Scene, Parent and SubScene Stylesheets ❯</router-link
      >
    </div>
  </article>
</template>
