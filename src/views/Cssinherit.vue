<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typeinherit">inherit</a></h3>
      <p>
        Each property has a type, which determines what kind of value and the
        syntax for specifying those values. In addition, each property may have
        a specified value of 'inherit', which means that, for a given node, the
        property takes the same computed value as the property for the node's
        parent. The 'inherit' value can be used on properties that are not
        normally inherited.
      </p>
      <p>
        If the 'inherit' value is set on the root element, the property is
        assigned its initial value.
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/types" class="btn btn-prev">❮ Types</router-link>
      <router-link to="/css/boolean" class="btn btn-next"
        >&lt;boolean&gt; ❯</router-link
      >
    </div>
  </article>
</template>
