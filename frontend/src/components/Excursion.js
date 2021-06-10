import React from 'react';

class Excursion extends React.Component {
	render(){

		let id = this.props.excursion.id
		let file = this.props.excursion.fotos[0].file
		let ruta_completa = "http://localhost/static/img/senderos"+"/"+id+"/"+file

		return (
			<div className="card bg-white-light me-2 mb-5" style={{width: '18rem', marginRight: '.5rem'}}>
				<img src={ruta_completa} className="card-img-top"/>
				<div className="card-body">
					<h5 className="card-title">{ this.props.excursion.nombre }</h5>
					<p className="card-text">{ this.props.excursion.descripcion }</p>
					<button
					className="btn btn-primary"
					onClick={() => this.props.handleInfo(this.props.excursion.id)}
					>
						Info
					</button>
				</div>
			</div>
		)
	}
}

export default Excursion