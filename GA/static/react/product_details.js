class Option extends React.Component {
  render () {
    let product = this.props.product;
    return (
      <option name={product.pk}>{product.name} - {product.type} - {product.size} - {product.brand} - {product.department}</option>
    );
  }
}

class DataList extends React.Component {
  constructor(props) {
    super(props);

    this.handleSelection = this.handleSelection.bind(this);
  }

  handleSelection(e) {
    this.props.handleKey(e.target.list.options, $("#product_info").val());
  }

  render () {
    let products = this.props.products.products;
    var product_list = [];
    for (var i = 0; i < products.length; i++) {
      product_list.push(<Option product={products[i]}/>);
    }
    return (
        <div className="form-group">
          <label>Search Product</label>
          <input onInput={this.handleSelection} id="product_info" className="form-control" type="text" list="options" autoComplete="off" />
          <datalist id="options">
            {product_list}
          </datalist>
        </div>
    );
  }
}

class HiddenInput extends React.Component {
  render () {
    return (
      <input type="hidden" id="id_product_class" name="product_class" value={this.props.primary_key} required />
    );
  }
}

class ProductDetails extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      key: 0,
      name: '',
      type: '',
      brand: '',
      size: '',
      department: '',
      amount: 0,
      date: '',
    }

    this.handleSubmitKey = this.handleSubmitKey.bind(this);
    this.handleAmountChange = this.handleAmountChange.bind(this);
  }

  handleSubmitKey(options, productText) {
    var i = 0;
    for(; i < options.length; i++) {
      if (options[i].innerText === productText) {
        let product = this.props.products.products[i];
        console.log(product);
        this.setState({
          key: product.pk,
          name: product.name,
          type: product.type,
          brand: product.brand,
          size: product.size,
          department: product.department,
          date: new Date().toDateString(),
        });
      }
    }
  }

  handleAmountChange(event) {
    this.setState({amount: event.target.value});
  }

  render () {
    return (
      <div className="container-fluid">
        <div className="form-group">
          <label>Destiny</label>
          <input className="form-control" type="text" id="id_destiny" name="destiny" value="Almacen" readOnly={true}/>
        </div>
        <DataList products={this.props.products} handleKey={this.handleSubmitKey}/>
        <div className="form-group">
          <label>Amount</label>
          <input id="id_amount" name="amount" className="form-control" type="number" onChange={this.handleAmountChange}/>
        </div>
        <HiddenInput primary_key={this.state.key} />
        <table className="table">
          <thead>
            <th>Name</th>
            <th>Type</th>
            <th>Brand</th>
            <th>Size</th>
            <th>Department</th>
            <th>Amount</th>
            <th>Date</th>
          </thead>
          <tbody>
            <td>{this.state.name}</td>
            <td>{this.state.type}</td>
            <td>{this.state.brand}</td>
            <td>{this.state.size}</td>
            <td>{this.state.department}</td>
            <td>{this.state.amount}</td>
            <td>{this.state.date}</td>
          </tbody>
        </table>
      </div>
    );
  }
}
