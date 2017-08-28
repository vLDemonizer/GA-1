class ProductDetails extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      type: '',
      brand: '',
      size: '',
      department: '',
      amount: '',
      date: '',
    }
    this.handleTable = this.handleTable.bind(this);
    this.handleSelect = this.handleSelect.bind(this);
  }

  handleTable() {
    let t = $("#id_product_class").val().split(" - ");
    this.setState({
      name: t[0],
      type: t[1],
      brand: t[2],
      size: t[3],
      department: t[4],
      amount: $("#id_amount").val(),
      date: new Date().toDateString()
    })
  }

  handleSelect(name, type, brand, size, department) {
    console.log(name);
    console.log(type);
  }

  render () {
    let products = this.props.products.products;
    var product_list = [];
    for (var i = 0; i < products.length; i++) {
      product_list.push(<option value={products[i].key} id={products[i].key}>
        {products[i].name} - {products[i].type} - {products[i].brand} - {products[i].size} - {products[i].department}
      </option>)
    }
    return (
      <div className="container-fluid">
        <div className="text-center">
          <h3 className="display-3">Product In</h3>
        </div>
        <div className="form-group">
          <label>Destiny</label>
          <input className="form-control" type="text" id="id_destiny" name="destiny" value="Almacen" readOnly={true}/>
        </div>
        <div className="form-group">
          <label>Search Product</label>
          <input id="id_product_class" name="product_class" className="form-control" type="text" list="options" />
          <datalist id="options">
            {product_list}
          </datalist>
        </div>
        <div className="form-group">
          <label>Amount</label>
          <input id="id_amount" name="amount" className="form-control" type="number" onChange={this.handleTable}/>
        </div>
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
