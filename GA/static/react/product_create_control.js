let departments = [
  'Equipo de Proteccion Personal',
  'Dotacion',
  'Equipos y Enseres',
  'Productos de Mantenimiento',
  'Ferreteria',
  'Papeleria',
  'Computacion',
  'Maquinaria',
];

class Name extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  100,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value.toUpperCase(),
        current: current
      });
  }

  render () {
    if (en) {
      return (
        <div className="col">
          <label>Name <small className="text-form text-muted">Character limit {this.state.current} of 100.</small></label>
          <input
            id="id_name"
            name="name"
            type="text"
            className="form-control"
            placeholder="Enter product name"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
          <small className="form-text text-muted">Remember to double check the information you are submitting</small>
        </div>
      );
    }
    else {
      return (
        <div className="col">
          <label>Nombre <small className="text-form text-muted"> Limite de caracteres: {this.state.current} de 100.</small></label>
          <input
            id="id_name"
            name="name"
            type="text"
            className="form-control"
            placeholder="Nombre del Producto"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
          <small className="form-text text-muted">Remember to double check the information you are submitting</small>
        </div>
      );
    }
  }
};

class ProductType extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  100,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value.toUpperCase(),
        current: current
      });
  }
  render () {
    if (en){
      return (
        <div className="col">
          <label>Product Type <small className="text-form text-muted">Character limit {this.state.current} of 100.</small></label>
          <input
            id="id_product_type"
            name="product_type"
            type="text"
            className="form-control"
            placeholder="Enter product type"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
        </div>
      );
    }
    else {
      return (
        <div className="col">
          <label>Tipo de Producto <small className="text-form text-muted"> Limite de caracteres: {this.state.current} de 100.</small></label>
          <input
            id="id_product_type"
            name="product_type"
            type="text"
            className="form-control"
            placeholder="Ingrese el Tipo de Producto"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
        </div>
      );
    }
  }
};

class Brand extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  30,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value.toUpperCase(),
        current: current
      });
  }
  render () {
    if (en){
      return (
        <div className="col">
          <label>Brand <small className="text-form text-muted">Character limit {this.state.current} of 30.</small></label>
          <input
            id="id_brand"
            name="brand"
            type="text"
            className="form-control"
            placeholder="Enter brand name"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
        </div>
      );
    }
    else {
      return (
        <div className="col">
          <label>Marca <small className="text-form text-muted"> Limite de caracteres {this.state.current} de 30.</small></label>
          <input
            id="id_brand"
            name="brand"
            type="text"
            className="form-control"
            placeholder="Ingrese la Marca"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
        </div>
      );
    }
  }
};

class Departments extends React.Component {
  render () {
    var options = [];
    for (var i = 0; i < departments.length; i++) {
      options.push(<option value={departments[i]} className="dropdown-item" key={'o' + i}>{departments[i]}</option>);
    }
    if (en){
      return (
        <div className="col">
          <label>Department</label>
          <select className="form-control" id="id_department" name="department" required>
            {options}
          </select>
        </div>
      );
    }
    else {
      return (
        <div className="col">
          <label>Departamento</label>
          <select className="form-control" id="id_department" name="department" required>
            {options}
          </select>
        </div>
      );
    }
  }
};

class Size extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  15,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value.toUpperCase(),
        current: current
      });
  }

  render () {
    if (en){
      return (
        <div className="col">
          <label>Size<small className="text-form text-muted"> Character Limit {this.state.current} de 15.</small></label>
          <input
            id="id_size"
            name="size"
            type="text"
            className="form-control"
            placeholder="Enter Size"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
        </div>
      );
    }
    else {
      return (
        <div className="col">
          <label>Tamaño o Talla<small className="text-form text-muted"> Limite de caracteres {this.state.current} de 15.</small></label>
          <input
            id="id_size"
            name="size"
            type="text"
            className="form-control"
            placeholder="Ingrese el Tamaño o la Talla del Producto"
            value={this.state.value}
            onChange={this.handleChange}
            required
          />
        </div>
      );
    }
  }
};

