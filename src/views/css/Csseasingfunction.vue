<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typeeasingfunction">&lt;easing-function&gt;</a></h3>
      <p class="grammar">
        linear | &lt;linear-easing-function&gt; |
        &lt;cubic-bezier-easing-function&gt; | &lt;step-easing-function&gt; |
        &lt;fx-easing-function&gt;
      </p>
      <p>
        <strong>Linear</strong>
        <span class="grammar" style="font-size: smaller">linear</span><br />
        The linear easing keyword is a simple linear mapping from the input
        progress value to the output progress value.<br />
        It it equivalent to <span class="grammar">linear(0, 1)</span>
      </p>
      <figure style="display: inline-block">
        <img
          src="/img/easing-linear_Sj7H.svg"
          width="200"
          alt="Linear easing function"
        />
      </figure>
      <p>
        <strong>Linear Easing Function</strong>
        <span class="grammar" style="font-size: smaller"
          >&lt;linear-easing-function&gt;</span
        ><br />
      </p>
      <p class="grammar">
        linear([
        <a href="#typenumber" class="typelink">&lt;number&gt;</a> &amp;&amp;
        <a href="#typepercentage" class="typelink">&lt;percentage&gt;{0,2}</a>
        ]#)
      </p>
      <p>
        The linear easing function interpolates linearly between its control
        points. The control points are specified as a comma-separated list of
        two or more items, where each item consists of a
        <a href="#typenumber" class="typelink">&lt;number&gt;</a>, optionally
        followed by one or two
        <a href="#typepercentage" class="typelink">&lt;percentage&gt;</a>
        values.
      </p>
      <p>
        The <a href="#typenumber" class="typelink">&lt;number&gt;</a> specifies
        the progress of the animation in time. The optional
        <a href="#typepercentage" class="typelink">&lt;percentage&gt;</a>
        specifies when that progress is reached; if two percentages are
        specified, they indicate a segment of time when the animation is paused.
        If no percentage is specified, the control point is spaced evenly
        between neighboring control points.
      </p>
      <p>Examples of linear easing functions:</p>
      <figure style="display: inline-block">
        <img
          src="/img/easing-linear-func1_Sj7H.svg"
          width="200"
          alt="linear easing function"
        />
        <figcaption style="margin-left: 40px" class="grammar">
          linear(0, 0.25, 1)
        </figcaption>
      </figure>
      <figure style="display: inline-block">
        <img
          src="/img/easing-linear-func2_Sj7H.svg"
          width="200"
          alt="linear easing function"
        />
        <figcaption style="margin-left: 20px" class="grammar">
          linear(0, 0.25 75%, 1)
        </figcaption>
      </figure>
      <figure style="display: inline-block">
        <img
          src="/img/easing-linear-func3_Sj7H.svg"
          width="200"
          alt="linear easing function"
        />
        <figcaption style="margin-left: 10px" class="grammar">
          linear(0, 0.25 25% 75%, 1)
        </figcaption>
      </figure>
      <p>
        <strong>Cubic Bézier Easing Functions</strong>
        <span class="grammar" style="font-size: smaller"
          >&lt;cubic-bezier-easing-function&gt;</span
        ><br />
      </p>
      <p class="grammar">
        ease | ease-in | ease-out | ease-in-out | cubic-bezier(<a
          href="#typenumber"
          class="typelink"
          >&lt;number&nbsp;[0,1]&gt;</a
        >, <a href="#typenumber" class="typelink">&lt;number&gt;</a>,
        <a href="#typenumber" class="typelink">&lt;number&nbsp;[0,1]&gt;</a>,
        <a href="#typenumber" class="typelink">&lt;number&gt;</a>)
      </p>
      <p>The values have the following meaning:</p>
      <table
        class="table table-dark table-striped table-hover table-bordered"
        role="presentation"
        summary="Cubic Bézier Easing Functions"
      >
        <tbody>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">ease</span>
            </td>
            <td>
              equivalent to
              <span class="grammar">cubic-bezier(0.25, 0.1, 0.25, 1)</span>
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">ease-in</span>
            </td>
            <td>
              equivalent to
              <span class="grammar">cubic-bezier(0.42, 0, 1, 1)</span>
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">ease-out</span>
            </td>
            <td>
              equivalent to
              <span class="grammar">cubic-bezier(0, 0, 0.58, 1)</span>
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">ease-in-out</span>
            </td>
            <td>
              equivalent to
              <span class="grammar">cubic-bezier(0.42, 0, 0.58, 1)</span>
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">cubic-bezier</span>
            </td>
            <td>
              defines the control points P1 and P2 using four real numbers:
              (x<sub>P1</sub>, y<sub>P1</sub>, x<sub>P2</sub>, y<sub>P2</sub>)
            </td>
          </tr>
        </tbody>
      </table>
      <p>
        A cubic Bézier function is defined by four control points, where P0 is
        fixed at (0,0) and P3 is fixed at (1,1). P1 and P2 are restricted to the
        interval [0,1] on the input progress axis:
      </p>
      <figure style="display: inline-block">
        <img
          src="/img/easing-cubicbezier_Sj7H.svg"
          width="200"
          alt="Cubic Bèzier easing function"
        />
      </figure>
      <p>
        <strong>Step Easing Functions</strong>
        <span class="grammar" style="font-size: smaller"
          >&lt;step-easing-function&gt;</span
        >
      </p>
      <p class="grammar">
        step-start | step-end | steps(<a href="#typenumber" class="typelink"
          >&lt;integer&gt;</a
        >[,&lt;step-position&gt;]?)
      </p>
      <p class="grammar">
        where &lt;step-position&gt; = jump-start | jump-end | jump-none |
        jump-both | start | end
      </p>
      <p>The values have the following meaning:</p>
      <table
        class="table table-dark table-striped table-hover table-bordered"
        role="presentation"
        summary="Step Easing Functions"
      >
        <tbody>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">step-start</span>
            </td>
            <td>equivalent to <span class="grammar">steps(1, start)</span></td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">step-end</span>
            </td>
            <td>equivalent to <span class="grammar">steps(1, end)</span></td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">steps</span>
            </td>
            <td>
              defines a step function with
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
              intervals and an optional
              <span class="grammar">&lt;step-position&gt;</span>;<br />if
              omitted, <span class="grammar">end</span> is implied
            </td>
          </tr>
          <tr>
            <td><br /></td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">jump-start</span>
            </td>
            <td>
              the interval starts with a rise point when the input progress
              value is 0
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">jump-end</span>
            </td>
            <td>
              the interval ends with a rise point when the input progress value
              is 1
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">jump-none</span>
            </td>
            <td>all rise points are within the open interval (0..1)</td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">jump-both</span>
            </td>
            <td>
              the interval starts with a rise point when the input progress
              value is 0, and ends with a rise point when the input progress
              value is 1
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">start</span>
            </td>
            <td>equivalent to <span class="grammar">jump-start</span></td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar">end</span>
            </td>
            <td>equivalent to <span class="grammar">jump-end</span></td>
          </tr>
        </tbody>
      </table>
      <p>Examples of step easing functions:</p>
      <figure style="display: inline-block">
        <img
          src="/img/easing-stepstart_Sj7H.svg"
          width="200"
          alt="jump-start easing function"
        />
        <figcaption style="margin-left: 30px" class="grammar">
          steps(3, jump-start)
        </figcaption>
      </figure>
      <figure style="display: inline-block">
        <img
          src="/img/easing-stepend_Sj7H.svg"
          width="200"
          alt="jump-end easing function"
        />
        <figcaption style="margin-left: 30px" class="grammar">
          steps(3, jump-end)
        </figcaption>
      </figure>
      <figure style="display: inline-block">
        <img
          src="/img/easing-stepnone_Sj7H.svg"
          width="200"
          alt="jump-none easing function"
        />
        <figcaption style="margin-left: 30px" class="grammar">
          steps(3, jump-none)
        </figcaption>
      </figure>
      <figure style="display: inline-block">
        <img
          src="/img/easing-stepboth_Sj7H.svg"
          width="200"
          alt="jump-both easing function"
        />
        <figcaption style="margin-left: 30px" class="grammar">
          steps(3, jump-both)
        </figcaption>
      </figure>
      <p>
        <strong>SMIL 3.0 Easing Functions</strong>
        <span class="grammar" style="font-size: smaller"
          >&lt;fx-easing-function&gt;</span
        ><br />
      </p>
      <p class="grammar">
        <code>-fx-ease-in</code> | <code>-fx-ease-out</code> |
        <code>-fx-ease-both</code>
      </p>
      <p>The values have the following meaning:</p>
      <table
        class="table table-dark table-striped table-hover table-bordered"
        role="presentation"
        summary="SMIL 3.0 Easing Functions"
      >
        <tbody>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar"><code>-fx-ease-in</code></span>
            </td>
            <td>
              SMIL 3.0 ease-in function with an acceleration factor of 0.2
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar"><code>-fx-ease-out</code></span>
            </td>
            <td>
              SMIL 3.0 ease-out function with a deceleration factor of 0.2
            </td>
          </tr>
          <tr>
            <td style="width: 120px; vertical-align: top">
              <span class="grammar"><code>-fx-ease-both</code></span>
            </td>
            <td>
              SMIL 3.0 ease-in/out function with an acceleration and
              decelaration factor of 0.2
            </td>
          </tr>
        </tbody>
      </table>
      <p>
        These functions are provided for compatibility with
        <code>javafx.animation.Interpolator</code> implementations of SMIL 3.0
        cubic bezier easing functions.
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/color-functions-color-function" class="btn btn-prev"
        >❮ Color Functions &lt;color-function&gt;</router-link
      >
      <router-link to="/css/text-bounds" class="btn btn-next"
        >&lt;text-bounds&gt; ❯</router-link
      >
    </div>
  </article>
</template>
