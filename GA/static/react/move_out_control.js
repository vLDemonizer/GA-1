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
    if (en) {
      return (
        <div style={{ marginBottom: "1rem" }}>
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
      );
    }
    else {
      return (
        <div style={{ marginBottom: "1rem" }}>
          <label>Buscar un Producto</label>
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

class ProductTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      amount: '',
      amountError: false,
      series: '',
      unit: '',
      next: false,
      submitError: false,
    }
    this.handleAmountChange = this.handleAmountChange.bind(this);
    this.handleSeries = this.handleSeries.bind(this);
    this.handleUnit = this.handleUnit.bind(this);
    this.submitSingleMoveOut = this.submitSingleMoveOut.bind(this);
  }

  submitSingleMoveOut(e) {
    e.preventDefault()
    let product_class = $('#id_product_class').val();
    let from = $('#id_from_location').val();
    let to = $('#id_destiny').val();
    let reason = $('#id_reason').val();
    let reason_description = $('#id_reason_description').val();
    let authorized_by = $('#id_authorized_by').val();
    let received_by = $('#id_received_by').val();
    $.ajax({
      url: '/inventario/ajax/single-product-out/',
      data: {
        'product_class': product_class,
        'from_location': from,
        'destiny': to,
        'reason': reason,
        'reason_description': reason_description,
        'authorized_by': authorized_by,
        'received_by': received_by,
        'series': this.state.series,
        'unit': this.state.unit,
      },
      dataType: 'json',
      success: (data) => {
        if (data) {
          this.setState({
            series:'',
            unit: '',
            next: true,
            submitError: false,
          });
          console.log('Chiabe bibeh')
        } else {
          console.log('Chiabe no bibeh')
          this.setState({
            submitError: true,
          });
        }
      }
    });
  }

  handleUnit(e) {
    var value = e.target.value;
    let limit = parseInt(this.props.unitLimit)
    if (value != '') {
      value = parseInt(value);
      if (value <= limit) {
        this.setState({
          unit: value 
        });
      }
    }
    else {
      this.setState({unit: ''});
    }
  }

  handleSeries(e) {
    var value = e.target.value;
    let limit = parseInt(this.props.seriesLimit)
    if (value != '') {
      value = parseInt(value);
      if (value <= limit) {
        this.setState({
          series: value 
        });
      }
    }
    else {
      this.setState({series: ''});
    }
  }


  handleAmountChange(event) {
    let rawValue = event.target.value;
    if (rawValue !== '') {
      let value = parseInt(rawValue);
      if (value > this.props.stock) {
        return;
      } else {
        this.setState({
          amount: value,
        });
      }
    } else {
      this.setState({
        amount: ''
      });
    }
  }

  render() {
    var table = '';
    let bulkTable = (
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
          <td>{this.props.name}</td>
          <td>{this.props.type}</td>
          <td>{this.props.brand}</td>
          <td>{this.props.size}</td>
          <td>{this.props.department}</td>
          <td style={{ width: "130px" }}>
            <input
              id="id_amount"
              name="amount"
              className="form-control"
              type="number"
              value={this.state.amount}
              onChange={this.handleAmountChange}
            />
          </td>
          <td>{this.props.stock}</td>
          <td>{this.props.date}</td>
        </tbody>
      </table>
    );
    let singleTable = (
      <div>
        <table className="table table-responsive">
          <thead>
            <th>Product Type Code</th>
            <th>Series</th>
            <th>Unit</th>
            <th>Date</th>
            <th></th>
          </thead>
          <tbody>
            <td>
              <input
                type="text"
                className="form-control"
                value={this.props.code}
                readOnly
              />
            </td>
            <td className="form-group">
              <label>S</label>
              <input
                type="number"
                className="td-input"
                id="series"
                value={this.state.series}
                onInput={this.handleSeries}
              />
            </td>
            <td className="form-group">
              <label>-</label>
              <input
                type="number"
                className="td-input"
                id="unit"
                value={this.state.unit}
                onInput={this.handleUnit}
              />
            </td>
            <td>{this.props.date}</td>
            <td>
              <button 
                className="btn btn-info"
                onClick={this.submitSingleMoveOut}
              >Load</button>
            </td>
          </tbody>
        </table>
      </div>
    );
    return (
      <div>
        {this.props.single ? singleTable : bulkTable}
      </div>
    )
  }
}

