<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typestring">&lt;string&gt;</a></h3>
    <p>Strings can either be written with double quotes or with single quotes.
      Double quotes cannot occur inside double quotes, unless escaped (e.g., as
      '\"' or as '\22'). Analogously for single quotes (e.g., "\'" or "\27").</p>
    <p class="example">"this is a 'string'"<br>
      "this is a \"string\""<br>
      'this is a "string"'<br>
      'this is a \'string\''</p>
    <p>A string cannot directly contain a newline. To include a newline in a
      string, use an escape representing the line feed character in ISO-10646
      (U+000A), such as "\A" or "\00000a". This character represents the generic
      notion of "newline" in CSS. See the 'content' property for an example.</p>
    </section>
    <div class="pagination">
      <router-link to="/css/boolean" class="btn btn-prev">❮ &lt;boolean&gt;</router-link>
      <router-link to="/css/number-----integer" class="btn btn-next">&lt;number&gt; &amp;         &lt;integer&gt; ❯</router-link>
    </div>
  </article>
</template>
