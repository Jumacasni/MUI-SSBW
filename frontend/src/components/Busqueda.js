import React from 'react';
import Form from 'react-bootstrap/Form';

class Busqueda extends React.Component {
	
	handleChange(event) {
	  // console.log(event.target.value)
	  this.props.handleBuscar(event.target.value)
  }

	render() {
		return (  
			<Form style={{marginTop:'8%', paddingBottom:'2%'}}>
				<Form.Group>
					<Form.Label>Buscar excursiones</Form.Label>  
					<Form.Control type="text" placeholder="..." onChange={this.handleChange.bind(this)}/>
				</Form.Group>
			</Form>
		)
	}
}

export default Busqueda