class Details extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      key: 0,
      name: '',
      type: '',
      brand: '',
      size: '',
      department: '',
      amount: 1,
      stock: 0,
      date: '',
      code: '',
      selective: false,
      seriesLimit: 0,
      unitLimit: 0,
    }

    this.handleSubmitKey = this.handleSubmitKey.bind(this);
    this.handleSingleProduct = this.handleSingleProduct.bind(this);
  }

  handleSingleProduct(e) {
    this.setState({
      selective: !this.state.selective
    })
  }

  handleSubmitKey(options, productText) {
    for (var i = 0; i < options.length; i++) {
      if (options[i].innerText === productText) {
        let product = this.props.products[i]; 0;
        $.ajax({
          url: '/inventario/ajax/get_product_stock/',
          data: {
            'product_class': product.pk,
            'location': $("#id_from_location").val(),
          },
          dataType: 'json',
          success: (data) => this.setState({
            stock: data.stock,
            code: data.code,
            seriesLimit: data.seriesLimit,
            unitLimit: data.unitLimit,
          })
        });
        this.setState({
          key: product.pk,
          name: product.fields.name,
          type: product.fields.product_type,
          brand: product.fields.brand,
          size: product.fields.size,
          department: product.fields.department,
          date: new Date().toDateString(),
        });
      }
    }
  }


  render() {
    let errorMessage = (<div className="form-errors">Amount Error: No puede sacar una cantidad mayor de la que hay en stock!</div>);
    return (
      <div>
        <ProductList
          products={this.props.products}
          handleKey={this.handleSubmitKey}
        />
        <div className="row" style={{ marginBottom: "1rem" }}>
          <div className="col">
            <label className="custom-control custom-checkbox mb-2 mr-sm-2 mb-sm-0">
              <input
                type="checkbox"
                className="custom-control-input"
                checked={this.state.selective}
                onClick={this.handleSingleProduct}
              />
              <span className="custom-control-indicator"></span>
              <span className="custom-control-description">Single Product</span>
            </label>
          </div>
        </div>
        <HiddenInput primary_key={this.state.key} name={"product_class"} />
        <ProductTable
          single={this.state.selective}
          seriesLimit={this.state.seriesLimit}
          unitLimit={this.state.unitLimit}
          name={this.state.name}
          type={this.state.type}
          brand={this.state.brand}
          size={this.state.size}
          department={this.state.department}
          stock={this.state.stock}
          date={this.state.date}
          code={this.state.code}
        />
      </div>
    );

  }
}

class LocationSelect extends React.Component {
  render() {
    let locations = this.props.locations;
    let name = this.props.name
    var location_list = [];
    // From can't have Desincorporacion
    var x = 0;
    if (this.props.from) {
      x = 1;
    }
    for (var i = 0; i < locations.length - x; i++) {
      location_list.push(<option value={i} key={'e' + i}>{locations[i]}</option>);
    }
    return (
      <div className="col">
        <label>{this.props.tittle}</label>
        <select id={"id_" + name} name={name} className="form-control">
          {location_list}
        </select>
      </div>
    );
  }
}

class Locations extends React.Component {
  render() {
    var locations = [];
    for (var i = 0; i < this.props.names.length; i++) {
      if (i === 0) {
        locations.push(
          <LocationSelect
            from={true}
            locations={this.props.locations}
            name={this.props.names[i]}
            tittle={this.props.tittles[i]}
          />
        );
      } else {
        locations.push(
          <LocationSelect
            locations={this.props.locations}
            name={this.props.names[i]}
            tittle={this.props.tittles[i]}
          />
        );
      }
    }
    return (
      <div className="row" style={{ marginBottom: "1rem" }}>
        {locations}
      </div>
    );
  }
}

