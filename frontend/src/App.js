import React from 'react';
import logo from './logo.gif';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

class App extends React.Component {

  state = {
    excursiones: []
  }

  componentDidMount(){
    fetch('http://localhost:8000/api/excursiones')
    .then(res => res.json())
    .then(data =>{
      this.setState({excursiones:data})
    })
  }

  render() {
    return (
      <Container fluid>
        <Navbar bg="light">
          <Navbar.Brand href="#home">
            <img
              alt=""
              src={logo}
              width="30"
              height="24"
              className="d-inline-block align-center"
            />{' '}
            <span>Senderos Granada</span>
          </Navbar.Brand>
        </Navbar>
      </Container>
    );
  }
}

export default App;
