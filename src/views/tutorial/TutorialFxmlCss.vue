<template>
  <div class="tutorial-container">
    <header class="hero-section">
      <div class="glow-orb glow-orb-1"></div>
      <div class="glow-orb glow-orb-2"></div>
      <div class="hero-content">
        <div class="badge">Step 3</div>
        <h1 class="title">Converting to FXML and CSS</h1>
        <p class="subtitle">Decoupling the interface from logic to create modern and organized applications.</p>
      </div>
    </header>

    <main class="content-wrapper">
      <section class="card info-card">
        <div class="card-header">
          <div class="icon-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          </div>
          <h2>1. The FXML Interface</h2>
        </div>
        <p class="card-desc">
          In the previous step, we created a <strong>Hello World</strong> entirely in Java. Although it works for simple interfaces, this quickly becomes confusing and difficult to maintain. The recommended approach in JavaFX is to separate the interface using <strong>FXML</strong> and the styling using <strong>CSS</strong>.<br><br>
          FXML is an XML-based language used to define the structure of your graphical interface. Here is how our Hello World looks in FXML:
        </p>
        <div class="code-block-wrapper">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">hello-view.fxml</span>
            <span class="language-tag">xml</span>
          </div>
          <pre><code><span class="comment">&lt;?xml version="1.0" encoding="UTF-8"?&gt;</span>

<span class="keyword">&lt;?import</span> javafx.scene.control.Button<span class="keyword">?&gt;</span>
<span class="keyword">&lt;?import</span> javafx.scene.control.Label<span class="keyword">?&gt;</span>
<span class="keyword">&lt;?import</span> javafx.scene.layout.VBox<span class="keyword">?&gt;</span>

&lt;<span class="class-name">VBox</span> alignment=<span class="string">"CENTER"</span> spacing=<span class="string">"20.0"</span> xmlns=<span class="string">"http://javafx.com/javafx/8"</span> xmlns:fx=<span class="string">"http://javafx.com/fxml/1"</span> fx:controller=<span class="string">"com.exemplo.HelloController"</span>&gt;
    &lt;<span class="class-name">Label</span> fx:id=<span class="string">"welcomeText"</span> text=<span class="string">"Welcome to JavaFX!"</span>/&gt;
    &lt;<span class="class-name">Button</span> text=<span class="string">"Click Here!"</span> onAction=<span class="string">"#onHelloButtonClick"</span>/&gt;
&lt;/<span class="class-name">VBox</span>&gt;</code></pre>
        </div>

        <JavaFxPreview title="JavaFX FXML App" style="margin-top: 1.5rem;">
          <div style="display: flex; flex-direction: column; align-items: center; gap: 20px; padding: 20px; color: #1a1a1a; background-color: #f4f4f4; border-radius: 8px;">
            <span>Welcome to JavaFX!</span>
            <button style="padding: 5px 10px; color: #1a1a1a;">Click Here!</button>
          </div>
        </JavaFxPreview>
        <p class="card-desc" style="margin-top: 1.5rem;">
          <strong>Golden Tip:</strong> Note the <code>fx:controller</code> attribute on the root element. It tells JavaFX which Java class (Controller) will manage this interface.
        </p>
      </section>

      <section class="card code-card">
        <div class="card-header">
          <div class="icon-wrapper accent-blue">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
          </div>
          <h2>2. Styling with CSS</h2>
        </div>
        <p class="card-desc">
          JavaFX allows using CSS (with minor variations) to style your components. Let's give our button and text a more premium touch.
        </p>
        <div class="code-block-wrapper">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">style.css</span>
            <span class="language-tag">css</span>
          </div>
          <pre><code><span class="class-name">.root</span> {
    <span class="keyword">-fx-background-color</span>: <span class="string">#1a1a2e</span>;
    <span class="keyword">-fx-padding</span>: <span class="number">40px</span>;
}

<span class="class-name">.label</span> {
    <span class="keyword">-fx-font-size</span>: <span class="number">24px</span>;
    <span class="keyword">-fx-font-family</span>: <span class="string">'Inter', sans-serif</span>;
    <span class="keyword">-fx-text-fill</span>: <span class="string">#ffffff</span>;
    <span class="keyword">-fx-font-weight</span>: <span class="keyword">bold</span>;
}

<span class="class-name">.button</span> {
    <span class="keyword">-fx-background-color</span>: <span class="string">#0f3460</span>;
    <span class="keyword">-fx-text-fill</span>: <span class="string">white</span>;
    <span class="keyword">-fx-font-size</span>: <span class="number">16px</span>;
    <span class="keyword">-fx-padding</span>: <span class="number">10px 20px</span>;
    <span class="keyword">-fx-background-radius</span>: <span class="number">8px</span>;
    <span class="keyword">-fx-cursor</span>: <span class="string">hand</span>;
}

