class Option extends React.Component {
  render() {
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

    this.handleSelection = this.handleSelection.bind(this);
  }

  handleSelection(e) {
    this.props.handleKey(e.target.list.options, $("#product_info").val());
  }

  render() {
    let products = this.props.products;
    var product_list = [];
    for (var i = 0; i < products.length; i++) {
      product_list.push(<Option product={products[i]} key={'a' + i} />);
    }
    return (
      <div className="col" style={{ marginBottom: "1rem" }}>
        <label>Search a Product</label>
        <input
          onInput={this.handleSelection}
          id="product_info"
          className="form-control"
          type="text"
          list="product_options"
          autoComplete="off"
          autoFocus=""
        />
        <datalist id="product_options">
          {product_list}
        </datalist>
      </div>
    );
  }
}

class HiddenInput extends React.Component {
  render() {
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

class CodeRanges extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      key: 0,
      name: '',
      type: '',
      brand: '',
      size: '',
      department: '',
      stock: 0,
      start: 0,
      end: 0,
      range: 0,
      anotherOne: false,
    };
    this.handleSubmitKey = this.handleSubmitKey.bind(this);
    this.checkInput = this.checkInput.bind(this);
    this.startInput = this.startInput.bind(this);
    this.endInput = this.endInput.bind(this);
    this.rangeInput = this.rangeInput.bind(this);
  }

  handleSubmitKey(options, productText) {
    for (var i = 0; i < options.length; i++) {
      if (options[i].innerText === productText) {
        let product = this.props.products[i]; 0;
        $.ajax({
          url: '/inventario/ajax/get_product_global_stock/',
          data: {
            'product_class': product.pk
          },
          success: (data) => this.setState({ stock: data })
        });
        this.setState({
          key: product.pk,
          name: product.fields.name,
          type: product.fields.product_type,
          brand: product.fields.brand,
          size: product.fields.size,
          department: product.fields.department,
          error: false,
        });
      }
    }
  }

  startInput(e) {
    this.setState({
      start: e.target.value,
      error: false,
    });
  }
  
  endInput(e) {
    this.setState({
      end: e.target.value,
      error: false,
    });
  }

  rangeInput(e) {
    this.setState({
      range: e.target.value,
      error: false,
    });
  }

  checkInput(e) {
    let start = this.state.start;
    let end = this.state.end;
    let range = this.state.range;
    let key = this.state.key;
    if (start <= 0 || end <= 0 || range <= 0 || key == 0) {
      e.preventDefault();
      this.setState({error: true});
    } else {
      e.preventDefault();
      let product_class = '?product_class=' + this.state.key;
      let start_info = '&start=' + this.state.start;
      let end_info = '&end=' + this.state.end;
      let code_range_info = '&code_range=' + this.state.range;
      let path = product_class + start_info + end_info + code_range_info
      $('#download').html("<iframe style='display:none;' src='/inventario/ajax/generate_file/" + path + "'><iframe>");
    }
  }

  render() {
    let error = this.state.error ? "All fields must have a valid value." : "";
    return (
      <div className="container-fluid">
        <ProductList products={this.props.products} handleKey={this.handleSubmitKey} />
        <HiddenInput primary_key={this.state.key} name={'product_class'} />
        <div className="form-errors">
          {error}
        </div>
        <table className="table table-responsive">
          <thead>
            <th>Name</th>
            <th>Type</th>
            <th>Brand</th>
            <th>Size</th>
            <th>Department</th>
            <th>Stock</th>
            <th>From</th>
            <th>To</th>
            <th>Range</th>
          </thead>
          <tbody>
            <td>{this.state.name}</td>
            <td>{this.state.type}</td>
            <td>{this.state.brand}</td>
            <td>{this.state.size}</td>
            <td>{this.state.department}</td>
            <td>{this.state.stock}</td>
            <td>
              <input 
                style={{ width: "110px" }}
                type="number"
                id="id_start"
                name="start"
                className="form-control"
                value={this.state.start}
                onInput={this.startInput}
                />
            </td>
            <td>
              <input 
                style={{ width: "110px" }}
                type="number" id="id_end"
                name="end"
                className="form-control"
                value={this.state.end}
                onInput={this.endInput}
              />
            </td>
            <td>
              <input
                style={{ width: "110px" }}
                type="number"
                id="id_code_range"
                name="code_range"
                className="form-control"
                value={this.state.range}
                onInput={this.rangeInput}
              />
            </td>
          </tbody>
        </table>
        <div className="text-center">
          <button 
            className="btn btn-primary"
            type="submit"
            onClick={this.checkInput}>Submit
          </button>
        </div>
      </div>
    );
  }
}