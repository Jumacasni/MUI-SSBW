import React from 'react';
import Excursion from './Excursion'

class ListaExcursiones extends React.Component {
	render(){
		console.log(this.props.excursiones)
		return (
				<div className="d-flex flex-wrap mt-5">
					{this.props.excursiones.map(excursion => (
	          <Excursion
						  key={excursion.id}
						  excursion={excursion}
						  handleInfo={this.props.handleInfo}
						/>
	        ))}
	      </div>
		)
	}
}

export default ListaExcursiones