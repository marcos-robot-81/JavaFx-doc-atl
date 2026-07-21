<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>@media</h4>
    <p>A media query is a method of testing certain aspects of the <a href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Scene.html">Scene</a>
        or <a href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/stage/Stage.html">Stage</a>. Media queries are independent of the contents of the
        scene graph, its styling, or any other internal aspect; they're only dependent on "external" configuration of
        the <code>Scene</code> or <code>Stage</code>.
    </p><p>Several media queries can be combined into a comma-separated <strong>media query list</strong>.
        A media query list evaluates to <code>true</code> if <em>any</em> of the media queries is <code>true</code>,
        and evaluates to <code>false</code> only if <em>all</em> the media queries are <code>false</code>.
        An empty media query list evaluates to <code>true</code>.
        </p><figure style="margin: 0">
            <img src="/img/media-query_Sj7H.svg" width="210" alt="Media Query List">
            <figcaption style="float: left; margin-top: 27px">
                <span class="grammar">&lt;media-query-list&gt;:</span>
            </figcaption>
        </figure>
    <p>A <strong>media query</strong> consists of one or more <strong>media features</strong>.
        A media feature tests a single, specific feature of the <code>Scene</code>.
        Syntactically, media features resemble CSS properties: they consist of a feature name, a colon, and a value to
        test for. Media features are always enclosed in parentheses. They may also be written in boolean form as just a
        feature name, or in range form using arithmetic comparison operators.
        </p><figure style="margin: 0">
            <img src="/img/media-feature_Sj7H.svg" width="430" alt="Media Feature">
            <figcaption style="float: left; margin-top: 16px">
                <span class="grammar">&lt;media-feature&gt;:</span>
            </figcaption>
        </figure>
    <h5>Evaluating Media Features in a Boolean Context</h5>
    <p>If the colon and value is omitted, the media feature is evaluated in a boolean context.
        This is a convenient shorthand for features that have a reasonable default value. A media feature that is
        evaluated in a boolean context evaluates to <code>true</code> if it would be <code>true</code> for any value
        <em>other</em> than the reasonable default value.
    </p><p>For example, the <code>prefers-reduced-motion</code> media feature has a default value of <code>no-preference</code>.
        When evaluated in a boolean context, the media feature evaluates to <code>false</code> if the user has indicated no
        preference, and evaluates to <code>true</code> if the user has indicated the <code>reduce</code> preference.
    </p><h5>Evaluating Media Features in a Range Context</h5>
    <p>A media feature with a range type can be evaluated in a range context with two forms:
        </p><ol>
            <li>The <strong>basic form</strong> consists of a feature name, an arithmetic comparison operator,
                and a value. For example:<br>
                <code>
                    (width &gt; 600px)<br>
                    (500px &lt;= height)<br>
                </code>
                <br>
            </li><li>The <strong>interval form</strong> consists of a feature name, nested between two comparison
                operators and two values. For example:<br>
                <code>
                    (600px &gt;= width &gt;= 400px)<br>
                    (10em &lt; height &lt;= 20em)<br>
                </code>
        </li></ol>
        Rather than evaluating media features in a range context, they can also be evaluated in a discrete context by
        writing the feature name with a "min-" or "max-" prefix:
        <ul>
            <li>Using the "min-" prefix on a feature name is equivalent to using the <code>&gt;=</code> operator, for example:<br>
                <code>(min-height: 500px)</code> is equivalent to <code>(height &gt;= 500px)</code><br>
                <br>
            </li><li>Using the "max-" prefix on a feature name is equivalent to using the <code>&lt;=</code> operator, for example:<br>
                <code>(max-width: 600px)</code> is equivalent to <code>(width &lt;= 600px)</code><br>
        </li></ul>
    <h5>Combining Media Features</h5>
    <p>Media features can be combined using boolean algebra (<code>not</code>, <code>and</code>, <code>or</code>):
    </p><ul>
        <li>Any media feature can be negated by placing the <code>not</code> operator before it:<br>
            <code>
                &nbsp;&nbsp;&nbsp;&nbsp;@media not (prefers-color-scheme: light) { ... }<br>
            </code>
            <br>
        </li><li>Two or more media features can be chained together, such that the query is only true if <em>all</em> the
            media features are true, by placing the <code>and</code> operator between them:<br>
            <code>
                &nbsp;&nbsp;&nbsp;&nbsp;@media (prefers-color-scheme: dark) and<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (prefers-reduced-motion) and<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (prefers-reduced-transparency) { ... }<br>
            </code>
            <br>
        </li><li>Two or more media features can be chained together, such that the query is true if <em>any</em> of the
            media features are true, by placing the <code>or</code> operator between them:<br>
            <code>
                &nbsp;&nbsp;&nbsp;&nbsp;@media (prefers-color-scheme: dark) or<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (prefers-reduced-motion) or<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (prefers-reduced-transparency) { ... }<br>
            </code>
            <br>
        </li><li>Expressions can be grouped by wrapping them in parentheses:<br>
            <code>
                &nbsp;&nbsp;&nbsp;&nbsp;@media (prefers-color-scheme: dark) and<br>
                
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
((prefers-reduced-motion) or (prefers-reduced-transparency)) { ... }<br>
                &nbsp;&nbsp;&nbsp;&nbsp;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;@media (prefers-color-scheme: dark) and (not (prefers-reduced-motion)) { ... }<br>
            </code>
            <br>
        </li><li>It is invalid to mix different boolean operators at the same "level" of a media query. For example,
            the following expression is invalid, as it is unclear what was meant:<br>
            <code>
                &nbsp;&nbsp;&nbsp;&nbsp;@media (prefers-color-scheme: dark) and<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (prefers-reduced-motion) or<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (prefers-reduced-transparency) { ... }<br>
            </code>
            <br>
            In this case, parentheses must be used to group expressions.
    </li></ul>
    <table class="table table-dark table-striped table-hover table-bordered"  id="mediafeatures">
        <caption>Available media features</caption>
        <tbody>
            <tr>
                <th class="propertyname subheader" scope="col">Viewport Characteristics</th>
                <th class="subheader" scope="col">Value</th>
                <th class="subheader" scope="col">Type</th>
                <th class="subheader" scope="col">Comments</th>
            </tr>
            <tr>
                <td class="value">width</td>
                <td class="value"><a href="#typelength" class="typeref">&lt;length&gt;</a></td>
                <td>range</td>
                <td>corresponds to <code>Scene.width</code></td>
            </tr>
            <tr>
                <td class="value">height</td>
                <td class="value"><a href="#typelength" class="typeref">&lt;length&gt;</a></td>
                <td>range</td>
                <td>corresponds to <code>Scene.height</code></td>
            </tr>
            <tr>
                <td class="value">aspect-ratio</td>
                <td class="value"><a href="#typenumber" class="typeref">&lt;number&gt;</a></td>
                <td>range</td>
                <td>aspect ratio = <code>width</code> / <code>height</code></td>
            </tr>
            <tr>
                <td class="value">orientation</td>
                <td class="value">portrait | landscape</td>
                <td>discrete</td>
                <td><code>portrait</code> if <code>height</code> &gt;= <code>width</code>, <code>landscape</code> otherwise</td>
            </tr>
            <tr>
                <td class="value">display-mode</td>
                <td class="value">fullscreen | standalone</td>
                <td>discrete</td>
                <td><code>fullscreen</code> if <code>Stage.isFullScreen()</code>, <code>standalone</code> otherwise</td>
            </tr>
            <tr>
                <th class="propertyname subheader" scope="col">User Preference</th>
                <th class="subheader" scope="col">Value</th>
                <th class="subheader" scope="col">Type</th>
                <th class="subheader" scope="col">Comments</th>
            </tr>
            <tr>
                <td class="value">prefers-color-scheme</td>
                <td class="value">light | dark</td>
                <td>discrete</td>
                <td></td>
            </tr>
            <tr>
                <td class="value">prefers-reduced-data</td>
                <td class="value">no-preference | reduce</td>
                <td>discrete</td>
                <td><code>no-preference</code> evaluates as <code>false</code></td>
            </tr>
            <tr>
                <td class="value">prefers-reduced-motion</td>
                <td class="value">no-preference | reduce</td>
                <td>discrete</td>
                <td><code>no-preference</code> evaluates as <code>false</code></td>
            </tr>
            <tr>
                <td class="value">prefers-reduced-transparency</td>
                <td class="value">no-preference | reduce</td>
                <td>discrete</td>
                <td><code>no-preference</code> evaluates as <code>false</code></td>
            </tr>
            <tr>
                <td class="value">-fx-prefers-persistent-scrollbars</td>
                <td class="value">no-preference | persistent</td>
                <td>discrete</td>
                <td><code>no-preference</code> evaluates as <code>false</code></td>
            </tr>
        </tbody>
    </table>
    </section>
    <div class="pagination">
      <router-link to="/css/font-face" class="btn btn-prev">❮ @font-face</router-link>
      <router-link to="/css/examples" class="btn btn-next">Examples ❯</router-link>
    </div>
  </article>
</template>
