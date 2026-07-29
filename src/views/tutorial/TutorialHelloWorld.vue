<template>
  <div class="tutorial-container">
    <header class="hero-section">
      <div class="glow-orb glow-orb-1"></div>
      <div class="glow-orb glow-orb-2"></div>
      <div class="hero-content">
        <div class="badge">Step 2</div>
        <h1 class="title">Hello World in JavaFX</h1>
        <p class="subtitle">Building your first interactive graphical interface step by step.</p>
      </div>
    </header>

    <main class="content-wrapper">
      <!-- Imports Section -->
      <section class="card info-card">
        <div class="card-header">
          <div class="icon-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
          </div>
          <h2>Understanding the Fundamental Imports</h2>
        </div>
        <p class="card-desc">
          Before we write the code for our application, it is crucial to understand the building blocks that JavaFX provides.
          Every JavaFX application needs to import some essential classes from the <code>javafx</code> package.
        </p>

        <ul class="import-list">
          <li class="import-item">
            <div class="import-name"><code>javafx.application.Application</code></div>
            <div class="import-desc">The base class for all JavaFX applications. Your main class must extend <code>Application</code> and implement the mandatory <code>start(Stage)</code> method, which is the entry point for the graphical interface.</div>
          </li>
          <li class="import-item">
            <div class="import-name"><code>javafx.stage.Stage</code></div>
            <div class="import-desc">Think of the <code>Stage</code> as a theater <strong>Stage</strong>. It represents the main operating system window where your application will live.</div>
          </li>
          <li class="import-item">
            <div class="import-name"><code>javafx.scene.Scene</code></div>
            <div class="import-desc">The <code>Scene</code> is the <strong>Scene</strong> that takes place on the stage. It contains the "tree" of all visual elements (nodes) that make up your interface. A stage can only display one scene at a time.</div>
          </li>
          <li class="import-item">
            <div class="import-name"><code>javafx.scene.layout.VBox</code></div>
            <div class="import-desc">A layout manager (Container). The <code>VBox</code> automatically organizes all its children into a single vertical column.</div>
          </li>
          <li class="import-item">
            <div class="import-name"><code>javafx.scene.control.*</code></div>
            <div class="import-desc">This package contains the interface controls the user interacts with. We will use the <code>Button</code> (Button for actions), <code>TextField</code> (Text box for input), and <code>Label</code> (Label to display texts).</div>
          </li>
        </ul>
      </section>

      <!-- Code Section -->
      <section class="card code-card">
         <div class="card-header">
          <div class="icon-wrapper accent-blue">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          </div>
          <h2>The Code: Interactive Hello World</h2>
        </div>
        <p class="card-desc">
          It's time to code! Below is the complete code. We created a text field for the user to type their name and a button that, when clicked, updates the message displayed on the screen formatted in English.
        </p>

        <div class="code-block-wrapper">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">HelloWorld.java</span>
            <span class="language-tag">java</span>
          </div>
          <pre><code><span class="keyword">import</span> javafx.application.Application;
<span class="keyword">import</span> javafx.geometry.Insets;
<span class="keyword">import</span> javafx.geometry.Pos;
<span class="keyword">import</span> javafx.scene.Scene;
<span class="keyword">import</span> javafx.scene.control.Button;
<span class="keyword">import</span> javafx.scene.control.Label;
<span class="keyword">import</span> javafx.scene.control.TextField;
<span class="keyword">import</span> javafx.scene.layout.VBox;
<span class="keyword">import</span> javafx.stage.Stage;

<span class="keyword">public class</span> <span class="class-name">HelloWorld</span> <span class="keyword">extends</span> <span class="class-name">Application</span> {

    <span class="annotation">@Override</span>
    <span class="keyword">public void</span> <span class="method">start</span>(Stage primaryStage) {
        <span class="comment">// 1. Creating the visual components</span>
        Label titleLabel = <span class="keyword">new</span> Label(<span class="string">"What is your name?"</span>);
        titleLabel.setStyle(<span class="string">"-fx-font-size: 16px; -fx-font-weight: bold;"</span>);
        
        TextField nameInput = <span class="keyword">new</span> TextField();
        nameInput.setPromptText(<span class="string">"Ex: John Doe"</span>);
        nameInput.setMaxWidth(<span class="number">200</span>);

        Button greetButton = <span class="keyword">new</span> Button(<span class="string">"Say Hello"</span>);
        greetButton.setStyle(<span class="string">"-fx-background-color: #2196F3; -fx-text-fill: #1a1a1a; -fx-cursor: hand;"</span>);

        Label resultLabel = <span class="keyword">new</span> Label();
        resultLabel.setStyle(<span class="string">"-fx-font-size: 18px; -fx-text-fill: #4CAF50;"</span>);

        <span class="comment">// 2. Adding the button click action</span>
        greetButton.setOnAction(event -> {
            String name = nameInput.getText();
            <span class="keyword">if</span> (name == <span class="keyword">null</span> || name.trim().isEmpty()) {
                resultLabel.setText(<span class="string">"Hello, World!"</span>);
                resultLabel.setStyle(<span class="string">"-fx-text-fill: #F44336;"</span>); <span class="comment">// Red if empty</span>
            } <span class="keyword">else</span> {
                resultLabel.setText(<span class="string">"Hello, "</span> + name + <span class="string">"!"</span>);
                resultLabel.setStyle(<span class="string">"-fx-text-fill: #4CAF50;"</span>); <span class="comment">// Green when it has a name</span>
            }
        });

        <span class="comment">// 3. Configuring the Layout (VBox organizes vertically)</span>
        VBox root = <span class="keyword">new</span> VBox(<span class="number">15</span>); <span class="comment">// 15px spacing between items</span>
        root.setAlignment(Pos.CENTER);
        root.setPadding(<span class="keyword">new</span> Insets(<span class="number">20</span>));
        root.getChildren().addAll(titleLabel, nameInput, greetButton, resultLabel);

        <span class="comment">// 4. Creating the Scene and placing it on the Stage</span>
        Scene scene = <span class="keyword">new</span> Scene(root, <span class="number">350</span>, <span class="number">250</span>);
        
        primaryStage.setTitle(<span class="string">"My First JavaFX App"</span>);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    <span class="keyword">public static void</span> <span class="method">main</span>(String[] args) {
        launch(args); <span class="comment">// Starts the JavaFX application</span>
    }
}</code></pre>
        </div>

        <JavaFxPreview title="My First JavaFX App">
          <div style="display: flex; flex-direction: column; gap: 15px; align-items: center; justify-content: center; padding: 20px; min-height: 250px; background-color: #f4f4f4; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <div style="font-size: 16px; font-weight: bold;">What is your name?</div>
            <input type="text" placeholder="Ex: John Doe" style="width: 100%; max-width: 200px; padding: 8px; border: 1px solid #a9a9a9; border-radius: 3px;" />
            <button class="javafx-btn" style="background-color: #2196F3; color: #1a1a1a; cursor: pointer; padding: 8px 15px; border: none; border-radius: 3px; font-weight: bold;">Say Hello</button>
            <div style="font-size: 18px; color: #4CAF50; min-height: 24px;"></div>
          </div>
        </JavaFxPreview>
      </section>
    </main>
  </div>
</template>