class NumberInput extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.props.limit) && event.target.value >= 0)
      this.setState({
        value: event.target.value,
        current: current
      });
  }

  render () {
    let name = this.props.name; 
    return (
      <div className="col">
        <label>{this.props.tittle} <small className="text-form text-muted">Character limit {this.state.current} of {this.props.limit}.</small></label>
        <input
          id={"id_" + name}
          name={name}
          type="number"
          step="0.01"
          className="form-control"
          placeholder={this.props.placeHolder}
          value={this.state.value}
          onChange={this.handleChange}
          required
        />
      </div>
    );
  }
}
class Description extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  120,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
  }

  render () {
    if (en) {
      return (
        <div className="form-group">
          <label>Description <small className="text-form text-muted">Character limit {this.state.current} of 120.</small></label>
          <textarea
            id="id_description"
            name="description"
            type="text"
            className="form-control"
            placeholder="Enter product's description name"
            rows="3"
            value={this.state.value}
            onChange={this.handleChange}
          required>
          </textarea>
        </div>
      );
    }
    else {
      return (
        <div className="form-group">
          <label>Descripcion del Producto <small className="text-form text-muted">Limite de caracteres: {this.state.current} de 120.</small></label>
          <textarea
            id="id_description"
            name="description"
            type="text"
            className="form-control"
            placeholder="Describa el Producto a Ingresar (Algo que le sirva para diferenciarlo de productos comunes)."
            rows="3"
            value={this.state.value}
            onChange={this.handleChange}
          required>
          </textarea>
        </div>
      );
    }
  }
};

class Prices extends React.Component {
  render () {
    let names = [
      'cost_value', 'our_value', 'their_value',
    ];
    let tittles = [
      'Cost', 'Our Price', 'Their Price',
    ];
    let es_tittles = [
      'Costo', 'Nuestro Precio', 'Precio Afuera',
    ];
    let placeHolder = 'Insert Amount';
    let es_placeHolder = 'Ingrese Cantidad';
    var prices = [];
    for (var i = 0; i < names.length; i++) {
      if (en) {
        prices.push(
          <NumberInput 
            name={names[i]} 
            tittle={tittles[i]} 
            placeHolder={placeHolder}
            limit={12}
          />
        )
      } else {
        prices.push(
          <NumberInput 
            name={names[i]} 
            tittle={es_tittles[i]} 
            placeHolder={es_placeHolder}
            limit={12}
          />
        )
      }
    }
    return (
      <div className="row" style={{marginTop: "1rem"}}>
        {prices}
      </div>
    );
  }
}

class ProductForm extends React.Component {
  render () {
    var disposable_label = "Es Liquido o Desechable?";
    var tittle = en ? "Minimum Amount" : "Cantidad Minima"
    var placeHolder = en ? "Insert Minimum Amount" : "Ingrese Cantidad Minima"
    if (en) {
      disposable_label = "Is Liquid or Disposable?";
    }
    return (
      <div className="container-fluid">
        <div className="row">
          <Name />
          <Brand />
        </div>
        <div className="row" style={{marginTop: "1rem"}}>
          <ProductType />
          <Departments />
        </div>
        <div className="row" style={{marginTop: "1rem"}}>
          <Size />
          <NumberInput 
            name={"min_amount"}
            tittle={tittle} 
            placeHolder={placeHolder}
            limit={8}
          />
        </div>
        {en || staff ? <Prices />: ''}
        <div className="form-group" style={{marginTop: "1rem"}}>
          <label className="btn btn-info"><span style={{color: 'white'}}>{disposable_label} </span>
          <input
            id="id_is_disposable"
            name="is_disposable"
            type="checkbox"
            autoComplete="off"
          />
          </label>
        </div>
        <Description />
      </div>
    );
  }
};

ReactDOM.render (
  <ProductForm />,
  document.getElementById('root')
);
