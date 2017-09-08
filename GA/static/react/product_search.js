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
        loaded: false,
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
      if (this.props.initial != '' && !this.state.loaded) {
        this.setState({value: this.props.initial, loaded: true});
      }
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
  };
  
  class ProductType extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: '',
        limit:  100,
        current: 0,
        loaded: false,
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
      if (this.props.initial != '' && !this.state.loaded) {
        this.setState({value: this.props.initial, loaded: true});
      }
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
};
  
class Brand extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: '',
        limit:  30,
        current: 0,
        loaded: false,
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
      if (this.props.initial != '' && !this.state.loaded) {
        this.setState({value: this.props.initial, loaded: true});
      }
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
}
  
class Departments extends React.Component {
    render () {
      var options = [];

      for (var i = 0; i < departments.length; i++) {
        if (this.props.initial === departments[i]) {
          options.push(<option value={departments[i]} className="dropdown-item" key={'o' + i} selected>{departments[i]}</option>);
        } else {
          options.push(<option value={departments[i]} className="dropdown-item" key={'o' + i}>{departments[i]}</option>);
        }
      }
        return (
          <div className="col">
            <label>Department</label>
            <select className="form-control" id="id_department" name="department" required>
              {options}
            </select>
          </div>
        );
      
    }
};
  
class Size extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: '',
        limit:  15,
        current: 0,
        loaded: false,
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
      if (this.props.initial != '' && !this.state.loaded) {
        this.setState({value: this.props.initial, loaded: true});
      }
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
};
  
  class NumberInput extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: 0,
        current: 0,
        loaded: false,
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
      if (this.props.initial != 0 && !this.state.loaded) {
        this.setState({value: this.props.initial, loaded: true});
      }
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
        loaded: false,
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
      if (this.props.initial != '' && !this.state.loaded) {
        this.setState({value: this.props.initial, loaded: true});
      }
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
}
  
class Prices extends React.Component {
    render () {
        let names = [
            'cost_value', 'our_value', 'their_value',
        ];
        let tittles = [
            'Cost', 'Our Price', 'Their Price',
        ];
        let placeHolder = 'Insert Amount';
        var prices = [];
        for (var i = 0; i < names.length; i++) {
            prices.push(
                <NumberInput 
                name={names[i]} 
                tittle={tittles[i]} 
                placeHolder={placeHolder}
                limit={12}
                initial={this.props.initials[i]}
                />
            )
        }
        return (
            <div className="row" style={{marginTop: "1rem"}}>
            {prices}
            </div>
        );
    }
}

class HiddenInput extends React.Component {
  render () {
    let name = this.props.name;
    return (
      <input
        type="hidden"
        id={"id_" + name}
        name={name}
        value={this.props.primary_key}
        required
      />
    );
  }
}

class Option extends React.Component {
    render () {
        let product = this.props.product.fields;
        let product_pk = this.props.product.pk;
        return (
            <option
                name={product_pk}
                >{product.name} - {product.product_type} - {product.size} - {product.brand} - {product.department}
            </option>
        );
    }
}

class ProductList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          key: 0,
          name: '',
          type: '',
          brand: '',
          size: '',
          department: '',
          description: '',
          is_disposable: false,
          min_amount: '',
          cost_value: '',
          our_value: '',
          their_value: '',
          
        };
        this.handleSelection = this.handleSelection.bind(this);
        this.changeState = this.changeState.bind(this);
    }
    
    changeState(e) {
      console.log(this.state.is_disposable)
      this.setState({is_disposable: !this.state.is_disposable})
    }

    handleSelection(e) {
        let options = e.target.list.options
        let productText = $("#product_info").val();
        for(var i = 0; i < options.length; i++) {
          if (options[i].innerText === productText) {
            let product = this.props.products[i];
            this.setState({
              key: product.pk,
              name: product.fields.name,
              type: product.fields.product_type,
              brand: product.fields.brand,
              size: product.fields.size,
              department: product.fields.department,
              description: product.fields.description,
              is_disposable: product.fields.is_disposable,
              min_amount: product.fields.min_amount,
              cost_value: product.fields.cost_value,
              our_value: product.fields.our_value,
              their_value: product.fields.their_value,
            });
          }
        }
    }
  
    render () {
        let products = this.props.products;
        var product_list = [];
        for (var i = 0; i < products.length; i++) {
            product_list.push(<Option product={products[i]} key={'a' + i}/>);
        }
        return (
            <div className="container-fluid">
                <div className="row" >
                  <div className="col">
                    <label>Search Product</label>
                    <input
                        onInput={this.handleSelection}
                        id="product_info"
                        className="form-control"
                        type="text"
                        list="product_options"
                        autoComplete="off"
                    />
                    <datalist id="product_options">
                        {product_list}
                    </datalist>
                  </div>
                </div>
                <HiddenInput primary_key={this.state.key} name={"product_class"}/>
                <div className="row" style={{marginTop: "1rem"}}>
                    <Name initial={this.state.name}/>
                    <Brand initial={this.state.brand}/>
                </div>
                <div className="row" style={{marginTop: "1rem"}}>
                    <ProductType initial={this.state.type}/>
                    <Departments initial={this.state.department}/>
                </div>
                <div className="row" style={{marginTop: "1rem"}}>
                    <Size initial={this.state.size}/>
                    <NumberInput 
                        name={"min_amount"}
                        tittle={"Minimum Amount"} 
                        placeHolder={"Inset Minimum Amount"}
                        limit={8}
                        initial={this.state.min_amount}
                    />
                </div>
                <Prices 
                  initials={[this.state.cost_value, this.state.our_value, this.state.their_value]}/>
                <div className="form-group" style={{marginTop: "1rem"}}>
                  <label className="btn btn-info"><span style={{color: 'white'}}>"Is Liquid or Disposable?" </span>
                  <input
                    id="id_is_disposable"
                    name="is_disposable"
                    type="checkbox"
                    autoComplete="off"
                    checked={this.state.is_disposable ? "checked" : null}
                    onClick={this.changeState}
                  />
                  </label>
                </div>
                <Description initial={this.state.description}/>
                <div className="text-center">
                  <button className="btn btn-primary">Submit</button>
                </div>
            </div>
        );
    }
}