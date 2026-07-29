<template>
  <div class="home-container">
    <div class="hero">
      <h1 class="title">JavaFX <span class="highlight">Modern Docs</span></h1>
      <p class="subtitle">
        The ultimate, beautifully designed documentation for JavaFX, FXML, and CSS.
      </p>
      
      <div class="cta-buttons">
        <router-link to="/fxml/overview" class="btn btn-primary">Start FXML Tutorial</router-link>
        <router-link to="/css/introduction" class="btn btn-secondary">Explore CSS Reference</router-link>
      </div>
    </div>

    <section class="features">
      <div class="feature-card">
        <div class="icon-wrapper">🚀</div>
        <h3>Modern Design</h3>
        <p>A complete visual overhaul of the classic JavaFX documentation, featuring dark mode, glassmorphism, and responsive layouts.</p>
      </div>
      <div class="feature-card">
        <div class="icon-wrapper">✨</div>
        <h3>Interactive Previews</h3>
        <p>Code blocks come to life! See immediate visual representations of FXML and CSS components right next to the code.</p>
      </div>
      <div class="feature-card">
        <div class="icon-wrapper">🛠️</div>
        <h3>Maven Ready</h3>
        <p>Dedicated guides for setting up and structuring modern JavaFX projects using Maven and modular architecture.</p>
      </div>
    </section>

    <section class="objective">
      <h2>Project Objective</h2>
      <p>
        Historically, learning JavaFX meant reading through dense, outdated, and visually unappealing Javadocs. 
        <strong>JavaFX Modern Docs</strong> changes that. Our goal is to provide developers with a premium, engaging, 
        and highly visual learning experience. By combining theoretical knowledge with practical visual previews and 
        modern web design principles, this project aims to become the definitive resource for building desktop applications 
        with Java and JavaFX.
      </p>
    </section>

    <footer class="home-footer">
      <p>Made with Gemini 3 by low</p>
    </footer>
  </div>
</template>

<style scoped>
.home-container {
  padding: 60px 40px;
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 60px;
}

.hero {
  text-align: center;
  padding: 40px 0;
}

.title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  color: var(--text-main);
}

.title .highlight {
  background: linear-gradient(90deg, #38bdf8, #818cf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subtitle {
  font-size: 1.3rem;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto 40px;
  line-height: 1.6;
}

.cta-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.btn {
  padding: 12px 28px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1.05rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #38bdf8, #818cf8);
  color: #fff;
  box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(56, 189, 248, 0.4);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--glass-border);
  color: var(--text-main);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
}

.feature-card {
  background: rgba(30, 41, 59, 0.5);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  padding: 30px;
  text-align: center;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  border-color: rgba(56, 189, 248, 0.4);
}

.icon-wrapper {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.feature-card h3 {
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: var(--text-main);
}

.feature-card p {
  color: var(--text-muted);
  line-height: 1.6;
  font-size: 0.95rem;
}

.objective {
  background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9));
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  padding: 40px;
  position: relative;
  overflow: hidden;
}

.objective::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #38bdf8, #818cf8);
}

.objective h2 {
  font-size: 2rem;
  margin-bottom: 20px;
  color: var(--text-main);
}

.objective p {
  color: var(--text-muted);
  line-height: 1.8;
  font-size: 1.1rem;
}

.home-footer {
  text-align: center;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid var(--glass-border);
  color: var(--text-muted);
  font-size: 0.9rem;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .title {
    font-size: 2.5rem;
  }
  .cta-buttons {
    flex-direction: column;
  }
  .home-container {
    padding: 30px 20px;
  }
}
</style>
