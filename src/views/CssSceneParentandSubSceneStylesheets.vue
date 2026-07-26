<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3>
        <a id="introstylesheets">Scene, Parent and SubScene Stylesheets</a>
      </h3>
      <p>
        CSS styles can come from style sheets or inline styles. Style sheets are
        loaded from the URLs specified in the
        <a
          href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Scene.html#getStylesheets--"
          >getStylesheets</a
        >
        property of the Scene object. If the scene‑graph contains a Control, a
        default user agent style sheet is loaded. Inline styles are specified
        via the Node <span style="font-weight: bold">setStyle</span> API. Inline
        styles are analogous to the style="..." attribute of an HTML element.
        Styles loaded from a Scene's style sheets take precedence over selectors
        from the user agent style sheet. Inline styles take precedence over
        styles originating elsewhere. The precedence order of style selectors
        can be modified using "!important" in a style declaration.
      </p>
      <p>
        Beginning with JavaFX 2.1, the Parent class has a
        <a
          href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Parent.html#getStylesheets--"
          >getStylesheets</a
        >
        property, allowing style sheets to be set on a container. This allows
        for one branch of of the scene‑graph to have a distinct set of styles.
        Any instance of Parent can have style sheets. A child will take its
        styles from its own inline styles, the style sheets of all its
        ancestors, and any style sheets from the Scene.
      </p>
      <p>
        Beginning with JavaFX 8u20, the Scene class has a
        <a
          href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Scene.html#getUserAgentStylesheet--"
          >getUserAgentStylesheet</a
        >
        property, allowing a user‑style sheet to be set on a Scene. This allows
        a Scene to have a set of user‑agent styles distinct from the platform
        default. When a user‑agent stylesheet is set on a Scene, the user‑agent
        styles are used instead of the styles from the platform default
        user‑agent stylesheet.
      </p>
      <p>
        Beginning with JavaFX 8u20, the SubScene class has a
        <a
          href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/SubScene.html#getUserAgentStylesheet--"
          >getUserAgentStylesheet</a
        >
        property, allowing a user‑style sheet to be set on a SubScene. This
        allows a SubScene of the scene‑graph to have set of user‑agent styles
        distinct from the platform default or from the Scene in which the
        SubScene is contained. When a user‑agent stylesheet is set on a
        SubScene, the user‑agent styles are used instead of the styles from the
        platform default user‑agent stylesheet or any user‑agent stylesheet set
        on the Scene.
      </p>
      <p>
        It is important to note that styles from a stylesheet added to a Scene
        or Parent, do not affect a SubScene which is a child or descendent of
        the Scene or Parent. Unless a user‑agent has been set on the SubScene,
        the SubScene will get styles from the a Scene's user‑agent stylesheet or
        the platform user‑agent stylesheet.
      </p>
      The implementation allows designers to style an application by using style
      sheets to override property values set from code. For example, a call to
      <code>rectangle.setFill(Color.YELLOW)</code> can be overridden by an
      inline‑style or a style from an author stylesheet. This has implications
      for the cascade; particularly, when does a style from a style sheet
      override a value set from code? The JavaFX CSS implementation applies the
      following order of precedence:
      <cite
        >a style from a user agent style sheet has lower priority than a value
        set from code, which has lower priority than a Scene or Parent style
        sheet. Inline styles have highest precedence. Style sheets from a Parent
        instance are considered to be more specific than those styles from Scene
        style sheets.</cite
      >
    </section>
    <div class="pagination">
      <router-link to="/css/css-and-the-javafx-scene-graph" class="btn btn-prev"
        >❮ CSS and the JavaFX Scene Graph</router-link
      >
      <router-link to="/css/naming-conventions" class="btn btn-next"
        >Naming Conventions ❯</router-link
      >
    </div>
  </article>
</template>
