<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typenumber">&lt;number&gt; &amp;
        &lt;integer&gt;</a></h3>
    <p>Some value types may have integer values (denoted by &lt;integer&gt;) or
      real number values (denoted by &lt;number&gt;). Real numbers and integers
      are specified in decimal notation only. An &lt;integer&gt; consists of one
      or more digits "0" to "9". A &lt;number&gt; can either be an
      &lt;integer&gt;, or it can be zero or more digits followed by a dot (.)
      followed by one or more digits. Both integers and real numbers may be
      preceded by a "-" or "+" to indicate the sign. -0 is equivalent to 0 and
      is not a negative number.</p>
    <p class="grammar">[+|-]? [[0-9]+|[0-9]*"."[0-9]+]</p>
    <p>Note that many properties that allow an integer or real number as a value
      actually restrict the value to some range, often to a non-negative value.</p>
    </section>
    <div class="pagination">
      <router-link to="/css/string" class="btn btn-prev">❮ &lt;string&gt;</router-link>
      <router-link to="/css/size" class="btn btn-next">&lt;size&gt; ❯</router-link>
    </div>
  </article>
</template>
