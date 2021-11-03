import logo from './logo.svg';
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';

import { Container,Row,Col } from 'react-bootstrap';
import Navegacion from './components/Navegacion';
import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Cursos from './components/Cursos';
import Informacion from './components/Informacion';
import Home from './components/Home';
function App() {
  return (
    <>
      <Router>
  <Navegacion/>
  <Container fluid>


      <div>


        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/cursos">
            <Cursos />
          </Route>
          <Route path="/informacion">
            <Informacion />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
 
      
  </Container>
  </Router>  
  </>
  );
}

export default App;
