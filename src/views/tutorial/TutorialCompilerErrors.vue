<template>
  <div class="tutorial-container">
    <header class="hero-section">
      <div class="glow-orb glow-orb-1"></div>
      <div class="glow-orb glow-orb-2"></div>
      <div class="hero-content">
        <div class="badge">Step 4</div>
        <h1 class="title">Reading Compiler Errors</h1>
        <p class="subtitle">Don't be afraid of the red messages in the console. Learn to decipher and resolve errors like a senior developer!</p>
      </div>
    </header>

    <main class="content-wrapper">
      <section class="card info-card">
        <div class="card-header">
          <div class="icon-wrapper">
            🚨
          </div>
          <h2>1. Identify the "Exception"</h2>
        </div>
        <p class="card-desc">The first thing to look for in the error is the word <strong>Exception</strong>. It tells you <em>what problem</em> Java encountered.</p>
        
        <ul class="import-list">
          <li class="import-item">
            <div class="import-name"><code>NullPointerException</code></div>
            <div class="import-desc">You tried to use an object that is <code>null</code> (empty). Java expected a real value but found nothing.</div>
          </li>
          <li class="import-item">
            <div class="import-name"><code>InvocationTargetException</code></div>
            <div class="import-desc">Very common when using <strong>FXMLLoader</strong>. It indicates that something went wrong while trying to load your FXML file or initialize your Controller.</div>
          </li>
        </ul>
      </section>

      <section class="card code-card">
        <div class="card-header">
          <div class="icon-wrapper accent-blue">
            📍
          </div>
          <h2>2. Find the Exact Line (Stack Trace)</h2>
        </div>
        <p class="card-desc">The <strong>Stack Trace</strong> is that long, intimidating list of method calls that Java spits out in the console. The golden tip is: scroll up the error and look for the <strong>first line that contains the name of your project/package</strong>.</p>
        
        <div class="code-block-wrapper">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">Console</span>
            <span class="language-tag">log</span>
          </div>
          <pre><code>Exception in thread "main" java.lang.NullPointerException
    at java.base/java.util.Objects.requireNonNull(Objects.java:208)
    <span class="keyword">at br.com.meuprojeto.Main.start(Main.java:25) 👈 Click here!</span>
    at javafx.graphics/com.sun.javafx.application.LauncherImpl.launchApplication1(LauncherImpl.java:825)</code></pre>
        </div>
        <p class="card-desc" style="margin-top: 1.5rem;">Modern IDEs usually make this text blue and clickable. Click the link and you will be taken exactly to the line of code where the error occurred!</p>

        <div class="info-alert">
          <strong>JavaFX Attention:</strong> In errors like <code>LoadException</code> (when something goes wrong while loading the interface), JavaFX is smart enough to point out the error <strong>directly inside your FXML file</strong>. <br><br>
          You will see something like: <code>Caused by: javafx.fxml.LoadException: /.../menu.fxml:26</code>.<br>
          This means the error is not in your Java code, but rather on <strong>line 26</strong> of the <code>menu.fxml</code> file (for example, a typo in a component name or an import that failed inside the FXML itself).
        </div>
      </section>

      <section class="card info-card">
        <div class="card-header">
          <div class="icon-wrapper">
            🧠
          </div>
          <h2>3. Translate Mentally</h2>
        </div>
        <p class="card-desc">Errors come in technical English, but they have super practical translations that you can quickly memorize in the JavaFX world:</p>
        
        <ul class="import-list">
          <li class="import-item">
            <div class="import-name"><code>"Location is not set"</code> or <code>"URL is null"</code></div>
            <div class="import-desc">
              <strong>Translation:</strong> You forgot, got the path wrong, or the FXML file is not in the correct <strong>resources</strong> folder.
            </div>
          </li>
          
          <li class="import-item">
            <div class="import-name"><code>"Cannot resolve symbol 'X'"</code></div>
            <div class="import-desc">
              <strong>Translation:</strong> You forgot to import the class or typed a variable name incorrectly in the code.
            </div>
          </li>
        </ul>
      </section>

      <section class="card code-card">
        <div class="card-header">
          <div class="icon-wrapper accent-blue">
            🔍
          </div>
          <h2>4. Case Study: Non-existent FXML File</h2>
        </div>
        <p class="card-desc">Look at this real example of a massive error that scares many beginners. Maven tried to run the project but failed miserably. How do you read this?</p>
        
        <div class="code-block-wrapper">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">Terminal (Maven)</span>
            <span class="language-tag">log</span>
          </div>
          <pre><code>Exception in Application start method
java.lang.reflect.InvocationTargetException
	... (lines hidden to focus on the main error)
Caused by: java.lang.RuntimeException: Exception in Application start method
	...
Caused by: javafx.fxml.LoadException: 
/home/her/.../target/classes/com/jurus/menu/menu.fxml:26
	...
<span class="keyword">Caused by: java.io.FileNotFoundException: /home/her/.../target/classes/com/jurus/smain.fxml (No such file or directory)</span>
	at java.base/java.io.FileInputStream.open0(Native Method)</code></pre>
        </div>
        
        <p class="card-desc" style="margin-top: 1.5rem;">
          <strong>How to decipher:</strong><br>
          When the error is very long, always scroll down and look for the last <strong><code>Caused by:</code></strong>. It is the real "culprit".<br><br>
          In this case, the root of the whole problem was: <code>java.io.FileNotFoundException</code>. JavaFX tried to load the <code>smain.fxml</code> file, but it doesn't exist inside the <code>target/classes/com/jurus/</code> folder. 
          <br><br>
          <strong>The Solution:</strong> Check if you typed the file name wrong in the code (e.g., <code>smain.fxml</code> instead of <code>main.fxml</code>) or if you forgot to place the FXML file inside the <code>src/main/resources/com/jurus/</code> folder before compiling with Maven!
        </p>
      </section>
    </main>
  </div>
</template>