<span class="class-name">.button:hover</span> {
    <span class="keyword">-fx-background-color</span>: <span class="string">#e94560</span>;
}</code></pre>
        </div>

        <JavaFxPreview title="JavaFX FXML App - Styled" style="margin-top: 1.5rem;">
          <div style="background-color: #1a1a2e; padding: 40px; display: flex; flex-direction: column; align-items: center; gap: 20px; border-radius: 8px;">
            <span style="font-size: 24px; font-family: 'Inter', sans-serif; color: #ffffff; font-weight: bold;">Welcome to JavaFX!</span>
            <button style="background-color: #0f3460; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px; cursor: pointer; border: none;" onmouseover="this.style.backgroundColor='#e94560'" onmouseout="this.style.backgroundColor='#0f3460'">Click Here!</button>
          </div>
        </JavaFxPreview>
      </section>

      <section class="card code-card">
        <div class="card-header">
          <div class="icon-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
          </div>
          <h2>3. The Java Code and the Controller</h2>
        </div>
        <p class="card-desc">
          Now, our main class stays super lean. We use <code>FXMLLoader</code> to read the FXML file and build the interface.
        </p>
        <div class="code-block-wrapper">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">HelloApplication.java</span>
            <span class="language-tag">java</span>
          </div>
          <pre><code><span class="keyword">package</span> com.exemplo;

<span class="keyword">import</span> javafx.application.Application;
<span class="keyword">import</span> javafx.fxml.FXMLLoader;
<span class="keyword">import</span> javafx.scene.Scene;
<span class="keyword">import</span> javafx.stage.Stage;

<span class="keyword">public class</span> <span class="class-name">HelloApplication</span> <span class="keyword">extends</span> <span class="class-name">Application</span> {
    <span class="annotation">@Override</span>
    <span class="keyword">public void</span> <span class="method">start</span>(Stage stage) <span class="keyword">throws</span> Exception {
        FXMLLoader fxmlLoader = <span class="keyword">new</span> FXMLLoader(HelloApplication.class.getResource(<span class="string">"hello-view.fxml"</span>));
        Scene scene = <span class="keyword">new</span> Scene(fxmlLoader.load(), <span class="number">400</span>, <span class="number">300</span>);
        
        <span class="comment">// Adding CSS</span>
        scene.getStylesheets().add(getClass().getResource(<span class="string">"style.css"</span>).toExternalForm());
        
        stage.setTitle(<span class="string">"Hello JavaFX with FXML and CSS!"</span>);
        stage.setScene(scene);
        stage.show();
    }

    <span class="keyword">public static void</span> <span class="method">main</span>(String[] args) {
        launch(args);
    }
}</code></pre>
        </div>

        <JavaFxPreview title="Hello JavaFX with FXML and CSS!" style="margin-top: 1.5rem;">
          <div style="background-color: #1a1a2e; padding: 40px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 20px; border-radius: 8px; min-height: 220px;">
            <span style="font-size: 24px; font-family: 'Inter', sans-serif; color: #ffffff; font-weight: bold; text-align: center;">Welcome to JavaFX!</span>
            <button style="background-color: #0f3460; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px; cursor: pointer; border: none;" onmouseover="this.style.backgroundColor='#e94560'" onmouseout="this.style.backgroundColor='#0f3460'">Click Here!</button>
          </div>
        </JavaFxPreview>

        <h2 style="margin-top: 2rem; margin-bottom: 1rem; font-size: 1.5rem;">Understanding the Controller and @FXML</h2>
        <p class="card-desc">
          The <strong>Controller</strong> is the "glue" between your interface (FXML) and your business logic. We use the <code>@FXML</code> annotation to inject visual components from FXML directly into Java, allowing interaction.
        </p>
        
        <div class="code-block-wrapper" style="margin-bottom: 2rem;">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">HelloController.java</span>
            <span class="language-tag">java</span>
          </div>
          <pre><code><span class="keyword">package</span> com.exemplo;

<span class="keyword">import</span> javafx.fxml.FXML;
<span class="keyword">import</span> javafx.scene.control.Label;

<span class="keyword">public class</span> <span class="class-name">HelloController</span> {
    
    <span class="comment">// Injects the Label that has fx:id="welcomeText" in FXML</span>
    <span class="annotation">@FXML</span>
    <span class="keyword">private</span> Label welcomeText;

    <span class="comment">// Method referenced in FXML by onAction="#onHelloButtonClick"</span>
    <span class="annotation">@FXML</span>
    <span class="keyword">protected void</span> <span class="method">onHelloButtonClick</span>() {
        welcomeText.setText(<span class="string">"Thanks for clicking! FXML + CSS is amazing."</span>);
    }
}</code></pre>
        </div>

        <JavaFxPreview title="Hello JavaFX with FXML and CSS!" style="margin-bottom: 2rem;">
          <div style="background-color: #1a1a2e; padding: 40px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 20px; border-radius: 8px; min-height: 220px;">
            <span style="font-size: 24px; font-family: 'Inter', sans-serif; color: #ffffff; font-weight: bold; text-align: center;">Thanks for clicking! FXML + CSS is amazing.</span>
            <button style="background-color: #0f3460; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px; cursor: pointer; border: none;" onmouseover="this.style.backgroundColor='#e94560'" onmouseout="this.style.backgroundColor='#0f3460'">Click Here!</button>
          </div>
        </JavaFxPreview>

        <ul class="import-list">
          <li class="import-item">
            <div class="import-name"><code>@FXML</code></div>
            <div class="import-desc">Signals to JavaFX that the variable or method should be accessible to the FXML loader (even if it is <code>private</code> or <code>protected</code>).</div>
          </li>
          <li class="import-item">
            <div class="import-name"><code>fx:id</code></div>
            <div class="import-desc">If you have a <code>&lt;Label fx:id="welcomeText"/&gt;</code> in FXML, the variable in Java <strong>must</strong> have exactly the same name.</div>
          </li>
        </ul>
      </section>
    </main>
  </div>
</template>
