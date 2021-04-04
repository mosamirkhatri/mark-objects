import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Report from "./components/Report";
import Upload from "./components/Upload";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path={"/"} component={Upload} />
        <Route path={"/report"} component={Report} />
        <Route path={"*"}>
          <h1>Error 404</h1>
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
