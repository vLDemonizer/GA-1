class ProductDetails extends React.Component{
  render(){
    return (
      <div className="container-fluid">
        <div className="form-group">
          <label>Where it will go</label>
          <input
            id="id_destiny"
            className="form-control"
            name="destiny"
            type="text"
          />
          <label>Product</label>
          <input
            id="id_product"
            className="form-control"
            name="product"
            type="text"
          />
          <label>Product Code Selection</label>
          <input
            id="id_product_code"
            className="form-control"
            name="product_code"
            type="text"
          />
          <label>Amount</label>
          <input
            id="id_amount"
            name="amount"
            className="form-control"
            type="number"
            KeyboardType = "number-pad"
          />
        </div>
        <h4>Why this product is moving out</h4>
      </div>
    );
  }
};

class ReasonSelect extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      selectedOption: 'Dotacion',
    }

    this.handleOptionChange = this.handleOptionChange.bind(this);
  }

  handleOptionChange(evt){
    this.setState({
      selectedOption: evt.target.value
    });
  }

  render(){
    //let error = (
      //<p style={{color: 'red'}}> Password dont match</p>
    //);

    return(
      <div className="row form-group">
        <div className="radio col">
          <label>
            <input type="radio" value="Dotacion"
              checked={this.state.selectedOption === 'Dotacion'}
              onChange={this.handleOptionChange}
            />
              Dotacion
            </label>
        </div>
        <div className="radio col">
          <label>
            <input type="radio" value="Deterioro"
              checked={this.state.selectedOption === 'Deterioro'}
              onChange={this.handleOptionChange}
            />
              Deterioro
            </label>
        </div>
        <div className="radio col">
          <label>
            <input type="radio" value="Perdida"
              checked={this.state.selectedOption === 'Perdida'}
              onChange={this.handleOptionChange}
            />
              Perdida
            </label>
        </div>
        <div className="radio col">
          <label>
            <input type="radio" value="Donacion"
              checked={this.state.selectedOption === 'Donacion'}
              onChange={this.handleOptionChange}
            />
              Donacion
            </label>
        </div>
        <div className="radio col">
          <label>
            <input type="radio" value="Otros"
              checked={this.state.selectedOption === 'Otros'}
              onChange={this.handleOptionChange}
            />
              Otros
            </label>
        </div>
      </div>
    );
  }
};

class MoveOut extends React.Component{
  render(){
    return (
      <div className="container-fluid">
        <ProductDetails />
        <ReasonSelect />
      </div>
    );
  }
};
ReactDOM.render(
  <MoveOut />,
  document.getElementById('root')
);
