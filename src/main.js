import { createApp } from "vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "./assets/main.css";
import "./assets/tutorial.css";
import App from "./App.vue";
import router from "./router";
import JavaFxPreview from "./components/JavaFxPreview.vue";

const app = createApp(App);
app.use(router);
app.component("JavaFxPreview", JavaFxPreview);
app.mount("#app");
