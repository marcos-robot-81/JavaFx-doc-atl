<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>Drop Shadow</h4>
    <p>A high-level effect that renders a shadow of the given content behind the
      content.</p>
    <p><span class="grammar">dropshadow( &lt;blur-type&gt; , <a href="#typecolor" class="typelink">&lt;color&gt;</a>
        , <a href="#typenumber" class="typelink">&lt;number&gt;</a> , <a href="#typenumber" class="typelink">&lt;number&gt;</a>
        , <a href="#typenumber" class="typelink">&lt;number&gt;</a> , <a href="#typenumber" class="typelink">&lt;number&gt;</a>
        )</span></p>
    <p style="margin-left: 40px;"><span class="grammar">&lt;blur-type&gt; = [
        gaussian | one-pass-box | three-pass-box | two-pass-box ]<br>
        <a href="#typecolor" class="typelink">&lt;color&gt;</a></span> The
      shadow Color.<br>
      <span class="grammar"><a href="#typenumber" class="typelink">&lt;number&gt;</a></span>
      The radius of the shadow blur kernel. In the range [0.0 ... 127.0],
      typical value 10.<br>
      <span class="grammar"><a href="#typenumber" class="typelink">&lt;number&gt;</a></span>
      The spread of the shadow. The spread is the portion of the radius where
      the contribution of the source material will be 100%. The remaining
      portion of the radius will have a contribution controlled by the blur
      kernel. A spread of 0.0 will result in a distribution of the shadow
      determined entirely by the blur algorithm. A spread of 1.0 will result in
      a solid growth outward of the source material opacity to the limit of the
      radius with a very sharp cutoff to transparency at the radius. Values
      should be in the range [0.0 ... 1.0].<br>
      <span class="grammar"><a href="#typenumber" class="typelink">&lt;number&gt;</a></span>
      The shadow offset in the x direction, in pixels. <br>
      <span class="grammar"><a href="#typenumber" class="typelink">&lt;number&gt;</a></span>
      The shadow offset in the y direction, in pixels. </p>
    </section>
    <div class="pagination">
      <router-link to="/css/effect" class="btn btn-prev">❮ &lt;effect&gt;</router-link>
      <router-link to="/css/inner-shadow" class="btn btn-next">Inner Shadow ❯</router-link>
    </div>
  </article>
</template>