class ReasonSelect extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 0,
      showTextArea: false,
    }
    this.checkReason = this.checkReason.bind(this);
  }

  checkReason(e) {
    let value = e.target.value;
    if (value == (this.props.reasons.length - 1)) {
      this.setState({ showTextArea: true });
    } else {
      this.setState({ showTextArea: false });
    }
  }

  render() {
    let reasons = this.props.reasons;
    var reason_list = [];
    for (var i = 0; i < reasons.length; i++) {
      if (i == (reasons.length - 1)) {
        reason_list.push(
          <option
            value={i}
            key={'c' + i}
            onClick={this.checkReason}
          >{reasons[i]}</option>
        );
      } else {
        reason_list.push(<option value={i} key={'c' + i}>{reasons[i]}</option>);
      }
    }
    var textArea = [];
    if (this.state.showTextArea) {
      textArea.push(
        <div className="form-group">
          <label>Reason Description</label>
          <textarea
            className="form-control"
            id="id_reason_description"
            name="reason_description"
            rows="2"
          ></textarea>
        </div>
      )
    }
    return (
      <div className="form-group">
        <label>Reason</label>
        <select id="id_reason"
          name="reason"
          onChange={this.checkReason}
          className="form-control"
        >
          {reason_list}
        </select>
        <br />
        {textArea}
      </div>
    );
  }
}

class UsersComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user_key: 0,
    }
    this.handleKey = this.handleKey.bind(this);
  }

  handleKey(e) {
    let options = e.target.list.options;
    let input_text = $("#" + this.props.name).val();
    for (var i = 0; i < options.length; i++) {
      if (options[i].innerText === input_text) {
        let key = this.props.users[i].pk;
        this.setState({
          user_key: key,
        });
      }
    }
  }

  render() {
    let users = this.props.users;
    var user_list = [];
    let name = this.props.name;
    for (var i = 0; i < users.length; i++) {
      user_list.push(
        <option name={users[i].pk}>
          {users[i].fields.first_name} {users[i].fields.last_name}
        </option>
      );
    }
    return (
      <div>
        <label>{this.props.tittle}</label>
        <input
          onInput={this.handleKey}
          id={name}
          name={name}
          className="form-control"
          type="text"
          list={name + "_options"}
          autoComplete="off"
        />
        <datalist id={name + "_options"}>
          {user_list}
        </datalist>
        <HiddenInput primary_key={this.state.user_key} name={name} />
      </div>
    );
  }
}

class Users extends React.Component {
  render() {
    let user = this.props.dispatchUser[0].fields
    let user_pk = this.props.dispatchUser[0].pk
    if (en) {
      return (
        <div className="row">
          <div className="col">
            <UsersComponent
              users={this.props.authorizedUsers}
              name={"authorized_by"}
              tittle={"Authorized By"}
            />
          </div>
          <div className="col">
            <UsersComponent
              users={this.props.receivingUsers}
              name={"received_by"}
              tittle={"Received By"}
            />
          </div>
          <div className="col">
            <div className="text-center">
              <label>
                Dispatched by:
              </label>
              <br />
              <p>
                {user.first_name} {user.last_name}
              </p>
              <input
                id="id_given_by"
                name="given_by"
                className="form-control"
                type="hidden"
                value={user_pk}
              />
            </div>
          </div>
        </div>
      );
    }
    else {
      return (
        <div className="row">
          <div className="col">
            <UsersComponent
              users={this.props.authorizedUsers}
              name={"authorized_by"}
              tittle={"Autorizado Por"}
            />
          </div>
          <div className="col">
            <UsersComponent
              users={this.props.receivingUsers}
              name={"received_by"}
              tittle={"Recibido Por"}
            />
          </div>
          <div className="col">
            <div className="text-center">
              <label>
                Dispachado Por:
              </label>
              <br />
              <p>
                {user.first_name} {user.last_name}
              </p>
              <input
                id="id_given_by"
                name="given_by"
                className="form-control"
                type="hidden"
                value={user_pk}
              />
            </div>
          </div>
        </div>
      );
    }
  }
}

