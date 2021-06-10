import React from 'react';
import logo from './logo.gif';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Busqueda from './components/Busqueda'
import ListaExcursiones from './components/ListaExcursiones'
import Info from './components/Info'

class App extends React.Component {

  constructor(props){
    super(props)
  
    this.state = {
      excursiones: [],
      info: ''
    }
  }

  componentDidMount(){
    fetch('http://localhost:80/api/excursiones')
    .then(res => res.json())
    .then(res =>{
      let excursion = res.map(e => {
        e.on = true
        return e
      })
      this.setState({excursiones: excursion})
    })
  }

  handleInfo = (id) => {
    if (id===''){
      this.setState({info: ''})
    }
    else{
      this.setState({info: id})
    }
  }

  infoDe = () => {
    const [e] = this.state.excursiones.filter(e => e.id === this.state.info)
    console.log(e)
    return e
  }

  handleBuscar = (bus) => {
    if(bus){
      console.log("hola")
      let excursion = this.state.excursiones.map(e => {
        let reg = new RegExp(bus, "i")
        if (!e.nombre.match(reg)){
          e.on = false
        }
        else{
          e.on = true
        }
        return e
      })
      this.setState({excursiones: excursion})
    }

    else{
      console.log("adios")
      let excursion = this.state.excursiones.map(e => {
        e.on = true
        return e
      })
      this.setState({excursiones: excursion})
    }
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
        <Container>
          {this.state.info ? <Info e = {this.infoDe()} handleInfo = {this.handleInfo} /> :
          <>
          <Busqueda handleBuscar={this.handleBuscar} />
          <ListaExcursiones
            excursiones = {this.state.excursiones.filter(e => e.on === true)}
            handleInfo = {this.handleInfo}
            />
          </>}
        </Container>
      </Container>
    );
  }
}

export default App;
