import React from 'react'
import { Navbar,Container,Nav,NavDropdown } from 'react-bootstrap'
import { Switch, Route, Link } from 'react-router-dom';

export default function Navegacion() {
    return (
<Navbar collapseOnSelect expand="lg" className="color-nav" variant="light">
  <Container>
  <Navbar.Brand as={Link} to="/">LSM ABBY</Navbar.Brand>
  <Navbar.Toggle aria-controls="responsive-navbar-nav" />
  <Navbar.Collapse id="responsive-navbar-nav">
    <Nav className="me-auto">
      <Nav.Link  as={Link} to="/cursos">Cursos</Nav.Link>
      <Nav.Link as={Link} to="/informacion">Informacion</Nav.Link>
      <NavDropdown title="Mas" id="collasible-nav-dropdown">
        <NavDropdown.Item href="#action/3.1">Dibuja y Aprende</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.2">Videos</NavDropdown.Item>
        
        <NavDropdown.Divider />
        <NavDropdown.Item href="#action/3.4">Comunidad</NavDropdown.Item>
      </NavDropdown>
    </Nav>
    <Nav>
      
      <Nav.Link as={Link} to="/contacto">
        Contactame
      </Nav.Link>
    </Nav>
  </Navbar.Collapse>
  </Container>
</Navbar>
    )
}