class MoveOut extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: ""
    };
    this.checkDirections = this.checkDirections.bind(this);
    this.names = ["from_location", "destiny"];
    if (en) {
      this.tittles = ["From", "To"];
    }
    else {
      this.tittles = ["Desde", "Hacia"];
    }
  }

  checkDirections(e) {
    let from = $("#id_" + this.names[0]).val();
    let to = $("#id_" + this.names[1]).val();
    if (en) {
      if (from === to) {
        this.setState({
          error: "You need to change the location, can't be the same."
        });
        e.preventDefault();
        return;
      }
      if (from === '1' && to === '2') {
        this.setState({
          error: "Office can't go to Plant."
        });
        e.preventDefault();
        return;
      }
      if (from === '2' && to === '1') {
        this.setState({
          error: "Plant can't go to Office."
        });
        e.preventDefault();
        return;
      }
    }
    else {
      if (from === to) {
        this.setState({
          error: "Desde y Hacia No Pueden ser Iguales"
        });
        e.preventDefault();
        return;
      }
      if (from === '1' && to === '2') {
        this.setState({
          error: "No Se Puede Hacer un Movimiento de Oficina a Planta"
        });
        e.preventDefault();
        return;
      }
      if (from === '2' && to === '1') {
        this.setState({
          error: "No Se Puede Hacer un Movimiento de Planta a Oficina"
        });
        e.preventDefault();
        return;
      }
    }
    this.setState({
      error: ''
    });
  }

  render() {
    if (en) {
      return (
        <div className="container-fluid">
          <div className="form-errors text-center">
            {this.state.error}
          </div>
          <Locations locations={this.props.locations}
            names={this.names}
            tittles={this.tittles}
            className="row"
          />
          <Details products={this.props.products} />
          <ReasonSelect reasons={this.props.reasons} />
          <Users
            authorizedUsers={this.props.admin_users}
            receivingUsers={this.props.retrieving_users}
            dispatchUser={this.props.current_user}
          />
          <div className="text-center" style={{ marginTop: "1rem" }}>
            <div className="btn-group">
              <input
                type="submit"
                className="btn btn-primary btn-lg"
                value="Submit"
                onClick={this.checkDirections} />
              <button
                id="id_redirect"
                name="redirect"
                className="btn btn-primary btn-lg"
                value=""
                onClick={() => { this.checkDirections; changeRedirect(); }}>Submit and Add</button>
            </div>
          </div>
          <br />
        </div>
      );
    }
    else {
      return (
        <div className="container-fluid">
          <div className="form-errors text-center">
            {this.state.error}
          </div>
          <Locations locations={this.props.locations}
            names={this.names}
            tittles={this.tittles}
            className="row"
          />
          <Details products={this.props.products} />
          <ReasonSelect reasons={this.props.reasons} />
          <Users
            authorizedUsers={this.props.admin_users}
            receivingUsers={this.props.retrieving_users}
            dispatchUser={this.props.current_user}
          />
          <div className="text-center" style={{ marginTop: "1rem" }}>
            <div className="btn-group">
              <input
                type="submit"
                className="btn btn-primary btn-lg"
                value="Cargar"
                onClick={this.checkDirections}
              />
              <button
                id="id_redirect"
                name="redirect"
                className="btn btn-primary btn-lg"
                value=""
                onClick={() => { this.checkDirections; changeRedirect(); }}
              >Cargar y Mover otro</button>
            </div>
          </div>
          <br />
        </div>
      );
    }
  }
}


