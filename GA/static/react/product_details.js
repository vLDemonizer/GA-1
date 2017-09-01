class Option extends React.Component {
  render () {
    let product = this.props.product;
    return (
      <option
        name={product.pk}>{product.name} - {product.type} - {product.size} - {product.brand} - {product.department}
      </option>
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
    if (en){
      return (
          <div className="form-group">
            <label>Search Product</label>
            <input
              onInput={this.handleSelection}
              id="product_info"
              className="form-control"
              type="text"
              list="options"
              autoComplete="off"
              required={true}
            />
            <datalist id="options">
              {product_list}
            </datalist>
          </div>
      );
    }
    else {
      return (
          <div className="form-group">
            <label>Buscar Producto</label>
            <input
              onInput={this.handleSelection}
              id="product_info"
              className="form-control"
              type="text"
              list="options"
              autoComplete="off"
              required={true}
            />
            <datalist id="options">
              {product_list}
            </datalist>
          </div>
      );
    }
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
      stock: 0,
      date: '',
    }

    this.handleSubmitKey = this.handleSubmitKey.bind(this);
    this.handleAmountChange = this.handleAmountChange.bind(this);
  }

  handleSubmitKey(options, productText) {
    for (var i = 0; i < options.length; i++) {
      if (options[i].innerText === productText) {
        let product = this.props.products.products[i];
        $.ajax({
          url: '/ajax/get_product_global_stock/',
          data : {
            'product_class': product.pk,
          },
          success: (data) => this.setState({stock: data})
          
        });
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
      if(event.target.value >= 0){
        this.setState({amount: parseInt(event.target.value.toString())});
        return true;
      }
      return false;
  }


  render () {
    if (en){
      return (
        <div className="container-fluid">
          <div className="form-group">
            <label>Destiny</label>
            <input
              className="form-control"
              type="text" id="id_destiny"
              name="destiny"
              value="Almacen"
              readOnly={true}
            />
          </div>
          <DataList products={this.props.products} handleKey={this.handleSubmitKey}/>
          <div className="form-group">
            <label>Amount</label>
            <input
              id="id_amount"
              name="amount"
              className="form-control"
              type="number"
              value={this.state.amount}
              onChange={this.handleAmountChange}
              required={this.state.amount < 1 ? true : false}
            />
          </div>
          <HiddenInput primary_key={this.state.key} />
          <table className="table table-responsive">
            <thead>
              <th>Name</th>
              <th>Type</th>
              <th>Brand</th>
              <th>Size</th>
              <th>Department</th>
              <th>Amount</th>
              <th>Stock</th>
              <th>Date</th>
            </thead>
            <tbody>
              <td>{this.state.name}</td>
              <td>{this.state.type}</td>
              <td>{this.state.brand}</td>
              <td>{this.state.size}</td>
              <td>{this.state.department}</td>
              <td>{this.handleAmountChange ? this.state.amount : ''}</td>
              <td>{this.state.stock}</td>
              <td>{this.state.date}</td>
            </tbody>
          </table>
        </div>
      );
    }
    else {
      return (
        <div className="container-fluid">
          <div className="form-group">
            <label>Destino</label>
            <input
              className="form-control"
              type="text" id="id_destiny"
              name="destiny"
              value="Almacen"
              readOnly={true}
            />
          </div>
          <DataList products={this.props.products} handleKey={this.handleSubmitKey}/>
          <div className="form-group">
            <label>Cantidad</label>
            <input
              id="id_amount"
              name="amount"
              className="form-control"
              type="number"
              value={this.state.amount}
              onChange={this.handleAmountChange}
              required={this.state.amount < 1 ? true : false}
            />
          </div>
          <HiddenInput primary_key={this.state.key} />
          <table className="table table-responsive">
            <thead>
              <th>Nombre</th>
              <th>Tipo</th>
              <th>Marca</th>
              <th>Tamaño o Talla</th>
              <th>Departamento</th>
              <th>Cantidad</th>
              <th>Stock</th>
              <th>Fecha</th>
            </thead>
            <tbody>
              <td>{this.state.name}</td>
              <td>{this.state.type}</td>
              <td>{this.state.brand}</td>
              <td>{this.state.size}</td>
              <td>{this.state.department}</td>
              <td>{this.handleAmountChange ? this.state.amount : ''}</td>
              <td>Nothing Yet</td>
              <td>{this.state.date}</td>
            </tbody>
          </table>
        </div>
      );
    }
  }
}
